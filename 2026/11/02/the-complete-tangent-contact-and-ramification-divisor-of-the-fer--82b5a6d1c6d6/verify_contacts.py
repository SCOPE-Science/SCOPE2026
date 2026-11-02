"""Exact finite-field checks for the Fermat norm-degree tangent-contact theorem.

Uses elementary polynomial quotient arithmetic, without third-party packages.
Checks every rational point over GF(8), GF(64), GF(27), GF(125),
and independently verifies the seven nontrivial tangent Taylor coefficients.
"""
from collections import Counter


class GF:
    def __init__(self, p, modulus):
        self.p = p
        self.n = len(modulus) - 1
        self.modulus = modulus
        self.Q = p ** self.n
        self.digits = [tuple((i // (p ** j)) % p for j in range(self.n)) for i in range(self.Q)]
        self.add = [[self.encode([(a[k] + b[k]) % p for k in range(self.n)])
                     for b in self.digits] for a in self.digits]
        self.neg = [self.encode([(-x) % p for x in a]) for a in self.digits]
        self.mul = [[self._multiply(a, b) for b in self.digits] for a in self.digits]
        self.inv = [0] * self.Q
        for i in range(1, self.Q):
            matches = [j for j in range(1, self.Q) if self.mul[i][j] == 1]
            assert len(matches) == 1, ('nonfield', p, modulus, i)
            self.inv[i] = matches[0]

    def encode(self, digits):
        return sum(int(v) * (self.p ** j) for j, v in enumerate(digits))

    def _multiply(self, aa, bb):
        p, n = self.p, self.n
        c = [0] * (2 * n - 1)
        for i, x in enumerate(aa):
            for j, y in enumerate(bb):
                c[i+j] = (c[i+j] + x*y) % p
        for k in range(2*n-2, n-1, -1):
            v = c[k]
            for j in range(n):
                c[k-n+j] = (c[k-n+j] - v * self.modulus[j]) % p
        return self.encode(c[:n])

    def power(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul[out][a]
            a = self.mul[a][a]
            n //= 2
        return out


def contact(F, P, q):
    d = q*q + q + 1
    M, A, neg = F.mul, F.add, F.neg
    G = [F.power(x, d-1) for x in P]
    E = None
    for i,j in ((0,1),(0,2),(1,2)):
        e = [0, 0, 0]
        e[i],e[j] = G[j], neg[G[i]]
        if all(x==0 for x in e):
            continue
        if all(A[M[P[i]][e[j]]][neg[M[P[j]][e[i]]]] == 0 for i,j in ((0,1),(0,2),(1,2))):
            continue
        E = e
        break
    assert E is not None, ('no tangent direction', P)
    assert all(A[M[G[i]][E[i]]][0] == M[G[i]][E[i]] for i in range(3))
    assert A[A[M[G[0]][E[0]]][M[G[1]][E[1]]]][M[G[2]][E[2]]] == 0
    sums = {}
    selector = {0:(0,0,0), 1:(1,0,0), q:(0,1,0), q+1:(1,1,0),
                q*q:(0,0,1), q*q+1:(1,0,1), q*q+q:(0,1,1), d:(1,1,1)}
    for ex, (b0,b1,b2) in selector.items():
        ss = 0
        for a,e in zip(P,E):
            p0=F.power(a,1); pq=F.power(a,q); pq2=F.power(a,q*q)
            e0=e; eq=F.power(e,q); eq2=F.power(e,q*q)
            factors = ((e0 if b0 else p0),
                       (eq if b1 else pq),
                       (eq2 if b2 else pq2))
            prod = M[M[factors[0]][factors[1]]][factors[2]]
            ss = A[ss][prod]
        sums[ex]=ss
    assert sums[0]==0 and sums[1]==0
    return min(ex for ex,c in sums.items() if ex>=2 and c)


def check(p, modulus, q, expected=None):
    F = GF(p, modulus)
    d = q*q+q+1
    assert F.Q >= q**3 and F.Q % (q**3)==0 or F.Q == q**3
    hist=Counter()
    for y in range(F.Q):
        for z in range(F.Q):
            P=(1,y,z)
            if F.add[F.add[F.power(1,d)][F.power(y,d)]][F.power(z,d)] == 0:
                v=contact(F,P,q)
                r=all(F.power(x,q**3)==x for x in P)
                intended = (d if 0 in P else q+1) if r else q
                assert v==intended,(q,F.Q,P,v,intended)
                hist[(v,r)]+=1
    for z in range(F.Q):
        P=(0,1,z)
        if F.add[F.power(1,d)][F.power(z,d)] == 0:
            v=contact(F,P,q)
            r=all(F.power(x,q**3)==x for x in P)
            intended = d if r else q
            assert v==intended,(q,F.Q,P,v,intended)
            hist[(v,r)]+=1
    # (0,0,1) is never on the curve.
    if F.Q == q**3:
        prediction={(d,True):3*d}
        if q>2:prediction[(q+1,True)]=(q-2)*d*d
        assert dict(hist)==prediction,(q,hist,prediction)
    if expected:assert dict(hist)==expected,(hist,expected)
    print('GF(%d), q=%d, degree=%d, tangent contact distribution=%s' % (F.Q,q,d,dict(sorted(hist.items()))))


if __name__=='__main__':
    check(2,[1,1,0,1],2)
    check(3,[1,2,0,1],3)
    check(2,[1,1,0,0,0,0,1],4)
    check(5,[1,1,0,1],5)
    check(2,[1,1,0,0,0,0,1],2)
    print('FERMAT_NORM_FLEX_EXHAUSTIVE_CONTACTS_OK')
