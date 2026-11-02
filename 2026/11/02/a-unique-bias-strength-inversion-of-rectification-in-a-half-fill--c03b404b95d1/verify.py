#!/usr/bin/env python3
"""Exact symbolic check of the six-configuration two-particle trap-ASEP theorem.

Run: python verify.py (requires sympy 1.10+). No random, sampled, or floating-point
steps are used to establish any polynomial identity.
"""
from itertools import combinations, product
from fractions import Fraction
import sympy as s

p,q,a,b,c,d=s.symbols('p q a b c d')
w=(a,b,c,d)
S=list(combinations(range(4),2))
I={x:i for i,x in enumerate(S)}
Q=s.zeros(6)
for i,occ in enumerate(S):
    for k in occ:
        for step,scale in ((1,p),(-1,q)):
            target=(k+step)%4
            if target not in occ:
                new=tuple(sorted((set(occ)-{k})|{target}))
                Q[i,I[new]]+=w[k]*scale
for i in range(6):
    Q[i,i]=-sum(Q[i,j] for j in range(6) if j!=i)
T=[s.expand((-Q).minor_submatrix(i,i).det(method='domain-ge')) for i in range(6)]
D=sum(T)
signed=[sum(w[k]*((p if (k+1)%4 not in occ else 0)
                     -(q if (k-1)%4 not in occ else 0)) for k in occ)
        for occ in S]
N=s.expand(sum(T[i]*signed[i] for i in range(6)))
A=a+c; B=b+d; P=a*c; R=b*d
h2=P*B-R*A
h1=(A+B)*(P-R)+A*B*(B-A)
H=(p*p+q*q)*h2+p*q*h1
F=4*a*b*c*d*(p-q)*(p+q)*(p*p+q*q)*(A*p+B*q)*(A*q+B*p)
assert s.expand(N-F)==0
Drev=D.xreplace({p:q,q:p})
Nrev=N.xreplace({p:q,q:p})
E=-4*a*b*c*d*p*q*(a-c)*(b-d)*(p-q)**2*(p+q)*(p*p+q*q)*(A*p+B*q)*(A*q+B*p)*H
assert s.expand(N*Drev+Nrev*D-E)==0
# Algebraic exact witness for a unique crossover in (0,1).
e=s.symbols('e',positive=True)
Hexample=s.factor(H.subs({a:1,b:2,c:4,d:9,p:(1+e)/2,q:(1-e)/2}))
assert s.expand(Hexample-(7-99*e**2)/2)==0
assert h2.subs({a:1,b:2,c:4,d:9})==-46
assert h1.subs({a:1,b:2,c:4,d:9})==106
# Directly solve 6x6 Markov stationarity using exact rational linear algebra;
# this is independent of determinant tree weights and the factorizations.
num=0
for rates in ((1,2,4,9),(1,2,3,9),(2,1,9,3),(1,4,4,1),
              (1,2,1,4),(1,2,4,2),(3,5,9,4),(1,3,4,8)):
    for up,down in ((s.Rational(2,5),s.Rational(3,5)),
                    (s.Rational(3,5),s.Rational(2,5)),
                    (s.Rational(5,6),s.Rational(1,6)),
                    (s.Rational(1,2),s.Rational(1,2))):
        Qn=Q.subs(dict(zip((a,b,c,d,p,q),rates+(up,down))))
        M=Qn.T.copy();M[5,:]=s.ones(1,6)
        z=s.zeros(6,1);z[5]=1
        pi=M.inv()*z
        Jreal=sum(pi[i]*signed[i].subs(dict(zip((a,b,c,d,p,q),rates+(up,down)))) for i in range(6))
        Jtheory=s.factor((N/D).subs(dict(zip((a,b,c,d,p,q),rates+(up,down)))))
        assert Jreal==Jtheory
        num+=1
# No globally vanishing H except equal unordered opposite pairs when both
# contrasts are nonzero. This follows from AM-GM and is proved in RESULT.md;
# here test its derived exact symbolic elimination identity.
AA,BB,PP,RR=s.symbols('AA BB PP RR',positive=True)
hfirst=PP*BB-RR*AA
hsecond=(AA+BB)*(PP-RR)+AA*BB*(BB-AA)
assert s.simplify(hsecond.subs({PP:RR*AA/BB})-(AA-BB)*(RR*(AA+BB)/BB-AA*BB))==0
print('PASS: 2 global polynomial identities; unique exact crossover;')
print(f'{num} independent exact-rational six-state stationary solves;')
print('and elimination identity for the reflection-only classification')
