"""Independent finite-field checks for the hook nilpotent centralizer rank census.
Usage: python check.py
"""
from itertools import product
from collections import Counter


def field(q):
    if q == 4:
        def add(a, b): return a ^ b
        def mul(a, b):
            r = 0
            while b:
                if b & 1: r ^= a
                b >>= 1
                a <<= 1
                if a & 4: a ^= 7
            return r
        return add, mul
    def add(a, b): return (a+b) % q
    def mul(a, b): return (a*b) % q
    return add, mul


def hook_matrix(n, data):
    # Basis 1,t,...,t^(n-1),u of k[t]/t^n + k.
    a = data[:n]
    b,c,d = data[n:]
    X = [[0]*(n+1) for _ in range(n+1)]
    for j in range(n):
        for k in range(n-j):
            X[j+k][j] = a[k]
    X[n][0] = c
    X[n-1][n] = b
    X[n][n] = d
    return X


def matrix_square_is_zero(X,add,mul):
    size = len(X)
    for i in range(size):
        for j in range(size):
            v=0
            for k in range(size):
                if X[i][k] and X[k][j]:
                    v = add(v,mul(X[i][k],X[k][j]))
            if v:return False
    return True


def rank(X,add,mul,q):
    a=[row[:] for row in X]
    h=len(a); w=len(a[0]); r=0
    for col in range(w):
        piv=next((j for j in range(r,h) if a[j][col]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        v=a[r][col]
        inv=next(x for x in range(1,q) if mul(x,v)==1)
        for j in range(col,w):a[r][j]=mul(inv,a[r][j])
        for i in range(r+1,h):
            v=a[i][col]
            if v:
                for j in range(col,w):
                    a[i][j]=add(a[i][j],mul(-v%q,a[r][j])) if q!=4 else add(a[i][j],mul(v,a[r][j]))
        r+=1
        if r==h:break
    return r


def expected(q,n):
    h=n//2
    data={0:1,1:(q-1)*(2*q+1)}
    for r in range(2,h+1):data[r]=(q-1)*(2*q-1)*q**(r-1)
    if n%2:data[h+1]=(q-1)**2*q**h
    return {k:v for k,v in data.items() if v}


def test(q,n):
    add,mul=field(q)
    counts=Counter()
    count=0
    for data in product(range(q),repeat=n+3):
        X=hook_matrix(n,data)
        if matrix_square_is_zero(X,add,mul):
            counts[rank(X,add,mul,q)]+=1
            count+=1
    target=expected(q,n)
    assert dict(counts)==target,(q,n,dict(counts),target)
    total=q**((n+3)//2) if n%2 else (2*q-1)*q**(n//2)
    assert count==total,(q,n,count,total)
    return sorted(counts.items())


def main():
    cases=[(2,n) for n in range(3,9)]+[(3,n) for n in range(3,7)]+[(4,n) for n in range(3,6)]+[(5,3)]
    for q,n in cases:
        print(f'q={q}, n={n}: {test(q,n)}',flush=True)
    print('HOOK_SQUARE_ZERO_RANK_OK',len(cases),'exhaustive fields/dimensions')

if __name__=='__main__':main()
