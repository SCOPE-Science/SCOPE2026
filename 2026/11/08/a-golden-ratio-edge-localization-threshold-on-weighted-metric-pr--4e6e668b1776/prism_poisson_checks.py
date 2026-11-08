"""Independent exact-rational Poisson-solver checks for weighted metric prisms.

Run: python prism_independent_check.py
"""
from fractions import Fraction
from sympy import Matrix, Rational, simplify, cos, pi

def laplacian_and_edges(n,h,kind=None,t=None):
    h=Rational(h)
    edges=[]
    for layer in range(2):
        for i in range(n):
            edges.append((layer*n+i,layer*n+((i+1)%n),Rational(1),'rim'))
    for i in range(n):
        edges.append((i,n+i,h,'rung'))
    node=2*n
    if kind is not None:
        j=next(i for i,e in enumerate(edges) if e[3]==kind)
        u,v,length,_=edges.pop(j)
        t=Rational(t)
        edges.extend([(u,node,length*t,'split'),(node,v,length*(1-t),'split')])
        N=2*n+1
    else:
        node=0;N=2*n
    return edges,node,N

def evaluate_direct(n,h,kind=None,t=None):
    edges,x,N=laplacian_and_edges(n,h,kind,t)
    L=sum((l for u,v,l,k in edges),Rational(0))
    lap=Matrix.zeros(N,N)
    weighted_lengths=[Rational(0)]*N
    for u,v,l,_ in edges:
        lap[u,u]+=1/l;lap[v,v]+=1/l
        lap[u,v]-=1/l;lap[v,u]-=1/l
        weighted_lengths[u]+=l;weighted_lengths[v]+=l
    rhs=Matrix([int(i==x)-weighted_lengths[i]/(2*L) for i in range(N)])
    assert sum(rhs)==0
    b=Matrix([Rational(0)] + list(lap[1:,1:].inv()*rhs[1:,:]))
    integrate=sum((l*(b[u]+b[v])/2 for u,v,l,k in edges),Rational(0))
    cubics=sum((l**3 for u,v,l,k in edges),Rational(0))
    offset=(cubics/(12*L)-integrate)/L
    return simplify(b[x]+offset)

def prediction(n,h,kind=None,t=None):
    h=Rational(h)
    H=sum((1/(1+h*(1-cos(2*pi*k/n))) for k in range(n)),Rational(0))/n
    v=(Rational(n*n-1,24*n)+h*H/4+(2+h**3)/(12*n*(2+h)**2))
    if kind is None:return simplify(v)
    c={'rim':H/2+h/(2*n*(2+h)), 'rung':h*(1-H)-h*h/(n*(2+h))}[kind]
    t=Rational(t)
    return simplify(v+t*(1-t)*c)

if __name__=='__main__':
    count=0
    for n in [3,4,5,6]:
        for h in [Rational(1,3),Rational(1),Rational(5,2)]:
            for kind,t in [(None,None),('rim',Rational(1,2)),('rung',Rational(1,2)),('rim',Rational(2,5)),('rung',Rational(3,7))]:
                actual=evaluate_direct(n,h,kind,t)
                expected=prediction(n,h,kind,t)
                assert simplify(actual-expected)==0,(n,h,kind,t,actual,expected)
                count+=1
    print('EXACT_REFINED_KIRCHHOFF_POISSON_CHECKS_PASSED',count)
