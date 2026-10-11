"""Reproduce exact K_{m,m} PQ adjacency Löwner-contact identities.

Dependencies: Python >=3.9, sympy >=1.10. Run `python verification/verify.py`.
This is finite verification, not the all-dimensional proof.
"""
import sympy as S


def test(m):
    n = 2*m
    dim = 2*(n-1)
    t = S.Integer(2)/(1+S.sqrt(8*n-7))
    assert S.simplify(1-t-2*(n-1)*t**2)==0
    I = S.eye(n)
    ones = S.ones(n, 1)
    H = I - ones*ones.T/n
    s = S.Matrix([1]*m+[-1]*m)
    Sproj = s*s.T/n
    H0 = H-Sproj
    A=S.zeros(n)
    for i in range(n):
        for j in range(n):
            if (i<m)!=(j<m): A[i,j]=1
    assert A*ones == m*ones
    assert S.simplify(A*Sproj+m*Sproj)==S.zeros(n)
    assert A*H0==S.zeros(n)
    V=[]
    for i in range(n):V.append((i,i,'diag'))
    for i in range(n):
        for j in range(n):
            if A[i,j]:V.append((i,j,'edge'))
    assert len(V)==n+2*m*m
    mean=S.zeros(2*n,1)
    cov=S.zeros(2*n)
    for i,j,kind in V:
        vec=S.zeros(2*n,1)
        vec[i]=1;vec[n+j]=1
        vec-=S.ones(2*n,1)/n
        wt=t/n if kind=='diag' else (1-t)/(2*m*m)
        mean+=wt*vec
        cov+=wt*(vec*vec.T)
    assert mean==S.zeros(2*n,1)
    cross=(t*H+(1-t)*(A/m-ones*ones.T/n))/n
    block=S.Matrix.hstack(H/n,cross)
    block2=S.Matrix.hstack(cross,H/n)
    model=block.col_join(block2)
    assert all(S.simplify(v)==0 for v in cov-model)
    def quad(i,j):
        a=S.zeros(n,1);b=S.zeros(n,1)
        a[i]=1;b[j]=1
        a-=ones/n;b-=ones/n
        u=(a+b)/S.sqrt(2);v=(a-b)/S.sqrt(2)
        usq=S.simplify((u.T*Sproj*u)[0]);vssq=S.simplify((v.T*Sproj*v)[0])
        u0sq=S.simplify((u.T*H0*u)[0]);v0sq=S.simplify((v.T*H0*v)[0])
        return S.simplify(usq/(2*t)+u0sq/(1+t)+vssq/(2*(1-t))+v0sq/(1-t))
    for i,j,kind in V:
        assert S.simplify(quad(i,j)-S.Rational(dim,n))==0,(m,i,j,kind)
    # Two independent norm expressions and their equality at t=t_*.
    qdiag=S.Rational(1,n)*(1/t+2*(n-2)/(1+t))
    qedge=S.Rational(1,n)*((n-2)/(1+t)+(n-1)/(1-t))
    assert S.simplify(qdiag-qedge)==0
    assert S.simplify(qdiag-S.Rational(dim,n))==0
    determinant=S.simplify(4*t*(1-t)*(1-t*t)**(n-2)/n**dim)
    assert determinant>0
    print('PASS',{'m':m,'n':n,'vertices':len(V),'dim':dim,
                  't':str(S.simplify(t)),'det_C_approx':float(determinant)})

for m in (2,3,4,5):
    test(m)
print('ALL_CHECKS_PASS')
