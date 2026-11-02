#!/usr/bin/env python3
"""Direct finite-field verification of the split three-block commuting-involution graph degree law."""
from itertools import product
from math import prod

def ops(q):
    if q == 4:
        add=lambda a,b:a^b
        def mul(a,b):
            x=(a&1)*(b&1); y=((a>>1)&1)*((b>>1)&1)
            return ((x^y)&1)|((((a&1)*((b>>1)&1))^(((a>>1)&1)*(b&1))^y)<<1)
        return add,mul
    return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q

def run(s,t,q):
    add,mul=ops(q)
    all_x=list(product(range(q),repeat=s*t))
    all_y=list(product(range(q),repeat=t))
    def xy(x,y):
        return tuple(__import__('functools').reduce(add,(mul(x[i*t+j],y[j]) for j in range(t)),0) for i in range(s))
    zero=(0,)*s
    records=[(x,y) for x in all_x for y in all_y if xy(x,y)==zero]
    def rank(x):
        A=[list(x[i*t:(i+1)*t]) for i in range(s)]
        r=0
        for col in range(t):
            p=next((j for j in range(r,s) if A[j][col]),None)
            if p is None: continue
            A[r],A[p]=A[p],A[r]
            for j in range(r+1,s):
                if A[j][col]:
                    v=A[j][col]
                    for k in range(col,t): A[j][k]=add(A[j][k], ((-mul(v,mul(A[r][k],pow(A[r][col],q-2,q))))%q if q!=4 else mul(v,mul(A[r][k],(1 if A[r][col]==1 else (3 if A[r][col]==2 else 2))))))
            r+=1
            if r==s: break
        return r
    # q = 2,3,4,5 supported (q=4 GF4 inverses encoded above)
    for x,y in records:
        actual=sum(xy(x,yy)==xy(xx,y) for xx,yy in records)
        if y == (0,)*t:
            a=rank(x)
            expected=q**(s*t)+(q**(t-a)-1)*q**(s*(t-1))
        else:
            expected=q*q**(s*(t-1))+(q**t-q)*q**(s*(t-2))
        assert actual==expected,(s,t,q,x,y,actual,expected)
    I=q**s * len(records)
    C=q**(2*s)*sum(sum(xy(x,yy)==xy(xx,y) for xx,yy in records) for x,y in records)
    CF=q**(2*s)*(q**(2*s*t)+(q+1)*(q**t-1)*q**(2*s*(t-1))+(q**t-1)*(q**t-q)*q**(s*(2*t-3))) if t>=2 else q**(2*s)*(q**(2*s)+(q*q-1))
    assert C==CF,(s,t,q,C,CF)
    return len(records),I,C

if __name__=='__main__':
    configs=[(1,1,2),(2,1,2),(1,2,2),(2,2,2),(1,3,2),(2,3,2),(1,2,3),(2,2,3),(1,2,4),(1,2,5)]
    checked=0
    for s,t,q in configs:
        info=run(s,t,q)
        checked+=info[0]
        print('OK',s,t,q,info,flush=True)
    print('THREE_BLOCK_INVOLUTION_DEGREE_CENSUS_OK',len(configs),checked)
