#!/usr/bin/env python3
from itertools import product, combinations

class Field:
    """Exact arithmetic for the finite fields whose orders are below 11, and for F_11."""
    def __init__(self, q):
        self.q = q
        if q in (2,3,5,7,11):
            self.kind = "prime"
        elif q in (4,8):
            self.kind = "binary_extension"
        elif q == 9:
            self.kind = "ternary_quadratic"
        else:
            raise ValueError(q)

    def add(self, a, b):
        if self.kind == "prime":
            return (a+b) % self.q
        if self.kind == "binary_extension":
            return a ^ b
        a0,a1 = a % 3, a // 3
        b0,b1 = b % 3, b // 3
        return ((a0+b0) % 3) + 3*((a1+b1) % 3)

    def neg(self, a):
        if self.kind == "prime":
            return (-a) % self.q
        if self.kind == "binary_extension":
            return a
        a0,a1 = a % 3, a // 3
        return ((-a0) % 3) + 3*((-a1) % 3)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.kind == "prime":
            return (a*b) % self.q
        if self.kind == "binary_extension":
            # F_4 = F_2[x]/(x^2+x+1), F_8 = F_2[x]/(x^3+x+1).
            modulus = {4:0b111, 8:0b1011}[self.q]
            degree = {4:2, 8:3}[self.q]
            out = 0
            aa, bb = a, b
            while bb:
                if bb & 1:
                    out ^= aa
                bb >>= 1
                aa <<= 1
                if aa & (1 << degree):
                    aa ^= modulus
            return out
        # F_9 = F_3[u]/(u^2+1), encoded as a0+3*a1, so u^2=2.
        a0,a1 = a % 3, a // 3
        b0,b1 = b % 3, b // 3
        return ((a0*b0 + 2*a1*b1) % 3) + 3*((a0*b1+a1*b0) % 3)

    def inv(self, a):
        assert a != 0
        for b in range(1,self.q):
            if self.mul(a,b) == 1:
                return b
        raise AssertionError("nonzero element without inverse")

    def div(self, a, b):
        return self.mul(a,self.inv(b))


def verify_field(F):
    q=F.q
    for a in range(q):
        assert F.add(a,0)==a and F.mul(a,1)==a and F.mul(a,0)==0
        assert F.add(a,F.neg(a))==0
        if a:
            assert F.mul(a,F.inv(a))==1
    for a,b,c in product(range(q), repeat=3):
        assert F.add(F.add(a,b),c)==F.add(a,F.add(b,c))
        assert F.mul(F.mul(a,b),c)==F.mul(a,F.mul(b,c))
        assert F.add(a,b)==F.add(b,a)
        assert F.mul(a,b)==F.mul(b,a)
        assert F.mul(a,F.add(b,c))==F.add(F.mul(a,b),F.mul(a,c))


def det3(F,a,b,c):
    t1=F.mul(a[0],F.sub(F.mul(b[1],c[2]),F.mul(b[2],c[1])))
    t2=F.mul(a[1],F.sub(F.mul(b[0],c[2]),F.mul(b[2],c[0])))
    t3=F.mul(a[2],F.sub(F.mul(b[0],c[1]),F.mul(b[1],c[0])))
    return F.add(F.sub(t1,t2),t3)


def cross(F,a,b):
    return (
        F.sub(F.mul(a[1],b[2]),F.mul(a[2],b[1])),
        F.sub(F.mul(a[2],b[0]),F.mul(a[0],b[2])),
        F.sub(F.mul(a[0],b[1]),F.mul(a[1],b[0])),
    )


def normalize(F,v):
    for x in v:
        if x:
            z=F.inv(x)
            return tuple(F.mul(z,y) for y in v)
    raise AssertionError("zero vector is not projective")


def projective_points(F):
    P={normalize(F,v) for v in product(range(F.q),repeat=3) if v!=(0,0,0)}
    assert len(P)==F.q*F.q+F.q+1
    return sorted(P)


def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield ()
        return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        rest=items[1:j]+items[j+1:]
        for tail in perfect_matchings(rest):
            yield ((a,b),)+tail

MATCHINGS=list(perfect_matchings(range(6)))
assert len(MATCHINGS)==15 and len(set(MATCHINGS))==15


def mds3_geometry(F,pts):
    assert len(pts)==6 and len(set(pts))==6
    # Ordinary MDS condition in PG(2,F): no three points collinear.
    for i,j,k in combinations(range(6),3):
        if det3(F,pts[i],pts[j],pts[k])==0:
            return False
    # Extra order-3 condition: for each perfect matching, its three joining lines are not concurrent.
    for matching in MATCHINGS:
        lines=[cross(F,pts[i],pts[j]) for i,j in matching]
        if det3(F,lines[0],lines[1],lines[2])==0:
            return False
    return True


def normalized_candidates(F):
    frame=((1,0,0),(0,1,0),(0,0,1),(1,1,1))
    P=projective_points(F)
    cand=[]
    for p in P:
        if p in frame:
            continue
        if all(det3(F,p,a,b)!=0 for a,b in combinations(frame,2)):
            cand.append(p)
    return frame,P,cand

expected_candidates={2:0,3:0,4:2,5:6,7:20,8:30,9:42,11:72}
expected_pairs={2:0,3:0,4:1,5:15,7:190,8:435,9:861,11:2556}
excluded_total=0
for q in (2,3,4,5,7,8,9,11):
    F=Field(q)
    verify_field(F)
    frame,P,cand=normalized_candidates(F)
    assert len(cand)==expected_candidates[q]
    pairs=list(combinations(cand,2))
    assert len(pairs)==expected_pairs[q]
    good=[]
    for x,y in pairs:
        if mds3_geometry(F,frame+(x,y)):
            good.append((x,y))
    if q<11:
        assert good==[]
        excluded_total += len(pairs)
    else:
        assert len(good)==72
        witness=((1,2,3),(1,7,4))
        assert witness in good
        assert mds3_geometry(F,frame+witness)

assert excluded_total==1502
print("VERIFY_OK fields=2,3,4,5,7,8,9 excluded_pairs=1502 q11_candidates=72 q11_good_pairs=72 witness=(1,2,3),(1,7,4)")
