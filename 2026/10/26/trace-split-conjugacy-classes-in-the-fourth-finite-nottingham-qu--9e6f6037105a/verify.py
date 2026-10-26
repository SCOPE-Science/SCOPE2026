#!/usr/bin/env python3
"""Direct finite-field checks for low Nottingham quotient conjugacy data.

Run with: python3 nottingham_qeven_verify.py
No external dependencies.
"""
from collections import Counter, defaultdict
from itertools import product
from random import Random

POLY = {2:0b11, 4:0b111, 8:0b1011, 16:0b10011}

def ops(q):
    poly=POLY[q]
    table=[[0]*q for _ in range(q)]
    for x in range(q):
        for y in range(q):
            z=0; a=x; b=y
            while b:
                if b&1: z ^= a
                b >>= 1; a <<= 1
                if a & q: a ^= poly
            table[x][y]=z
    def inv(x):
        assert x
        for z in range(1,q):
            if table[x][z]==1: return z
        assert False
    def trace(x):
        t=0; y=x
        for _ in range(q.bit_length()-1):
            t ^= y
            y=table[y][y]
        assert t in (0,1)
        return t
    return table,inv,trace

def compose(f,g,M):
    # 0-indexed polynomials of length six; directly substitute and truncate.
    powers=[[1,0,0,0,0,0]]
    for _ in range(5):
        z=[0]*6
        for j,uj in enumerate(powers[-1]):
            if uj:
                for k,vk in enumerate(g[:6-j]):
                    z[j+k] ^= M[uj][vk]
        powers.append(z)
    z=[0]*6
    for k,fk in enumerate(f):
        if fk:
            for j,v in enumerate(powers[k]):
                z[j] ^= M[fk][v]
    return z

def action(elem,A,B,M):
    a,b,c,d=elem
    h=b ^ M[a][a]
    delta_c=M[a][M[A][A]] ^ M[h][A] ^ M[a][B]
    delta_d=M[b][M[A][A]] ^ M[M[a][a]][B]
    return (a,b,c ^ delta_c,d ^ delta_d)

def signature(elem,M,inv,trace):
    a,b,c,d=elem
    if a==0 and b==0: return ('center',c,d)
    if a==0: return ('a0',b,d ^ M[inv(b)][M[c][c]])
    h=b ^ M[a][a]
    if not h: return ('h0',a,b,d ^ M[a][c])
    t=d ^ M[a][c]
    den=M[h][M[a][a]]
    return ('generic',a,b,trace(M[t][inv(den)]))

def expected_sizes(q):
    if q==2: return {1:q*q,q:2*q*(q-1)+(q-1)**2*q*q//q}
    return {1:q*q,q:2*q*(q-1),q*q//2:2*(q-1)**2}

def run(q):
    M,inv,trace=ops(q)
    groups=defaultdict(list)
    for elem in product(range(q), repeat=4):
        groups[signature(elem,M,inv,trace)].append(elem)
    sizes=Counter(len(z) for z in groups.values())
    assert sizes == expected_sizes(q),(q,sizes,expected_sizes(q))
    assert len(groups)==5*q*q-6*q+2
    assert sum(k*n for k,n in sizes.items())==q**4
    for key,members in groups.items():
        a,b,c,d=members[0]
        orbit={action((a,b,c,d),A,B,M) for A in range(q) for B in range(q)}
        assert orbit==set(members),(q,key,len(orbit),len(members))
    rng=Random(57101+q)
    checks=0
    if q in (2,4):
        cases=list(product(range(q),repeat=4))
        pairs=((f,g) for f in cases for g in cases)
    else:
        pairs=((tuple(rng.randrange(q) for _ in range(4)),
                tuple(rng.randrange(q) for _ in range(4))) for _ in range(4000))
    for f,g in pairs:
        a,b,c,d=f; A,B,C,D=g
        F=[0,1,a,b,c,d]; G=[0,1,A,B,C,D]
        fg=compose(F,G,M); gf=compose(G,F,M)
        h=b ^ M[a][a]
        pred= (M[a][M[A][A]] ^ M[h][A] ^ M[a][B]==0 and
               M[b][M[A][A]] ^ M[M[a][a]][B]==0)
        assert (fg==gf)==pred
        fp=action(f,A,B,M)
        assert compose([0,1,*fp],G,M)==gf
        checks+=1
    print(f'q={q}: classes={len(groups)} sizes={dict(sorted(sizes.items()))} direct_pairs={checks} OK')

if __name__=='__main__':
    for q in POLY: run(q)
    print('NOTTINGHAM_QEVEN_CONJUGACY_OK')
