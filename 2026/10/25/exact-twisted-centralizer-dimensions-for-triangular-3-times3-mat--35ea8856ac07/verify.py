"""Exact finite-field checks for the 3x3 upper-triangular twisted-centralizer census.

Usage: python verify.py. Pure Python, no external dependencies.
"""
from itertools import product


class Field:
    def __init__(self, q):
        self.q = q
        if q not in (4, 5, 7):
            raise ValueError('Supported fields are 4, 5, and 7')

    def add(self, a, b):
        return (a ^ b) if self.q == 4 else (a + b) % self.q

    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.q != 4:
            return (a * b) % self.q
        res = 0
        for i in range(2):
            if (b >> i) & 1:
                res ^= a << i
        for i in (2,):
            if (res >> i) & 1:
                res ^= 0b111 << (i-2)  # x^2+x+1
        return res

    def inv(self, a):
        assert a != 0
        for b in range(1, self.q):
            if self.mul(a, b) == 1:
                return b
        raise AssertionError('Not a field')


def nullity(A, omega, F):
    a,b,c,x,y,z = A
    add,sub,mul = F.add,F.sub,F.mul
    negw = F.neg(omega)
    om_one = sub(1, omega)
    mat = [
        [mul(om_one,a),0,0,0,0,0],
        [0,mul(om_one,b),0,0,0,0],
        [0,0,mul(om_one,c),0,0,0],
        [mul(negw,x),x,0,sub(a,mul(omega,b)),0,0],
        [0,mul(negw,y),y,0,sub(b,mul(omega,c)),0],
        [mul(negw,z),0,z,mul(negw,y),x,sub(a,mul(omega,c))],
    ]
    rank = 0
    for col in range(6):
        pivot = next((i for i in range(rank,6) if mat[i][col]),None)
        if pivot is None:
            continue
        mat[rank],mat[pivot] = mat[pivot],mat[rank]
        invp = F.inv(mat[rank][col])
        for j in range(col,6):
            mat[rank][j] = mul(mat[rank][j],invp)
        for i in range(rank+1,6):
            factor = mat[i][col]
            if factor:
                for j in range(col,6):
                    mat[i][j] = sub(mat[i][j],mul(factor,mat[rank][j]))
        rank+=1
    return 6-rank


def theoretical(q):
    m=q-1
    return {
        0:q**3*m*(q*q-5*q+7),
        1:q*q*m*(6*q*q-13*q-2),
        2:q*q*m*(7*q-1),
        3:q*m*(4*q-1),
        4:2*q*m,
        5:m,
        6:1,
    }


def check(q,omegas):
    F=Field(q)
    for omega in omegas:
        assert omega not in (0,1,F.neg(1))
        counts={k:0 for k in range(7)}
        for A in product(range(q),repeat=6):
            counts[nullity(A,omega,F)]+=1
        expected=theoretical(q)
        assert counts==expected,(q,omega,counts,expected)
        number=sum(counts[k]*q**k for k in counts)
        formula=q**3*(2*q-1)*(11*q*q-15*q+5)
        assert number==formula,(number,formula)
        print(f'GF({q}), omega={omega}: dimensions {counts}, pairs={number}, verified')


if __name__=='__main__':
    check(4,[2,3])
    check(5,[2,3])
    check(7,[2,3,4,5])
    print('VERIFY_OK')
