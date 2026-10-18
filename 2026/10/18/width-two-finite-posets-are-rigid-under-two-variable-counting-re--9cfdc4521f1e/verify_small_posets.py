#!/usr/bin/env python3
"""Exhaustive independent small-poset check for counting refinement."""
import collections
import hashlib
import itertools

def strict_transitive(n, rows):
    return all(not (rows[j] & ~rows[i]) for i in range(n)
               for j in range(n) if (rows[i] >> j) & 1)

def width_at_most_two(n, rows):
    for a,b,c in itertools.combinations(range(n),3):
        if not any((rows[x] >> y) & 1 or (rows[y] >> x) & 1
                   for x,y in ((a,b),(a,c),(b,c))):
            return False
    return True

def fingerprint(n, rows):
    # Uniform deterministic fingerprints, meaningful across structures.
    colors=[b'']*n
    for _ in range(n+1):
        news=[]
        for x in range(n):
            counts=collections.Counter((colors[y], 0 if rows[x] >> y & 1
                   else 1 if rows[y] >> x & 1 else 2)
                   for y in range(n) if y != x)
            profile=(colors[x],tuple(sorted((c,k,v) for (c,k),v in counts.items())))
            news.append(hashlib.sha256(repr(profile).encode('utf8')).digest())
        colors=news
    return tuple(sorted(colors))

def isomorphic(n, rows, other):
    return any(all(((rows[x] >> y) & 1) == ((other[p[x]] >> p[y]) & 1)
                   for x in range(n) for y in range(n))
               for p in itertools.permutations(range(n)))

def main():
    for n in range(1,7):
        pairs=list(itertools.combinations(range(n),2))
        groups={}
        total=two=0
        for mask in range(1<<len(pairs)):
            rows=[0]*n
            for bit,(i,j) in enumerate(pairs):
                if mask >> bit & 1: rows[i] |= 1<<j
            if not strict_transitive(n, rows): continue
            total += 1
            w2=width_at_most_two(n, rows)
            two += w2
            key=fingerprint(n,rows)
            groups.setdefault(key,[]).append((tuple(rows),w2))
        checked=0
        for group in groups.values():
            examples=[row for row,w2 in group if w2]
            if not examples: continue
            representative=examples[0]
            for other,_ in group:
                checked += 1
                assert isomorphic(n,representative,other), (n,representative,other)
        print(f'n={n} naturally_labelled_posets={total} width_le_2={two} fingerprints={len(groups)} matching_competitors={checked}')
    print('SMALL_POSETS_OK')
if __name__=='__main__':main()
