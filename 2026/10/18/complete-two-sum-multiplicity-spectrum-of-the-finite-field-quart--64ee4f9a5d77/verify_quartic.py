#!/usr/bin/env python3
"""Exhaustive direct finite-field check of quartic graph twofold fibers."""
from collections import Counter

def predicted(q, chi):
    eps=chi(-1); eta=chi(-6); delta=chi(-3)
    g=4 if q%4==1 else 2
    A=(q-4-2*eta-eps-2*delta)//8
    B=(q-4+2*eta-eps+2*delta)//8
    C=(q-2+eps)//4
    assert 8*A==q-4-2*eta-eps-2*delta
    assert 8*B==q-4+2*eta-eps+2*delta
    assert 4*C==q-2+eps
    arr=[(q-1)*((q-1)//2+B+(1-delta)//2)+(q-1)-(q-1)//g,
         1+(q-1)*(1-eta)//2,
         (q-1)*(C+(1+delta)//2)+(q-1)//2*(g==2),
         (q-1)*(1+eta)//2,
         (q-1)*A+(q-1)//4*(g==4)]
    assert sum(arr)==q*q,(q,arr)
    return arr

def run(p, d=None):
    if d is None:
        q=p
        elems=list(range(q))
        add=lambda x,y:(x+y)%p
        mul=lambda x,y:(x*y)%p
        neg=lambda x:(-x)%p
        embed=lambda x:x%p
    else:
        q=p*p
        elems=list(range(q))
        add=lambda x,y:((x%p+y%p)%p) + p*((x//p+y//p)%p)
        mul=lambda x,y:((x%p)*(y%p)+d*(x//p)*(y//p))%p + p*(((x%p)*(y//p)+(x//p)*(y%p))%p)
        neg=lambda x:(-x%p)+p*(-(x//p)%p)
        embed=lambda x:x%p
    def powf(x,n):
        v=embed(1)
        while n:
            if n&1:v=mul(v,x)
            x=mul(x,x); n//=2
        return v
    def chi(z):
        z=embed(z)
        if z==0:return 0
        zz=powf(z,(q-1)//2)
        assert zz in (embed(1),embed(-1)),(p,d,z,zz)
        return 1 if zz==embed(1) else -1
    pred=predicted(q,chi)
    counts={}
    fourths={x:powf(x,4) for x in elems}
    for t in elems:
        for u in elems:
            k=(add(t,u),add(fourths[t],fourths[u]))
            counts[k]=counts.get(k,0)+1
    h=Counter(counts.values())
    result=[q*q-len(counts)]+[h.get(j,0) for j in range(1,5)]
    assert not any(j>4 for j in h), (q,h)
    assert result==pred,(q,d,result,pred)
    assert sum(j*result[j] for j in range(5))==q*q
    assert sum(j*j*result[j] for j in range(5))==3*q*q-3*q-2*chi(-3)*(q-1)+1
    print(f'q={q:3d} characteristic={p:2d} degree={1 if d is None else 2} chi(-1,-3,-6)={chi(-1),chi(-3),chi(-6)} distribution={result} energy={sum(j*j*result[j] for j in range(5))}')

if __name__=='__main__':
    for p in [5,7,11,13,17,19,23,29,31,37,41,43,47]:run(p)
    run(5,2) # 2 nonsquare modulo 5
    run(7,3) # 3 nonsquare modulo 7
    run(11,2) # 2 nonsquare modulo 11
    print('ALL exhaustive direct convolution checks passed.')
