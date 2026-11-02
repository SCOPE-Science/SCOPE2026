"""Exact checks for the four-snapshot triangle SIS threshold separation.
Run: python verify.py (Python 3.9 or later; standard library only).
"""
from fractions import Fraction as F
from itertools import permutations
I=lambda n:[[F(i==j) for j in range(n)] for i in range(n)]
def mm(X,Y):
 return [[sum(X[i][k]*Y[k][j] for k in range(len(X))) for j in range(len(Y[0]))] for i in range(len(X))]
def mv(X,v):
 return [sum(x*y for x,y in zip(r,v)) for r in X]
def edge(i,j):
 M=I(3)
 M[i][i]=M[j][j]=F(5,4)
 M[i][j]=M[j][i]=F(3,4)
 return M
def order(*q):
 P=I(3)
 for E in q: P=mm(E,P)
 return P
def det3(M):
 a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
 return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
def cp(M):
 tr=sum(M[i][i] for i in range(3))
 tr2=sum(mm(M,M)[i][i] for i in range(3))
 return (tr,(tr*tr-tr2)/2,det3(M))
A=edge(0,1); B=edge(1,2); C=edge(0,2)
for perm in permutations([A,B,C]):
 assert cp(order(*perm))==cp(order(A,B,C))
X=order(A,A,B,C);Y=order(A,B,A,C)
assert cp(X)==(F(1015,128),F(745,128),F(1)),cp(X)
assert cp(Y)==(F(1985,256),F(1553,256),F(1)),cp(Y)
u=[F(x) for x in (16,11,16)];v=[F(x) for x in (16,11,14)]
assert [x-7*y for x,y in zip(mv(X,u),u)]==[F(167,128),F(55,32),F(513,128)]
assert [7*y-x for x,y in zip(mv(Y,v),v)]==[F(59,256),F(157,64),F(381,256)]
assert all(x>0 for x in [a-7*b for a,b in zip(mv(X,u),u)])
assert all(x>0 for x in [7*b-a for a,b in zip(mv(Y,v),v)])
# All 24 orders have exactly two characteristic polynomials (dihedral order types).
classes={cp(order(*p)) for p in permutations([A,A,B,C])}
assert classes=={cp(X),cp(Y)}, classes
print('PASS: 6 three-snapshot permutations, two exact four-snapshot spectra,')
print('      rational Perron upper/lower certificates, all 24 four-snapshot orders.')
