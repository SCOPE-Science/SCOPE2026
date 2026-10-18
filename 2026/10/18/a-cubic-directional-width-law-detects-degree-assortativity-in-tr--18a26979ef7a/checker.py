"""Independent finite graph checks and Gaussian-integral checks for a cubical zonotope width theorem."""
from collections import Counter
from itertools import combinations
from math import sqrt, pi, asin, gamma, erf, exp
from fractions import Fraction


def constants():
    base = 8 / pi**1.5
    return dict(
        matching=base,
        wedge=base*(sqrt(3)/2 + pi/12),
        path=base*(1/sqrt(2) + asin(1/sqrt(3)) - asin(1/3)/4),
        star=base*(1/sqrt(2) + 9*asin(1/3)/4),
        same=8/sqrt(pi), adjacent_pair=5/sqrt(pi), disjoint_pair=4/sqrt(pi)
    )


def types_of_three(edges):
    counts=Counter(v for e in edges for v in e)
    adj=sum(n*(n-1)//2 for n in counts.values())
    if adj==3: return 'star'
    if adj==2: return 'path'
    if adj==1: return 'wedge'
    if adj==0: return 'matching'
    raise AssertionError('three edges should be triangle-free')


def graph_motifs(n, edges):
    deg=[0]*n
    for a,b in edges: deg[a]+=1;deg[b]+=1
    m=len(edges)
    L=sum(d*(d-1)//2 for d in deg)
    S=sum(d*(d-1)*(d-2)//6 for d in deg)
    T=sum((deg[a]-1)*(deg[b]-1) for a,b in edges)
    N=Counter(types_of_three(es) for es in combinations(edges,3))
    assert N['star']==S and N['path']==T
    assert N['wedge']==(m-2)*L-3*S-2*T
    assert N['matching']==m*(m-1)*(m-2)//6-(m-2)*L+2*S+T
    return m,L,S,T,N


def predicted_moment(n,edges):
    m,L,S,T,N=graph_motifs(n,edges)
    c=constants()
    gaussian=(m*c['same']
       +6*(4*(m*(m-1)//2)+L)/sqrt(pi)
       +6*sum(N[t]*c[t] for t in ('star','path','wedge','matching')))
    radial=2**1.5*gamma((n+2)/2)/gamma((n-1)/2)
    return gaussian/radial


def h(x):
    return sqrt(2/pi)*exp(-x*x/2)+x*erf(x/sqrt(2))


def phi(x):
    return exp(-x*x/2)/sqrt(2*pi)


def simpson(f, steps=1200, bound=8.0):
    assert steps%2==0
    dx=2*bound/steps
    return dx/3*sum((1 if i==0 or i==steps else 4 if i%2 else 2)
        *f(-bound+i*dx) for i in range(steps+1))


def independent_integrals():
    c=constants()
    star=simpson(lambda x: phi(x)*h(x)**3)
    assert abs(star-c['star']) < 2e-8, (star,c['star'])
    N=960
    dx=16/N
    xs=[-8+i*dx for i in range(N+1)]
    fx=[phi(x)*h(x) for x in xs]
    w=[(1 if i==0 or i==N else 4 if i%2 else 2) for i in range(N+1)]
    path=(dx/3)**2*sum(w[i]*fx[i]*w[j]*fx[j]*abs(xs[i]-xs[j])
        for i in range(N+1) for j in range(N+1))
    assert abs(path-c['path'])<3e-5, (path,c['path'])
    beta=c['path']-2*c['wedge']+c['matching']
    assert -0.026<beta< -0.025
    return star,path,beta



def certified_negative_contrast():
    # Rational alternating bounds for arctan, coupled to Machin's identity.
    def atan_partial(x, last):
        return sum(((-1)**k * x**(2*k+1) / (2*k+1)
                    for k in range(last+1)), Fraction(0))
    one5=Fraction(1,5)
    one239=Fraction(1,239)
    # Six terms through k=5 are a lower bound, one term is upper.
    pi_lower=4*(4*atan_partial(one5,5)-one239)
    assert pi_lower>Fraction(314159,100000)
    sqrt3_lower=Fraction(173205,100000)
    inv_sqrt2_upper=Fraction(707107,1000000)
    half_inv_sqrt2_lower=Fraction(353553,1000000)
    assert sqrt3_lower**2<3
    assert 2*inv_sqrt2_upper**2>1
    assert 8*half_inv_sqrt2_lower**2<1
    a_up=atan_partial(inv_sqrt2_upper,20)
    b_lo=atan_partial(half_inv_sqrt2_lower,9)
    # Strict upper bound for the dimensionless constant in beta.
    contrast_upper=(1+inv_sqrt2_upper-sqrt3_lower-pi_lower/6
                    +a_up-b_lo/4)
    assert contrast_upper < Fraction(-18,1000)
    return float(contrast_upper)


def main():
    first=[(0,1),(1,2),(2,3),(0,4),(0,5)]
    second=[(0,1),(1,3),(0,2),(2,4),(0,5)]
    motifs=[graph_motifs(6,es) for es in (first,second)]
    assert sorted(motifs[0][-1].values()) != sorted(motifs[1][-1].values())
    assert motifs[0][:3]==motifs[1][:3]
    assert motifs[0][3]==3 and motifs[1][3]==4
    moments=[predicted_moment(6,es) for es in (first,second)]
    c=constants()
    radial=2**1.5*gamma(4)/gamma(2.5)
    assert abs((moments[1]-moments[0])-6*(c['path']-2*c['wedge']+c['matching'])/radial)<1e-12
    for m in range(3,10):
        path_edges=[(i,i+1) for i in range(m)]
        star_edges=[(0,i+1) for i in range(m)]
        graph_motifs(m+1,path_edges)
        graph_motifs(m+1,star_edges)
        assert predicted_moment(m+1,path_edges)>0
    star,path,beta=independent_integrals()
    upper=certified_negative_contrast()
    print('PASS: finite motif partition / independent Gaussian integrals / same-degree trees')
    print('two degree-equivalent trees P4 counts:',motifs[0][3],motifs[1][3])
    print('spherical cubic moments:',repr(moments))
    print('exact negative contrast coefficient (numerically):',repr(beta))
    print('independent integrals star/path:',repr(star),repr(path))
    print('rigorous rational upper bound for sign bracket:',repr(upper))


if __name__=='__main__':main()
