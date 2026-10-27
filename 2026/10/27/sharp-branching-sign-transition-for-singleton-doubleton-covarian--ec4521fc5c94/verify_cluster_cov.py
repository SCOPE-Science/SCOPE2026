"""Exact finite checks for singleton/doubleton cluster covariance; Python standard library only."""
from fractions import Fraction
from itertools import product


def prufer_edges(code):
    n=len(code)+2
    deg=[1]*n
    for v in code:deg[v]+=1
    edges=[]
    for v in code:
        u=next(i for i in range(n) if deg[i]==1)
        edges.append((u,v))
        deg[u]-=1;deg[v]-=1
    a,b=(i for i in range(n) if deg[i]==1)
    return n,edges+[(a,b)]


def cov_formula(n,edges,p):
    q=1-p
    nb=[set() for _ in range(n)]
    for u,v in edges:nb[u].add(v);nb[v].add(u)
    d=[len(x) for x in nb]
    total=Fraction(0)
    for u,v in edges:
        near=(nb[u]|nb[v])-{u,v}
        total+=p*q**(d[u]+d[v]-2)*(-q**d[u]-q**d[v]+(p/q)*sum((q**d[w] for w in near),Fraction(0)))
    return total


def cov_enumeration(n,edges,p):
    q=1-p
    a=b=c=Fraction(0)
    m=len(edges)
    for bits in product((0,1),repeat=m):
        prob=p**sum(bits)*q**(m-sum(bits))
        d=[0]*n
        for bit,(u,v) in zip(bits,edges):
            if bit:d[u]+=1;d[v]+=1
        I=d.count(0)
        J=sum(bit and d[u]==1 and d[v]==1 for bit,(u,v) in zip(bits,edges))
        a+=prob*I;b+=prob*J;c+=prob*I*J
    return c-a*b


def star(k):return k+1,[(0,i) for i in range(1,k+1)]

def spider(k):return 2*k+1,[(0,2*i+1) for i in range(k)]+[(2*i+1,2*i+2) for i in range(k)]

def star_closed(k,p):
    q=1-p
    return k*p*q**(k-1)*((k-1)-k*q-q**k)

def spider_closed(k,p):
    q=1-p
    return k*p*(-q**(2*k)-q**(k+2)+p*((k-1)*q**(k+1)+2*q**k)-q**3-q**2)


def main():
    tested=0
    # All labeled trees with at most six vertices; the finite computation is not the proof.
    for n in range(2,7):
        for code in product(range(n), repeat=n-2):
            order,edges=prufer_edges(code)
            for p in (Fraction(1,3),Fraction(1,2)):
                assert cov_formula(order,edges,p)==cov_enumeration(order,edges,p),(n,code,p)
                tested+=1
    print('ALL_LABELED_TREES_EXACT_PASS cases=',tested)
    for k in range(2,8):
        for p in (Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(9,10)):
            n,edges=star(k)
            assert star_closed(k,p)==cov_formula(n,edges,p)==cov_enumeration(n,edges,p)
            n,edges=spider(k)
            assert spider_closed(k,p)==cov_formula(n,edges,p)
            if k<=6:
                assert spider_closed(k,p)==cov_enumeration(n,edges,p)
    print('STAR_AND_SUBDIVIDED_STAR_EXACT_PASS k=2..7, exhaustive spider k<=6')
    for k in range(3,101):
        for p in (Fraction(j,30) for j in range(1,30)):
            assert spider_closed(k,p)<0
    assert spider_closed(2,Fraction(2,3))==0
    assert spider_closed(2,Fraction(1,2))<0
    assert spider_closed(2,Fraction(3,4))>0
    print('SIGN_CHECK_PASS k=3..100, path k=2 transition')
    print('VERIFY_OK')

if __name__=='__main__':main()
