"""Reproducible exact LZ77 phase-spectrum census for order-five binary de Bruijn necklaces.

Run with Python >=3.9: python check.py. No external dependencies.
The routines deliberately use two distinct cycle-generation descriptions and
independent longest-previous-factor calculations.
"""
from collections import Counter
import hashlib, json

N = 32
EXPECTED = {
 'joint': {
  '10,11':12, '10,12':66, '10,13':276, '10,14':642, '10,15':178,'10,16':8,
  '11,11':66,'11,12':1034,'11,13':3828,'11,14':6118,'11,15':2704,'11,16':90,
  '12,12':1968,'12,13':10124,'12,14':14026,'12,15':5448,'12,16':122,
  '13,13':5446,'13,14':9362,'13,15':2414,'13,16':36,
  '14,14':1366,'14,15':200,'15,15':2,
 },
 'gain': {'0':8848,'1':20732,'2':20334,'3':11878,'4':3468,'5':268,'6':8},
 'rooted_overlap': {'10':1182,'11':13840,'12':31688,'13':17258,'14':1566,'15':2},
 'rooted_disjoint': {'11':78,'12':3068,'13':19674,'14':31514,'15':10946,'16':256},
 'necklace_gain_range': {'0,2':12,'0,3':544,'0,4':1158,'0,5':192,'0,6':8,'1,3':12,'1,4':94,'1,5':28},
}

def feedback_cycles():
    """For each context x of four bits, route 0x and 1x bijectively to x0,x1."""
    for rule in range(1 << 16):
        state = 0
        seen = 0
        out = []
        for _ in range(N):
            if (seen >> state) & 1:
                break
            seen |= 1 << state
            out.append(str(state >> 4))
            a, x = state >> 4, state & 15
            state = ((state << 1) & 31) | (a ^ ((rule >> x) & 1))
        if seen == (1 << N) - 1 and state == 0:
            yield ''.join(out)

def normalize(w):
    assert len(w) == N
    at = (w + w).find('00000')
    assert 0 <= at < N
    return w[at:] + w[:at]

def euler_cycles():
    """Independently order the two outgoing edges at each four-bit vertex.
    Hierholzer recursion enumerates 65,536 edge-order rules, with duplicates.
    """
    seen = set()
    for rule in range(1 << 16):
        used = [0] * 16
        reversed_edges = []
        def visit(v):
            while used[v] < 2:
                k = used[v]
                used[v] += 1
                b = ((rule >> v) & 1) ^ k
                visit(((v << 1) & 15) | b)
                reversed_edges.append(b)
        visit(0)
        assert len(reversed_edges) == N
        w = ''.join(str(b) for b in reversed(reversed_edges))
        seen.add(normalize(w))
    return seen

def parse_by_direct_matching(w, allow_overlap):
    """At each head compare its suffix to every earlier suffix, then greedy step."""
    n = len(w)
    pos = 0
    phrases = []
    while pos < n:
        best = 0
        source = -1
        for j in range(pos):
            lim = n - pos if allow_overlap else min(n - pos, pos - j)
            match = 0
            while match < lim and w[pos + match] == w[j + match]:
                match += 1
            if match > best:
                source, best = j, match
        phrases.append((pos, max(1, best), source if best else -1))
        pos += max(1, best)
    return phrases

def parse_by_suffix_lcp_dp(w, allow_overlap):
    """Independently compute the suffix-LCP matrix by right-to-left DP."""
    n = len(w)
    lcp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if w[i] == w[j]:
                lcp[i][j] = 1 + lcp[i + 1][j + 1]
    pos = 0
    phrases = []
    while pos < n:
        best = 0
        for j in range(pos):
            match = lcp[pos][j]
            if not allow_overlap:
                match = min(match, pos - j)
            best = max(best, match)
        phrases.append((pos, max(1, best)))
        pos += max(best, 1)
    return phrases

def count_profile():
    feedback = list(feedback_cycles())
    assert len(feedback) == 2048
    assert len(set(feedback)) == 2048
    assert all(w.startswith('00000') and len({(w+w)[i:i+5] for i in range(32)})==32 for w in feedback)
    alternate = euler_cycles()
    assert len(alternate) == 2048
    assert alternate == set(feedback), 'two independent graph methods disagree'
    joint = Counter()
    gain = Counter()
    overlap_hist = Counter()
    disjoint_hist = Counter()
    cycle_gain_range = Counter()
    cycle_extrema = Counter()
    for word in feedback:
        cycle_data = []
        for root in range(N):
            w = word[root:] + word[:root]
            a_phrases = parse_by_direct_matching(w, True)
            d_phrases = parse_by_direct_matching(w, False)
            a = len(a_phrases)
            d = len(d_phrases)
            a_dp = parse_by_suffix_lcp_dp(w, True)
            d_dp = parse_by_suffix_lcp_dp(w, False)
            assert [(x,y) for x,y,_ in a_phrases] == a_dp
            assert [(x,y) for x,y,_ in d_phrases] == d_dp
            assert a <= d
            joint[f'{a},{d}'] += 1
            gain[str(d-a)] += 1
            overlap_hist[str(a)] += 1
            disjoint_hist[str(d)] += 1
            cycle_data.append((a,d))
        aa=[x for x,y in cycle_data]
        dd=[y for x,y in cycle_data]
        gg=[y-x for x,y in cycle_data]
        cycle_gain_range[f'{min(gg)},{max(gg)}'] += 1
        cycle_extrema[f'{min(aa)},{max(aa)},{min(dd)},{max(dd)}']+=1
    computed = {
        'joint':dict(sorted(joint.items())),
        'gain':dict(sorted(gain.items())),
        'rooted_overlap':dict(sorted(overlap_hist.items())),
        'rooted_disjoint':dict(sorted(disjoint_hist.items())),
        'necklace_gain_range':dict(sorted(cycle_gain_range.items())),
    }
    assert computed == EXPECTED, 'enumerated spectrum differs from expected exact certificate'
    assert sum(joint.values()) == 65536
    assert sum(cycle_gain_range.values()) == 2048
    assert len(cycle_extrema)==31
    return computed,dict(sorted(cycle_extrema.items()))

if __name__=='__main__':
    result, extrema = count_profile()
    print('VERIFY_OK')
    print('Cycles: 2048; rooted traversals: 65536; cycle extrema types: 31')
    print('Rooted joint histogram:',json.dumps(result['joint'],sort_keys=True))
    print('Rooted overlapping-LZ77 histogram:',json.dumps(result['rooted_overlap'],sort_keys=True))
    print('Rooted nonoverlapping-LZ77 histogram:',json.dumps(result['rooted_disjoint'],sort_keys=True))
    print('Rooted overlap-benefit histogram:',json.dumps(result['gain'],sort_keys=True))
    print('Per-cycle benefit-range histogram:',json.dumps(result['necklace_gain_range'],sort_keys=True))
