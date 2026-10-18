"""Graph-level color refinement, independent of the orbit-quotient implementation."""
from collections import defaultdict
from itertools import product


def run_graph(sizes):
    v = list(product(*(range(q) for q in sizes)))
    id_of = {x:i for i,x in enumerate(v)}
    adj = [[] for _ in v]
    for i,x in enumerate(v):
        for coordinate,q in enumerate(sizes):
            for symbol in range(q):
                if symbol != x[coordinate]:
                    y = x[:coordinate]+(symbol,)+x[coordinate+1:]
                    adj[i].append(id_of[y])
    color = [int(any(x)) for x in v]
    number_factors = len(sizes)
    number_distinct = len(set(sizes))
    stable_round = number_factors if number_distinct>1 else number_factors-1
    labels = tuple(sorted(set(sizes)))
    for t in range(stable_round+2):
        expected_classes = defaultdict(set)
        observed_classes = defaultdict(set)
        for i, x in enumerate(v):
            weight = sum(z != 0 for z in x)
            profile = tuple(sum(z != 0 and sizes[j]==q for j,z in enumerate(x)) for q in labels)
            if t >= number_factors or weight < t:
                expected_key = ('orbit', profile)
            elif weight == t:
                expected_key = ('shell',t)
            else:
                expected_key = ('outside',)
            observed_classes[color[i]].add(i)
            expected_classes[expected_key].add(i)
        assert {frozenset(s) for s in expected_classes.values()} == {frozenset(s) for s in observed_classes.values()}, (sizes,t)
        signatures = []
        for i in range(len(v)):
            multiplicities = defaultdict(int)
            for j in adj[i]:
                multiplicities[color[j]] += 1
            signatures.append((color[i], tuple(sorted(multiplicities.items()))))
        keys = {s:k for k,s in enumerate(sorted(set(signatures)))}
        nxt = [keys[s] for s in signatures]
        if t < stable_round:
            assert len(set(nxt)) > len(set(color)),(sizes,t)
        else:
            assert len(set(nxt)) == len(set(color)),(sizes,t)
        color = nxt
    return len(v), len(set(color)), stable_round


def main():
    samples = [(2,), (3,), (2,2), (2,3), (3,4), (2,2,2), (2,2,3), (2,3,4),
               (2,2,2,2), (2,2,3,3), (3,3,4,4), (2,3,4,5),
               (2,2,2,2,2,3), (2,2,3,3,3,4), (2,3,3,4,4),
               (2,3,4,5,6), (3,4,5,6), (2,2,2,2,2,2,3,3)]
    visited = 0
    for sizes in samples:
        num,cl,depth = run_graph(sizes)
        visited += num
        print(f'{sizes}: vertices={num}, classes={cl}, depth={depth}')
    print(f'PASS graph-level partition/replay for {len(samples)} products and {visited} vertices')

if __name__=='__main__':
    main()
