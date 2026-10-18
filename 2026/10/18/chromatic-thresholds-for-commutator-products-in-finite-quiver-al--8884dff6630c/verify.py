"""Finite checks for exact commutator image and graph-coloring thresholds."""
from itertools import product, combinations
from collections import defaultdict


def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def neg(a,q):
    return a if q==4 else (-a)%q

def mul(a,b,q):
    if q!=4: return (a*b)%q
    p=0
    while b:
        if b&1: p^=a
        b>>=1; a<<=1
        if a&4: a^=7
    return p

def inv(a,q):
    assert a
    for b in range(1,q):
        if mul(a,b,q)==1: return b
    raise AssertionError

def unit_set(n,arcs,q):
    for diag in product(range(1,q),repeat=n):
        for rad in product(range(q),repeat=len(arcs)):
            yield diag,rad

def product_unit(x,y,arcs,q):
    d,a=x;e,b=y
    return (tuple(mul(t,s,q) for t,s in zip(d,e)),
            tuple(add(mul(d[i],b[h],q),mul(a[h],e[j],q),q)
                  for h,(i,j) in enumerate(arcs)))

def inverse_unit(x,arcs,q):
    d,a=x
    di=tuple(inv(z,q) for z in d)
    v=tuple(neg(mul(mul(di[i],a[h],q),di[j],q),q) for h,(i,j) in enumerate(arcs))
    return (di,v)

def commutator(x,y,arcs,q):
    return product_unit(product_unit(product_unit(x,y,arcs,q),
                              inverse_unit(x,arcs,q),arcs,q),
                        inverse_unit(y,arcs,q),arcs,q)

def colorable(n,edges,r):
    for cols in product(range(r),repeat=n):
        if all(cols[a]!=cols[b] for a,b in edges):
            return True
    return False

def run_small(n,arcs,q):
    xs=list(unit_set(n,arcs,q))
    actual=set()
    for x in xs:
        for y in xs:
            diag,rad=commutator(x,y,arcs,q)
            assert all(t==1 for t in diag)
            actual.add(rad)
    predicted=set()
    for r in product(range(q),repeat=len(arcs)):
        if q==2:
            allowed=not any(r)
        else:
            support={(min(i,j),max(i,j)) for z,(i,j) in zip(r,arcs) if z!=0 and i!=j}
            allowed=not any(z!=0 and i==j for z,(i,j) in zip(r,arcs)) and colorable(n,support,(q-1)**2)
        if allowed: predicted.add(r)
    assert actual==predicted,(n,arcs,q,sorted(predicted-actual),sorted(actual-predicted))
    print('DIRECT_UNIT_MULTIPLICATION_OK',n,len(arcs),q,len(xs),len(actual))

# Note: the checker uses actual truncated-path-algebra multiplication,
# not the semidirect-product commutator formula of the proof.
for spec in [
    (2,[(0,1)],2),
    (2,[(0,1)],3),
    (2,[(0,1),(0,0)],3),
    (3,[(0,1),(1,2)],3),
    (3,[(0,1),(1,2),(2,0)],3),
    (2,[(0,1)],4),
    (2,[(0,1),(1,0)],4),
]:
    run_small(*spec)

# Complete graph K5 over F3 has chromatic number 5, so no single
# commutator can have all ten radical coordinates nonzero.
n=5;arcs=list(combinations(range(n),2));q=3
for t in product((1,2),repeat=n):
    for s in product((1,2),repeat=n):
        separated={(i,j) for (i,j) in arcs if (t[i],s[i])!=(t[j],s[j])}
        assert len(separated)<len(arcs)
print('K5_ONE_COMMUTATOR_FULL_SUPPORT_EXCLUDED')

# Four independent F3^* labels yield 16 combined colors, allowing
# a K5 coloring. Construct two commutators, each directly via algebra
# multiplication, whose product has every radical coordinate = 1.
labels=[(1,1,1,1),(1,1,1,2),(1,1,2,1),(1,2,1,1),(2,1,1,1)]
t1=tuple(v[0] for v in labels);s1=tuple(v[1] for v in labels)
t2=tuple(v[2] for v in labels);s2=tuple(v[3] for v in labels)
zero=(0,)*len(arcs); a=[0]*len(arcs);b=[0]*len(arcs);c=[0]*len(arcs);d=[0]*len(arcs)
for h,(i,j) in enumerate(arcs):
    # commutator formula is (1-s) a + (t-1) b, where
    # all multiplication is F3 arithmetic.
    if s1[i]!=s1[j]:
        coeff=1-mul(s1[i],inv(s1[j],3),3)
        a[h]=inv(coeff%3,3)
    elif t1[i]!=t1[j]:
        coeff=mul(t1[i],inv(t1[j],3),3)-1
        b[h]=inv(coeff%3,3)
    elif s2[i]!=s2[j]:
        coeff=1-mul(s2[i],inv(s2[j],3),3)
        c[h]=inv(coeff%3,3)
    else:
        assert t2[i]!=t2[j]
        coeff=mul(t2[i],inv(t2[j],3),3)-1
        d[h]=inv(coeff%3,3)
# In the (1+x)t coordinates used by product_unit, the effective
# commutator coefficients differ by endpoint diagonal factors.
# Instead independently brute-force the two single-commutator radical
# coordinate images with those diagonals and solve each edge.
def coeffs_for(t,s,e):
    # Evaluate the full algebra commutator on basis-vector radical components
    # without invoking the closed commutator formula.
    h=arcs.index(e);A=[0]*len(arcs);B=[0]*len(arcs)
    A[h]=1
    outa=commutator((t,tuple(A)),(s,zero),arcs,3)[1][h]
    B[h]=1
    outb=commutator((t,zero),(s,tuple(B)),arcs,3)[1][h]
    return outa,outb
A=[0]*len(arcs);B=[0]*len(arcs);C=[0]*len(arcs);D=[0]*len(arcs)
for h,e in enumerate(arcs):
    c1,c2=coeffs_for(t1,s1,e)
    c3,c4=coeffs_for(t2,s2,e)
    coeffs=[c1,c2,c3,c4]
    ix=next(i for i,x in enumerate(coeffs) if x)
    [A,B,C,D][ix][h]=inv(coeffs[ix],3)
rad1=commutator((t1,tuple(A)),(s1,tuple(B)),arcs,3)
rad2=commutator((t2,tuple(C)),(s2,tuple(D)),arcs,3)
res=product_unit(rad1,rad2,arcs,3)
assert res[0]==(1,)*n and res[1]==(1,)*len(arcs)
print('K5_TWO_COMMUTATORS_EXPLICIT_WITNESS_OK',len(arcs))
print('ALL_EXACT_COMMUTATOR_CHECKS_PASSED')
