"""Finite-field checks for exact ordered rank-one square-zero summand fibers.
No external dependencies.  Run: python verify.py
"""
from itertools import product
from collections import Counter


def field(q):
    if q == 4:
        def add(a, b): return a ^ b
        def mul(a, b):
            x = 0
            for i in range(2):
                for j in range(2):
                    if ((a >> i) & 1) and ((b >> j) & 1):
                        x ^= 1 << (i + j)
            if x & 4:
                x ^= 7  # t^2=t+1 over F_2
            return x
    else:
        assert q in (2,3,5,7)
        def add(a, b): return (a + b) % q
        def mul(a, b): return (a * b) % q
    zero = 0
    neg = [next(b for b in range(q) if add(a, b) == zero) for a in range(q)]
    inv = [None] + [next(b for b in range(1,q) if mul(a,b) == 1) for a in range(1,q)]
    return add, mul, neg, inv


def rank(rows, q, add, mul, neg, inv):
    a = [list(x) for x in rows]
    if not a: return 0
    m = len(a); n = len(a[0]); r = 0
    for j in range(n):
        pivot = next((i for i in range(r,m) if a[i][j]),None)
        if pivot is None: continue
        a[r],a[pivot] = a[pivot],a[r]
        fac=inv[a[r][j]]
        a[r]=[mul(fac,x) for x in a[r]]
        for i in range(m):
            if i != r and a[i][j]:
                x=a[i][j]
                a[i]=[add(y,neg[mul(x,z)]) for y,z in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r


def normalize(v, mul, inv):
    t=next(x for x in v if x)
    return tuple(mul(inv[t],x) for x in v)


def count_formula(B, n, q, add, mul, neg, inv):
    tr=0
    for i in range(n):tr=add(tr,B[i*n+i])
    if tr: return 0
    M=[B[i*n:(i+1)*n] for i in range(n)]
    r=rank(M,q,add,mul,neg,inv)
    if r==0:return (q**n-1)*(q**(n-1)-1)//(q-1)
    if r==1:return 2*q**(n-1)-q-2
    if r>=3:return 0
    # rank-two image is B-invariant; the restrictions' rational eigenlines
    col=[tuple(B[i*n+j] for i in range(n)) for j in range(n)]
    u=next(v for v in col if any(v))
    v=next(v for v in col if rank([u,v],q,add,mul,neg,inv)==2)
    lines={normalize(tuple(add(mul(a,x),mul(b,y)) for x,y in zip(u,v)),mul,inv)
           for a,b in product(range(q),repeat=2) if a or b}
    assert len(lines)==q+1
    e=e0=0
    for x in lines:
        bx=tuple(sum((0,)) for _ in []) if False else tuple(
            __import__('functools').reduce(add,(mul(B[i*n+j],x[j]) for j in range(n)),0)
            for i in range(n))
        if rank([x,bx],q,add,mul,neg,inv)==1:
            e+=1
            if not any(bx):e0+=1
    return q*e0+q+1-e


def verify(q,n,all_targets=True):
    add,mul,neg,inv=field(q)
    vectors=list(product(range(q),repeat=n))
    # Enumerate rank-one square-zero matrices once, dividing scalar redundancy
    roots=set()
    for u in vectors:
        if not any(u):continue
        for phi in vectors:
            if not any(phi):continue
            t=0
            for x,y in zip(u,phi):t=add(t,mul(x,y))
            if t:continue
            roots.add(tuple(mul(u[i],phi[j]) for i in range(n) for j in range(n)))
    predicted_roots=(q**n-1)*(q**(n-1)-1)//(q-1)
    assert len(roots)==predicted_roots
    fiber=Counter(tuple(add(x,y) for x,y in zip(X,Y)) for X in roots for Y in roots)
    assert sum(fiber.values())==predicted_roots**2
    tested=set(fiber)
    if all_targets:tested.update(product(range(q),repeat=n*n))
    else:
        tested.add((0,)*(n*n))
        # also probe a diagonal scalar multiple of rank two projection
        if n>=2:
            for s in range(1,q):
                a=[0]*(n*n)
                a[0]=a[n+1]=s
                tested.add(tuple(a))
    for B in tested:
        expected=count_formula(B,n,q,add,mul,neg,inv)
        got=fiber[B]
        assert expected==got,(q,n,B,expected,got)
    print('q=',q,'n=',n,'summands=',predicted_roots,
          'nonzero_target_fibers=',len(fiber),
          'checked_targets=',len(tested),'VERIFY_OK')


if __name__=='__main__':
    for q,n,full in [(2,2,True),(3,2,True),(4,2,True),(5,2,True),
                     (2,3,True),(3,3,True),(4,3,False),(2,4,True)]:
        verify(q,n,full)
    print('VERIFY_OK')
