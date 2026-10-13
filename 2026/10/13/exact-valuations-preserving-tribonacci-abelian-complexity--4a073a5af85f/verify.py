#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json

MU={'0':'01','1':'02','2':'0'}
def morph(w): return ''.join(MU[c] for c in w)
def pv(w): return tuple(w.count(str(i)) for i in range(3))
def wsum(w,a): return sum(a[int(c)] for c in w)

w='0'
for _ in range(22):
    w=morph(w)
assert len(w)>300000

pairs={
 'mid0':('102010102','001020100',(2,-1,-1)),
 'mid1':('020','101',(-1,2,-1)),
 'mid2':('01001','20102',(-1,-1,2)),
}
for key,(u,v,d) in pairs.items():
    assert w.find(u)>=0 and w.find(v)>=0,(key,u,v)
    got=tuple(pv(v)[i]-pv(u)[i] for i in range(3))
    assert got==d,(key,got,d,pv(u),pv(v))

# Pure integer geometry forced by equal length plus 2-balance.
D=[]
for d in product(range(-2,3),repeat=3):
    if d!=(0,0,0) and sum(d)==0:
        D.append(d)
assert len(D)==18
for d in D:
    nz=[x for x in d if x]
    if 0 in d:
        # The only zero-coordinate directions are equality directions.
        assert sorted(abs(x) for x in nz) in ([1,1],[2,2])
    else:
        # Otherwise one coordinate has magnitude two and the others magnitude one.
        assert sorted(abs(x) for x in d)==[1,1,2]

# For all small integer valuations, the algebraic no-collision criterion over
# every possible 2-balanced Parikh difference is exactly distinct + non-AP.
def good(a):
    return len(set(a))==3 and all(2*a[i] != a[(i+1)%3]+a[(i+2)%3] for i in range(3))
def no_kernel(a):
    return all(sum(a[i]*d[i] for i in range(3)) != 0 for d in D)
for a in product(range(9),repeat=3):
    assert good(a)==no_kernel(a),(a,good(a),no_kernel(a))

# Direct finite stress check on the actual Tribonacci language.  Prefix counts
# avoid any assumption about the displayed witness factors.
N=120000
x=w[:N]
pref=[[0]*(N+1) for _ in range(3)]
for i,ch in enumerate(x):
    for a in range(3): pref[a][i+1]=pref[a][i]
    pref[int(ch)][i+1]+=1

def parikh(i,n):
    return tuple(pref[a][i+n]-pref[a][i] for a in range(3))

factor_vectors={}
for n in range(1,121):
    s={parikh(i,n) for i in range(N-n+1)}
    factor_vectors[n]=s
    for p in s:
        for q in s:
            assert all(abs(p[j]-q[j])<=2 for j in range(3)),(n,p,q)

# Compare additive and abelian class counts for a representative box of
# valuations through length 120.  This is supplementary to the symbolic proof.
for a in product(range(5),repeat=3):
    for n,s in factor_vectors.items():
        ab=len(s)
        ad=len({sum(a[j]*p[j] for j in range(3)) for p in s})
        if good(a):
            assert ad==ab,(a,n,ad,ab)
    if not good(a):
        # Exact witnesses force a strict collision at length 1, 3, 5, or 9.
        if len(set(a))<3:
            assert len({a[0],a[1],a[2]})<3
        else:
            if 2*a[0]==a[1]+a[2]: u,v=pairs['mid0'][:2]
            elif 2*a[1]==a[0]+a[2]: u,v=pairs['mid1'][:2]
            else:
                assert 2*a[2]==a[0]+a[1]
                u,v=pairs['mid2'][:2]
            assert pv(u)!=pv(v) and wsum(u,a)==wsum(v,a)

cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text(encoding='utf-8'))
assert cert['source_primary_msc']=='68R15'
print('VERIFY_OK witnesses=3 difference_vectors=18 valuations_0..8=729 '
      'direct_prefix=120000 lengths=1..120 valuations_0..4=125 '
      'classification=distinct_and_non_arithmetic_progression')
