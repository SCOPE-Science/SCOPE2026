"""Finite, independent k-variable back-and-forth checks for commuting permutations.
Usage: python check_pebbles.py
No external modules.
"""
from itertools import product, combinations_with_replacement
from collections import Counter
from math import lcm


def torus(a, b, s):
    assert a >= 1 and b >= 1 and 0 <= s < a
    f = []; g = []
    for y in range(b):
        for x in range(a):
            f.append(y*a + (x+1)%a)
            if y+1 < b: g.append((y+1)*a + x)
            else: g.append((x-s)%a)
    return tuple(f), tuple(g)


def direct_sum(parts):
    f=[]; g=[]; off=0
    for (a,b,s) in parts:
        p,q=torus(a,b,s)
        f.extend(off+i for i in p); g.extend(off+i for i in q)
        off+=a*b
    return tuple(f),tuple(g)


def order(f):
    cur=tuple(range(len(f)))
    for i in range(1,100):
        cur=tuple(f[x] for x in cur)
        if all(cur[j]==j for j in range(len(f))):return i
    raise AssertionError('order too big')


def shifts(f,g,A,B):
    n=len(f); result=[]
    for x in range(n):
        track={}; yy=x
        for b in range(B):
            xx=yy
            for a in range(A):
                track[(a,b)]=xx
                xx=f[xx]
            yy=g[yy]
        result.append(track)
    return result


def orbit_spectrum(f,g,A,B,sh):
    remaining=set(range(len(f))); spec=Counter()
    while remaining:
        x=min(remaining); orbit=set(sh[x].values())
        assert orbit<=remaining
        remaining-=orbit
        stabilizer=tuple(z for z,v in sh[x].items() if v==x)
        assert all(tuple(z for z,v in sh[y].items() if v==y)==stabilizer for y in orbit)
        spec[stabilizer]+=1
    return spec


def fixed_point_types(u,v,k,max_iter=50):
    (f,g),(h,j)=u,v
    A=lcm(order(f),order(h)); B=lcm(order(g),order(j))
    shA=shifts(f,g,A,B); shB=shifts(h,j,A,B)
    specA=orbit_spectrum(f,g,A,B,shA)
    specB=orbit_spectrum(h,j,A,B,shB)
    predicted={c:min(m,k) for c,m in specA.items()}=={c:min(m,k) for c,m in specB.items()}
    domains=[len(f),len(h)]
    tuples=[list(product(range(n),repeat=k)) for n in domains]
    indices=[{t:i for i,t in enumerate(ts)} for ts in tuples]
    # Atomic equality of arbitrary composed unary terms is encoded by
    # all bounded displacement equations between each pair of variables.
    atom=[]
    for ts,sh in zip(tuples,[shA,shB]):
        atom.append([tuple(tuple(z for z in sorted(sh[x]) if sh[x][z]==y)
                           for x in t for y in t) for t in ts])
    def canon(keys):
        vocab={key:i for i,key in enumerate(sorted(set(keys),key=repr))}
        return [vocab[key] for key in keys]
    lengths=list(map(len,tuples))
    typ=canon(atom[0]+atom[1])
    iterations=0
    for iterations in range(max_iter):
        split=[typ[:lengths[0]],typ[lengths[0]:]]
        keys=[]
        for side,ts in enumerate(tuples):
            ids=split[side]; idx=indices[side]; n=domains[side]
            for t in ts:
                pos=idx[t]; one=[]
                for i in range(k):
                    vals=set()
                    for a in range(n):
                        nt=t[:i]+(a,)+t[i+1:]
                        vals.add(ids[idx[nt]])
                    one.append(tuple(sorted(vals)))
                keys.append((ids[pos],tuple(one)))
        nxt=canon(keys)
        if len(set(nxt))==len(set(typ)):
            typ=nxt; break
        typ=nxt
    else: raise AssertionError('type refinement failed to stabilize')
    observed=set(typ[:lengths[0]])==set(typ[lengths[0]:])
    return predicted,observed,iterations+1


def main():
    types=[(1,1,0),(2,1,0),(1,2,0),(2,1,1),(3,1,0),(1,3,0),(2,2,0),(2,2,1)]
    # Retain distinct actions with no more than eight elements.
    examples={}
    for r in range(1,4):
        for tup in combinations_with_replacement(types,r):
            n=sum(a*b for a,b,s in tup)
            if n<=8:
                a=direct_sum(tup)
                examples[a]=tup
    examples=list(examples.items())
    # Deterministic coverage of distinct action shapes and edge cases.
    cases=[]
    for i in range(min(40,len(examples))):
        for j in range(i+1,min(40,len(examples))):
            if (i*17+j*13)%7==0:cases.append((examples[i],examples[j]))
    corner=[
        ([(2,2,0)]*2,[(2,2,0)]*3),
        ([(2,2,1)],[(2,2,0)]),
        ([(2,1,0)],[(2,1,0)]*2),
        ([(1,1,0)]*2,[(1,1,0)]*3),
        ([(3,1,0)],[(1,3,0)]),
        ([(1,1,0),(2,1,0)],[(1,1,0),(2,1,0),(2,1,0)]),
    ]
    for left,right in corner:cases.append(((direct_sum(left),left),(direct_sum(right),right)))
    total=0; positives=Counter(); maxround=0
    for (a,ad),(b,bd) in cases:
        if len(a[0])>9 or len(b[0])>9: continue
        for k in (1,2,3):
            predicted,actual,rounds=fixed_point_types(a,b,k)
            assert predicted==actual,(ad,bd,k,predicted,actual)
            total+=1; maxround=max(maxround,rounds)
            positives[(k,actual)]+=1
    print('k-pebble fixed-point comparisons:',total)
    print('equivalent/non-equivalent breakdown:',sorted(positives.items()))
    print('maximum refinement rounds:',maxround)
    print('all predicted truncations matched stable logic types: PASS')

if __name__=='__main__':main()
