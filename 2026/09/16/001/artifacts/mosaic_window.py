"""Finite-scale checks for the corrected mosaic arithmetic-window record.

The script does NOT estimate beta(alpha) from a rational number.  It checks the
exact two-step conjugacy numerically and illustrates how continued-fraction
convergents can be chosen so log(q_{n+1})/q_n approaches a prescribed positive
scale.  Every finite continued fraction printed below is, of course, rational.
"""
from decimal import Decimal, getcontext
from math import cos, pi, exp, log

getcontext().prec = 60


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def inv2(A):
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]


def maxerr(A,B):
    return max(abs(A[i][j]-B[i][j]) for i in range(2) for j in range(2))

E=0.73
lam=1.7
phi=0.271828
A=[[E-2*lam*cos(2*pi*phi),-1.0],[1.0,0.0]]
B=[[E,-1.0],[1.0,0.0]]
P=[[1.0,0.0],[-1.0,E]]
target=[[E*E-2-2*lam*E*cos(2*pi*phi),-1.0],[1.0,0.0]]
err=maxerr(matmul(matmul(P,matmul(B,A)),inv2(P)),target)
assert err < 1e-12
print('two_step_conjugacy_max_error =',err)

# Illustrative continued-fraction denominator growth.  Choosing a_{n+1}
# roughly exp(beta_target*q_n) makes log(q_{n+1})/q_n approach beta_target.
beta_target=0.08
q_prev,q=1,2
rows=[]
for n in range(4):
    a=max(1,int(round(exp(beta_target*q))))
    q_next=a*q+q_prev
    rows.append((n,a,q_prev,q,q_next,log(q_next)/q))
    q_prev,q=q,q_next
    if q>10**8:
        break
for row in rows:
    print('finite_CF_step',row)

print('NOTE: finite convergents are rational; no finite-sample beta(alpha) is asserted.')
