#!/usr/bin/env python3
"""Exact integer checks for a precanonical Rao profile on a (2,2,2) K3."""

def rao_by_exceptional_filtration(m,t):
    assert m>=1 and t<=2*m
    if t==2*m:
        # K3 Riemann--Roch for mE, with E^2=-2, h^0(mE)=1, h^2(mE)=0.
        return m*m-1
    k=2*m-t
    assert k>0
    return sum(max(0,2*j-k-1) for j in range(1,m+1))

def rao_closed(m,t):
    if t<=1: return 0
    if t<2*m: return t*t//4
    return m*m-1

def test():
    H2,HE,E2=8,1,-2
    D2=4*H2+4*HE+E2
    assert D2==34 and 2*HE+E2==0 and 2*H2+HE==17
    for m in range(1,65):
        assert (m*m*D2)//2+1==17*m*m+1
        for t in range(-3,2*m+1):
            assert rao_by_exceptional_filtration(m,t)==rao_closed(m,t),(m,t)
        h0=4*m*m+2+rao_closed(m,m)
        assert h0==4*m*m+2+m*m//4
        assert (h0%2==1)==(m%4==2)
    assert [rao_closed(2,t) for t in range(2,5)]==[1,2,3]
    assert [rao_closed(3,t) for t in range(2,7)]==[1,2,4,6,8]
    assert 4*2*2+2+2*2//4==19
    assert 4*3*3+2+3*3//4==40
    print('VERIFY_OK: 64 family parameters, all twists -3 through 2m, Rao endpoint and spin parity')

if __name__=='__main__': test()
