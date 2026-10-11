#!/usr/bin/env python3
"""Exact pair-fiber and numerical fourth-moment checks for finite-field hyperbola extension.

Prime fields and selected quadratic extension fields; the all-field theorem is analytic.
"""
import cmath
import math
import random
from collections import defaultdict


class Field:
    def __init__(self, p, nonsquare=None):
        self.p = p
        self.c = nonsquare
        self.q = p * (p if nonsquare is not None else 1)

    def parts(self, v):
        return (v % self.p, v // self.p)

    def elt(self, a, b=0):
        return (a % self.p) + (b % self.p) * self.p

    def add(self, x, y):
        a, b = self.parts(x)
        c, d = self.parts(y)
        return self.elt(a + c, b + d)

    def neg(self, x):
        a, b = self.parts(x)
        return self.elt(-a, -b)

    def mul(self, x, y):
        a, b = self.parts(x)
        c, d = self.parts(y)
        if self.c is None:
            return self.elt(a*c)
        return self.elt(a*c + self.c*b*d, a*d + b*c)

    def inv(self, x):
        if x == 0:
            raise ZeroDivisionError
        a, b = self.parts(x)
        if self.c is None:
            return self.elt(pow(a, self.p-2, self.p))
        delta = (a*a-self.c*b*b) % self.p
        recip = pow(delta, self.p-2, self.p)
        return self.elt(a*recip, -b*recip)

    def char(self, x):
        a, b = self.parts(x)
        trace = a if self.c is None else 2*a
        return cmath.exp(2j*math.pi*(trace % self.p)/self.p)


def convolution(f, F):
    z = defaultdict(complex)
    nonzero = list(range(1, F.q))
    for a in nonzero:
        for b in nonzero:
            key = (F.add(a, b), F.add(F.inv(a), F.inv(b)))
            z[key] += f[a]*f[b]
    return sum(abs(v)**2 for v in z.values())


def formula(f, F):
    singles = list(range(1, F.q))
    U = sum(abs(f[a])**2 for a in singles)
    seen = set()
    pairs = []
    for a in singles:
        if a in seen:
            continue
        b = F.neg(a)
        seen.add(a)
        seen.add(b)
        pairs.append((a, b))
    s, d, z = [], [], []
    for a, b in pairs:
        u, v = abs(f[a])**2, abs(f[b])**2
        s.append(u+v)
        d.append(u-v)
        z.append(2*f[a]*f[b])
    k = len(pairs)
    energy = 2*U*U - 1.5*sum(x*x for x in s) + 0.5*sum(x*x for x in d) + abs(sum(z))**2
    deficit = 1.5*sum((x-U/k)**2 for x in s)
    deficit += sum((U/x-0.5)*y*y for x, y in zip(s, d) if x > 0)
    for i in range(k):
        for j in range(i+1, k):
            if s[i] and s[j]:
                deficit += s[i]*s[j]*abs(z[i]/s[i]-z[j]/s[j])**2
    C = 3-3/(F.q-1)
    return energy, deficit, C*U*U-deficit


def direct_fourier(f, F):
    total = 0.0
    for u in range(F.q):
        for v in range(F.q):
            value = sum(f[a]*F.char(F.add(F.mul(u, a), F.mul(v, F.inv(a))))
                        for a in range(1,F.q))
            total += abs(value)**4
    return total/(F.q**2)




def check_binary_conics(F):
    """Independent enumeration for split and nonsplit nonzero binary conics."""
    from collections import Counter
    squares = {F.mul(a,a) for a in range(1,F.q)}
    nonsquare = next(a for a in range(1,F.q) if a not in squares)
    rng = random.Random(1000+F.q)
    count = 0
    for kind in ("split", "nonsplit"):
        def quad(x, y):
            if kind == "split":
                return F.mul(x,y)
            return F.add(F.mul(x,x), F.neg(F.mul(nonsquare,F.mul(y,y))))
        S = [(x,y) for x in range(F.q) for y in range(F.q) if quad(x,y)==1]
        M = len(S)
        assert M == F.q-1 if kind == "split" else M == F.q+1, (F.q,kind,M)
        idx = {t:i for i,t in enumerate(S)}
        neg = lambda z:(F.neg(z[0]),F.neg(z[1]))
        pairs=[]
        paired=set()
        for v in S:
            if v in paired:continue
            w=neg(v)
            assert w in idx and w!=v
            paired.add(v);paired.add(w)
            pairs.append((v,w))
        assert len(pairs)==M//2
        fibers=Counter((F.add(a[0],b[0]),F.add(a[1],b[1])) for a in S for b in S)
        assert fibers[(0,0)]==M
        assert all(val in (1,2) for key,val in fibers.items() if key!=(0,0))
        for itr in range(6):
            f={v:complex(rng.uniform(-1,1),rng.uniform(-1,1)) for v in S}
            if itr == 0:
                for v in S:f[v]=1+0j
            if itr == 1:
                for v in S:f[v]=0j if v!=S[0] else 1+0j
            energy=sum(abs(sum(f[a]*f[b]
                for a in S for b in S if (F.add(a[0],b[0]),F.add(a[1],b[1]))==key))**2
                for key in fibers)
            U=sum(abs(f[v])**2 for v in S)
            sq=[];diff=[];zz=[]
            for v,w in pairs:
                av,bv=abs(f[v])**2,abs(f[w])**2
                sq.append(av+bv);diff.append(av-bv);zz.append(2*f[v]*f[w])
            predicted=2*U*U-1.5*sum(x*x for x in sq)+0.5*sum(y*y for y in diff)+abs(sum(zz))**2
            deficit=1.5*sum((x-2*U/M)**2 for x in sq)
            deficit+=sum((U/x-0.5)*y*y for x,y in zip(sq,diff) if x)
            for i in range(M//2):
                for j in range(i+1,M//2):
                    if sq[i] and sq[j]:
                        deficit+=sq[i]*sq[j]*abs(zz[i]/sq[i]-zz[j]/sq[j])**2
            sharp=3-3/M
            assert abs(energy-predicted)<1e-9*max(1,energy),(F.q,kind)
            assert abs(sharp*U*U-energy-deficit)<1e-9*max(1,energy),(F.q,kind)
            assert deficit>=-1e-9
            if itr==0 and F.q<=9:
                direct=sum(abs(sum(f[(x,y)]*F.char(F.add(F.mul(a,x),F.mul(b,y)))
                    for x,y in S))**4 for a in range(F.q) for b in range(F.q))/F.q**2
                assert abs(direct-energy)<1e-9*max(1,energy)
            count+=1
    return count

def run():
    choices = [Field(p) for p in (3, 5, 7, 11, 13)] + [Field(3, 2), Field(5, 2)]
    rand = random.Random(548287)
    tests = 0
    fourier = 0
    fibers = 0
    for F in choices:
        assert F.q % 2 == 1
        for a in range(1,F.q):
            assert F.mul(a,F.inv(a)) == 1
        seen = defaultdict(int)
        for a in range(1,F.q):
            for b in range(1,F.q):
                seen[(F.add(a,b),F.add(F.inv(a),F.inv(b)))] += 1
        assert seen[(0,0)] == F.q-1
        for key,mult in seen.items():
            if key != (0,0):
                assert mult in (1,2)
        fibers += 1
        for iteration in range(9):
            f = {a: complex(rand.uniform(-1,1), rand.uniform(-1,1))
                 for a in range(1,F.q)}
            if iteration == 0:
                f = {a: 1+0j for a in f}
            if iteration == 1:
                f = {a: 1 if a % 2 else -1 for a in f}
            if iteration == 2:
                f = {a: (1+0j if a == 1 else 0j) for a in f}
            E = convolution(f, F)
            analytic, deficit, recomposed = formula(f, F)
            tol = 3e-10*max(1,abs(E))
            assert abs(E-analytic) < tol, (F.q, E, analytic)
            assert abs(E-recomposed) < tol, (F.q,E,recomposed)
            assert deficit > -tol, (F.q, deficit)
            tests += 1
            if F.q <= 9 and iteration in (0, 3, 6):
                brute = direct_fourier(f,F)
                assert abs(E-brute) < 1e-9*max(1,E), (F.q,E,brute)
                fourier += 1
        # Equality family: choose independently the phase of each opposite pair,
        # and choose inverse phases within each pair so that products agree.
        f = {}
        paired = set()
        for a in range(1,F.q):
            if a in paired:
                continue
            b = F.neg(a)
            paired.update((a,b))
            phase = rand.random()*2*math.pi
            f[a] = cmath.exp(1j*phase)
            f[b] = cmath.exp(1j*(0.3-phase))
        E = convolution(f,F)
        U = F.q-1
        assert abs(E-(3-3/U)*U*U)<1e-9*max(1,E), (F.q,E)
        tests += 1
    conics = sum(check_binary_conics(F) for F in choices)
    print('VERIFY_OK fields=%d pair_fiber_classes=%d energy_and_deficit_tests=%d direct_fourier_tests=%d conic_deficit_tests=%d' %
          (len(choices),fibers,tests,fourier,conics))


if __name__ == '__main__':
    run()
