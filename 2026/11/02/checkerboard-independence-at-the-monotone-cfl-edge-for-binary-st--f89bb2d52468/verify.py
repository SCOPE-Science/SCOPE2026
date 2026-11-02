"""Exact small-state checks for binary-lattice stochastic-rounding heat schemes.

This standalone verification checks small dimensions. General statements rely on a proof.
"""
from fractions import Fraction as F
from itertools import product
from sympy import Matrix, Rational, eye

def transition(m,h):
    states=list(product((0,1),repeat=m))
    ix={s:k for k,s in enumerate(states)}
    mat=[]
    for state in states:
        p=[]
        for i in range(m):
            left=F(1,2) if i==0 else state[i-1]
            right=F(1,2) if i==m-1 else state[i+1]
            pi=(1-2*h)*state[i]+h*(left+right)
            assert 0<=pi<=1, (m,h,state,i,pi)
            p.append(pi)
        row=[]
        for s in states:
            pr=F(1)
            for j,bit in enumerate(s): pr*= p[j] if bit else 1-p[j]
            row.append(Rational(pr.numerator,pr.denominator))
        assert sum(row)==1
        mat.append(row)
    return states, Matrix(mat)

def stationary(P):
    size=P.rows
    A=P.T-eye(size)
    A[size-1,:]=Matrix(1,size,[1]*size)
    b=Matrix(size,1,[0]*(size-1)+[1])
    pi=A.inv()*b
    assert (P.T*pi)==pi
    assert sum(pi)==1 and all(z>0 for z in pi)
    return pi

def corr(states,pi,i,j):
    return sum(pi[k]*(2*s[i]-1)*(2*s[j]-1) for k,s in enumerate(states))

def parity_independence(states,pi):
    m=len(states[0]); odd=tuple(range(0,m,2)); even=tuple(range(1,m,2))
    dist_a={};dist_b={};joint={}
    for k,s in enumerate(states):
        a=tuple(s[i] for i in odd);b=tuple(s[i] for i in even)
        dist_a[a]=dist_a.get(a,0)+pi[k]
        dist_b[b]=dist_b.get(b,0)+pi[k]
        joint[a,b]=joint.get((a,b),0)+pi[k]
    assert all(joint[a,b]==dist_a[a]*dist_b[b] for a,b in joint)

count=0
for m,hs in [(2,[F(1,6),F(1,2),F(7,12)]),(3,[F(1,4),F(1,2)]),(4,[F(1,4),F(1,2)])]:
    for h in hs:
        states,P=transition(m,h)
        pi=stationary(P)
        for i in range(m):
            assert sum(pi[k]*(2*s[i]-1) for k,s in enumerate(states))==0
            for j in range(i+1,m):
                c=corr(states,pi,i,j)
                expected = 0 if h==F(1,2) and (j-i)%2 else 1 if h<F(1,2) or (j-i)%2==0 else -1
                assert ((1 if c>0 else 0)-(1 if c<0 else 0))==expected, (m,h,i,j,c,expected)
                count+=1
                if m==2:
                    want=Rational(2*(1-2*h),4-5*h)
                    assert c==want,(h,c,want)
                if m==3 and h==F(1,2) and (i,j)==(0,2):
                    assert c==Rational(1,4)
        if h==F(1,2): parity_independence(states,pi)
print('VERIFY_OK exact stationary Markov chains and checkerboard correlations:',count,'pair checks')
