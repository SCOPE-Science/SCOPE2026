#!/usr/bin/env python3
"""Finite search for shelling orders for third-power-cycle three-cut complexes."""
import json
from itertools import combinations
from pathlib import Path


def disconnects(n, triple):
    root = {x:x for x in triple}
    def find(x):
        while root[x] != x:
            x = root[x]
        return x
    for i,j in combinations(triple,2):
        if min((i-j)%n,(j-i)%n) <= 3:
            root[find(i)] = find(j)
    return len({find(x) for x in triple})>1


def facets(n):
    return [((1<<n)-1) ^ sum(1<<v for v in t)
            for t in combinations(range(n),3) if disconnects(n,t)]


def ridges(n,prior,f):
    return sum(1<<v for v in range(n) if (f>>v)&1 and any((f &~(1<<v)) == ((f &~(1<<v)) & g) for g in prior))


def is_legal(prior, f, R):
    return bool(R) and all(R & ~g for g in prior)


def compute_shelling(n):
    F = facets(n)
    sequence=[min(F)];rest=set(F)-set(sequence)
    while rest:
        candidates=[]
        for f in rest:
            R=ridges(n, sequence,f)
            if is_legal(sequence,f,R): candidates.append((R.bit_count(),f))
        if not candidates: raise RuntimeError(f'Stuck at {len(sequence)} / {len(F)}')
        _,chosen=max(candidates)
        sequence.append(chosen);rest.remove(chosen)
    return sequence

if __name__=='__main__':
    data={"schema_version":1,"definition":"Facets are n-bit nonnegative integers; bit v represents vertex v of the 3-cut complex of C_n cubed.","shellings":{str(n):compute_shelling(n) for n in [13,14]}}
    out=Path(__file__).parent/'shellings.json'
    out.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
    print('GENERATED',*[f'{n}:{len(data["shellings"][str(n)])}' for n in [13,14]])
