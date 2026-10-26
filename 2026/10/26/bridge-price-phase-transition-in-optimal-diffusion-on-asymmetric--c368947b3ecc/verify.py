"""Exact primal/dual checks and independent numerical spectral cross-checks.
Requires Python 3, numpy; does not download data.
"""
from fractions import Fraction as F
import numpy as np


def design(p, q, s, B=F(1)):
    assert isinstance(p,int) and isinstance(q,int) and p>=q>=1
    s=F(s); B=F(B); assert s>0 and B>0
    N=p+q+2
    sc=F(p-q,q+1)
    if s>=sc:
        mu=F(q+1,N)*(2+s)
        xs=[-mu,1-mu,1+s-mu,2+s-mu]
        C=p*xs[0]**2+xs[1]**2+xs[2]**2+q*xs[3]**2
        lam=B/C
        a=lam*mu; b=lam*(2+s-mu); c=lam*((p+1)*mu-1)/s
        x=[xs[0]]*p+[xs[1],xs[2]]+[xs[3]]*q
        gamma=F(0)
        branch='line'
    else:
        C=p+s*s+q*(s+1)**2
        lam=B/C; a=lam; b=lam*(s+1); c=lam*(q+1+F(q,1)/s)
        h=F(q+(q+1)*s,p)
        x=[-h]*p+[F(0),s]+[s+1]*q
        gamma=F(p,p-1)*(1-h*h)
        branch='split'
    return {'p':p,'q':q,'s':s,'B':B,'C':C,'gap':lam,'a':a,'b':b,'c':c,
            'x':x,'gamma':gamma,'branch':branch}


def check(p,q,s,B=F(1), spectral=True):
    t=design(p,q,s,B)
    n=p+q+2; lam=t['gap']; a=t['a']; b=t['b']; c=t['c']; x=t['x']; gamma=t['gamma']
    assert all(v>0 for v in (a,b,c))
    assert p*a+q*b+s*s*c==B
    assert sum(x)==0
    edges=[(i,p,a,F(1)) for i in range(p)]+[(p,p+1,c,s*s)]+[(p+1,p+2+j,b,F(1)) for j in range(q)]
    # Exact eigenvector identity for all vertices.
    Lx=[F(0) for _ in range(n)]
    for i,j,w,_ in edges:
        Lx[i]+=w*(x[i]-x[j]); Lx[j]+=w*(x[j]-x[i])
    assert Lx==[lam*y for y in x], (p,q,s,Lx,x)
    # A dual Gram Q = xx^T + gamma(I-J/p) on first p vertices.
    trace=sum(z*z for z in x)+gamma*(p-1)
    assert trace==t['C']
    for i,j,w,cost in edges:
        extra=gamma*F(p-1,p) if ((i<p) != (j<p)) else F(0)
        assert (x[i]-x[j])**2+extra==cost, (p,q,s,i,j)
    if gamma>0:
        assert a==lam
        # Every left-leaf contrast is a unit-gap eigenvector.
        for k in range(1,p):
            z=[F(0) for _ in range(n)]; z[0]=F(-1); z[k]=F(1)
            Lz=[F(0) for _ in range(n)]
            for i,j,w,_ in edges:
                Lz[i]+=w*(z[i]-z[j]); Lz[j]+=w*(z[j]-z[i])
            assert Lz==[lam*y for y in z]
    if spectral:
        mat=np.zeros((n,n),float)
        for i,j,w,_ in edges:
            ww=float(w)
            mat[i,i]+=ww;mat[j,j]+=ww;mat[i,j]-=ww;mat[j,i]-=ww
        e=np.linalg.eigvalsh(mat)
        assert abs(e[1]-float(lam))<=2e-9, (p,q,s,e[:6],lam)
        multiplicity=(p if gamma>0 or s==F(p-q,q+1) else 1)
        assert sum(abs(y-float(lam))<2e-9 for y in e)==multiplicity, (p,q,s,multiplicity,e)
    return t


def main():
    tests=0; spectral=0; count_line=count_split=0
    for p in range(1,14):
      for q in range(1,p+1):
        sc=F(p-q,q+1)
        svals={F(1,10),F(1,4),F(1,2),F(1),F(3,2),F(2),F(4)}
        if sc>0:svals.update({sc,F(9,10)*sc,F(11,10)*sc})
        for s in sorted(svals):
            t=check(p,q,s)
            tests+=1
            if t['branch']=='line':count_line+=1
            else:count_split+=1
    # Independent perturbations of every conductance: Rayleigh dual upper bound.
    rng=np.random.default_rng(21102026)
    comparisons=0
    for p,q,s in [(3,2,F(1,4)),(3,2,F(2)),(7,1,F(1,2)),(8,3,F(2)),(10,2,F(5))]:
        t=check(p,q,s)
        n=p+q+2
        edges=[(i,p,F(1)) for i in range(p)]+[(p,p+1,s*s)]+[(p+1,p+2+j,F(1)) for j in range(q)]
        cost=np.array([float(v) for _,_,v in edges])
        for _ in range(200):
            rr=rng.dirichlet(np.ones(len(edges)))
            w=rr/cost
            mat=np.zeros((n,n))
            for (i,j,_),v in zip(edges,w):
                mat[i,i]+=v;mat[j,j]+=v;mat[i,j]-=v;mat[j,i]-=v
            got=np.linalg.eigvalsh(mat)[1]
            assert got<=float(t['gap'])+1e-9
            comparisons+=1
    # Exact matching of the two branch costs and their first derivatives at crossover.
    import sympy as sp
    pp,qq,ss=sp.symbols('p q s')
    N=pp+qq+2
    mu=(qq+1)*(2+ss)/N
    Cline=pp*mu**2+(1-mu)**2+(1+ss-mu)**2+qq*(2+ss-mu)**2
    Csplit=pp+ss**2+qq*(ss+1)**2
    assert sp.simplify(Cline-Csplit+(pp-qq-(qq+1)*ss)**2/N)==0
    print('EXACT parameter and dual-certificate checks:',tests)
    print('line cases:',count_line,'split cases:',count_split)
    print('Independent asymmetric conductance comparisons:',comparisons)
    print('Exact Cline-Csplit square identity: PASS')
    print('All tests passed')

if __name__=='__main__':main()
