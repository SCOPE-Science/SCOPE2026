"""Independent symbolic cross-check of the five-orbit quintic-cover census.
Requires SymPy. No imports from checker.py.
"""
import json
from itertools import combinations
from math import comb
from collections import Counter
import sympy as sp

x,y,u = sp.symbols('x y u')

def binary_form(mask):
    return sp.Poly(sum(((mask>>i)&1)*x**i*y**(5-i) for i in range(6)), x, y, modulus=2)

def affine(mask):
    return sp.Poly(sum(((mask>>i)&1)*x**i for i in range(6)), x, modulus=2)

def sf(mask):
    p=affine(mask)
    inf_ok=(mask>>5)&1 or (mask>>4)&1
    return bool(inf_ok and sp.gcd(p,p.diff()).degree()==0)

def coprime_projectively(f,g):
    return ((f>>5)&1 or (g>>5)&1) and sp.gcd(affine(f),affine(g)).degree()==0


def image(mask,matrix):
    a,b,c,d=matrix
    polynomial=sp.Poly(binary_form(mask).as_expr().subs({x:a*x+b*y,y:c*x+d*y}, simultaneous=True), x,y,modulus=2)
    out=0
    for (i,j),coef in polynomial.terms():
        assert i+j==5 and coef==1
        out|=1<<i
    return out


def critical(mask_f,mask_g):
    f,g=affine(mask_f).as_expr(),affine(mask_g).as_expr()
    w=sp.Poly(sp.expand(sp.diff(f,x)*g-sp.diff(g,x)*f),x,modulus=2)
    mask=0
    for (i,),coef in w.terms():
        assert i%2==0
        mask|=1<<(i//2)
    return mask


def branch(mask_f,mask_g,critical_mask):
    crit=0b111 if critical_mask==0b10101 else critical_mask
    cp=sum(((crit>>i)&1)*x**i for i in range(crit.bit_length()))
    f=affine(mask_f).as_expr()
    g=affine(mask_g).as_expr()
    resultant=sp.Poly(sp.resultant(cp,f-u*g,x),u)
    resultmask=0
    for (i,),coef in resultant.terms():
        if coef%2:resultmask|=1<<i
    factors=sp.factor_list(sp.Poly(sum((resultmask>>i&1)*u**i for i in range(resultmask.bit_length())),u,modulus=2))[1]
    assert len(factors)==1
    return resultmask, factors[0][0].degree(), factors[0][1]


def verify():
    squarefree=[m for m in range(1,64) if sf(m)]
    assert len(squarefree)==24
    P=set()
    for f,g in combinations(squarefree,2):
        if sf(f^g) and coprime_projectively(f,g):
            P.add(tuple(sorted((f,g,f^g))))
    assert len(P)==22
    matrices=[(a,b,c,d) for a in range(2) for b in range(2) for c in range(2) for d in range(2) if a*d-b*c in (-1,1)]
    assert len(matrices)==6
    seen=set();rows=[]
    for p in sorted(P):
        if p in seen:continue
        orbit={tuple(sorted(image(mask,M) for mask in p)) for M in matrices}
        assert orbit<=P and not orbit&seen
        seen|=orbit
        k=critical(p[0],p[1]); b,bd,mult=branch(p[0],p[1],k)
        rows.append(dict(representative=list(p),size=len(orbit),critmask=k,branchmask=b,branchdegree=bd,branchmultiplicity=mult))
    assert seen==P
    assert rows==[
      {'representative':[18,37,55],'size':3,'critmask':19,'branchmask':25,'branchdegree':4,'branchmultiplicity':1},
      {'representative':[19,33,50],'size':1,'critmask':21,'branchmask':7,'branchdegree':2,'branchmultiplicity':1},
      {'representative':[19,41,58],'size':6,'critmask':31,'branchmask':25,'branchdegree':4,'branchmultiplicity':1},
      {'representative':[22,35,53],'size':6,'critmask':31,'branchmask':19,'branchdegree':4,'branchmultiplicity':1},
      {'representative':[22,43,61],'size':6,'critmask':19,'branchmask':21,'branchdegree':2,'branchmultiplicity':2}]
    print(json.dumps({'squarefree_forms':24,'pencils':22,'orbits':5,'symbolic_rows':rows},sort_keys=True,indent=2))

if __name__=='__main__':
    verify()
