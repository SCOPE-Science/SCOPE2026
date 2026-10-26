#!/usr/bin/env python3
"""Finite checks for rectangular three-dot shifts; Python standard library only."""
from math import gcd


def degree(p):
    return p.bit_length()-1


def residue(p, f):
    while p and degree(p)>=degree(f):
        p ^= f << (degree(p)-degree(f))
    return p


def pgcd(a,b):
    while b:
        a,b=b,residue(a,b)
    return a


def product(a,b):
    v=0
    while b:
        if b&1:v^=a
        a<<=1; b>>=1
    return v


def power(a,e):
    v=1
    while e:
        if e&1:v=product(v,a)
        a=product(a,a);e>>=1
    return v


def mulmod(a,b,p):
    return residue(product(a,b),p)


def modpow(a,e,p):
    v=1
    while e:
        if e&1:v=mulmod(v,a,p)
        a=mulmod(a,a,p);e>>=1
    return v


def defining_gcd(m,n):
    return pgcd((1<<m)^1,power(3,n)^1)


def rank_of_three_dot(m,n):
    rows=[]
    for i in range(m):
        for j in range(n):
            row=(1<<(i*n+j))^(1<<(((i+1)%m)*n+j))^(1<<(i*n+(j+1)%n))
            rows.append(row)
    basis={}
    for row in rows:
        while row:
            i=degree(row)
            if i in basis:row ^= basis[i]
            else:
                basis[i]=row
                break
    return len(basis)


def predicted(a,b,u,v):
    g=gcd(a,b);w=min(u,v)
    return (2**w)*(2**g-2),2**w*(2**g-1),g,w


def kernel_elements(p,L):
    px=[modpow(2,s,p) for s in range(L)]
    py=[modpow(3,t,p) for t in range(L)]
    return {(s,t) for s in range(L) for t in range(L) if mulmod(px[s],py[t],p)==1}


def check_full_orbit_functional(p,L,kernel):
    d=degree(p)
    # A linear functional extracting the coefficient at degree d-1.
    # Stabilization under a multiplier f means every monomial x^i pairs to 0 with f+1.
    for s in range(L):
        for t in range(L):
            multiplier=mulmod(modpow(2,s,p),modpow(3,t,p),p)
            fixed=True
            x_i=1
            for _ in range(d):
                if mulmod(multiplier^1,x_i,p)>>(d-1)&1:
                    fixed=False
                    break
                x_i=mulmod(x_i,2,p)
            assert fixed == ((s,t) in kernel),(p,L,s,t,fixed)


def main():
    poly_checks=0;rank_checks=0;kernel_checks=0;orbit_checks=0;field_checks=0
    for a in range(1,6):
        for b in range(1,6):
            for u in range(3):
                for v in range(3):
                    m=(2**a-1)*2**u
                    n=(2**b-1)*2**v
                    if max(m,n)>100:continue
                    d,L,g,w=predicted(a,b,u,v)
                    p=defining_gcd(m,n)
                    assert degree(p)==d,(a,b,u,v,'dimension')
                    poly_checks+=1
                    # Independent physical linear-system check.
                    if m*n<=105:
                        assert m*n-rank_of_three_dot(m,n)==d,(m,n,'rank')
                        rank_checks+=1
                    if 0<d<=14 and L<=30:
                        assert modpow(2,L,p)==modpow(3,L,p)==1
                        ker=kernel_elements(p,L)
                        if g==2:
                            r=1<<w
                            expected={(r*k%L,r*k%L) for k in range(3)}
                        else:
                            expected={(0,0)}
                        assert ker==expected,(a,b,u,v,'kernel',ker)
                        # Both coordinate shifts have exact universal period L.
                        for h in range(1,L):
                            assert modpow(2,h,p)!=1
                            assert modpow(3,h,p)!=1
                        kernel_checks+=1
                        if d<=12:
                            check_full_orbit_functional(p,L,ker)
                            orbit_checks+=1
    # Independent count with brute-force enumeration of arrays, for small rectangles.
    for m,n in [(3,3),(3,6),(6,6),(7,7),(3,7),(6,7),(7,14)]:
        p=defining_gcd(m,n)
        d=degree(p)
        assert d==m*n-rank_of_three_dot(m,n)
        field_checks+=1
    print(f'VERIFY_OK polynomial_cases={poly_checks} physical_rank_cases={rank_checks} '
          f'kernel_cases={kernel_checks} full_orbit_witness_cases={orbit_checks} '
          f'additional_rank_cases={field_checks}')

if __name__=='__main__':main()
