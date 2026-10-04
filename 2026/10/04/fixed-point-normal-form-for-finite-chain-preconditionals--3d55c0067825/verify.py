#!/usr/bin/env python3
from itertools import product
from math import factorial

def check_pre(op):
    n=len(op); top=n-1
    q=lambda a,b: op[a][b]
    for a in range(n):
        if q(top,a)>a: return False
    for a,b in product(range(n), repeat=2):
        if min(a,b)>q(a,b): return False
        if q(a,b)>q(a,min(a,b)): return False
    for a,b,c in product(range(n), repeat=3):
        if q(a,min(b,c))>q(a,b): return False
        d=min(a,b)
        if q(a,q(d,c))>q(d,c): return False
    return True

def check_T(op):
    if not check_pre(op): return False
    n=len(op); top=n-1
    return all(op[a][a]==top and min(a,op[a][0])==0 for a in range(n))

def check_F(op):
    if not check_T(op): return False
    return all(a<=op[op[a][0]][0] for a in range(len(op)))

def raw_counts(n):
    pc=tc=fc=0
    for flat in product(range(n), repeat=n*n):
        op=tuple(tuple(flat[a*n:(a+1)*n]) for a in range(n))
        if check_pre(op):
            pc+=1; tc+=int(check_T(op)); fc+=int(check_F(op))
    return pc,tc,fc

assert raw_counts(1)==(1,1,1)
assert raw_counts(2)==(2,1,1)
assert raw_counts(3)==(8,1,1)

def candidates(n,a):
    if a==n-1: return [(frozenset(range(a)),a)]
    return [(frozenset(i for i in range(a) if (mask>>i)&1),r)
            for r in range(a,n) for mask in range(1<<a)]

def compatible(Sb,rb,a,Sa,ra):
    if not Sb.issubset(Sa): return False
    return (rb in Sa) if rb<a else (ra<=rb)

def states(n):
    st=[()]
    for a in range(n):
        nxt=[]
        for Sa,ra in candidates(n,a):
            for hist in st:
                if all(compatible(Sb,rb,a,Sa,ra) for Sb,rb in hist):
                    nxt.append(hist+((Sa,ra),))
        st=nxt
    return st

def build_op(n,hist):
    out=[]
    for a,(S,r) in enumerate(hist):
        F=sorted(set(S)|{r})
        out.append(tuple(min(x for x in F if x>=b) if b<=a else r for b in range(n)))
    return tuple(out)

expected=[1,2,8,47,359,3344,36530,455907]
for n,e in enumerate(expected,1):
    st=states(n)
    assert len(st)==e,(n,len(st),e)
    if n<=6:
        for hist in st:
            assert check_pre(build_op(n,hist))
    if n>=2:
        # Count T/F directly from normal-form data, and directly recheck all such operations.
        tf=[]
        top=n-1
        for hist in st:
            ok=all(r==top for S,r in hist)
            ok=ok and all((a==0 or 0 in hist[a][0]) for a in range(n))
            if ok: tf.append(hist)
        assert len(tf)==factorial(n-2),(n,len(tf))
        for hist in tf:
            op=build_op(n,hist)
            assert check_T(op) and check_F(op)

print('PRECONDITIONAL_COUNTS',expected)
print('TF_COUNTS',[1]+[factorial(n-2) for n in range(2,9)])
print('VERIFY_OK')
