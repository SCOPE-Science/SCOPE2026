"""Reproduce exact Schur-square identities and example graph calculations.

Requires SymPy; no floating-point data or network downloads are used.
Run: python verify.py
"""
import sympy as sp


def assert_zero_matrix(M):
    if any(sp.simplify(a) != 0 for a in M):
        raise AssertionError('matrix identity failed')


def graph_cycle(n):
    A = sp.zeros(n)
    for i in range(n):
        A[i, (i+1) % n] = A[(i+1) % n, i] = 1
    return A


def graph_petersen():
    A = sp.zeros(10)
    edges = [(i, (i+1) % 5) for i in range(5)]
    edges += [(5+i, 5+(i+2) % 5) for i in range(5)]
    edges += [(i, i+5) for i in range(5)]
    for i,j in edges:
        A[i,j] = A[j,i] = 1
    return A


def graph_rook(q):
    n = q*q
    A = sp.zeros(n)
    for a in range(n):
        for b in range(a+1,n):
            if a//q == b//q or a%q == b%q:
                A[a,b] = A[b,a] = 1
    return A


def check_srg(A, n,k,lam,mu,r,s):
    I,J = sp.eye(n),sp.ones(n)
    assert A == A.T
    assert all(A[i,i]==0 for i in range(n))
    assert_zero_matrix(A*sp.ones(n,1)-k*sp.ones(n,1))
    assert_zero_matrix(A*A-(lam-mu)*A-(k-mu)*I-mu*J)
    E0=J/sp.Integer(n)
    Er=(A-s*I-(k-s)*E0)/(r-s)
    Es=(r*I-A+(k-r)*E0)/(r-s)
    assert_zero_matrix(E0+Er+Es-I)
    assert_zero_matrix(Er*Er-Er)
    assert_zero_matrix(Es*Es-Es)
    assert_zero_matrix(Er*Es)
    H=E0.multiply_elementwise(E0)+Er.multiply_elementwise(Er)+Es.multiply_elementwise(Es)
    m=sp.simplify(sp.trace(Er)); p=sp.simplify(sp.trace(Es))
    ell=n-k-1
    d=(1+m*m+p*p)/sp.Integer(n)**2
    e=(1+m*m*r*r/sp.Integer(k)**2+p*p*s*s/sp.Integer(k)**2)/sp.Integer(n)**2
    f=(1+m*m*(r+1)**2/sp.Integer(ell)**2+p*p*(s+1)**2/sp.Integer(ell)**2)/sp.Integer(n)**2
    assert_zero_matrix(H - ((d-f)*I+(e-f)*A+f*J))
    eigen_r=sp.simplify(d-f+(e-f)*r)
    eigen_s=sp.simplify(d-f+(e-f)*s)
    target_r=sp.simplify((r*r+s*(s+2))/(r-s)**2-2*r*(s+1)/((k-r)*(r-s)))
    assert sp.simplify(eigen_r-target_r)==0
    assert_zero_matrix(H*Er-eigen_r*Er)
    assert_zero_matrix(H*Es-eigen_s*Es)
    assert_zero_matrix(H*E0-E0)
    assert eigen_r>0 and eigen_s>0
    assert H.rank()==n
    return n, sp.simplify(eigen_r),sp.simplify(eigen_s)


def general_symbolic_identity():
    k,r,s=sp.symbols('k r s',real=True)
    n=sp.factor((k-r)*(k-s)/(k+r*s))
    ell=sp.factor(n-k-1)
    m=sp.factor((-k-(n-1)*s)/(r-s))
    p=sp.factor(n-1-m)
    d=(1+m*m+p*p)/n**2
    e=(1+m*m*r*r/k**2+p*p*s*s/k**2)/n**2
    f=(1+m*m*(r+1)**2/ell**2+p*p*(s+1)**2/ell**2)/n**2
    expression=sp.factor(d-f+(e-f)*r)
    desired=(r*r+s*(s+2))/(r-s)**2-2*r*(s+1)/((k-r)*(r-s))
    assert sp.factor(expression-desired)==0
    # The complement has the same three spectral projections with
    # r_complement=-1-s and s_complement=-1-r.
    kc=sp.factor(ell)
    rc=-1-s
    sc=-1-r
    analogous=(rc*rc+sc*(sc+2))/(rc-sc)**2-2*rc*(sc+1)/((kc-rc)*(rc-sc))
    assert sp.factor((d-f+(e-f)*s)-analogous)==0
    return 2


def main():
    symbolic=general_symbolic_identity()
    examples=[
        ('cycle-five',graph_cycle(5),5,2,0,1,(-1+sp.sqrt(5))/2,(-1-sp.sqrt(5))/2),
        ('petersen',graph_petersen(),10,3,0,1,sp.Integer(1),sp.Integer(-2)),
        ('rook-three',graph_rook(3),9,4,1,2,sp.Integer(1),sp.Integer(-2)),
        ('rook-four',graph_rook(4),16,6,2,2,sp.Integer(2),sp.Integer(-2)),
    ]
    J,I=sp.ones(10),sp.eye(10)
    examples.append(('complement-petersen',J-I-graph_petersen(),10,6,3,4,sp.Integer(1),sp.Integer(-2)))
    for name,A,n,k,lam,mu,r,s in examples:
        N,v_r,v_s=check_srg(A,n,k,lam,mu,r,s)
        print(name,N,'nonprincipal=',v_r,v_s)
    print('VERIFY_OK symbolic_identities=%s exact_SRG_graphs=%s full_rank_checks=%s'%(symbolic,len(examples),len(examples)))

if __name__ == '__main__':
    main()
