#!/usr/bin/env python3
"""Self-contained finite cross-checks for sparse binary closed factors."""
from itertools import combinations

def is_closed(w):
    if len(w) <= 1:
        return True
    for h in range(1, len(w)):
        v = w[:h]
        if v != w[-h:]:
            continue
        if sum(w[t:t+h] == v for t in range(len(w)-h+1)) == 2:
            return True
    return False

def brute_closed(w):
    return {w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1) if is_closed(w[i:j])}

def predicted_closed(a,b,c):
    w='0'*a+'1'+'0'*b+'1'+'0'*c
    out = {'0'*r for r in range(1,max(a,b,c)+1)} | {'1'}
    out |= {'0'*r+'1'+'0'*r for r in range(1, min(b,max(a,c))+1)}
    for i in range(a+1):
        for j in range(c+1):
            if i == j or (i<=b and j<=b):
                out.add('0'*i+'1'+'0'*b+'1'+'0'*j)
    return out

def formula(a,b,c):
    x=min(a,b); y=min(c,b)
    return a+b+c+2 + max(x,y)*(min(x,y)+1)

def optimum(n):
    s=n-2; k,r=divmod(s,3)
    extra={0:k*(k+1),1:k*(k+1),2:(k+1)**2}[r]
    if r==0:return n+extra,{(k,k,k)}
    if r==1:
        triples={(k+1,k,k),(k,k+1,k),(k,k,k+1)}
        if k>=1: triples.update({(k-1,k+1,k+1),(k+1,k+1,k-1)})
        return n+extra,triples
    return n+extra,{(k,k+1,k+1),(k+1,k+1,k)}

def run():
    checked=0
    for n in range(2,17):
        s=n-2
        actual=[]
        for a in range(s+1):
            for b in range(s-a+1):
                c=s-a-b
                w='0'*a+'1'+'0'*b+'1'+'0'*c
                brute=brute_closed(w)
                predicted=predicted_closed(a,b,c)
                assert brute==predicted,('set discrepancy',n,a,b,c,brute^predicted)
                assert len(brute)==formula(a,b,c),('count discrepancy',n,a,b,c)
                actual.append((len(brute),(a,b,c)))
                checked+=1
        value,winners=optimum(n)
        assert max(v for v,_ in actual)==value,('maximum discrepancy',n)
        assert {t for v,t in actual if v==value}==winners,('optimizer discrepancy',n)
    for n in range(17,101):
        s=n-2
        actual=[]
        for a in range(s+1):
            for b in range(s-a+1):
                c=s-a-b
                actual.append((formula(a,b,c),(a,b,c)))
        value,winners=optimum(n)
        assert max(v for v,_ in actual)==value,('large formula maximum',n)
        assert {t for v,t in actual if v==value}==winners,('large formula optimizers',n)
    for n in range(1,35):
        assert all(len(brute_closed('0'*a+'1'+'0'*(n-1-a)))==n for a in range(n))
        assert len(brute_closed('0'*n))==n
    print('CHECK_OK',checked,'independent complete factor-set comparisons for weight 2, n=2..16;',
          'all formula optimizer claims through n=100; singleton and zero-weight through n=34')
if __name__=='__main__':run()
