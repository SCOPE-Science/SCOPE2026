#!/usr/bin/env python3
"""Exact small-instance checks for the periodic-correction digit-appending theorem.
This is finite corroboration, not a proof for all indices or parameters.
"""
from fractions import Fraction as F
from itertools import product

def poly(coefs, n):
    return sum((F(c) * n**i for i,c in enumerate(coefs)), F(0))

def val(b, A, coeffs, n):
    z=F(A)*b**n+poly(coeffs[n % len(coeffs)], n)
    assert z.denominator==1 and z>0, (b,A,n,z)
    return int(z)

def graph(b, coeffs, limit):
    P=len(coeffs)
    good={r: F(c[0]) for r,c in enumerate(coeffs) if len(c)==1 and -1 <= F(c[0]) <=0}
    E=set()
    for r,c in good.items():
        for k in range(1,limit+1):
            s=(r+k)%P
            if s not in good: continue
            d=good[s]-b**k*c
            if d.denominator==1 and 0<=d<b**k:
                E.add((r,s,k,int(d)))
    return good,E

def cycle_exists(vertices, edges):
    adj={r:[] for r in vertices}
    for r,s,k,d in edges:adj[r].append(s)
    visiting,seen=set(),set()
    def dfs(r):
        if r in visiting:return True
        if r in seen:return False
        visiting.add(r)
        for s in adj[r]:
            if dfs(s):return True
        visiting.remove(r); seen.add(r)
        return False
    return any(dfs(r) for r in vertices if r not in seen)

def nmin(b,coeffs):
    P=len(coeffs)
    for N in range(1,P+1):
        V,E=graph(b,coeffs,N)
        if cycle_exists(V,E):return N
    return None

cases=[
  ('binary shifted repunit',2,F(1),[[-1]],1),
  ('ternary half-repunit',3,F(1,2),[[F(-1,2)]],1),
  ('positive correction',2,F(1),[[1]],None),
  ('period-two rational',2,F(1,3),[[F(-1,3)],[F(-2,3)]],1),
  ('period-four bottleneck',2,F(1,3),[[F(-1,3)],[F(-2,3)],[F(-1,3)],[F(1,3)]],2),
  ('polynomially bad residue',2,F(1),[[0,1],[-1]],2),
  ('all nonconstant',2,F(1),[[1,1]],None),
]

checks=0
for name,b,A,cs,expect in cases:
    assert nmin(b,cs)==expect,(name,nmin(b,cs),expect)
    P=len(cs)
    # Each tail finite edge with k<=5 agrees with the corresponding exact digit test.
    V,E=graph(b,cs,5)
    for n in range(25,36):
      for k in range(1,6):
        a=val(b,A,cs,n); aa=val(b,A,cs,n+k)
        successful=[]
        for t in range(1,9):
            d=aa-b**t*a
            if 0<=d<b**t:successful.append((t,d))
        for t,d in successful:
            assert t==k,(name,n,k,t,d)
            if n%P in V and (n+k)%P in V:
                assert (n%P,(n+k)%P,k,d) in E,(name,n,k,d,E)
        if n%P in V and (n+k)%P in V:
            delta=cs[(n+k)%P][0]-b**k*cs[n%P][0]
            if delta.denominator==1 and 0<=delta<b**k:
                assert (k,int(delta)) in successful,(name,n,k,successful)
        checks+=1
    print(name, 'N_min=',expect, 'tail comparisons=',11*5)
print('TOTAL_EXACT_TAIL_COMPARISONS',checks)
print('CERTIFICATE_OK')
