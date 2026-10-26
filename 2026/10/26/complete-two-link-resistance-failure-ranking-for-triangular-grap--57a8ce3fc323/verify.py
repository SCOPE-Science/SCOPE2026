"""Independent exact checks for two edge failures of triangular graphs J(n,2).
Run: python verify_triangular_new.py; requires sympy >=1.11.
This finite checker supplements the general spectral proof; it does not prove it.
"""
import itertools
import sympy as sp
from collections import Counter

z=sp.symbols('z', integer=True, positive=True)
N=z*(z-1)/2
R=(z+1)/(z*(z-1))
S=(z*z+3*z-2)/(2*z*z*(z-1)**2)

def formula(k,h):
    c=(z*k+h)/(2*z*(z-1))
    t=(z*z*k+(3*z-2)*h)/(4*z*z*(z-1)**2)
    return sp.factor(2*N*((1-R)*S+c*t)/((1-R)**2-c*c))

KINDS=((1,1),(1,0),(0,2),(0,1),(0,0))
D={kind:formula(*kind) for kind in KINDS}
assert sp.simplify(D[(1,1)]- (z*z+3*z-2)*(4*z*z-7*z-3)/(2*(z-3)*(2*z+1)*(2*z*z-3*z-1)))==0
assert sp.simplify(D[(0,0)]- (z*z+3*z-2)/(2*(z*z-2*z-1)))==0
for kind1,kind2 in zip(KINDS,KINDS[1:]):
    diff=sp.factor(D[kind1]-D[kind2])
    num,den=sp.fraction(diff)
    assert all(c>=0 for c in sp.Poly(sp.expand(num.subs(z,z+5)),z).all_coeffs())
    assert all(c>=0 for c in sp.Poly(sp.expand(den.subs(z,z+5)),z).all_coeffs())

def graph(n):
    vv=list(itertools.combinations(range(n),2));edge=[]
    for i in range(len(vv)):
        for j in range(i+1,len(vv)):
            if len(set(vv[i])&set(vv[j]))==1:edge.append((i,j))
    return vv,edge

def shape(vv,e,f):
    def mover(pair):
        A,B=map(lambda ix:set(vv[ix]),pair)
        return list(A-B)[0],list(B-A)[0]
    b,c=mover(e); d,g=mover(f)
    k=int(e[0]==f[0])-int(e[0]==f[1])-int(e[1]==f[0])+int(e[1]==f[1])
    h=int(b==d)-int(b==g)-int(c==d)+int(c==g)
    if k<0 or (k==0 and h<0):k,h=-k,-h
    return k,h

def counts_expected(n):
    return {(1,1):n*(n-1)*(n-2)**2//2,
            (1,0):n*(n-1)*(n-2)*(n-3)//2,
            (0,2):n*(n-1)*(n-2)*(n-3)//4,
            (0,1):n*(n-1)*(n-2)**2*(n-3)//2,
            (0,0):n*n*(n-1)*(n-2)*(n-3)*(n-4)//8}

def kirchhoff(vv,edges):
    M=len(vv);L=sp.zeros(M)
    for u,v in edges:
        L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
    T=L[:M-1,:M-1]
    X=T.inv()
    return sp.expand(M*sp.trace(X)-sum(X))

n_shapes=0
for n in range(5,10):
    vv,edges=graph(n);counter=Counter(); reps={}
    for e,f in itertools.combinations(edges,2):
        kind=shape(vv,e,f);counter[kind]+=1;reps.setdefault(kind,(e,f))
    assert dict(counter)==counts_expected(n),(n,counter,counts_expected(n))
    assert set(counter)==set(KINDS)
    n_shapes+=len(counter)
    if n<=7:
        baseline=kirchhoff(vv,edges)
        for kind,(e,f) in reps.items():
            actual=sp.factor(kirchhoff(vv,[x for x in edges if x!=e and x!=f])-baseline)
            assert actual==D[kind].subs(z,n),(n,kind,actual,D[kind].subs(z,n))
        print('matrix_n',n,'classes',len(reps),'pairs',sum(counter.values()))
    else:
        print('orbit_n',n,'classes',len(reps),'pairs',sum(counter.values()))
print('VERIFY_OK symbolic_differences=4 orbit_classifications=',n_shapes,' exact_matrix_comparisons=15')
