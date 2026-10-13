#!/usr/bin/env python3
"""Self-contained finite verification of the chain parameter formulas.

Only standard Python; constructs operations rather than querying a counting sequence.
Finite tests are supplementary to the all-size proof in RESULT.md.
"""
from itertools import product
from math import comb


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def compositions(n, parts):
    if parts == 0:
        if n == 0:
            yield ()
        return
    for first in range(1, n - parts + 2):
        for tail in compositions(n - first, parts - 1):
            yield (first,) + tail


def sugihara_product(i, j):
    if abs(i) > abs(j):
        return i
    if abs(j) > abs(i):
        return j
    return min(i, j)


def gsm(k, lengths):
    """Finite chain GSM with odd Sugihara skeleton [-k,...,k]."""
    assert len(lengths) == k + 1 and min(lengths) >= 1
    order = tuple((i, p) for i in range(-k, k+1)
                  for p in range(lengths[i+k] if i <= 0 else 1))
    idx = {u: n for n, u in enumerate(order)}
    top = {i: idx[(i, (lengths[i+k]-1 if i <= 0 else 0))]
           for i in range(-k, k+1)}
    d = len(order)
    e = top[0]
    star = tuple(top[-i] for i, p in order)
    dot = [[0]*d for _ in range(d)]
    resid = [[0]*d for _ in range(d)]
    for a,(i,p) in enumerate(order):
        for b,(j,q) in enumerate(order):
            if i == j:
                dot[a][b] = (min(a,b) if i <= 0 else max(a,b))
            else:
                target = sugihara_product(i,j)
                dot[a][b] = a if target == i else b
            resid[a][b] = max(star[a], b) if a <= b else min(star[a], b)
    return dict(d=d, e=e, dot=dot, resid=resid,
                order=order, star=star, k=k, lengths=tuple(lengths))


def reflection(G):
    """Reflection of a finite linearly ordered Dunn monoid."""
    d = G['d']; n = 2*d + 2
    def mirror(x):
        return n-1-x
    neg = tuple(mirror(x) for x in range(n))
    dot = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == 0 or y == 0:
                z = 0
            elif x == n-1 or y == n-1:
                z = n-1
            elif 1 <= x <= d and 1 <= y <= d:
                z = 1 + G['dot'][x-1][y-1]
            elif d < x < n-1 and d < y < n-1:
                z = n-1
            else:
                a = (x-1) if x <= d else (y-1)
                bprime = y if x <= d else x
                b = mirror(bprime)-1
                z = mirror(1 + G['resid'][a][b])
            dot[x][y] = z
    return dict(n=n, e=1+G['e'], neg=neg, dot=dot)


def extension(S, shell):
    """Replace zero of odd Sugihara chain by the central reflection S."""
    n0=S['n']; assert n0 % 2 == 0
    n=n0+2*shell
    e=S['e']+shell
    neg=[None]*n
    for x in range(shell):
        neg[x] = n-1-x
        neg[n-1-x]=x
    for x in range(n0):
        neg[shell+x] = shell+S['neg'][x]
    dot=[[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            cx = shell <= x < shell+n0
            cy = shell <= y < shell+n0
            if cx and cy:
                z=shell+S['dot'][x-shell][y-shell]
            elif cx:
                z=y
            elif cy:
                z=x
            else:
                # External points, indexed -shell..-1 and 1..shell.
                def ext(v):
                    if v < shell: return v-shell
                    return v-(shell+n0)+1
                a,b=ext(x),ext(y)
                w=sugihara_product(a,b)
                z=(w+shell) if w < 0 else (shell+n0+w-1)
            dot[x][y]=z
    return dict(n=n,e=e,neg=tuple(neg),dot=dot)


def sugihara(n):
    if n % 2:
        k=(n-1)//2
        labels=tuple(range(-k,k+1))
        e=k
    else:
        k=n//2
        labels=tuple(range(-k,0))+tuple(range(1,k+1))
        e=k
    idx={a:i for i,a in enumerate(labels)}
    neg=tuple(idx[-a] for a in labels)
    dot=[[idx[sugihara_product(a,b)] for b in labels] for a in labels]
    return dict(n=n,e=e,neg=neg,dot=dot)


def elementary_axioms(A, intensive=False):
    n=A['n']; e=A['e']; dot=A['dot']; neg=A['neg']
    assert all(neg[neg[x]]==x for x in range(n))
    assert all(neg[x]==n-1-x for x in range(n))
    assert all(dot[x][e]==x and dot[e][x]==x for x in range(n))
    assert all(dot[x][y]==dot[y][x] for x in range(n) for y in range(n))
    assert all(dot[x][y] <= dot[x][z] for x in range(n)
               for y in range(n) for z in range(y,n))
    assert all(x <= dot[x][x] for x in range(n))
    residual=lambda x,y:neg[dot[x][neg[y]]]
    assert all((dot[x][y] <= z)==(y <= residual(x,z))
               for x in range(n) for y in range(n) for z in range(n))
    if intensive:
        assert all(dot[dot[x][y]][z]==dot[x][dot[y][z]]
                   for x in range(n) for y in range(n) for z in range(n))
        closure=set(range(e+1))|{e}
        changed=True
        while changed:
            old=set(closure)
            for x in old:
                closure.add(neg[x])
                for y in old:
                    closure.update((dot[x][y],residual(x,y),min(x,y),max(x,y)))
            changed=(closure!=old)
        assert closure==set(range(n))
    return sum(dot[x][x] != x for x in range(n))


def main():
    checks=0
    for n in range(1,22):
        expected = 1 if n%2 else fibonacci(n//2+1)
        # Enumerate canonical parameters without using Fibonacci recurrence.
        params=[]
        if n%2:
            params=[('sugihara', n)]
        else:
            t=n//2
            params=[('sugihara', n)]
            for d in range(1,t):
                shell=t-d-1
                for k in range((d-1)//2+1):
                    for lens in compositions(d-k, k+1):
                        params.append(('reflect', d, shell, k, lens))
        assert len(params)==expected
        checks+=1
        by_nonidem={}
        full_signatures=[]
        for prm in params:
            if prm[0]=='sugihara':
                A=sugihara(n)
                assert elementary_axioms(A) == 0
                r=0
            else:
                _,d,s,k,lens=prm
                G=gsm(k,lens)
                A=extension(reflection(G),s)
                assert A['n']==n
                r=d
                if n<=16:
                    assert elementary_axioms(A, intensive=n<=12)==d
                else:
                    assert sum(A['dot'][i][i]!=i for i in range(n))==d
            by_nonidem[r]=by_nonidem.get(r,0)+1
            if n <= 16:
                full_signatures.append((A['e'], tuple(A['neg']), tuple(map(tuple,A['dot']))))
            checks+=1
        target={0:1} if n%2 else {0:1, **{d:fibonacci(d) for d in range(1,n//2)}}
        assert by_nonidem==target, (n,by_nonidem,target)
        if n <= 16:
            assert len(set(full_signatures)) == len(full_signatures), ('collision', n)
        checks+=1
        print(n, expected, sorted(by_nonidem.items()))
    # Independent enumeration of all weak compositions of fiber surpluses.
    for d in range(1,21):
        count=sum(sum(1 for _ in compositions(d-k,k+1))
                  for k in range((d-1)//2+1))
        assert count==fibonacci(d)
        checks+=1
    print('VERIFY_OK',checks,'parameter identities, exact operation tables and finite axioms')


if __name__=='__main__':
    main()
