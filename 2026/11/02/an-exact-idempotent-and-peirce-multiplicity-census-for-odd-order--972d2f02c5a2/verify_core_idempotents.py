#!/usr/bin/env python3
"""Exact orbit/weight census and independent numerical algebra checks for finite odd abelian core quandles."""
from itertools import product
from math import gcd, lcm, prod, pi
import cmath
import numpy as np

def add(a,b,mods): return tuple((x+y)%n for x,y,n in zip(a,b,mods))
def scale(a,k,mods): return tuple((k*x)%n for x,n in zip(a,mods))
def group(mods): return list(product(*(range(n) for n in mods)))
def order_elem(a,mods): return lcm(*(n//gcd(n,x) for x,n in zip(a,mods)))
def mul_order_two(h):
    if h==1:return 1
    m=1
    while pow(2,m,h)!=1:m+=1
    return m

def orbit_data(mods):
    zero=(0,)*len(mods); universe=set(group(mods)); universe.remove(zero)
    out=[]
    while universe:
        rep=min(universe); h=order_elem(rep,mods); m=mul_order_two(h)
        cyc=[scale(rep,2**j,mods) for j in range(m)]
        inv=scale(rep,-1,mods) in cyc
        orb=set(cyc)|{scale(k,-1,mods) for k in cyc}
        assert orb<=universe
        universe-=orb
        roots=(2**(m//2)+1) if inv else (2**m-1)
        assert len(orb)==(m if inv else 2*m)
        out.append((rep,cyc,inv,roots,orb))
    return sorted(out,key=lambda x:x[0])

def assignments(mods):
    orbits=orbit_data(mods); zero=(0,)*len(mods)
    for choice in product(*[range(o[3]+1) for o in orbits]):
        c={x:0j for x in group(mods)}
        for (rep,cyc,inv,roots,orb),choice_i in zip(orbits,choice):
            if choice_i==0:continue
            zeta=cmath.exp(2j*pi*(choice_i-1)/roots)
            for j,x in enumerate(cyc):
                c[x]=zeta**(2**j)
                if not inv:c[scale(x,-1,mods)]=zeta**(-2**j)
        for a0 in (0,1):
            c[zero]=complex(a0)
            yield c

def check(mods):
    elements=group(mods); n=len(elements); zero=(0,)*len(mods)
    orbits=orbit_data(mods)
    predicted=2*prod(1+r for rep,cyc,inv,r,orb in orbits)
    idx={x:i for i,x in enumerate(elements)}
    # Ordinary discrete Fourier inverse for finite abelian groups.
    character=np.array([[cmath.exp(2j*pi*sum((k_i*x_i)/d for k_i,x_i,d in zip(k,x,mods))) for k in elements] for x in elements])
    basis_index=[[idx[add(scale(x,-1,mods),scale(y,2,mods),mods)] for y in elements] for x in elements]
    count=0; histogram={}
    for c in assignments(mods):
        count+=1
        for k in elements:
            assert abs(c[k]-c[scale(k,-1,mods)]*c[scale(k,2,mods)])<5e-7
        support=sum(abs(c[k])>0.01 for k in elements)
        augmentation=round(c[zero].real)
        histogram[(support,augmentation)]=histogram.get((support,augmentation),0)+1
        vals=np.array([c[k] for k in elements])
        a=(character@vals)/n
        product_vec=np.zeros(n,dtype=complex)
        for i,x in enumerate(elements):
            for j,y in enumerate(elements):
                product_vec[basis_index[i][j]]+=a[i]*a[j]
        assert np.max(np.abs(product_vec-a))<2e-7
        rho=np.zeros((n,n),dtype=complex)
        for i,x in enumerate(elements):
            for j,y in enumerate(elements):rho[basis_index[i][j],i]+=a[j]
        assert np.max(np.abs(rho@rho@rho-rho))<2e-7
        assert abs(np.trace(rho)-augmentation)<2e-7
        assert abs(np.trace(rho@rho)-(support))<2e-7
    assert count==predicted
    return count, [(o[0],len(o[4]),o[3]) for o in orbits], histogram

if __name__=='__main__':
    for mods in [(3,),(5,),(7,),(9,),(11,),(15,),(3,3)]:
        total,orbs,hist=check(mods)
        print('CHECK',mods,'idempotents',total,'orbit_factors',[(size,roots) for rep,size,roots in orbs], 'support_categories',len(hist))
    assert check((9,))[0]==80 and check((3,3))[0]==512
    print('VERIFY_OK: Fourier idempotents, direct quandle multiplication and Peirce polynomial identities')
