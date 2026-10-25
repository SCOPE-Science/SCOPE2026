#!/usr/bin/env python3
"""Exhaustive finite-field checks for regular nilpotents in nilpotent centralizers.

Independent direct enumeration of matrix products/powers, with no Sage dependency.
Run: python check.py
"""
from collections import Counter
from itertools import product
from math import prod


def field(q):
    if q in (2, 3):
        return [[(a+b)%q for b in range(q)] for a in range(q)], [[(a*b)%q for b in range(q)] for a in range(q)]
    if q == 4:
        # GF(4) = F2[z]/(z*z+z+1), binary packed coefficients.
        def mul(a, b):
            v=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1: v ^= 1<<(i+j)
            if v&8: raise AssertionError
            if v&4: v ^= 7
            return v
        return [[a^b for b in range(q)] for a in range(q)], [[mul(a,b) for b in range(q)] for a in range(q)]
    raise ValueError(q)


def mm(A,B,n,add,mul):
    return tuple(__import__('functools').reduce(lambda u,v:add[u][v], [mul[A[i*n+k]][B[k*n+j]] for k in range(n)],0) for i in range(n) for j in range(n))


def zmat(n): return (0,)*(n*n)


def ident(n): return tuple(int(i==j) for i in range(n) for j in range(n))


def jordan(parts):
    n=sum(parts); A=[0]*(n*n); s=0
    for d in parts:
        for t in range(d-1): A[(s+t)*n+(s+t+1)]=1
        s += d
    return tuple(A)


def matadd(A,B,add):return tuple(add[a][b] for a,b in zip(A,B))


def nilpotent(B,n,add,mul):
    C=ident(n); zero=zmat(n)
    for _ in range(n):
        C=mm(C,B,n,add,mul)
        if C == zero: return True
    return False


def regular_nilpotent(B,n,add,mul):
    C=ident(n)
    zero=zmat(n)
    for i in range(1,n+1):
        C=mm(C,B,n,add,mul)
        if C==zero:return i==n
    return False


def jordan_partitions(n):
    def rec(left,maxpart):
        if left==0:
            yield ()
        for a in range(min(left,maxpart),0,-1):
            for tail in rec(left-a,a): yield (a,)+tail
    return list(rec(n,n))


def expected_nils(parts,q):
    c=sum(min(a,b) for a in parts for b in parts)
    return q**(c-len(parts))


def phi_count(m,q):
    # Numerator of Phi_m multiplied by q^sum? used as integer rational via Fraction.
    from fractions import Fraction
    return prod((Fraction(q**j-1,q**j) for j in range(1,m+1)),start=__import__('fractions').Fraction(1))


def expected_regular(parts,q):
    from collections import Counter
    n=sum(parts); counts=Counter(parts)
    if parts==(1,)*n:
        return expected_nils(parts,q)*prod((__import__('fractions').Fraction(q**j-1,q**j) for j in range(2,n+1)),start=__import__('fractions').Fraction(1))
    if parts[0]-parts[-1]>1:
        return 0
    return expected_nils(parts,q)*prod((phi_count(m,q) for m in counts.values()),start=__import__('fractions').Fraction(1))


def test(q,n):
    add,mul=field(q)
    all_matrices=product(range(q),repeat=n*n)
    shapes=jordan_partitions(n)
    bases=[]
    for parts in shapes:
        A=jordan(parts); bases.append((parts,A))
    count=Counter(); regs=Counter(); fibers={}
    for cells in all_matrices:
        B=tuple(cells)
        good=[]
        for parts,A in bases:
            if mm(A,B,n,add,mul)==mm(B,A,n,add,mul): good.append((parts,A))
        if not good: continue
        if not nilpotent(B,n,add,mul): continue
        reg=regular_nilpotent(B,n,add,mul)
        for parts,A in good:
            count[parts]+=1
            if reg:
                regs[parts]+=1
                k=len(parts)
                if parts==(1,)*n:
                    candidate_f=[(0,)*n]
                elif parts[0]-parts[-1] <= 1:
                    candidate_f=[(0,)*k + (u,) +v for u in range(1,q) for v in product(range(q),repeat=n-k-1)]
                else:
                    raise AssertionError('unexpected regular nilpotent')
                powers=[ident(n)]
                for j in range(1,n): powers.append(mm(powers[-1],B,n,add,mul))
                for f in candidate_f:
                    D=zmat(n)
                    for scalar,P in zip(f,powers):
                        if scalar:
                            D=matadd(D,tuple(mul[scalar][x] for x in P),add)
                    if D==A: fibers[(parts,f)]=fibers.get((parts,f),0)+1
    tested_fibers=0
    for parts,A in bases:
        eN=expected_nils(parts,q)
        eR=expected_regular(parts,q)
        assert int(eR)==eR,(q,n,parts,'fractional',eR)
        assert count[parts]==eN,(q,n,parts,'nilcount',count[parts],eN)
        assert regs[parts]==eR,(q,n,parts,'regcount',regs[parts],eR)
        k=len(parts)
        if eR:
            fcount=(q-1)*q**(n-k-1) if k<n else 1
            assert eR%fcount==0
            ff=[value for (shape,poly),value in fibers.items() if shape==parts]
            assert len(ff)==fcount and set(ff)=={eR//fcount},(q,n,parts,'fibers',ff,eR//fcount)
            tested_fibers+=len(ff)
        else:
            assert not any(shape==parts for shape,poly in fibers)
    return len(shapes),sum(count.values()),sum(regs.values()),tested_fibers


def main():
    cases=[(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]
    total=Counter()
    for q,n in cases:
        sh,c,r,f=test(q,n)
        total['shapes']+=sh;total['nilpotent_centralizer_elements']+=c
        total['regular_pairs']+=r;total['uniform_poly_fibers']+=f
        print('PASS q=%d n=%d partitions=%d nilpotent_commuters=%d regular_commuters=%d uniform_fibers=%d'%(q,n,sh,c,r,f))
    print('ALL_REGULAR_NILPOTENT_CENTRALIZER_CHECKS_PASSED '+ ' '.join('%s=%s'%(k,total[k]) for k in ('shapes','nilpotent_centralizer_elements','regular_pairs','uniform_poly_fibers')))

if __name__=='__main__':main()
