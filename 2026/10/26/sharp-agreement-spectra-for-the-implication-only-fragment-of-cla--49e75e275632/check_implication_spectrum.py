#!/usr/bin/env python3
"""Standalone exact checker for implication-only equational probabilities.

Pure Python. Tests constructive witnesses and small-arity complete term clones.
The universal argument is in RESULT.md, not inferred from finite tests.
"""

def var(i):
    return ('v', i)

def imp(a,b):
    return ('i', a, b)

def disj(a,b):
    return imp(imp(a,b), b)

def shift(t,by):
    if t[0]=='v': return var(t[1]+by)
    return imp(shift(t[1],by),shift(t[2],by))

def eval_term(t,values):
    if t[0]=='v': return values[t[1]]
    return (not eval_term(t[1],values)) or eval_term(t[2],values)

def truth_term(n,j):
    """Implication-only term on n Boolean inputs true at exactly j points."""
    assert n>=1 and (1<<(n-1))<=j<=(1<<n)
    x=var(0)
    if n==1:
        return x if j==1 else imp(x,x)
    if j==(1<<n):
        return imp(x,x)
    r=(1<<n)-j
    m=next(m for m in range(1,n) if (1<<(m-1))<=r<=(1<<m))
    f=imp(truth_term(m,r),var(m))
    for k in range(m+1,n):
        f=disj(f,var(k))
    return f

def agreement_terms(n,d):
    """Two implication-only terms agreeing at exactly d of the 2**n inputs."""
    assert n>=2 and (1<<(n-2))<=d<=(1<<n)
    x,y=var(0),var(1)
    if n==2:
        return {
           1:(x,imp(x,y)),
           2:(x,y),
           3:(x,imp(y,x)),
           4:(x,x),
        }[d]
    if d<=(1<<(n-1)):
        a=shift(truth_term(n-1,d),1)
        return x,imp(x,a)
    if d<=5*(1<<(n-3)):
        j=3*(1<<(n-2))-d
        a=shift(truth_term(n-2,j),2)
        return x,imp(imp(x,a),y)
    if d<=3*(1<<(n-2)):
        j=d-(1<<(n-1))
        a=shift(truth_term(n-2,j),2)
        return x,imp(y,imp(a,x))
    j=d-(1<<(n-1))
    a=shift(truth_term(n-1,j),1)
    return x,imp(a,x)

def count(n,t):
    return sum(bool(eval_term(t,[(i>>v)&1 for v in range(n)]))
               for i in range(1<<n))

def agree(n,a,b):
    return sum(eval_term(a,[(i>>v)&1 for v in range(n)]) ==
               eval_term(b,[(i>>v)&1 for v in range(n)])
               for i in range(1<<n))

def small_clone(n):
    mask=(1<<(1<<n))-1
    s={sum(((i>>j)&1)<<i for i in range(1<<n)) for j in range(n)}
    while True:
        cur=list(s)
        nxt=s|{(mask^a)|b for a in cur for b in cur}
        if nxt==s:break
        s=nxt
    vals={2**n-(a^b).bit_count() for a in s for b in s}
    expected=set(range(1<<(n-2), (1<<n)+1)) if n>=2 else {1,2}
    assert vals==expected, (n,sorted(vals))
    return len(s)

if __name__ == '__main__':
    witnesses=0
    for n in range(1,9):
        for j in range(1<<(n-1), (1<<n)+1):
            f=truth_term(n,j)
            got=count(n,f)
            assert got==j,(n,j,got)
            witnesses+=1
        if n>=2:
            for j in range(1<<(n-2), (1<<n)+1):
                a,b=agreement_terms(n,j)
                got=agree(n,a,b)
                assert got==j,(n,j,got)
                witnesses+=1
    sizes=[small_clone(n) for n in range(1,5)]
    assert sizes==[2,6,38,942],sizes
    print('IMPLICATION_EQUATIONAL_SPECTRUM_EXACT_OK',witnesses,'constructive_checks','clone_sizes',sizes)
