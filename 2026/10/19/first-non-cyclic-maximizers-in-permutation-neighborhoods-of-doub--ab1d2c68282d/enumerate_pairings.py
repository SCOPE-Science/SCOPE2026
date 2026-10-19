"""Independent exact census, recursively enumerating perfect matchings.

For each matching all 2^k assignments of one endpoint per letter to the
first subsequence are explored, inducing precisely the incident permutations.
"""
import argparse
from collections import defaultdict
import json


def matchings(positions):
    if not positions:
        yield ()
        return
    first = positions[0]
    for j in range(1,len(positions)):
        second = positions[j]
        for tail in matchings(positions[1:j]+positions[j+1:]):
            yield ((first,second),)+tail


def run(k):
    if not 1 <= k <= 6:
        raise ValueError('The verified range is 1..6')
    degree = defaultdict(int)
    count = 0
    for matching in matchings(tuple(range(2*k))):
        count+=1
        matching = tuple(sorted(matching))
        letters = [None]*(2*k)
        for i,(u,v) in enumerate(matching):
            letters[u] = letters[v] = i
        for_split=set()
        for bits in range(1<<k):
            chosen = {matching[i][(bits>>i)&1] for i in range(k)}
            A = tuple(letters[j] for j in range(2*k) if j in chosen)
            B = tuple(letters[j] for j in range(2*k) if j not in chosen)
            locations = {a:i for i,a in enumerate(B)}
            gamma = tuple(locations[a] for a in A)
            for_split.add(''.join(str(j+1) for j in gamma))
        for gamma in for_split:
            degree[gamma]+=1
    assert count == __import__('math').prod(range(1,2*k,2))
    return dict(degree)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('k',type=int)
    print(json.dumps(run(parser.parse_args().k),sort_keys=True,separators=(',',':')))
