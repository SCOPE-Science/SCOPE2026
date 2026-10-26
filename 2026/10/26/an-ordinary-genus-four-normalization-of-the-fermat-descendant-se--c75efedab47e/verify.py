#!/usr/bin/env python3
"""Exact finite-field checks for a characteristic-three plane-sextic normalization."""
from collections import Counter

MODULI = {1: [0, 1], 2: [1, 0, 1], 3: [2, 2, 0, 1]}

class Field:
    def __init__(self, degree):
        self.n = degree
        self.q = 3 ** degree
        self.modulus = MODULI[degree]
        self.vectors = [tuple((j // (3 ** i)) % 3 for i in range(degree)) for j in range(self.q)]
        self.add_table = [[self.index(tuple((a+b)%3 for a,b in zip(self.vectors[x],self.vectors[y]))) for y in range(self.q)] for x in range(self.q)]
        self.mul_table = [[self.mult_raw(x, y) for y in range(self.q)] for x in range(self.q)]
        self.one = 1
    def index(self, coeffs):
        return sum(c * (3 ** i) for i,c in enumerate(coeffs))
    def mult_raw(self, x, y):
        n = self.n
        raw = [0] * (2 * n - 1)
        for i,a in enumerate(self.vectors[x]):
            for j,b in enumerate(self.vectors[y]):
                raw[i+j] = (raw[i+j] + a*b) % 3
        for i in range(len(raw)-1, n-1, -1):
            factor = raw[i]
            for j in range(n):
                raw[i-n+j] = (raw[i-n+j] - factor*self.modulus[j]) % 3
        return self.index(raw[:n])
    def add(self, *terms):
        x = 0
        for y in terms:
            x = self.add_table[x][y]
        return x
    def mul(self, *terms):
        x = 1
        for y in terms:
            x = self.mul_table[x][y]
        return x
    def pow(self, x, exponent):
        ans = 1
        while exponent:
            if exponent & 1: ans = self.mul(ans,x)
            x = self.mul(x,x)
            exponent //= 2
        return ans

def projective_points(K):
    return ([(1,y,z) for y in range(K.q) for z in range(K.q)]
        + [(0,1,z) for z in range(K.q)] + [(0,0,1)])

def curve_counts(K, lam):
    m,a,p = K.mul,K.add,K.pow
    count_d, count_e = 0, 0
    singular = 0
    for x,y,z in projective_points(K):
        X,Y,Z=p(x,2),p(y,2),p(z,2)
        d=a(p(x,6),p(y,6),p(z,6),m(lam,X,Y,Z))
        e=a(p(x,3),p(y,3),p(z,3),m(lam,x,y,z))
        count_d += d == 0
        count_e += e == 0
        if d == 0 and (m(x,Y,Z)==0 and m(X,y,Z)==0 and m(X,Y,z)==0):
            singular += 1
    count_f = 1
    for x in range(K.q):
        rhs = a(p(x,3),m(2,lam,p(x,2)),m(p(lam,2),x),m(2,p(lam,2)))
        count_f += sum(K.pow(y,2)==rhs for y in range(K.q))
    return count_d,count_e,count_f,singular

def trace_power(a, index):
    if index == 0: return 2
    if index == 1: return a
    x, y = 2, a
    for _ in range(2, index+1):
        x,y=y,a*y-3*x
    return y

def main():
    table=[]
    for lam in (1,2):
        base=Field(1)
        d1,e1,f1,sing1 = curve_counts(base,lam)
        te,tf = 4-e1,4-f1
        assert d1 == 4-te-3*tf
        assert te % 3 != 0 and tf % 3 != 0
        assert sing1 == 0
        for n in (1,2,3):
            K=Field(n)
            d,e,f,sing=curve_counts(K,lam)
            q=3**n
            expected = q+1-trace_power(te,n)-3*trace_power(tf,n)
            assert d==expected, (lam,n,d,expected)
            assert e==q+1-trace_power(te,n), (lam,n,e)
            assert f==q+1-trace_power(tf,n), (lam,n,f)
            assert sing==(0 if n%2 else 6), (lam,n,sing)
            table.append((lam,q,d,e,f,sing))
    print('lambda q #plane_sextic #elliptic_E #elliptic_F #rational_singular_points')
    for row in table: print(*row)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
