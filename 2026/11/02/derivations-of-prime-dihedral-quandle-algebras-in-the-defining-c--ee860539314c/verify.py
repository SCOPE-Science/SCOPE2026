#!/usr/bin/env python3
"""Finite-field checks for the modular dihedral quandle derivation classification.
Only standard Python is used. Run: python3 verify_modular_quandle.py
"""
from math import lcm

def multiplicative_order_2(p):
    x=2%p
    r=1
    while x != 1:
        x=(2*x)%p
        r+=1
    return r

def exponents(p):
    return [j for j in range(1,p) if j%2 and pow(2,j,p)==2]

def rank_mod_sparse(p):
    # Exact derivation system in the ORIGINAL quandle basis:
    # D(e_{2j-i}) = D(e_i)*e_j + e_i*D(e_j).
    pivot={}
    inv2=pow(2,-1,p)
    for i in range(p):
      for j in range(p):
        target=(2*j-i)%p
        for k in range(p):
          row={}
          terms=((k*p+target,1),(((2*j-k)%p)*p+i,-1),((((k+i)*inv2)%p)*p+j,-1))
          for col,a in terms:
              z=(row.get(col,0)+a)%p
              if z: row[col]=z
              elif col in row: del row[col]
          while row:
              lead=min(row)
              old=pivot.get(lead)
              if old is None:
                  z=pow(row[lead],-1,p)
                  pivot[lead]={c:(v*z)%p for c,v in row.items()}
                  break
              f=row[lead]
              for c,v in old.items():
                  z=(row.get(c,0)-f*v)%p
                  if z:row[c]=z
                  elif c in row:del row[c]
    return len(pivot)

def add(a,b,p):
    out=a.copy()
    for j,c in b.items():
        d=(out.get(j,0)+c)%p
        if d:out[j]=d
        elif j in out:del out[j]
    return out

def scaled(a,c,p):
    return {j:(v*c)%p for j,v in a.items() if (v*c)%p}

def mul(a,b,p):
    out={}
    for i,x in a.items():
      for j,y in b.items():
        if i+j < p:
          z=(out.get(i+j,0)+x*y)%p
          if z:out[i+j]=z
          elif i+j in out:del out[i+j]
    return out

def derivative(a,p):
    return {j-1:(j*c)%p for j,c in a.items() if j and (j*c)%p}

def star(a,b,p):
    out={}
    for i,x in a.items():
      for j,y in b.items():
        if i+j < p:
          v=(out.get(i+j,0)+x*y*pow(-1,i,p)*pow(2,j,p))%p
          if v:out[i+j]=v
          elif i+j in out:del out[i+j]
    return out

def deriv(A,B,f,p):
    return add(mul(A,f,p),mul(B,derivative(f,p),p),p)

def check(p,check_rank=False):
    E=exponents(p)
    ord2=multiplicative_order_2(p)
    assert len(E)==(p-1)//lcm(2,ord2)
    basis=[({j:1},{}) for j in E]+[({},{j:1}) for j in E]
    # Full Leibniz identities on every pair of u-monomials for each claimed basis derivation.
    for A,B in basis:
       for i in range(p):
         x={i:1}
         for j in range(p):
           y={j:1}
           lhs=deriv(A,B,star(x,y,p),p)
           rhs=add(star(deriv(A,B,x,p),y,p),star(x,deriv(A,B,y,p),p),p)
           assert lhs==rhs,(p,A,B,i,j,lhs,rhs)
    # Bracket of every pair agrees with the claimed closed Lie algebra formula.
    for A,B in basis:
      for C,D in basis:
        E1=add(mul(B,derivative(C,p),p),scaled(mul(D,derivative(A,p),p),-1,p),p)
        E2=add(mul(B,derivative(D,p),p),scaled(mul(D,derivative(B,p),p),-1,p),p)
        assert set(E1).issubset(set(exponents(p))) and set(E2).issubset(set(exponents(p)))
        for j in range(p):
          f={j:1}
          lhs=add(deriv(A,B,deriv(C,D,f,p),p),scaled(deriv(C,D,deriv(A,B,f,p),p),-1,p),p)
          assert lhs==deriv(E1,E2,f,p),(p,j,A,B,C,D,lhs)
    if check_rank:
        rank=rank_mod_sparse(p)
        assert p*p-rank==2*len(E),(p,p*p-rank,2*len(E))
    print('PASS',p,'ord2',ord2,'allowed_exponents',E,'dimension',2*len(E),'original_basis_rank',p*p-rank if check_rank else 'not-run')

if __name__=='__main__':
    for p in [3,5,7,11,17,31]:
        check(p,p<=17)
    print('MODULAR_QUANDLE_DERIVATION_OK')
