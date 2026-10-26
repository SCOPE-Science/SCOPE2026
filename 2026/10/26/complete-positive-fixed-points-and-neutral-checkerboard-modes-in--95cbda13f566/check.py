#!/usr/bin/env python3
"""Exact finite checks for an NSFD p-diffusion fixed-point classification.

Run with Python 3 standard library: python3 check.py
Finite tests corroborate, but do not replace, the analytical proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def reflect(i, top):
    if i == -1:
        return 1
    if i == top + 1:
        return top - 1
    assert 0 <= i <= top
    return i

def calc(u, nx, ny, power=4, h=F(1), tau=F(3, 7)):
    """Return exact NSFD update for p=4 or 6, zero reaction."""
    assert power in (4, 6)
    def at(i, j):
        return u[reflect(i, nx), reflect(j, ny)]
    phi = {}
    for i in range(nx+1):
        for j in range(ny+1):
            dx=(at(i+1,j)-at(i-1,j))/(2*h)
            dy=(at(i,j+1)-at(i,j-1))/(2*h)
            phi[i,j]=(dx*dx+dy*dy)**((power-2)//2)
    def val(i,j):
        i=reflect(i,nx);j=reflect(j,ny)
        return u[i,j]*phi[i,j]
    return {(i,j):(u[i,j]+tau*(val(i-1,j)+val(i+1,j)+val(i,j-1)+val(i,j+1)))/(1+4*tau*phi[i,j])
            for i in range(nx+1) for j in range(ny+1)}

def periodic_parity(nx,ny,colors):
    return {(i,j):F(colors[(i%2,j%2)]) for i in range(nx+1) for j in range(ny+1)}

def edge_energy_checker(N,p,a,b):
    u={(i,j):F(a if (i+j)%2==0 else b) for i in range(N+1) for j in range(N+1)}
    h=F(1,N)
    acc=sum(abs(u[i+1,j]-u[i,j])**p for i in range(N) for j in range(N+1))
    acc+=sum(abs(u[i,j+1]-u[i,j])**p for i in range(N+1) for j in range(N))
    return h**(2-p)*acc

def main():
    count=0
    for nx,ny in [(2,2),(2,3),(3,2),(3,3),(4,5),(7,6)]:
        for power in (4,6):
            for tau in (F(1,9),F(2,3),F(5,1)):
                for colors in ((1,2,3,4),(5,5,5,5),(1,6,6,1),(F(1,7),F(19,3),F(11,5),F(99,7))):
                    u=periodic_parity(nx,ny,{(0,0):colors[0],(0,1):colors[1],(1,0):colors[2],(1,1):colors[3]})
                    assert calc(u,nx,ny,power,F(1,max(nx,ny)),tau)==u
                    count+=1
    for N in range(2,13):
        for p in (3,4,5,6,7):
            for a,b in ((1,2),(F(3,7),F(11,13))):
                lhs=edge_energy_checker(N,p,a,b)
                rhs=2*(1+F(1,N))*N**p*abs(F(a)-F(b))**p
                assert lhs == rhs,(N,p,lhs,rhs)
                count+=1
    rng=Random(260700489)
    for nx,ny in ((2,2),(2,3),(3,2),(3,3)):
        for _ in range(180):
            u={(i,j):F(rng.randint(1,7)) for i in range(nx+1) for j in range(ny+1)}
            out=calc(u,nx,ny,4,F(1),F(1,7))
            assert all(x>0 for x in out.values())
            equal=all(out[k]==v for k,v in u.items())
            parity=all(u[i,j]==u[i%2,j%2] for i in range(nx+1) for j in range(ny+1))
            assert equal==parity,(nx,ny,u)
            count+=1
    # Quadratic vanishing of the update defect at checkerboards for p=4.
    for nx,ny in ((2,2),(3,4)):
        colors={(0,0):1,(0,1):3,(1,0):5,(1,1):2}
        base=periodic_parity(nx,ny,colors)
        perturb={(i,j):F((3*i+5*j)%7-3) for i,j in base}
        for k in (5,6,7,8):
            t=F(1,2**k)
            x={idx:base[idx]+t*perturb[idx] for idx in base}
            update=calc(x,nx,ny,4,F(1),F(1,7))
            residual=max(abs(update[idx]-x[idx]) for idx in x)
            assert residual <= 200*t*t, (nx,ny,k,residual)
            count+=1
    assert edge_energy_checker(4,4,1,2)==640
    print('EXACT_CHECKS_PASSED',count)

if __name__=='__main__':
    main()
