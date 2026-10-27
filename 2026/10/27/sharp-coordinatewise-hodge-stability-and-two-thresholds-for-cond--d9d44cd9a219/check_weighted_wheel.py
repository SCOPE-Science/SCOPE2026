#!/usr/bin/env python3
"""Exact rational checks for weighted wheel edge-gradient stability."""
import sympy as S

def check(cond, msg):
    if cond is not True and cond != S.true:
        raise AssertionError(msg)

def projection(n, root_t):
    t=root_t**2
    R=S.zeros(n)
    for j in range(n):
        R[j,j]-=1
        R[(j+1)%n,j]+=1
    B=R.row_join(root_t*S.eye(n))
    A=B*B.T
    G=A.inv()
    P=B.T*G*B
    return G,P,A

checks=0
for n in range(3,13):
    for root_t in [S.Rational(1,4),S.Rational(1,2),S.Integer(1),S.Integer(2)]:
        t=root_t**2
        G,P,A=projection(n,root_t)
        g0=G[0,0];gm=G[0,n//2]
        lr=S.factor(2*(1-t*g0)+2*root_t*(g0-gm))
        ls=S.factor(1+2*root_t*(g0-gm))
        check(A==t*S.eye(n)+2*S.eye(n)-S.Matrix(n,n,lambda i,j: int((i-j)%n in (1,n-1))),f'A construction n={n} t={t}');checks+=1
        check(P==P.T,f'symmetric n={n} t={t}');checks+=1
        check(P*P==P,f'idempotent n={n} t={t}');checks+=1
        check(G*S.ones(n,1)==(1/t)*S.ones(n,1),f'constant green n={n} t={t}');checks+=1
        check(all(G[i,j]>0 for i in range(n) for j in range(n)),f'green positivity n={n} t={t}');checks+=1
        check(all(G[0,j] >= G[0,(j+1)%n] for j in range(n//2)),f'green monotonic n={n} t={t}');checks+=1
        check(all(S.Add(*[abs(P[i,j]) for j in range(2*n)])==lr for i in range(n)),f'rim row n={n} t={t}');checks+=1
        check(all(S.Add(*[abs(P[i,j]) for j in range(2*n)])==ls for i in range(n,2*n)),f'spoke row n={n} t={t}');checks+=1
        check(lr-ls==1-2*t*g0,f'row competition n={n} t={t}');checks+=1
        check(ls<2,f'spoke strict two-bound n={n} t={t}');checks+=1
        # Exact sign vector attains each computed row norm.
        row=0 if lr>=ls else n
        sign=S.Matrix([S.sign(P[row,j]) if P[row,j]!=0 else 1 for j in range(2*n)])
        check(abs((P*sign)[row])==max(lr,ls),f'attainment n={n} t={t}');checks+=1
        check(max(abs(z) for z in sign)==1,f'bounded sign input n={n} t={t}');checks+=1
print('Matrix identity assertions:',checks)

G,P,_=projection(6,S.Rational(1,2))
g0,gm=G[0,0],G[0,3]
lr=2*(1-S.Rational(1,4)*g0)+g0-gm
check((g0,gm,lr)==(S.Rational(1188,1105),S.Rational(512,1105),S.Rational(2292,1105)),'six-rim witness')
checks+=1

u,v=S.symbols('u v',real=True)
p5=1-u-u**2+u**4-u**6+u**7+u**8
F5=(1-u**2)*(1+u**10)-u*(1-u**4)*(1-u**6)
check(S.expand(F5-(1-u**4)*p5)==0,'five-rim factorization');checks+=1
num=S.expand((v+2)**8*p5.subs(u,(v+1)/(v+2)))
positive=v**8+6*v**7+11*v**6+v**5+v**4+89*v**3+224*v**2+219*v+79
check(S.simplify(num-positive)==0,'positive polynomial substitution');checks+=1
check(S.Rational(1)-S.Rational(1,2)-S.Rational(1,4)-S.Rational(1,64)==S.Rational(15,64),'small-u positivity bound');checks+=1

# Spectral derivative at the critical infinite-volume weight.
t=S.symbols('t',positive=True)
s=S.sqrt(t/(t+4))
check(S.simplify(s.diff(t).subs(t,S.Rational(4,3))-S.Rational(9,64))==0,'threshold derivative');checks+=1
r=(t+2-S.sqrt(t*(t+4)))/2
check(S.simplify(r.subs(t,S.Rational(4,3))-S.Rational(1,3))==0,'critical decay ratio');checks+=1

print('ALL EXACT CHECKS PASSED:',checks,'assertions')
