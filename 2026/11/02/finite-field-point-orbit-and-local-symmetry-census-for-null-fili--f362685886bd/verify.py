#!/usr/bin/env python3
"""Self-contained, exhaustive small-field checks for null-filiform Leibniz algebra element orbits and linear local automorphisms.
Run: python3 verify.py
"""
from itertools import product
from math import gcd

def field(q):
    if q in (2, 3):
        return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    if q == 4:
        def mul(a,b):
            out=0
            for i in range(2):
                if (b>>i)&1: out ^= a<<i
            if out&8: out ^= 8^4^2
            if out&4: out ^= 4^2^1
            return out
        return lambda a,b:a^b, mul
    raise ValueError('not supported')

def matvec(cols,x,add,mul,n):
    out=[0]*n
    for j in range(n):
        for i in range(n):
            out[i]=add(out[i],mul(cols[j][i],x[j]))
    return tuple(out)

def bracket(x,y,add,mul,n):
    return (0,)+tuple(mul(y[0],x[i]) for i in range(n-1))

def full_rank(cols,add,mul,n,q):
    """Gaussian elimination, using multiplication tables to invert pivots."""
    inv={a:next(b for b in range(1,q) if mul(a,b)==1)
         for a in range(1,q)}
    rows=[[cols[j][i] for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if rows[r][col]),None)
        if pivot is None:return False
        rows[col],rows[pivot]=rows[pivot],rows[col]
        t=inv[rows[col][col]]
        rows[col]=[mul(t,x) for x in rows[col]]
        for r in range(col+1,n):
            factor=rows[r][col]
            if factor:
                rows[r]=[add(rows[r][j],mul(factor,rows[col][j])) for j in range(n)]
    return True

def automorphism(cols,vecs,add,mul,n,q):
    # This checks the defining multiplication, without using the normal form.
    z=(0,)*n
    e=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    for i in range(n):
        for j in range(n):
            actual=bracket(cols[i],cols[j],add,mul,n)
            expected=cols[i+1] if j==0 and i<n-1 else z
            if actual!=expected:return False
    # Verify linear invertibility by matrix elimination, not the normal form.
    return full_rank(cols,add,mul,n,q)

def expected_local(cols,q,n,add,mul):
    for j in range(n):
        if any(cols[j][i] for i in range(j)):return False
        if cols[j][j] not in {power(a,j+1,mul) for a in range(1,q)}:return False
    return True

def power(a,k,mul):
    out=1
    for _ in range(k):out=mul(out,a)
    return out

def check(q,n):
    add,mul=field(q)
    vecs=list(product(range(q),repeat=n))
    matrices=product(vecs, repeat=n)
    aut=[]
    for cols in matrices:
        if automorphism(cols,vecs,add,mul,n,q): aut.append(cols)
    expected_aut=(q-1)*q**(n-1)
    assert len(aut)==expected_aut, (q,n,'aut',len(aut),expected_aut)
    orbit={v:set() for v in vecs}
    for v in vecs:
        for a in aut:orbit[v].add(matvec(a,v,add,mul,n))
    all_orbits={frozenset(orb) for orb in orbit.values()}
    predicted_orbits=1+sum(gcd(i,q-1) for i in range(1,n+1))
    assert len(all_orbits)==predicted_orbits, (q,n,'orbits',len(all_orbits),predicted_orbits)
    for x in vecs:
        if x==(0,)*n:
            assert orbit[x]=={x}
            continue
        m=next(i+1 for i,t in enumerate(x) if t)
        C={power(a,m,mul) for a in range(1,q)}
        leading={mul(x[m-1],c) for c in C}
        expected={v for v in vecs if v[:m-1]==(0,)*(m-1) and v[m-1] in leading}
        assert orbit[x]==expected, (q,n,'orbit vectors',x)
        stabilizers=sum(matvec(a,x,add,mul,n)==x for a in aut)
        assert stabilizers==gcd(m,q-1)*q**(m-1), (q,n,'stabilizers',x,stabilizers)
    local_count=0
    # Exhaustive enumeration of ALL q^(n*n) linear operators, not just triangular matrices.
    for cols in product(vecs,repeat=n):
        loc=all(matvec(cols,v,add,mul,n) in orbit[v] for v in vecs)
        expected=expected_local(cols,q,n,add,mul)
        assert loc==expected, (q,n,'local matrix',cols,loc,expected)
        local_count+=loc
    den=1
    for i in range(1,n+1): den*=gcd(i,q-1)
    expected_loc=q**(n*(n-1)//2)*(q-1)**n//den
    assert local_count==expected_loc, (q,n,'local count',local_count,expected_loc)
    return (q,n,len(aut),len(all_orbits),local_count)

def main():
    rows=[]
    for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:
        row=check(q,n);rows.append(row);print('q={} n={} automorphisms={} point_orbits={} local_automorphisms={}'.format(*row))
    print('NULL_FILIFORM_FINITE_LOCAL_AUT_OK {} exhaustive matrix configurations'.format(len(rows)))
if __name__=='__main__':main()
