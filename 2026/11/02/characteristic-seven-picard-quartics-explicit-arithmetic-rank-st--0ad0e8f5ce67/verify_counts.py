#!/usr/bin/env python3
"""Independent finite-field point-count check for characteristic-seven Picard quartics.
Uses only integer polynomial arithmetic; no symbolic Cartier routines.
"""
from collections import Counter

P=7

def field_data(n):
    mods={1:[0,1],2:[1,0,1],3:[1,1,0,1]}
    poly=mods[n]
    q=P**n
    digits=[tuple((v//(P**j))%P for j in range(n)) for v in range(q)]
    encode=lambda v:sum(v[j]*P**j for j in range(n))
    add=[[encode(tuple((digits[x][j]+digits[y][j])%P for j in range(n))) for y in range(q)] for x in range(q)]
    mul=[]
    for x in range(q):
        row=[]
        for y in range(q):
            tmp=[0]*(2*n-1)
            for i,xx in enumerate(digits[x]):
                for j,yy in enumerate(digits[y]):tmp[i+j]=(tmp[i+j]+xx*yy)%P
            for degree in range(len(tmp)-1,n-1,-1):
                z=tmp[degree]
                for j in range(n):tmp[degree-n+j]=(tmp[degree-n+j]-z*poly[j])%P
            row.append(encode(tuple(tmp[:n])))
        mul.append(row)
    cube=[0]*q
    for y in range(q):cube[mul[mul[y][y]][y]]+=1
    squared=[mul[x][x] for x in range(q)]
    fourth=[mul[squared[x]][squared[x]] for x in range(q)]
    return add,mul,cube,squared,fourth

def point_count(field,a,b,c):
    add,mul,cube,sq,fourth=field
    n=len(cube)
    total=1
    for x in range(n):
        fx=add[fourth[x]][mul[a][sq[x]]]
        fx=add[fx][mul[b][x]]
        fx=add[fx][c]
        total+=cube[fx]
    return total

def quartic_smooth(a,b,c):
    # Independent polynomial gcd over F7, with high-degree-first normalization
    f=[c,b,a,0,1]
    df=[b,(2*a)%7,0,4]
    def trimmed(v):
        while v and v[-1]==0:v.pop()
        return v
    def rem(u,v):
        u=trimmed(u[:]);v=trimmed(v[:])
        while u and len(u)>=len(v):
            coeff=u[-1]*pow(v[-1],-1,7)%7
            sh=len(u)-len(v)
            for j,w in enumerate(v):u[sh+j]=(u[sh+j]-coeff*w)%7
            trimmed(u)
        return u
    f=trimmed(f);df=trimmed(df)
    while df:f,df=df,rem(f,df)
    return len(f)==1

fields=[field_data(n) for n in (1,2,3)]
counts=Counter()
examples={}
for a in range(P):
    for b in range(P):
        for c in range(P):
            if not quartic_smooth(a,b,c):continue
            N=[point_count(fields[n-1],a,b,c) for n in (1,2,3)]
            S=[N[n-1]-(7**n+1) for n in (1,2,3)]
            L1=S[0];L2=(S[0]*L1+S[1])//2;L3=(S[0]*L2+S[1]*L1+S[2])//3
            pr=max([i for i,Li in enumerate([L1,L2,L3],start=1) if Li%7] or [0])
            key=(a,b,c)
            predicted=3 if a else (0 if c==0 or (b**4-4*c**3)%7==0 else 1)
            assert pr==predicted,(key,N,[L1,L2,L3],pr,predicted)
            counts[pr]+=1
            examples.setdefault(pr,(key,N,[L1,L2,L3]))
assert counts=={0:12,1:30,3:252},counts
print('POINT_COUNTS_OK',dict(counts))
print('EXAMPLES',examples)
