#!/usr/bin/env python3
"""Reproducibility checks for geometric path-reflection fixed complexes.
No external files or libraries required.
"""
from itertools import combinations
from collections import defaultdict

def valid(bits):
    return all(not (bits[i] and bits[i+1] and bits[i+2]) for i in range(len(bits)-2))

def orbit_faces(n):
    orbits=[]
    seen=set()
    for i in range(n):
        if i not in seen:
            o={i,n-1-i}
            seen.update(o)
            orbits.append(o)
    faces=set()
    for mask in range(1<<len(orbits)):
        selected=set().union(*(o for i,o in enumerate(orbits) if mask>>i&1)) if mask else set()
        word=[int(i in selected) for i in range(n)]
        if valid(word):faces.add(mask)
    return orbits,faces

def model_faces(n,orbits):
    k=len(orbits)
    faces=set()
    for mask in range(1<<k):
        # Independent modelling: constrained binary half-words, no orbit-to-original expansion.
        if n%2==0:
            m=n//2
            b=[(mask>>i)&1 for i in range(m)]
            ok=valid(b) and not (m>=2 and b[m-2] and b[m-1])
        else:
            m=n//2
            # Orbit order from left endpoint to centre: b_m,...,b_1,c
            b=[(mask>>(m-1-j))&1 for j in range(m)] # b1,...,bm
            c=(mask>>m)&1
            ok=valid(b) and not (m>=1 and c and b[0])
        if ok:faces.add(mask)
    return faces

def homology_f2(faces,k):
    by=defaultdict(list)
    for mask in faces:
        by[mask.bit_count()-1].append(mask)
    ranks={}
    for d in range(1,max(by, default=-1)+1):
        lows={b:i for i,b in enumerate(by[d-1])}
        basis={}
        for f in by[d]:
            x=0
            for i in range(k):
                if f & (1<<i): x^=1<<lows[f^(1<<i)]
            while x:
                p=x.bit_length()-1
                if p not in basis: basis[p]=x; break
                x^=basis[p]
        ranks[d]=len(basis)
    return {d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0) for d,fs in by.items() if d>=0}

def prediction(n):
    m=(n+1)//2
    return {m//2-1:1} if m%2==0 else {}

def main():
    tested=0
    for n in range(1,26):
        orbits,faces=orbit_faces(n)
        model=model_faces(n,orbits)
        assert faces==model,(n,len(faces),len(model),faces^model)
        tested+=len(faces)
        if n<=21:
            bet=homology_f2(faces,len(orbits))
            reduced={d:v for d,v in bet.items() if (d!=0 and v) or (d==0 and v>1)}
            reduced={d:(v-1 if d==0 else v) for d,v in reduced.items()}
            assert reduced==prediction(n),(n,reduced,prediction(n))
            print(f'{n:2d} orbit_vertices={len(orbits):2d} faces={len(faces):4d} reduced_betti={reduced}')
    print('PASS: 25 exact orbit-description comparisons; 21 mod-two homology comparisons; total admissible orbit subsets:',tested)
if __name__=='__main__':main()
