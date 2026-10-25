#!/usr/bin/env python3
"""Exact smooth-pencil and projectivity-orbit census for O(2,3) on P1xP1/F2.

Use: python enumerate_pencils.py [catalogue-output.csv]
Requires only Python 3.10+ and gf2_ideal.py in the same directory.
"""
from collections import Counter
from itertools import combinations, product
import csv, json, sys
from gf2_ideal import smooth

S={mask for mask in range(1,4096) if smooth(mask)}
assert len(S)==1116
P={tuple(sorted((a,b,a^b))) for a,b in combinations(sorted(S),2) if a^b in S}
assert len(P)==44070

rpoints=((1,0),(0,1),(1,1))
points=tuple((p,q) for p in rpoints for q in rpoints)

def evaluate(F,p,q):
    a,b=p; c,d=q
    result=0
    for i in range(3):
        for j in range(4):
            if (F>>(4*i+j))&1:
                result ^= a**(2-i)*b**i*c**(3-j)*d**j
    return result

def basecount(pencil):
    A,B,_=pencil
    return sum(evaluate(A,p,q)==evaluate(B,p,q)==0 for p,q in points)

basehist=Counter(basecount(p) for p in P)
assert dict(basehist)=={0:6066,1:16884,2:17424,3:3696}

# Full automorphism group preserving the bidegree class O(2,3) is
# PGL2(F2) x PGL2(F2), of order 6*6=36.
GL2=[(a,b,c,d) for a,b,c,d in product((0,1),repeat=4) if (a*d^b*c)]
assert len(GL2)==6

def mul(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            e=(i+k,j+l)
            C[e]=C.get(e,0)^(a&b)
    return {m:v for m,v in C.items() if v}

def powpoly(A,k):
    P={(0,0):1}
    for _ in range(k):P=mul(P,A)
    return P

def action_table(M,N):
    X0={(1,0):M[0],(0,1):M[1]}
    X1={(1,0):M[2],(0,1):M[3]}
    Y0={(1,0):N[0],(0,1):N[1]}
    Y1={(1,0):N[2],(0,1):N[3]}
    cols=[]
    for i in range(3):
        for j in range(4):
            A=mul(powpoly(X0,2-i),powpoly(X1,i))
            B=mul(powpoly(Y0,3-j),powpoly(Y1,j))
            C=0
            for (a,b) in A:
                for (c,d) in B:C^=1<<(4*b+d)
            cols.append(C)
    table=[0]*4096
    for x in range(1,4096):
        lsb=x&-x
        table[x]=table[x^lsb]^cols[lsb.bit_length()-1]
    return table

T=[action_table(M,N) for M in GL2 for N in GL2]
assert len(T)==36
assert all({f[x] for x in S}==S for f in T)

unseen=P.copy()
orbits=[]
while unseen:
    p=min(unseen)
    orbit={tuple(sorted(f[x] for x in p)) for f in T}
    assert orbit<=P
    rep=min(orbit)
    orbits.append((rep,len(orbit),basecount(rep)))
    unseen-=orbit
orbits.sort()
orbit_hist=Counter(size for _,size,_ in orbits)
assert dict(orbit_hist)=={6:1,12:3,18:30,36:1208}
assert len(orbits)==1242
assert sum(size for _,size,_ in orbits)==44070
assert Counter({k:sum(size for rep,size,b in orbits if b==k) for k in range(4)}) == basehist

if len(sys.argv)>1:
    with open(sys.argv[1],'w',newline='',encoding='utf8') as h:
        w=csv.writer(h)
        w.writerow(['form_mask_1','form_mask_2','form_mask_3','orbit_size','rational_base_points'])
        w.writerows((a,b,c,size,base) for (a,b,c),size,base in orbits)

stats={
 'sections_total_nonzero':4095,
 'smooth_sections':len(S),
 'pencils_all_smooth':len(P),
 'pencil_projective_orbits':len(orbits),
 'orbit_size_frequencies':{str(k):v for k,v in sorted(orbit_hist.items())},
 'rational_base_point_frequencies':{str(k):v for k,v in sorted(basehist.items())},
 'orbit_size_by_base_point_count':{str(k):{str(sz):sum(1 for _,s,b in orbits if s==sz and b==k) for sz in (6,12,18,36) if any(s==sz and b==k for _,s,b in orbits)} for k in range(4)},
 'all_smooth_pencil_members':3,
 'full_linear_system_coordinate_group_order':36,
}
print(json.dumps(stats,indent=2,sort_keys=True))
