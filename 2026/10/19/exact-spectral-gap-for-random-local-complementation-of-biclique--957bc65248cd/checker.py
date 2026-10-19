"""Reproduce local-complementation transition and spectral checks (no network)."""
from collections import deque
from itertools import combinations
import sympy as sp


def edges_to_mask(k, edges):
    return sum(1 << (min(a,b)*k + max(a,b)) for a,b in edges)


def local_complement(g, k, v):
    nb = [i for i in range(k) if i != v and (g >> (min(i,v)*k + max(i,v))) & 1]
    return g ^ edges_to_mask(k, combinations(nb,2))


def family(m,n):
    k=m+n; L=range(m); R=range(m,k)
    c = set(combinations(L,2)); d=set(combinations(R,2))
    cross={(a,b) for a in L for b in R}
    f={('B',): edges_to_mask(k,cross),
       ('CL',): edges_to_mask(k,cross|c),
       ('CR',): edges_to_mask(k,cross|d)}
    for a in L:
        f[('U',a)]=edges_to_mask(k, {(min(a,x),max(a,x)) for x in L if x!=a}|d|{(a,b) for b in R})
    for b in R:
        f[('V',b)]=edges_to_mask(k, {(min(b,x),max(b,x)) for x in R if x!=b}|c|{(a,b) for a in L})
    for a in L:
        for b in R:
            f[('W',a,b)]=edges_to_mask(k, {(min(a,x),max(a,x)) for x in L if x!=a}|
                                     {(min(b,x),max(b,x)) for x in R if x!=b}|{(a,b)})
    assert len(f)==m*n+m+n+3 and len(set(f.values()))==len(f)
    return f


def predicted_next(key,v,m,n):
    k=m+n; tag=key[0]
    if tag=='B': return ('CR',) if v<m else ('CL',)
    if tag=='CL': return ('U',v) if v<m else ('B',)
    if tag=='CR': return ('B',) if v<m else ('V',v)
    if tag=='U':
        a=key[1]
        return ('CL',) if v==a else (('U',a) if v<m else ('W',a,v))
    if tag=='V':
        b=key[1]
        return ('CR',) if v==b else (('V',b) if v>=m else ('W',v,b))
    a,b=key[1:]
    return ('V',b) if v==a else (('U',a) if v==b else ('W',a,b))


def full_transition(m,n):
    f=family(m,n); rev={value:key for key,value in f.items()}; k=m+n
    original=f[('B',)]; seen={original}; queue=deque([original])
    while queue:
        g=queue.popleft()
        for v in range(k):
            h=local_complement(g,k,v)
            if h not in seen:
                seen.add(h);queue.append(h)
    assert seen==set(f.values())
    keys=list(f); idx={key:i for i,key in enumerate(keys)}
    A=sp.zeros(len(keys))
    for a, g in f.items():
        for v in range(k):
            h=local_complement(g,k,v)
            assert rev[h]==predicted_next(a,v,m,n), (m,n,a,v,rev[h])
            A[idx[a],idx[rev[h]]]+=1
    assert A==A.T and list(A*sp.ones(A.rows,1))==[k]*A.rows
    return A


def quartic(m,n,t):
    N=m+n
    return (t**4-3*(N+1)*t**3 +
            (2*(m*m+n*n)+7*m*n+7*N+2)*t**2 -
            (4*m*n*N+11*m*n+2*(m*m+n*n)+4*N)*t +
            2*m*n*(m*n+N+3))


def expected_polynomial(m,n,t):
    N=m+n
    return (t*(t-(N+1))*quartic(m,n,t)*
            (t-1)**(m+n-2)*
            (t-(n+2))**(m-1)*
            (t-(m+2))**(n-1)*
            (t-2)**((m-1)*(n-1)))


def main():
    t=sp.Symbol('t')
    for m in range(2,6):
        for n in range(2,6):
            A=full_transition(m,n)
            N=m+n
            assert sp.expand(A.charpoly(t).as_expr().subs(t,N-t)-(-1)**A.rows*expected_polynomial(m,n,t))==0, (m,n)
            # charpoly of adjacency evaluated at N-t = (-1)^K charpoly(Laplace)(t).
            print('PASS',m,n,'orbit_size',A.rows,'spectral_gap',f'1/{N}')
    print('All orbit, transition and exact spectral-polynomial checks passed.')

if __name__=='__main__': main()
