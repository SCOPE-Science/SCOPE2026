"""Exact rational checks for the complete-bipartite stochastic dispersal calculation.
Run with Python 3: python verify.py
No third-party dependencies. Finite checks supplement, not replace, the all-size proof.
"""
from fractions import Fraction as F
import json


def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

def matadd(A,B):
    return [[x+y for x,y in zip(row1,row2)] for row1,row2 in zip(A,B)]

def scalar(q,A):
    return [[q*x for x in row] for row in A]

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def ident(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]

def value(n,a,d):
    return (1/(1-a*a)+1/(1-a*a*(1-2*d)**2)+(n-2)/(1-a*a*(1-d)**2))/n

def der_sign(n,a,d):
    return 2*(2*d-1)/(1-a*a*(2*d-1)**2)**2 - (n-2)*(1-d)/(1-a*a*(1-d)**2)**2


def check(n,a,d):
    m=n//2
    I=ident(n)
    u=[F(1) for _ in range(n)]
    s=[F(1) if i<m else F(-1) for i in range(n)]
    J=[[u[i]*u[j]/n for j in range(n)] for i in range(n)]
    H=[[s[i]*s[j]/n for j in range(n)] for i in range(n)]
    R=[[I[i][j]-J[i][j]-H[i][j] for j in range(n)] for i in range(n)]
    P=[[F(1,m) if (i<m)!=(j<m) else F(0) for j in range(n)] for i in range(n)]
    T=matadd(scalar(1-d,I),scalar(d,P))
    B=scalar(a,T)
    C=matadd(matadd(scalar(1/(1-a*a),J),scalar(1/(1-a*a*(1-2*d)**2),H)),scalar(1/(1-a*a*(1-d)**2),R))
    assert matadd(mm(mm(B,C),list(map(list,zip(*B)))),I)==C
    assert all(C[i][i]==value(n,a,d) for i in range(n))
    assert tr(C)==n*value(n,a,d)
    assert sum(C[i][j] for i in range(n) for j in range(n)) / (n*n)==1/(n*(1-a*a))
    return C[0][0]


def main():
    runs=[]
    for n in (4,6,8):
        for a in (F(1,3),F(1,2),F(2,3)):
            for d in (F(0),F(1,4),F(1,2),F(2,3),F(3,4),F(1)):
                v=check(n,a,d)
                runs.append({'n':n,'a':str(a),'d':str(d),'stationary_patch_variance':str(v)})
            assert der_sign(n,a,F(1,2))<0
            assert der_sign(n,a,F(1))>0
            if n==4:
                assert der_sign(n,a,F(2,3))==0
            else:
                assert der_sign(n,a,F(2,3))<0
                assert der_sign(n,a,F(n,n+2))>0
    assert check(6,F(1,2),F(3,4)) == F(1,6)*(F(4,3)+F(16,15)+F(256,63))
    return {'schema_version':1,'method':'exact rational matrix Lyapunov equality and analytic stationary-variance formula','test_cases':len(runs),'passed':True,'n_values':[4,6,8],'a_values':['1/3','1/2','2/3'],'d_values':['0','1/4','1/2','2/3','3/4','1'],'example_n6_a1over2_d3over4_variance':str(check(6,F(1,2),F(3,4))),'scope':'Finite tests corroborate algebra only; all-size and asymptotic statements are proved analytically.'}

if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,separators=(',',':')))
