#!/usr/bin/env python3
"""Independent enumeration for the four-dimensional monomial complete intersection.
Run: python3 check.py. No third-party packages required.
"""
from collections import Counter
from itertools import product


def add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def neg(x, q):
    return x if q == 4 else (-x) % q


def mul(x, y, q):
    if q != 4:
        return (x * y) % q
    out = 0
    if y & 1:
        out ^= x
    if y & 2:
        out ^= x << 1
    if out & 4:
        out ^= 0b111  # t^2 + t + 1 = 0, for F_4 = F_2[t]/(...)
    return out


def inv(x, q):
    for y in range(1, q):
        if mul(x, y, q) == 1:
            return y
    raise ValueError('non-invertible field element')


def linear_rank(columns, q):
    h = len(columns[0]); w = len(columns)
    a = [[columns[j][i] for j in range(w)] for i in range(h)]
    r = 0
    for col in range(w):
        k = next((i for i in range(r, h) if a[i][col] != 0), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        factor = inv(a[r][col], q)
        a[r] = [mul(z, factor, q) for z in a[r]]
        for i in range(r + 1, h):
            factor = a[i][col]
            if factor:
                a[i] = [add(u, neg(mul(factor,v,q),q),q) for u,v in zip(a[i],a[r])]
        r += 1
        if r == h:
            break
    return r


# Basis: 1, X, Y, XY in F_q[X,Y]/(X^2,Y^2).
MON = [(0,0),(1,0),(0,1),(1,1)]


def times(a,b,q):
    out=[0]*4
    for i,(xi,yi) in enumerate(MON):
        for j,(xj,yj) in enumerate(MON):
            if xi+xj > 1 or yi+yj > 1:
                continue
            k=MON.index((xi+xj,yi+yj))
            out[k]=add(out[k],mul(a[i],b[j],q),q)
    return tuple(out)


def vector_add(a,b,q):
    return tuple(add(x,y,q) for x,y in zip(a,b))


def derivation_columns(u,v,q):
    z=(0,)*4; one=(1,0,0,0); X=(0,1,0,0); Y=(0,0,1,0)
    return (z,u,v,vector_add(times(u,Y,q),times(X,v,q),q))


def is_derivation(columns,q):
    zero=(0,)*4
    for i in range(4):
        for j in range(4):
            prod=times(tuple(int(k==i) for k in range(4)),
                       tuple(int(k==j) for k in range(4)),q)
            # Since basis products are zero or another basis vector.
            lhs=zero if prod==zero else columns[prod.index(1)]
            ei=tuple(int(k==i) for k in range(4))
            ej=tuple(int(k==j) for k in range(4))
            rhs=vector_add(times(columns[i],ej,q),times(ei,columns[j],q),q)
            if lhs!=rhs:return False
    return True


def predicted_derivations(q):
    if q%2:
        return {0:1,1:q*q-1,2:3*q*q*(q-1),3:q*q*(q-1)*(q-2)}
    return {0:1,1:(q-1)*(q+1)**2,
            2:q*(q-1)*(q**4+3*q**3+2*q*q-1),
            3:q**3*(q-1)*(q**4+q**3-2*q-1)}


def predicted_automorphisms(q):
    if q%2:
        return 2*q*q*(q-1)**2
    return q*q*(q*q-1)*(q*q-q)


def main():
    for q in (2,3,4):
        deriv=Counter(); autom=0; candidates=0
        values=range(q)
        for params in product(values,repeat=8):
            u=params[:4];v=params[4:]
            columns=derivation_columns(u,v,q)
            valid=is_derivation(columns,q)
            if valid:
                deriv[linear_rank(columns,q)]+=1
            # Endomorphism is determined by u,v and is invertible iff
            # the 4 x 4 substitution matrix has full rank.
            if times(u,u,q)==(0,)*4 and times(v,v,q)==(0,)*4:
                candidates+=1
                cols=((1,0,0,0),u,v,times(u,v,q))
                if linear_rank(cols,q)==4:
                    autom+=1
        assert dict(deriv)==predicted_derivations(q),(q,deriv)
        assert autom==predicted_automorphisms(q),(q,autom)
        print('q=',q,'derivations=',sum(deriv.values()),
              'rank_counts=',[deriv[i] for i in range(4)],
              'automorphisms=',autom,'endomorphisms=',candidates)
    print('CHECKER_OK')

if __name__=='__main__':main()
