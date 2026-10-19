"""Exact arithmetic checks for affine-group three-term convolution determinants.

Run: python3 CHECK.py
All computations use Python's standard library and integer arithmetic.
The all-prime-power theorem is proved separately; these are finite checks.
"""
from itertools import product


class Field:
    def __init__(self, p, r, poly=None):
        self.p, self.r, self.q, self.poly = p, r, p**r, poly
        if r > 1:
            assert len(poly) == r + 1 and poly[-1] == 1

    def digits(self, a):
        out = []
        for _ in range(self.r):
            out.append(a % self.p)
            a //= self.p
        return out

    def enc(self, x):
        return sum((a % self.p) * self.p**i for i, a in enumerate(x))

    def add(self, x, y):
        return self.enc([(a + b) % self.p for a, b in zip(self.digits(x), self.digits(y))])

    def neg(self, x):
        return self.enc([-a for a in self.digits(x)])

    def mul(self, x, y):
        if self.r == 1:
            return x * y % self.p
        a, b = self.digits(x), self.digits(y)
        c = [0] * (2*self.r-1)
        for i in range(self.r):
            for j in range(self.r):
                c[i+j] = (c[i+j]+a[i]*b[j]) % self.p
        for k in range(2*self.r-2, self.r-1, -1):
            t = c[k]
            for i in range(self.r):
                c[k-self.r+i] = (c[k-self.r+i]-t*self.poly[i]) % self.p
        return self.enc(c[:self.r])

    def primitive(self):
        for x in range(2, self.q):
            y, seen = 1, set()
            for _ in range(self.q - 1):
                seen.add(y)
                y = self.mul(y, x)
            if len(seen) == self.q - 1 and y == 1:
                return x
        raise AssertionError('no primitive element')


def bareiss(M):
    M = [list(row) for row in M]
    n = len(M)
    prev, sign = 1, 1
    for k in range(n-1):
        if M[k][k] == 0:
            pivot = next((i for i in range(k+1,n) if M[i][k]), None)
            if pivot is None:
                return 0
            M[k], M[pivot] = M[pivot], M[k]
            sign = -sign
        x = M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z = M[i][j]*x - M[i][k]*M[k][j]
                assert z % prev == 0
                M[i][j] = z // prev
            M[i][k] = 0
        prev = x
    return sign*M[-1][-1]


def rank_mod(M, p):
    A = [[v % p for v in row] for row in M]
    rows, cols, r = len(A), len(A[0]), 0
    for j in range(cols):
        i = next((k for k in range(r,rows) if A[k][j]), None)
        if i is None:
            continue
        A[r], A[i] = A[i], A[r]
        inv = pow(A[r][j], -1, p)
        for k in range(r+1,rows):
            if A[k][j]:
                factor = A[k][j]*inv % p
                for h in range(j,cols):
                    A[k][h] = (A[k][h] - factor*A[r][h]) % p
        r += 1
        if r == rows:
            break
    return r


def matrices(F, b, c):
    q, a = F.q, F.primitive()
    assert b != 0 and a != 1
    e, t, h = (1,0), (1,b), (a,c)
    mul = lambda x,y: (F.mul(x[0],y[0]), F.add(x[1],F.mul(x[0],y[1])))
    S = [e,t,h]
    # Affine permutation representation on the q-point line.
    line = [[0]*q for _ in range(q)]
    for x in range(q):
        for s,d in S:
            y = F.add(F.mul(s,x),d)
            line[y][x] += 1
    # Regular representation of the affine group.
    els = [(s,d) for s in range(1,q) for d in range(q)]
    idx = {g:i for i,g in enumerate(els)}
    reg = [[0]*len(els) for _ in els]
    for j,g in enumerate(els):
        for h0 in S:
            reg[idx[mul(h0,g)]][j] += 1
    return line, reg


def predicted(F):
    q,p,r = F.q,F.p,F.r
    B = (2**(q//p-1)-1) if p%2 else 1
    C = 2**(q-1)-(-1)**(q-1)
    return 3*B, C*(B**(q-1)), (q-1 if p%2 and r==1 else 0)


def main():
    fields = [Field(3,1),Field(5,1),Field(7,1),Field(11,1),
              Field(2,2,[1,1,1]),Field(2,3,[1,1,0,1]),
              Field(3,2,[1,0,1])]
    checks=0
    for F in fields:
        q=F.q
        for b,c in [(1,0),(1,1 if q>2 else 0)]:
            point,reg=matrices(F,b,c)
            d_point,d_reg,null=predicted(F)
            assert bareiss(point)==d_point, ('point',q,b,c)
            checks+=1
            if q<=7:
                assert bareiss(reg)==d_reg, ('regular',q,b,c)
                checks+=1
            if q>=8:
                # Exact expected group determinant reduced modulo two primes.
                for modulus in (101,103):
                    assert det_mod(reg,modulus)==d_reg%modulus
                    checks+=1
            if d_reg==0:
                assert rank_mod(reg,101)==q*(q-1)-null
                checks+=1
    print('PASS: %d checks on q = 3,4,5,7,8,9,11.' % checks)


def det_mod(M,p):
    A=[[x%p for x in row] for row in M]
    n=len(A)
    out=1
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None:
            return 0
        if k!=j:
            A[j],A[k]=A[k],A[j]
            out=-out
        v=A[j][j]
        out=out*v%p
        inv=pow(v,-1,p)
        for i in range(j+1,n):
            if A[i][j]:
                mult=A[i][j]*inv%p
                for l in range(j,n):
                    A[i][l]=(A[i][l]-mult*A[j][l])%p
    return out%p

if __name__=='__main__':
    main()
