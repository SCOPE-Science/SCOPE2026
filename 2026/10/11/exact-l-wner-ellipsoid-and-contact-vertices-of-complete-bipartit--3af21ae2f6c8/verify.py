"""Exact rational verification of bipartite graphical-zonotope enclosing ellipsoids.
Run: python3 verify.py. Only Python standard library is used.
"""
from fractions import Fraction as F
from itertools import product, combinations


def signs_near_balanced(k):
    h = k & 1
    return [s for s in product((-1, 1), repeat=k) if sum(s)**2 == h]


def endpoint(p, q, signs):
    x = [F(0) for _ in range(p+q)]
    for i in range(p):
        for j in range(q):
            z = F(signs[i*q+j],2)
            x[i] += z
            x[p+j] -= z
    assert sum(x) == 0
    return tuple(x)


def shape_entry(p, q, i, j):
    c=F(p*q,4)
    if i==j:
        return c*(q if i<p else p)
    return -c if ((i<p)!=(j<p)) else F(0)


def gauge(p,q,x):
    am=sum(x[:p])/p
    bm=sum(x[p:])/q
    assert p*am+q*bm == 0
    ua=sum((t-am)**2 for t in x[:p]); ub=sum((t-bm)**2 for t in x[p:])
    w=p*am*am+q*bm*bm
    return ua/F(p*q*q,4)+ub/F(p*p*q,4)+w/F(p*q*(p+q),4)


def contact_sign(p,q,s):
    rows_all_identical=all(s[i*q+j] == s[j] for i in range(p) for j in range(q))
    columns_all_identical=all(s[i*q+j] == s[i*q] for i in range(p) for j in range(q))
    return rows_all_identical or columns_all_identical


def weights(p,q):
    d=p+q-1; hp=p%2; hq=q%2
    alpha=F(p*p*(p-1),d*(p*p-hp))
    beta=F(q*q*(q-1),d*(q*q-hq))
    gamma=F(1,d)*(1-F((p-1)*hp,p*p-hp)-F((q-1)*hq,q*q-hq))
    assert alpha+beta+gamma==1 and min(alpha,beta,gamma)>0
    return alpha,beta,gamma


def covariance(p,q):
    aa=signs_near_balanced(p); bb=signs_near_balanced(q)
    alpha,beta,gamma=weights(p,q)
    family=[]
    for a in aa: family.append((endpoint(p,q,tuple(a[i] for i in range(p) for j in range(q))),alpha/len(aa)))
    for b in bb: family.append((endpoint(p,q,tuple(b[j] for i in range(p) for j in range(q))),beta/len(bb)))
    for t in (-1,1): family.append((endpoint(p,q,(t,)*(p*q)),gamma/2))
    n=p+q; d=n-1
    assert sum(w for _,w in family)==1
    assert all(sum(w*x[k] for x,w in family)==0 for k in range(n))
    for i in range(n):
        for j in range(n):
            got=sum(w*x[i]*x[j] for x,w in family)
            want=shape_entry(p,q,i,j)/d
            assert got == want, ('covariance mismatch',p,q,i,j,got,want)
            if __debug__ and i==0 and j==0: pass
    assert all(gauge(p,q,x)==1 for x,w in family)


def exhaustive(p,q):
    matched=set()
    for s in product((-1,1),repeat=p*q):
        x=endpoint(p,q,s)
        g=gauge(p,q,x)
        assert 0<=g<=1,('containment',p,q,s,g)
        assert (g==1)==contact_sign(p,q,s),('contact',p,q,s,g)
        if g==1: matched.add(x)
    assert len(matched)==2**p+2**q-2,(p,q,len(matched))


def main():
    c=0
    for p in range(2,10):
        for q in range(2,10):
            covariance(p,q); c+=1
    e=0
    for p,q in [(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(3,3),(3,4),(3,5),(4,4)]:
        exhaustive(p,q); e+=1
    print('PASS:',c,'exact all-coordinate covariance checks; ',e,'exhaustive sign-cube contact/containment checks')

if __name__ == '__main__':
    main()
