#!/usr/bin/env python3
"""Exact reproducibility for the finite-ring Rule 62 three-cycle formula."""
import sympy as s
from fractions import Fraction

RULE=62

def bit(a,b,c):
    return (RULE >> (4*a+2*b+c)) & 1

def step3(z):
    while len(z)>1:
        z=[bit(*z[i:i+3]) for i in range(len(z)-2)]
    return z[0]

def transfer():
    M=s.zeros(64)
    H=s.zeros(4)
    for u in range(64):
        z=[(u>>(5-j))&1 for j in range(6)]
        for b in (0,1):
            if step3(z+[b])==z[3]:
                M[u, ((u&31)<<1)|b]+=1
    for u in range(4):
        a,b=(u>>1), (u&1)
        for c in (0,1):
            if bit(a,b,c)==b:
                H[u,((u&1)<<1)|c]+=1
    return M,H

def all_three_cycles(n):
    mask=(1<<n)-1
    def nxt(v):
        out=0
        for i in range(n):
            a=(v>>((i-1)%n))&1
            b=(v>>i)&1
            c=(v>>((i+1)%n))&1
            out |= bit(a,b,c)<<i
        return out
    fixed1=fixed3=0
    for state in range(1<<n):
        u=nxt(state)
        if u==state:fixed1+=1
        if nxt(nxt(u))==state:fixed3+=1
    assert (fixed3-fixed1)%3==0
    return fixed1,(fixed3-fixed1)//3,fixed3

def schur_test():
    # Ascending rational coefficients for monic Q(3z/2)/(3/2)^8.
    R=Fraction(3,2)
    a=[Fraction(c)*R**(k-8) for k,c in enumerate((1,2,1,2,3,1,1,1,1))]
    ratios=[]
    for degree in range(8,0,-1):
        assert len(a)==degree+1
        lead,con=a[-1],a[0]
        ratio=abs(con/lead)
        assert ratio<1,(degree,ratio)
        ratios.append((degree,ratio))
        v=[lead*a[j+1]-con*a[degree-j-1] for j in range(degree)]
        assert v[-1]!=0
        a=[b/v[-1] for b in v]
    return ratios

def main():
    t=s.symbols('t')
    M,H=transfer()
    Q=t**8+t**7+t**6+t**5+3*t**4+2*t**3+t**2+2*t+1
    expected=t**51*(t-1)*(t**2+1)*(t**2-t-1)*Q
    assert s.expand(M.charpoly(t).as_expr()-expected)==0
    assert s.expand(H.charpoly(t).as_expr()-t**3*(t-1))==0
    ratios=schur_test()
    count=[]
    for n in range(1,13):
        f,c,ff=all_three_cycles(n)
        assert f==1
        assert ff==int(s.trace(M**n))
        assert f==int(s.trace(H**n))
        assert c==(int(s.trace(M**n))-1)//3
        count.append(c)
    assert count==[0,0,1,0,5,7,7,24,22,35,77,87]
    print('VERIFY_OK transfer_states=64 characteristic_polynomials=2 exact_schur_stages=8 direct_ring_lengths=12')
    print('C1_to_C12=',count)
    print('schur_ratios=',[(d, str(z)) for d,z in ratios])

if __name__=='__main__':main()
