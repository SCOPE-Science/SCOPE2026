#!/usr/bin/env python3
"""Exact reproduction of the four-season two-patch matrix ordering theorem.
Requires Python 3 and SymPy. No external data files are used.
"""
from fractions import Fraction as F
from itertools import permutations, product
from sympy import Matrix, diag, symbols, factor, simplify

p = symbols('p')
a = symbols('a1:5')
b = symbols('b1:5')
P = Matrix([[1-p,p],[p,1-p]])
S = [diag(a[i],b[i])*P for i in range(4)]

def trace_for(order):
    Q=Matrix.eye(2)
    for k in order: Q=Q*S[k]
    return Q.trace()

def cross(i,j):
    return a[i]*b[j]-a[j]*b[i]

I=(0,1,2,3); H=(0,1,3,2); L=(0,2,1,3)
K=p**2*(1-2*p)
assert simplify(trace_for(H)-trace_for(I)-K*cross(0,1)*cross(2,3))==0
assert simplify(trace_for(I)-trace_for(L)-K*cross(0,3)*cross(1,2))==0
assert simplify(trace_for(H)-trace_for(L)-K*cross(0,2)*cross(1,3))==0
# Every four-factor word is trace-equivalent to one of the three representatives
for order in permutations(range(4)):
    assert any(simplify(trace_for(order)-trace_for(rep))==0 for rep in (I,H,L))
# Matrices are P-selfadjoint in the algebraic sense M.T = P M P^{-1} (p!=1/2).
for i in range(4):
    assert simplify(S[i].T*P-P*S[i])==Matrix.zeros(2)
# For one, two and three factors, all orders have a common trace and determinant.
for k in (1,2,3):
    vals=[]
    for order in permutations(range(k)):
        Q=Matrix.eye(2)
        for j in order:Q=Q*S[j]
        vals.append((Q.trace(),Q.det()))
    assert all(simplify(v[0]-vals[0][0])==0 and simplify(v[1]-vals[0][1])==0 for v in vals)

# Independent exact arithmetic, including p on either side of 1/2 and all sign combinations.
def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)] for i in (0,1)]

def mat_for(rate_pair,m):
    r,s=rate_pair
    return [[r*(1-m),r*m],[s*m,s*(1-m)]]

def stats(order,rates,m):
    Q=[[F(1),F(0)],[F(0),F(1)]]
    for j in order:Q=mul(Q,mat_for(rates[j],m))
    return Q[0][0]+Q[1][1],Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]

count=0
for m in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
    for x in [1,2,3,4,5]:
        for y in [6,7,8,9]:
            rates=[(F(x),F(2)),(F(y),F(2)),(F(10),F(2)),(F(12),F(2))]
            t_h,d_h=stats(H,rates,m);t_i,d_i=stats(I,rates,m);t_l,d_l=stats(L,rates,m)
            assert d_h==d_i==d_l
            k=m*m*(1-2*m)
            def c(i,j):return rates[i][0]*rates[j][1]-rates[j][0]*rates[i][1]
            assert t_h-t_i == k*c(0,1)*c(2,3)
            assert t_i-t_l == k*c(0,3)*c(1,2)
            assert t_h-t_l == k*c(0,2)*c(1,3)
            count+=1

m=F(1,4); q=F(16,29)
rates=[(F(i)*q,q) for i in (1,2,3,4)]
for order in (H,I,L):
    t,d=stats(order,rates,m)
    print(''.join(str(i+1) for i in order),'trace',t,'det',d,'det(I-Q)',1-t+d)
assert (1-stats(H,rates,m)[0]+stats(H,rates,m)[1])<0
assert (1-stats(L,rates,m)[0]+stats(L,rates,m)[1])>0
assert 0<stats(H,rates,m)[1]<1
print('EXACT_CHECK_OK',count,'rational samples plus symbolic universal identities')
