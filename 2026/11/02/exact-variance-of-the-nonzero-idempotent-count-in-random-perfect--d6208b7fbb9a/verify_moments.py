#!/usr/bin/env python3
"""Independent direct enumeration of nonzero idempotents for uniformly random invertible
structure matrices of finite-dimensional evolution algebras over selected finite fields.
No symbolic theorem or predicted count is used in the enumeration itself.
"""
from itertools import product
from fractions import Fraction


def field(p, degree):
    if degree == 1:
        q = p
        add = [[(a + b) % p for b in range(q)] for a in range(q)]
        mul = [[(a * b) % p for b in range(q)] for a in range(q)]
    else:
        assert (p, degree) in ((2, 2), (3, 2))
        q = p * p
        add, mul = [[0] * q for _ in range(q)], [[0] * q for _ in range(q)]
        for a in range(q):
            for b in range(q):
                x, y, z, w = a % p, a // p, b % p, b // p
                add[a][b] = ((x + z) % p) + p * ((y + w) % p)
                # alpha^2=alpha+1 for p=2; alpha^2=-1 for p=3.
                const = (x*z + y*w*(1 if p == 2 else -1)) % p
                coeff = (x*w + y*z + y*w*(1 if p == 2 else 0)) % p
                mul[a][b] = const + p*coeff
    one = 1
    inv = {a: next(b for b in range(1,q) if mul[a][b]==one) for a in range(1,q)}
    return q, add, mul, inv


def field_and_neg(p, degree):
    q,add,mul,inv = field(p,degree)
    neg = [next(b for b in range(q) if add[a][b] == 0) for a in range(q)]
    return q,add,mul,inv,neg


def nonsingular(flat,n,add,mul,inv,neg):
    m=[list(flat[i*n:(i+1)*n]) for i in range(n)]
    for c in range(n):
        row=next((r for r in range(c,n) if m[r][c]),None)
        if row is None:return False
        m[c],m[row]=m[row],m[c]
        u=inv[m[c][c]]
        for j in range(c,n):m[c][j]=mul[u][m[c][j]]
        for r in range(c+1,n):
            z=m[r][c]
            if z:
                for j in range(c,n):m[r][j]=add[m[r][j]][neg[mul[z][m[c][j]]]]
    return True


def case(p, degree, n):
    q,add,mul,inv,neg=field_and_neg(p,degree)
    vectors=[v for v in product(range(q),repeat=n) if any(v)]
    sq=[tuple(mul[t][t] for t in v) for v in vectors]
    num=total=fall2=0
    distribution={}
    for flat in product(range(q),repeat=n*n):
        if not nonsingular(flat,n,add,mul,inv,neg):continue
        num+=1
        count=0
        for x,s in zip(vectors,sq):
            for i in range(n):
                z=0
                for j in range(n):z=add[z][mul[flat[i*n+j]][s[j]]]
                if z!=x[i]:break
            else:count+=1
        total+=count
        fall2+=count*(count-1)
        distribution[count]=distribution.get(count,0)+1
    predicted=Fraction(1) if p==2 else 1-Fraction((q-1)*((2*q-1)**n-2*q**n+1),2*(q**n-1)*(q**n-q))
    assert num>0 and total==num and Fraction(fall2,num)==predicted, (p,degree,n,num,total,fall2,predicted)
    print('p=%d degree=%d n=%d q=%d GL=%d mean=%s factorial_second=%s distribution=%s PASS' % (p,degree,n,q,num,Fraction(total,num),Fraction(fall2,num),sorted(distribution.items())),flush=True)

if __name__ == '__main__':
    for prm in [(2,1,2),(3,1,2),(5,1,2),(7,1,2),(2,1,3),(3,1,3),(2,1,4),(2,2,2),(3,2,2),(2,2,3)]:
        case(*prm)
    print('VERIFY_OK')
