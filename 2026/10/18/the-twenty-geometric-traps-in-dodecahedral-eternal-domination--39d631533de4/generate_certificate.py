"""Exhaustive finite certificate for all-guards-move defense of GP(10,2)."""
import json
import itertools
import collections
import hashlib
import sys

N = 20
OUTER = 10
FULL = (1 << N) - 1
EDGES = set()
for i in range(OUTER):
    for a, b in ((i, (i+1)%OUTER), (i, OUTER+i), (OUTER+i, OUTER+(i+2)%OUTER)):
        EDGES.add(tuple(sorted((a,b))))
EDGES = sorted(EDGES)
NEIGHBORS = [0]*N
for a,b in EDGES:
    NEIGHBORS[a] |= 1 << b
    NEIGHBORS[b] |= 1 << a


def vertices(s):
    return tuple(i for i in range(N) if (s >> i) & 1)


def dominating_masks(k):
    return [sum(1 << i for i in c)
            for c in itertools.combinations(range(N), k)
            if (lambda d: d == FULL)(__import__('functools').reduce(
                lambda x, v: x | (1 << v) | NEIGHBORS[v], c, 0))]


def destinations(s, allowed):
    source = vertices(s)
    reachable = set()
    def rec(i, dest):
        if i == len(source):
            if dest in allowed:
                reachable.add(dest)
            return
        bits = NEIGHBORS[source[i]] | (1 << source[i])
        while bits:
            bit = bits & -bits
            bits ^= bit
            if not (dest & bit):
                rec(i + 1, dest | bit)
    rec(0, 0)
    return reachable


def shells(x):
    dist = [-1] * N
    dist[x] = 0
    queue = collections.deque([x])
    while queue:
        v = queue.popleft()
        for w in vertices(NEIGHBORS[v]):
            if dist[w] < 0:
                dist[w] = dist[v] + 1
                queue.append(w)
    return [sum(1 << v for v in range(N) if dist[v] == d)
            for d in range(6)]


def run():
    dom_small = {str(k):len(dominating_masks(k)) for k in range(1, 6)}
    assert all(not v for v in dom_small.values())
    dom6 = dominating_masks(6)
    dom7 = dominating_masks(7)
    set6, set7 = set(dom6), set(dom7)
    assert len(dom6) == 10 and len(dom7) == 780

    fatal6 = []
    for s in dom6:
        options = destinations(s, set6)
        uncovered = [v for v in range(N) if not (s >> v) & 1 and not any((t >> v) & 1 for t in options)]
        fatal6.append([s, uncovered])
    assert all(len(x[1]) == 2 for x in fatal6)

    options7 = {s: destinations(s, set7) for s in dom7}
    fatal7 = {s:[v for v in range(N) if not (s >> v) & 1 and not any((t >> v) & 1 for t in options7[s])]
              for s in dom7}
    bad = {s for s in dom7 if fatal7[s]}
    good = set7 - bad
    assert len(good)==760 and len(bad)==20
    assert all(len(fatal7[s])==1 for s in bad)
    assert sorted(fatal7[s][0] for s in bad)==list(range(20))
    shellbad = {shells(v)[1] | shells(v)[4] | shells(v)[5]:v for v in range(N)}
    assert set(shellbad)==bad
    assert all(fatal7[s] == [shellbad[s]] for s in bad)
    assert [m.bit_count() for m in shells(0)] == [1,3,6,6,3,1]

    witness=[]
    min_responses=100000
    for s in sorted(good):
        response=[]
        for v in range(N):
            if (s >> v)&1:continue
            goodtargets=sorted(t for t in options7[s] if t in good and (t >> v) & 1)
            assert goodtargets, (s,v)
            min_responses=min(min_responses,len(goodtargets))
            response.append([v,goodtargets[0]])
        assert len(response)==13
        witness.append([s,response])

    certificate = {
      'format':'dodecahedral-eternal-domination-v1',
      'vertices':list(range(N)),
      'edges':[list(e) for e in EDGES],
      'dominating_counts_1_through_5':dom_small,
      'dominating_six':dom6,
      'fatal_attacks_six':fatal6,
      'dominating_seven':dom7,
      'bad_seven':[[s,fatal7[s][0]] for s in sorted(bad)],
      'good_seven_winning_response_table':witness,
      'min_good_responses_per_attack':min_responses,
    }
    path = sys.argv[1] if len(sys.argv)>1 else 'certificate.json'
    with open(path,'w',encoding='utf-8',newline='\n') as f:
        json.dump(certificate,f,sort_keys=True,separators=(',',':'),ensure_ascii=True)
        f.write('\n')
    with open(path,'rb') as f:
        raw=f.read()
    print('domination_counts='+str(dom_small))
    print('dom6='+str(len(dom6))+' dom7='+str(len(dom7)))
    print('bad7='+str(len(bad))+' safe7='+str(len(good)))
    print('shells='+str([shells(0)[i].bit_count() for i in range(6)]))
    print('fatal6_per_state='+str(collections.Counter(len(x[1]) for x in fatal6)))
    print('fatal7_per_state='+str(collections.Counter(len(v) for v in fatal7.values())))
    print('minimum_safe_response_choices='+str(min_responses))
    print('certificate_bytes='+str(len(raw)))
    print('certificate_sha256='+hashlib.sha256(raw).hexdigest())

if __name__ == '__main__':
    run()
