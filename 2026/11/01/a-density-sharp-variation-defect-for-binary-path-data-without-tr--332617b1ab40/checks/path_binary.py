#!/usr/bin/env python3
"""Exact rational consistency checks for a finite-path variation identity."""
from fractions import Fraction
from itertools import product


def profile(bits):
    n = len(bits)
    zeros = {j for j, bit in enumerate(bits) if not bit}
    h = []
    for j in range(n):
        densities = []
        for r in range(n):
            lo, hi = max(0, j-r), min(n-1, j+r)
            densities.append(Fraction(sum(k in zeros for k in range(lo, hi+1)), hi-lo+1))
        h.append(min(densities))
    return h


def runs(bits):
    n=len(bits)
    j=0
    while j<n:
        if bits[j]:
            j+=1
            continue
        k=j
        while k+1<n and not bits[k+1]:
            k+=1
        yield (j,k)
        j=k+1


def verify(bits):
    n=len(bits)
    m=bits.count(0)
    if not 0<m<n or any(bits[j:j+3]==(0,0,0) for j in range(n-2)):
        return 0
    h=profile(bits)
    vf=sum(bits[j]!=bits[j+1] for j in range(n-1))
    vh=sum(abs(h[j]-h[j+1]) for j in range(n-1))
    terms=[]
    condition=True
    for j,k in runs(bits):
        b=1 if (j==0 or k==n-1) else 2
        H=max(h[j:k+1])
        terms.append((b,H))
        if k-j==1 and b==1:
            assert h[j]==h[k]
        local_any=False
        for v in range(j,k+1):
            ok=all(n*sum(bits[x]==0 for x in range(max(0,v-r),min(n-1,v+r)+1))
                   >=m*(min(n-1,v+r)-max(0,v-r)+1) for r in range(n))
            local_any=local_any or ok
        assert local_any == (H==Fraction(m,n))
        condition &=local_any
    assert vf==sum(b for b,_ in terms)
    assert vh==sum((b*H for b,H in terms),Fraction(0))
    defect=Fraction(m,n)*vf-vh
    assert defect==sum((b*(Fraction(m,n)-H) for b,H in terms),Fraction(0))
    assert defect>=0
    assert (defect==0)==condition
    return 1


def main():
    count=0
    for n in range(3,15):
        for bits in product((0,1),repeat=n):
            count+=verify(bits)
    assert verify((1,1,0,1,0,1,0,1,1))
    ex=(0,1,0,0,0,1,0)
    m=ex.count(0)
    h=profile(ex)
    assert [1-h[j] for j in range(1,6)]==[Fraction(1),Fraction(1,3),Fraction(2,5),Fraction(1,3),Fraction(1)]
    local=sum(abs(h[j+1]-h[j]) for j in range(1,5))
    assert local==Fraction(22,15) and local>Fraction(2*m,len(ex))
    print('EXACT_PATH_CHECK_OK',count)

if __name__=='__main__':
    main()
