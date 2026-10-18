#!/usr/bin/env python3
"""Exact-arithmetic reproducibility checks for a ternary denumerant identity."""

def denumerants(c, end):
    result=[0]*(end+2)
    result[0]=1
    for weight in (2,3,c):
        for n in range(weight,end+2):
            result[n]+=result[n-weight]
    return result

def two_coin(n):
    if n<0: return 0
    return sum((n-3*y)%2==0 for y in range(n//3+1))

def e(k):
    return (-1 if k%6==0 else 1 if k%6 in (1,5) else 0)

def direct_difference(c,n):
    q,r=divmod(n,c)
    return (1 if r==c-1 else 0)+sum(e(r+i*c) for i in range(q+1))

def predicted_last(c):
    if c==1:return 0
    if c%6==1:return 7*c-7
    if c%6==5:return 7*c-5
    return None

def verify():
    count=0
    for m in range(-1,301):
        assert two_coin(m+1)-two_coin(m)==e(m),('pair',m)
        count+=1
    for c in range(1,201):
        end=20*c+30
        vals=denumerants(c,end)
        for n in range(end+1):
            d=vals[n+1]-vals[n]
            assert d==direct_difference(c,n),(c,n,d,direct_difference(c,n))
            count+=1
        t=predicted_last(c)
        if t is not None:
            assert vals[t+1]==vals[t],('boundary',c,t)
            assert all(vals[n+1]>vals[n] for n in range(t+1,end+1)),('tail',c,t)
            assert max(n for n in range(end+1) if vals[n+1]<=vals[n])==t,('last',c,t)
        else:
            for k in (0,1,2,3):
                n=6*c*k
                assert vals[n+1]<vals[n],('persistent',c,k)
    print('VERIFY_OK',count)

if __name__=='__main__':verify()
