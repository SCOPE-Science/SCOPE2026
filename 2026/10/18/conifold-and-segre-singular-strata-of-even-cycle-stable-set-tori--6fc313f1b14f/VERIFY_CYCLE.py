#!/usr/bin/env python3
"""Exact finite tests for even-cycle stable-set toric singular strata.
Uses integral matrices; no numerical tolerance or external data.
The all-parameter proof is given separately.
"""
from itertools import product, combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def odd(i): return i%2==1

def valid(x):
    n=len(x)
    return all((x[i-1]<=x[i%n] if odd(i) else x[i-1]>=x[i%n])
               for i in range(1,n+1))

def flags(x):
    n=len(x); a=[]
    for i in range(1,n+1):
        if odd(i) and x[i-1]==0:a.append(('lower',i))
        if not odd(i) and x[i-1]==1:a.append(('upper',i))
    for i in range(1,n+1):
        if x[i-1]==x[i%n]:a.append(('edge',i))
    return a

def ray(flag,n):
    a,i=flag; v=[0]*n
    if a=='lower':v[i-1]=-1
    elif a=='upper':v[i-1]=1
    else:
        j=i%n+1
        lo,hi=(i,j) if odd(i) else (j,i)
        v[lo-1]+=1;v[hi-1]-=1
    return v

def local_trigger(x,i):
    n=len(x); b=1 if odd(i) else 0
    return all(x[(j-1)%n]==b for j in (i-1,i,i+1))

def pins(S,n):
    f={}
    for i in S:
        b=1 if odd(i) else 0
        for j in (i-1,i,i+1):
            k=(j-1)%n+1
            if k in f and f[k]!=b:return None
            f[k]=b
    return f

def is_cyclic_independent(S,n):
    return not any(((i%n)+1 in S) for i in S)

def verify(n):
    assert n>=4 and n%2==0
    vs=[w for w in product((0,1),repeat=n) if valid(w)]
    bad=0
    for w in vs:
        A=flags(w)
        assert len(A)>=n
        T=[i for i in range(1,n+1) if local_trigger(w,i)]
        assert (len(A)>n)==bool(T)
        assert len(A)==n if not T else len(A)>n
        if T:bad+=1
        else:
            M=Matrix.hstack(*(Matrix(ray(f,n)) for f in A))
            assert abs(int(M.det()))==1
        M=Matrix.hstack(*(Matrix(ray(f,n)) for f in A))
        D=smith_normal_form(M,domain=ZZ)
        diag=[abs(int(D[j,j])) for j in range(min(D.rows,D.cols)) if D[j,j]]
        assert len(diag)==n and all(d==1 for d in diag)
    assert bad==len(vs)-1
    assert sum(len(flags(w))==n for w in vs)==1
    for i in range(1,n+1):
        b=1 if odd(i) else 0
        t=[w for w in vs if local_trigger(w,i)]
        assert t
        j=(i-2)%n+1; k=i%n+1
        F=[('upper' if b else 'lower',j),('upper' if b else 'lower',k),
           ('edge',j),('edge',i)]
        for w in t:assert all(f in flags(w) for f in F)
        M=Matrix.hstack(*(Matrix(ray(f,n)) for f in F))
        assert M.rank()==3
        assert M[:,0]+M[:,2]==M[:,1]+M[:,3]
        # three of four rays are primitive lattice independent: TU
        for s in combinations(range(4),3):
            W=M[:,s]
            assert W.rank()==3
            assert any(abs(int(W[list(rows),:].det()))==1 for rows in combinations(range(n),3))
    E=Matrix.hstack(*(Matrix(ray(('edge',i),n)) for i in range(1,n+1)))
    assert E.rank()==n-1
    assert E[:,list(range(0,n,2))]*Matrix.ones(n//2,1)==E[:,list(range(1,n,2))]*Matrix.ones(n//2,1)
    for q in range(n):
        W=E[:,[a for a in range(n) if a!=q]]
        assert W.rank()==n-1
        assert any(abs(int(W[list(rows),:].det()))==1 for rows in combinations(range(n),n-1))
    subset_checked=0
    for bits in product((0,1),repeat=n):
        S=[i+1 for i,v in enumerate(bits) if v]
        f=pins(S,n)
        actual=bool(f is not None and any(all(w[j-1]==b for j,b in f.items()) for w in vs))
        expect=is_cyclic_independent(set(S),n)
        assert actual==expect,(n,S,actual,expect)
        # Diagonal P^1 intersects local component collection iff all pins agree.
        meets_global=bool(actual and (not S or len({odd(i) for i in S})==1))
        predicted_global=bool(f is not None and (not f or len(set(f.values()))==1))
        assert meets_global==predicted_global,(n,S)
        subset_checked+=1
    print(f'n={n}: vertices={len(vs)}, smooth=1, singular={bad}; {n} local conifold components + 1 Segre line; {subset_checked} intersection subsets')

if __name__=='__main__':
    for n in (4,6,8,10):verify(n)
    print('VERIFY_OK')
