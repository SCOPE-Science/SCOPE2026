"""Reproduce two-conductance star heat-Lipschitz identities (standard library)."""
from fractions import Fraction
from math import exp, sqrt, log


def data(k, a, b, t):
    tr = 2*a + (k+1)*b
    det = (k+2)*a*b
    delta = sqrt(tr*tr-4*det)
    alpha = (tr-delta)/2
    beta = (tr+delta)/2
    d = k*b-2*a
    X = ((beta+d)*exp(-alpha*t)-(alpha+d)*exp(-beta*t))/delta
    return X, alpha, beta, delta


def norm_direct(k, a, b, t):
    # Independent uniformization of the full (k+2)-state Markov heat kernel.
    n = k+2
    weights = [a]+[b]*k
    q = sum(weights)
    P = [[0.0]*n for _ in range(n)]
    P[0][0] = 0.0
    for i,c in enumerate(weights,1):
        P[0][i]=c/q
        P[i][0]=c/q
        P[i][i]=1-c/q
    rows = [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
    H = [[0.0]*n for _ in range(n)]
    coeff = exp(-q*t)
    mass = 0.0
    for degree in range(300):
        for i in range(n):
            for j in range(n):
                H[i][j]+=coeff*rows[i][j]
        mass+=coeff
        if degree>q*t and 1-mass < 4e-15:
            break
        new = [[sum(rows[i][h]*P[h][j] for h in range(n)) for j in range(n)] for i in range(n)]
        rows=new
        coeff *= q*t/(degree+1)
    assert mass>1-3e-14, (k,a,b,t,mass)
    edge_norms=[]
    for leaf in range(1,n):
        # For a star graph with unit metric edges, these are the
        # independent independent coordinate response coefficients.
        heat_row = [H[leaf][v]-H[0][v] for v in range(n)]
        coefficient=[heat_row[j]-0 for j in range(1,n)]
        edge_norms.append(sum(abs(c) for c in coefficient))
    return edge_norms,H


def exact_intertwining(k,a,b):
    # D maps functions to leaf minus hub gradients; Q is -L.
    n=k+2; weights=[Fraction(a)]+[Fraction(b)]*k
    Q=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j,c in enumerate(weights,1):
        Q[0][0]-=c;Q[j][j]-=c;Q[0][j]=c;Q[j][0]=c
    D=[[-Fraction(1)]+[Fraction(int(j==i)) for j in range(1,n)] for i in range(1,n)]
    m=k+1
    B=[[-weights[j]- (weights[i] if i==j else 0) for j in range(m)] for i in range(m)]
    left=[[sum(D[i][h]*Q[h][j] for h in range(n)) for j in range(n)] for i in range(m)]
    right=[[sum(B[i][h]*D[h][j] for h in range(m)) for j in range(n)] for i in range(m)]
    assert left==right


def run():
    tested=0; unique_edges=0; gradient_checks=0; large_limits=0
    for k,a,b in [(2,1,2),(2,1,10),(3,2,5),(5,1,11),(6,3,4),(2,1,1),(3,2,2)]:
        exact_intertwining(k,a,b);gradient_checks+=1
        for t in [0.01,0.07,0.2,0.6]:
            analytic,alpha,beta,delta=data(k,a,b,t)
            other,H=norm_direct(k,a,b,t)
            assert abs(analytic-other[0])<3e-11, (k,a,b,t,analytic,other)
            assert abs(other[1]-other[-1])<1e-11, (k,a,b,t,other)
            if b>a:
                assert other[0]>max(other[1:])+1e-13, (k,a,b,t,other)
                unique_edges+=1
            else: assert max(other)-min(other)<1e-11
            tested+=1
    for k in range(2,9):
        a=1; b=10**5
        X,alpha,beta,delta=data(k,a,b,1/sqrt(a*b))
        assert 0 < (2*k+1)/(k+1)-X < 0.06
        large_limits+=1
    assert Fraction(3*2+1-2*1,1)>0
    print('CHECK_OK exact_gradient_intertwining',gradient_checks,'independent_full_heat_cases',tested,'strict_slow_leaf_cases',unique_edges,'singular_limit_cases',large_limits)

if __name__=='__main__':run()
