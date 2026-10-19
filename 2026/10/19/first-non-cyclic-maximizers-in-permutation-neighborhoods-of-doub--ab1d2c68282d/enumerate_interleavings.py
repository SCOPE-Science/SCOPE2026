"""Exact permutation-neighborhood census via ordered shuffles.

A size-k pair partition of positions is represented as a sorted tuple of
k ordered pairs. Each word on k distinct twice-used letters determines one.
"""
import argparse
import itertools
import json


def run(k):
    if not 1 <= k <= 6:
        raise ValueError('The verified range is 1..6')
    masks = tuple(itertools.combinations(range(2*k), k))
    result = {}
    for gamma in itertools.permutations(range(k)):
        reverse_position = [0]*k
        for i,j in enumerate(gamma):
            reverse_position[j] = i
        B = tuple(reverse_position)
        present = set()
        for positions in masks:
            chosen = set(positions)
            sourceA = iter(range(k))
            sourceB = iter(B)
            starts = [-1]*k
            pairs = [None]*k
            for pos in range(2*k):
                symbol = next(sourceA) if pos in chosen else next(sourceB)
                if starts[symbol] == -1:
                    starts[symbol] = pos
                else:
                    pairs[symbol] = (starts[symbol],pos)
            assert all(pair is not None for pair in pairs)
            present.add(tuple(sorted(pairs)))
        result[''.join(str(j+1) for j in gamma)] = len(present)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('k',type=int)
    print(json.dumps(run(parser.parse_args().k),sort_keys=True,separators=(',',':')))
