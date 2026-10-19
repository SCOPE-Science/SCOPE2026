"""Exact finite-state checks for gated symmetric exclusion fluctuations."""
from fractions import Fraction
from itertools import combinations
import sympy as s

R=s.Rational

def lap(n,edges):
    L=s.zeros(n)
    for a,b,r in edges:
        L[a,a]+=r;L[b,b]+=r;L[a,b]-=r;L[b,a]-=r
    return L

def matrices(n,edges_on,edges_off,p,kappa):
    L_on=lap(n,edges_on);L_off=lap(n,edges_off)
    I=s.eye(n)
    A=L_on+(1-p)*kappa*I
    D=L_off+p*kappa*I
    B=-(1-p)*kappa*I
    C=-p*kappa*I
    return s.BlockMatrix([[A,B],[C,D]]).as_explicit()

def states(n,k):
    return list(combinations(range(n),k))

def full_lap(n,k,edges_on,edges_off,p,kappa):
    config=states(n,k); m=len(config); idx={x:i for i,x in enumerate(config)}
    H=s.zeros(2*m)
    for gate,edges in enumerate((edges_on,edges_off)):
        for i,occupied in enumerate(config):
            occupied=set(occupied)
            for a,b,r in edges:
                if (a in occupied)!=(b in occupied):
                    new=tuple(sorted(occupied.symmetric_difference({a,b})))
                    j=idx[new]
                    H[gate*m+i,gate*m+i]+=r
                    H[gate*m+i,gate*m+j]-=r
    for i in range(m):
        H[i,i]+=(1-p)*kappa
        H[i,m+i]-=(1-p)*kappa
        H[m+i,m+i]+=p*kappa
        H[m+i,i]-=p*kappa
    return H,config

def solve_zero_mode(H,x):
    # H preserves uniformly site-centered functions separately in gate layers.
    n=len(x)//2
    A=s.Matrix(H);y=s.Matrix(x)
    # Gauge global constant by replacing first row with weighted stationary average of potentials.
    A[0,:]=s.Matrix([[1]*len(x)])
    y[0]=0
    return A.inv()*y

def variance(n,k,edges_on,edges_off,p,kappa,h):
    h=s.Matrix(h);assert sum(h)==0
    X=s.Matrix(list(h)+list(h))
    H=matrices(n,edges_on,edges_off,p,kappa)
    v=solve_zero_mode(H,X)
    chi=R(k*(n-k),n*(n-1))
    vpred=2*chi*(p*(h.dot(v[:n,0]))+(1-p)*(h.dot(v[n:,0])))
    FH,cfg=full_lap(n,k,edges_on,edges_off,p,kappa)
    obs=s.Matrix([sum(h[i] for i in c) for _gate in range(2) for c in cfg])
    vfull=solve_zero_mode(FH,obs)
    mm=len(cfg)
    direct=2*(p*sum(obs[i]*vfull[i] for i in range(mm))+(1-p)*sum(obs[mm+i]*vfull[mm+i] for i in range(mm)))/mm
    assert s.simplify(vpred-direct)==0,(vpred,direct)
    return s.factor(vpred)

def run():
    p=R(2,5); r=R(3,2)
    n=4;k=2;a=2;b=2
    all_edges=[(u,v,r) for u in range(n) for v in range(u+1,n)]
    off=[e for e in all_edges if (e[0]<a)==(e[1]<a)]
    h=[R(1)-R(a,n) if i<a else -R(a,n) for i in range(n)]
    varstat=R(k*(n-k)*a*b,n*n*(n-1))
    for K in (R(1,10),R(1),R(3),R(11,7)):
        actual=variance(n,k,all_edges,off,p,K,h)
        expected=2*varstat*(1/(p*r*n)+(1-p)/(p*K))
        assert s.factor(actual-expected)==0,(actual,expected)
    print('complete graph gated exact formula 4 switch rates: PASS')
    # Generic graph with a two-component off state; repeated at four switching speeds.
    n=5;k=2;p=R(1,3)
    on=[(i,(i+1)%n,R(1)) for i in range(n)]
    off=[(0,1,R(1)),(2,3,R(1)),(3,4,R(1))]
    h=[R(3,5),R(3,5),-R(2,5),-R(2,5),-R(2,5)]
    L=2*R(k*(n-k),n*(n-1))*R(1-p,p)*sum(x*x for x in h)
    vals=[]
    for K in (R(1,2),R(1,10),R(1,100),R(1,1000)):
        V=variance(n,k,on,off,p,K,h)
        assert s.factor(K*V-L)>=0
        # Non-asymptotic lower bound K V >= L should hold; replace inequality.
        vals.append((K,V,s.factor(K*V-L)))
    print('generic cycle values:',vals)
    # An observable orthogonal to both disconnected OFF-component constants:
    # no divergent coefficient, and its exact finite small-rate variance stays bounded.
    orth=[R(1),-R(1),R(1),-R(1),R(0)]
    symbolic_kappa=s.symbols('z',positive=True)
    # Matrix identity on vertex sector gives full closed rational function in z.
    reduced=matrices(n,on,off,p,symbolic_kappa)
    x=s.Matrix(orth+orth)
    solved=solve_zero_mode(reduced,x)
    v=s.factor(2*R(k*(n-k),n*(n-1))*(
         p*s.Matrix(orth).dot(solved[:n,0])+
         (1-p)*s.Matrix(orth).dot(solved[n:,0])))
    assert s.limit(v,symbolic_kappa,0,dir='+').is_finite
    assert s.limit(symbolic_kappa*v,symbolic_kappa,0,dir='+')==0
    for K in (R(1,2),R(1,10)):
        assert s.simplify(variance(n,k,on,off,p,K,orth)-v.subs(symbolic_kappa,K))==0
    print('off-component-orthogonal observable, finite slow-switching variance: PASS')
    # OFF graph can remain connected: the cut projection vanishes.
    connected_off=[(i,i+1,R(1)) for i in range(n-1)]
    for K in (R(1,2),R(1,20)):
        v=variance(n,k,on,connected_off,p,K,h)
        assert v>0
    print('connected OFF graph finite exact generator comparisons: PASS')
    # Exclusion duality is independent of the number of particles.
    n=4;p=R(3,7);r=R(2)
    all_edges=[(u,v,r) for u in range(n) for v in range(u+1,n)]
    off=[e for e in all_edges if (e[0]<2)==(e[1]<2)]
    h=[R(1,2),R(1,2),-R(1,2),-R(1,2)]
    for k in (1,2,3):
        varstat=R(k*(n-k)*2*2,n*n*(n-1))
        for K in (R(1,5),R(5,3)):
            got=variance(n,k,all_edges,off,p,K,h)
            target=2*varstat*(1/(p*r*n)+(1-p)/(p*K))
            assert s.factor(got-target)==0
    print('complete graph 3 distinct particle counts and switching values: PASS')

if __name__=='__main__':run()
