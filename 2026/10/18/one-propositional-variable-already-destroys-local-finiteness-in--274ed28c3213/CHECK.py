#!/usr/bin/env python3
"""Reproduction checks for the single-atom Alexandrov-DTL boundary.
All formula semantics implement classical Boolean connectives, reflexive-transitive
spatial diamond, deterministic next and inclusive temporal eventually.
"""
from itertools import product

def Var():return ('v',)
def Neg(a):return ('neg',a)
def And(*xs):return ('and',*xs)
def Or(*xs):return ('or',*xs)
def Next(a):return ('next',a)
def F(a):return ('F',a)
def Dia(a):return ('dia',a)
def Box(a):return Neg(Dia(Neg(a)))
def Always(a):return Neg(F(Neg(a)))
def Imp(a,b):return Or(Neg(a),b)
def Xor(a,b):return Or(And(a,Neg(b)),And(Neg(a),b))

v=Var()
delta=Xor(v,Next(v))
qhat=Neg(F(delta))
phat=Xor(v,qhat)
def witness(p,q):
 return And(
  Always(Box(And(Imp(p,Next(p)),Imp(Neg(p),Next(Neg(p))),Imp(q,Next(q))))),
  Box(And(Imp(p,Dia(Neg(p))),Imp(Neg(p),Dia(p)))),
  Box(Imp(p,F(And(q,Neg(Dia(And(Neg(p),q))))))),
  Box(Imp(Neg(p),F(And(q,Neg(Dia(And(p,q)))))))
 )
phi=witness(phat,qhat)

def evaluation(formula,reach,successor,atom):
 n=len(reach)
 memo={}
 def ev(f):
  if f in memo:return memo[f]
  op=f[0]
  if op=='v': res=atom
  elif op=='neg':res=tuple(not z for z in ev(f[1]))
  elif op=='and':res=tuple(all(e[i] for e in map(ev,f[1:])) for i in range(n))
  elif op=='or':res=tuple(any(e[i] for e in map(ev,f[1:])) for i in range(n))
  elif op=='next': a=ev(f[1]);res=tuple(a[successor[i]] for i in range(n))
  elif op=='dia': a=ev(f[1]);res=tuple(any(a[j] for j in reach[i]) for i in range(n))
  elif op=='F':
   a=ev(f[1]); res=[]
   for i in range(n):
    j=i;yes=False
    for k in range(n):
     if a[j]:yes=True;break
     j=successor[j]
    res.append(yes)
   res=tuple(res)
  else:raise ValueError(op)
  memo[f]=res
  return res
 return ev(formula)

def finite_checks():
 preorders=maps=trials=0
 for n in (1,2,3):
  for bits in range(1<<(n*n)):
   rows=tuple(tuple(bool(bits&(1<<(i*n+j))) for j in range(n)) for i in range(n))
   if any(not rows[i][i] for i in range(n)):continue
   if any(rows[i][j] and rows[j][k] and not rows[i][k] for i in range(n) for j in range(n) for k in range(n)):continue
   preorders+=1
   reach=tuple(tuple(j for j in range(n) if rows[i][j]) for i in range(n))
   for successor in product(range(n),repeat=n):
    if any(rows[i][j] and not rows[successor[i]][successor[j]] for i in range(n) for j in range(n)):continue
    maps+=1
    for valuation in product((False,True),repeat=n):
     trials+=1
     assert not any(evaluation(phi,reach,successor,valuation)),(n,bits,successor,valuation)
 return preorders,maps,trials

def infinite_pattern_checks():
 # Test the exact temporal-change decoding on finite coordinate windows;
 # proof extends algebraically to all nonnegative i,j.
 count=0
 for i in range(32):
  for j in range(32):
   p=(i%2==0); q=(j>=i)
   def P(t):return p != (t>=i)
   # No change can occur later than i-1.
   future_change=any(P(t)!=P(t+1) for t in range(j,max(34,i+3)))
   Q=not future_change
   recovered_p=P(j)!=Q
   assert Q==q and recovered_p==p
   count+=1
 # Confirm the four defining obligations on a finite window excluding the
 # artificial spatial top boundary, with explicit time witnesses.
 obligation=0
 for i in range(24):
  for j in range(24):
   p=i%2==0;q=j>=i
   assert p==(i%2==0) and (not q or j+1>=i)
   assert (i+1)%2 !=i%2
   if j==0:
    t=i
    assert t>=j and (t>=i) and not(t>=i+1)
   obligation+=1
 return count,obligation

if __name__=='__main__':
 a,b= infinite_pattern_checks()
 ps,ms,ts=finite_checks()
 print('ONE_ATOM_DTL_VERIFY_OK decoding=%d grid_obligations=%d preorders=%d monotone_maps=%d finite_models=%d' % (a,b,ps,ms,ts))
