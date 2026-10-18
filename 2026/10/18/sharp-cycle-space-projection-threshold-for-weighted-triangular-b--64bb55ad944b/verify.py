#!/usr/bin/env python3
"""Exact column checks and optional independent full LP for triangular books.

Requires Python 3 standard library. Full non-symmetric LP also requires NumPy/SciPy.
"""
from fractions import Fraction as F


def lam(m, t):
    t = F(t)
    assert m >= 2 and 0 < t <= 2
    if m*(2-t) >= 4:
        return 1+t/2, F(0)
    v = t*(t+2)/(m*(t*t+4)+4*t)
    return m*(t+2)**2/(m*(t*t+4)+4*t), -v


def exact_check(m, t):
    t = F(t)
    expected, u = lam(m,t)
    E = 2*m+1
    # The cycle basis uses the first coordinate for the common edge.
    z = [[F(-1)]+[F(i == k) for i in range(m)]+[F(i == k) for i in range(m)] for k in range(m)]
    cols = []
    cols.append([sum(u*z[k][j] for k in range(m)) for j in range(E)])
    for block in range(2):
        for i in range(m):
            coeff=[(1+u)/2 if k==i else u/2 for k in range(m)]
            cols.append([sum(coeff[k]*z[k][j] for k in range(m)) for j in range(E)])
    # Projection identity on the independent cycle vectors.
    for k in range(m):
        out=[cols[1+k][j]+cols[1+m+k][j]-cols[0][j] for j in range(E)]
        assert out == z[k]
    w=[t]+[F(1)]*(2*m)
    colnorm=[sum(w[j]*abs(col[j]) for j in range(E))/w[i] for i,col in enumerate(cols)]
    assert max(colnorm)==expected,(m,t,colnorm,expected)
    # Audit the one-variable lower envelope at its breakpoints.
    def norm(u):
        return max(m*(2+t)*abs(u)/t,abs(1+u)+(m-1)*abs(u)+t*abs(1+m*u)/2)
    pts=[F(0),-F(1,m),F(-1),u]+[F(j,10*m) for j in range(-100*m,100*m+1)]
    assert all(norm(z)>=expected for z in pts)
    return expected


def solve_full_lp(m,t):
    """Independent optimization of an arbitrary, not-necessarily-invariant projection."""
    import numpy as np
    from scipy.optimize import linprog
    t=float(t)
    E=2*m+1
    Z=np.zeros((E,m));Z[0,:]=-1
    for i in range(m):Z[1+i,i]=1;Z[1+m+i,i]=1
    w=np.ones(E);w[0]=t
    nq=m*E;na=E*E;idx=nq+na
    nvar=idx+1;Aeq=[];beq=[];Aub=[];bub=[]
    for a in range(m):
        for b in range(m):
            row=np.zeros(nvar)
            for j in range(E):row[a*E+j]=Z[j,b]
            Aeq.append(row);beq.append(float(a==b))
    for i in range(E):
        for j in range(E):
            for sgn in [1,-1]:
                row=np.zeros(nvar);row[nq+i*E+j]=-1
                for a in range(m):row[a*E+j]=sgn*Z[i,a]
                Aub.append(row);bub.append(0.)
    for j in range(E):
        row=np.zeros(nvar);row[idx]=-w[j]
        for i in range(E):row[nq+i*E+j]=w[i]
        Aub.append(row);bub.append(0.)
    c=np.zeros(nvar);c[idx]=1.
    out=linprog(c,A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,
        bounds=[(None,None)]*nq+[(0,None)]*(na+1),method='highs')
    assert out.success,out.message
    return out.fun


def main():
    samples=[F(1,10),F(1,2),F(2,3),F(1),F(5,4),F(3,2),F(9,5),F(2)]
    tests=0
    for m in range(2,16):
        for t in samples:
            exact_check(m,t);tests+=1
    print('Exact tests:',tests,'passed')
    try:
        from scipy.optimize import linprog
        import numpy
    except ImportError:
        print('Full LP skipped: optional SciPy/NumPy missing')
    else:
        lp=0
        for m in range(2,7):
            for t in [F(1,2),F(1),F(3,2),F(2)]:
                value=float(lam(m,t)[0])
                solved=solve_full_lp(m,t)
                assert abs(solved-value) <= 1e-8,(m,t,value,solved)
                lp+=1
        print('Independent full LP tests:',lp,'passed')

if __name__ == '__main__':
    main()
