"""Exact-rational reproducibility checks for two-state monotone affine witnesses."""
from fractions import Fraction as Q
from itertools import product, combinations


def witness(block_lengths, unused=0):
    assert block_lengths and all(t >= 1 for t in block_lengths)
    n = sum(block_lengths)
    k = len(block_lengths)
    eps = Q(1, 2 ** (2*n + 10))
    maps = [(Q(1, 2), Q(1, 4))]  # p,q: f(x)=p*x+q
    states = [Q(0)]
    cuts = []
    word = []
    for i, count in enumerate(block_lengths):
        p, q = maps[-1]
        for _ in range(count):
            states.append(p*states[-1]+q)
            word.append(i)
        if i+1 < k:
            cut = (states[-2]+states[-1])/2
            cuts.append(cut)
            maps.append((p+eps, q-eps*cut))
    maps += [(Q(0), Q(0))] * unused
    assert all(0 <= q <= q+p <= 1 for p,q in maps)
    assert all(states[j] < states[j+1] < Q(1,2) for j in range(n))
    assert all(cuts[i] < cuts[i+1] for i in range(len(cuts)-1))
    for j in range(n):
        vals = [p*states[j]+q for p,q in maps]
        assert vals[word[j]] > max(v for a,v in enumerate(vals) if a != word[j]) if len(maps)>1 else True
        assert vals[word[j]] == states[j+1]
    return tuple(word), maps, states


def value(z, maps):
    x = Q(0)
    for a in z:
        p,q=maps[a]
        x=p*x+q
    return x


def exact_tests():
    cases = total = 0
    for n in range(1,8):
        for k in range(1, min(n,4)+1):
            for cuts in combinations(range(1,n), k-1):
                block_lengths = tuple(b-a for a,b in zip((0,)+cuts,cuts+(n,)))
                word, maps, states = witness(block_lengths, unused=int(k==1))
                win = states[-1]
                for z in product(range(len(maps)), repeat=n):
                    actual=value(z,maps)
                    assert (actual == win) == (z == word), (block_lengths,z)
                    assert actual <= win, (block_lengths,z, actual,win)
                    total += 1
                cases += 1
    for blocks in [(1,)*20,(3,)*10,(1,5,2,8,3,7),(40,), (20,20,20)]:
        word, maps, states = witness(blocks,unused=1)
        assert len(word)==sum(blocks)
        cases+=1
    print(f"PASS {cases} block profiles; {total} exactly compared competitor words; long profiles passed exact local inequalities")

if __name__=='__main__':
    exact_tests()
