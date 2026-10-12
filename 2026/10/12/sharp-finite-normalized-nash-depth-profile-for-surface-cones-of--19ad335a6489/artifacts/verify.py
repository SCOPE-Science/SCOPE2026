"""Exact finite classification of normalized Nash-blowup depth for surface cones.

For every primitive two-dimensional cone of determinant q <= 65, compute its
minimal (normalized) Nash blowup fan using the two-dimensional continued-
fraction/Hilbert-basis construction of Atanasov--Lopez--Perry--Proudfoot--
Thaddeus (arXiv:0910.5028, Proposition 4.11--4.14). Uses only Python stdlib.
"""
from functools import lru_cache
from math import gcd
from fractions import Fraction
from pathlib import Path
import csv

MAX_INDEX = 65

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def primitive(a):
    g = gcd(abs(a[0]), abs(a[1]))
    assert g >= 1
    return (a[0] // g, a[1] // g)

def bezout(a, b):
    """Return integers x,y with a*x+b*y = 1, for primitive (a,b)."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    r0, r1 = a, b
    while r1:
        k = r0 // r1
        r0, r1 = r1, r0 - k*r1
        x0, x1 = x1, x0 - k*x1
        y0, y1 = y1, y0 - k*y1
    assert abs(r0) == 1
    return (x0, y0) if r0 == 1 else (-x0, -y0)

@lru_cache(None)
def hilbert_basis(p, q):
    """All indecomposables in cone((1,0),(p,q)), in increasing slope.

    Any nonzero indecomposable either is a primitive extreme ray or lies in
    the half-open fundamental parallelogram: subtracting either primitive
    ray otherwise would split it. Thus x <= p+1 and y <= q. The bounding
    rectangle below is slightly enlarged; scanning by y and then x ensures
    every proper additive summand was processed earlier.
    """
    assert q >= 1 and 0 <= p < q and gcd(p,q) == 1
    if q == 1:
        return ((1,0),(0,1))
    pool = [(x,y) for y in range(q+1) for x in range(p+q+1)
            if (x,y) != (0,0) and q*x >= p*y]
    pool_set = set(pool)
    irreducibles = []
    for x,y in pool:
        if not any((x-a,y-b) in pool_set for a,b in irreducibles):
            irreducibles.append((x,y))
    # Fractions, never floating-point slopes.
    irreducibles.sort(key=lambda v:(Fraction(v[1],v[0]) if v[0] else Fraction(q+1,1),v[0]+v[1]))
    assert irreducibles[0] == (1,0)
    assert irreducibles[-1] == (p,q)
    assert all(cross(a,b) == 1 for a,b in zip(irreducibles,irreducibles[1:]))
    return tuple(irreducibles)

def normalize(a, b):
    """Put two primitive CCW rays in standard cyclic-cone normal form."""
    a,b=primitive(a),primitive(b)
    if cross(a,b)<0: a,b=b,a
    q=cross(a,b)
    assert q>=1
    if q==1: return (0,1)
    u,v=bezout(*a)
    p=(u*b[0]+v*b[1]) % q
    assert gcd(p,q)==1 and 0<p<q
    return (p,q)

@lru_cache(None)
def children(p,q):
    """Every maximal cone in the normalized Nash subdivision.

    In dimension 2 only consecutive Hilbert-basis sums are relevant
    (arXiv:0910.5028, Props. 4.11--4.12). Discard collinear intermediate
    sums, take primitive tangent rays of the resulting unbounded polygon,
    and transport to standard form by unimodular arithmetic.
    """
    if q==1:return ()
    h=hilbert_basis(p,q)
    sums=[(h[i][0]+h[i+1][0],h[i][1]+h[i+1][1]) for i in range(len(h)-1)]
    if len(sums)==1:
        return ((0,1),)
    retained=[]
    for i in range(len(sums)):
        if i in (0,len(sums)-1):retained.append(i)
        else:
            left=(sums[i][0]-sums[i-1][0],sums[i][1]-sums[i-1][1])
            right=(sums[i+1][0]-sums[i][0],sums[i+1][1]-sums[i][1])
            if cross(left,right)!=0:retained.append(i)
    result=[]
    for k,i in enumerate(retained):
        if k==0: a=h[0]
        else:
            j=retained[k-1]
            a=(sums[j][0]-sums[i][0], sums[j][1]-sums[i][1])
        if k==len(retained)-1: b=h[-1]
        else:
            j=retained[k+1]
            b=(sums[j][0]-sums[i][0], sums[j][1]-sums[i][1])
        result.append(normalize(a,b))
    return tuple(result)

@lru_cache(None)
def depth(p,q):
    """Number of rounds until *all* affine charts are smooth."""
    if q==1:return 0
    ch=children(p,q)
    assert ch
    # The surface termination theorem proves recursion is finite.
    # Detect a repeated state rather than assuming finite exploration.
    for s in ch:
        assert s!=(p,q), ('unchanged singular child',p,q,ch)
    return 1+max(depth(*c) for c in ch)

def main():
    # All primitive determinant-q cones appear as cone((1,0),(p,q)) with
    # 1 <= p < q, gcd(p,q)=1. Redundancies under swapping the rays are OK.
    rows=[]
    counts={}
    for q in range(2,MAX_INDEX+1):
        row=[]
        for p in range(1,q):
            if gcd(p,q)!=1:continue
            d=depth(p,q)
            rows.append((q,p,d))
            row.append((p,d))
        expected=(q-1).bit_length()  # ceil(log2(q)) without floating point
        assert max(d for p,d in row)==expected,(q,row)
        assert [p for p,d in row if d==expected]==[q-1],(q,row)
        counts[q]=len(row)
    assert len(rows)==1307
    assert depth(64,65)==7
    assert depth(63,65)==6
    assert all(d<=6 for q,p,d in rows if q<=64)
    expected_onsets=((1,2),(2,3),(3,5),(4,9),(5,17),(6,33),(7,65))
    for d,q in expected_onsets:
        assert depth(q-1,q)==d
    # Explicit deepest branch is an independent readily auditable witness.
    p,q=64,65
    witness=[(p,q)]
    while q>1:
        p,q=max(children(p,q),key=lambda child:depth(*child))
        witness.append((p,q))
    assert witness==[(64,65),(63,65),(31,33),(15,17),
                    (7,9),(3,5),(1,3),(0,1)]
    # Compare the complete certificate table with exact regenerated values.
    import sys, io
    buf=io.StringIO(newline="")
    w=csv.writer(buf,lineterminator="\n")
    w.writerow(("index","parameter","depth"))
    w.writerows(rows)
    generated=buf.getvalue()
    if len(sys.argv)>1:
        out=Path(sys.argv[1])
        if out.exists():
            assert out.read_text(encoding="utf-8") == generated, "certificate table mismatch"
        else:
            out.parent.mkdir(parents=True,exist_ok=True)
            out.write_text(generated,encoding="utf-8")
    print('VERIFIED',len(rows),'primitive representatives; first depth-seven index 65; unique p=64')
    print('ONSET',expected_onsets)
    print('WITNESS',witness)

if __name__=='__main__':main()
