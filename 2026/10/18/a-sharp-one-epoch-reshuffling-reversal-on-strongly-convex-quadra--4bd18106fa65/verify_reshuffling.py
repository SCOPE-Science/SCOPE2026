"""Finite exact-arithmetic checks for the two-quadratic reshuffling phase theorem.

Requires only the Python standard library. Computation illustrates the algebraic
identities; the written proof handles all real parameters in their stated range.
"""
from fractions import Fraction as F
from itertools import product

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mv(a,v):
    return [sum(a[i][j]*v[j] for j in range(2)) for i in range(2)]
def inner(x,a,y):
    return sum(x[i]*sum(a[i][j]*y[j] for j in range(2)) for i in range(2))
def check(b,p):
    assert 0<b<1 and 0<p<1
    P=[[F(0),F(0)],[F(0),b]]
    Q=[[p/2,p/2],[p/2,p/2]]
    H=[[(F(1) if i==j else F(0))-(P[i][j]+Q[i][j])/2 for j in range(2)] for i in range(2)]
    x0=[F(1),F(0)]
    after=[]
    for a,c in product((P,Q),repeat=2):
        y=mv(c,mv(a,x0))
        after.append(inner(y,H,y)/2)
    iid=sum(after)/4
    rr=(after[1]+after[2])/2
    poly=-2*b**3-b*b*p+4*b*b+2*b*p*p+4*p**3-8*p*p
    assert rr-iid==p*p*poly/128, (b,p,rr,iid)
    sq_rr=(sum(t*t for t in mv(P,mv(Q,x0)))+sum(t*t for t in mv(Q,mv(P,x0))))/2
    sq_iid=sum(sum(t*t for t in mv(c,mv(a,x0))) for a,c in product((P,Q),repeat=2))/4
    assert sq_rr-sq_iid==p*p*(b*b-2*p*p)/16
    if p==F(1,2):assert rr-iid==(4*b-3)*(1+b-b*b)/1024
    return poly

def main():
    count=0; winners=0; ties=0
    for den in range(2,24):
        for a in range(1,den):
            for c in range(1,den):
                t=check(F(a,den),F(c,den))
                count+=1
                winners+=int(t>0);ties+=int(t==0)
    assert check(F(7,8),F(1,2))>0
    assert check(F(3,4),F(1,2))==0
    assert check(F(1,2),F(1,2))<0
    print(f'PASS exact rational {count} parameter pairs; RR-worse {winners}; tie {ties}')
    print('PASS objective and norm-squared formulas, including the 3/4 phase threshold')

if __name__=='__main__': main()
