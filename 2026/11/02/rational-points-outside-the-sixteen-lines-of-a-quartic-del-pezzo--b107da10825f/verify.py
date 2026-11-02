#!/usr/bin/env python3
"""Exact finite verification of signed-cycle point-count formulas for quartic del Pezzo complements.

Uses only the Python standard library. The table is exhaustive in the Weyl group W(D5)
represented by the 1920 even signed permutations on five coordinates.
"""
from itertools import permutations, combinations
from collections import Counter

N=5
V=tuple(x for x in range(1<<N) if x.bit_count()%2==0)
EDGES=tuple((a,b) for a,b in combinations(V,2) if (a^b).bit_count()==4)
assert len(V)==16 and len(EDGES)==40

def signed_cycles(p,s):
    seen=set(); pos=[]; neg=[]
    for i in range(N):
        if i in seen: continue
        j=i; length=0; sign=1
        while j not in seen:
            seen.add(j); length+=1
            sign *= -1 if (s>>j)&1 else 1
            j=p[j]
        (pos if sign==1 else neg).append(length)
    return (tuple(sorted(pos,reverse=True)),tuple(sorted(neg,reverse=True)))

def act(x,p,s):
    y=s
    for i in range(N):
        if (x>>i)&1: y ^= 1<<p[i]
    return y

def invariants(p,s):
    action={x:act(x,p,s) for x in V}
    assert set(action.values())==set(V)
    fix=sum(action[v]==v for v in V)
    ff=sum(action[a]==a and action[b]==b for a,b in EDGES)
    sw=sum(action[a]==b and action[b]==a for a,b in EDGES)
    trace=sum((-1 if (s>>i)&1 else 1) for i in range(N) if p[i]==i)
    return (fix,ff,sw,trace)

# First entry of every pair is positive-cycle partition, second negative-cycle partition.
# Table columns: signed-cycle type; number of group elements; f, e_ff, e_sw, t.
EXPECTED={
 ((1,1,1,1,1),()):(1,16,40,0,5),
 ((2,1,1,1),()):(20,8,12,0,3),
 ((2,2,1),()):(60,4,2,2,1),
 ((3,1,1),()):(80,4,4,0,2),
 ((3,2),()):(160,2,0,0,0),
 ((4,1),()):(240,2,1,1,1),
 ((5,),()):(384,1,0,0,0),
 ((1,1,1),(1,1)):(10,0,0,0,1),
 ((1,),(1,1,1,1)):(5,0,0,8,-3),
 ((1,1),(2,1)):(60,0,0,0,1),
 ((1,),(2,2)):(60,0,0,0,1),
 ((1,),(3,1)):(160,0,0,2,0),
 ((),(2,1,1,1)):(20,0,0,0,-3),
 ((2,1),(1,1)):(60,0,0,4,-1),
 ((2,),(2,1)):(120,0,0,0,-1),
 ((3,),(1,1)):(80,0,0,0,-2),
 ((),(3,2)):(160,0,0,0,0),
 ((),(4,1)):(240,0,0,0,-1),
}

def calc():
    seen={}; cnt=Counter(); group_order=0
    for p in permutations(range(N)):
        for s in range(1<<N):
            if s.bit_count()%2: continue
            group_order+=1
            c=signed_cycles(p,s)
            val=invariants(p,s)
            if c in seen: assert seen[c]==val,(c,val,seen[c])
            else: seen[c]=val
            cnt[c]+=1
    assert group_order==120*16==1920
    assert len(seen)==len(EXPECTED)==18
    for c,nums in EXPECTED.items():
        assert (cnt[c],)+seen[c]==nums,(c,cnt[c],seen[c],nums)
    assert sum(cnt.values())==1920
    print('WEYL_D5_EXHAUSTIVE: 1920 even signed permutations in 18 classes')
    print('CLEBSCH_GRAPH: 16 vertices, 40 edges; all 18 class certificates verified')
    for c in sorted(seen,key=str):
        f,ff,sw,t=seen[c]
        A=1+t-f;B=1-f+ff-sw
        print('CLASS',str(c),'SIZE',cnt[c],'FIX',f,'FIXED_EDGES',ff,
              'SWAPPED_EDGES',sw,'ROOT_TRACE',t,'OPEN_POLY',f'1*q^2+({A})*q+({B})')
    # Small-field possibilities: a negative predicted value rules out the group type.
    for q in (2,3,4,5,7,11):
        z=[];bad=[]
        for c,(f,ff,sw,t) in seen.items():
            v=q*q+(1+t-f)*q+1-f+ff-sw
            if v==0:z.append(c)
            if v<0:bad.append(c)
        print('FIELD',q,'ZERO_TYPES',sorted(map(str,z)),'NEGATIVE_NONREALIZABLE',sorted(map(str,bad)))
    assert [c for c,(f,ff,sw,t) in seen.items() if 9+(1+t-f)*3+1-f+ff-sw==0]==[((2,2,1),())]
    assert [c for c,(f,ff,sw,t) in seen.items() if 25+(1+t-f)*5+1-f+ff-sw==0]==[((1,1,1,1,1),())]
    for q in [2,4]+list(range(6,32)):
        assert all(q*q+(1+t-f)*q+1-f+ff-sw!=0 for f,ff,sw,t in seen.values())
    print('ZERO_CLASSIFICATION_OK')
    return seen,cnt

def check_geometric_blowups():
    # F_7 split example: points (1,t,t^2), t=0,1,2,3,4 on a smooth conic.
    p=7
    points=[(1,t,t*t%p) for t in range(5)]
    def cross(a,b):return tuple((a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3])%p for i in range(3))
    lines=[cross(a,b) for a,b in combinations(points,2)]
    plane=[(1,y,z) for y in range(p) for z in range(p)]+[(0,1,z) for z in range(p)]+[(0,0,1)]
    u=[v for v in plane if (v[0]*v[2]-v[1]*v[1])%p and all(sum(i*j for i,j in zip(v,l))%p for l in lines)]
    assert len(u)==(p-5)**2==4
    print('SPLIT_F7_DIRECT_BLOWUP_COMPLEMENT: 4')
    # F_3 example: the five points on a smooth conic have Frobenius type 2^2 1.
    # Use F_9=F_3[i] with i^2=-1; code a+3b for a+b*i.
    def add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    def neg(a):return ((-a)%3)+3*((-(a//3))%3)
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):
        x,y=a%3,a//3;u,v=b%3,b//3
        return (x*u+2*y*v)%3+3*((x*v+y*u)%3)
    def cross9(a,b):return tuple(sub(mul(a[(i+1)%3],b[(i+2)%3]),mul(a[(i+2)%3],b[(i+1)%3])) for i in range(3))
    tt=(0,3,6,4,7) # 0, i, -i, 1+i, 1-i
    bp=[(1,t,mul(t,t)) for t in tt]
    lns=[cross9(a,b) for a,b in combinations(bp,2)]
    plane3=[(1,y,z) for y in range(3) for z in range(3)]+[(0,1,z) for z in range(3)]+[(0,0,1)]
    def dot9(l,v):
        r=0
        for x,y in zip(l,v):r=add(r,mul(x,y))
        return r
    uu=[v for v in plane3 if sub(mul(v[0],v[2]),mul(v[1],v[1]))!=0 and all(dot9(l,v)!=0 for l in lns)]
    assert len(uu)==0
    print('NON_SPLIT_F3_DIRECT_BLOWUP_COMPLEMENT: 0')
    print('VERIFY_OK')

if __name__=='__main__':
    calc();check_geometric_blowups()
