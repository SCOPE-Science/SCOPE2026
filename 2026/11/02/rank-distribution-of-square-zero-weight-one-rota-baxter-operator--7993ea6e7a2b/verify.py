#!/usr/bin/env python3
"""Independent checks of square-zero Rota--Baxter rank distributions.

Run: python3 verify.py. Only finite tests; the general proof is separate.
"""
from itertools import product

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
        if q == 4:
            self.add = [[a ^ b for b in range(4)] for a in range(4)]
            self.neg = list(range(4))
            def gf4mul(a, b):
                p = 0
                for i in range(2):
                    for j in range(2):
                        if (a >> i) & 1 and (b >> j) & 1:
                            p ^= (1 << (i+j))
                if p & 8: p ^= 0b1110  # x^3=x^2+x
                if p & 4: p ^= 0b111  # x^2=x+1
                return p
            self.mul = [[gf4mul(a,b) for b in range(4)] for a in range(4)]
        else:
            self.add = [[(a+b) % q for b in range(q)] for a in range(q)]
            self.neg = [(-a) % q for a in range(q)]
            self.mul = [[a*b % q for b in range(q)] for a in range(q)]
    def plus(self,a,b): return self.add[a][b]
    def minus(self,a,b): return self.add[a][self.neg[b]]
    def times(self,a,b): return self.mul[a][b]


def symp(a,b,n,F):
    s=0
    for j in range(n):
        s=F.plus(s, F.minus(F.times(a[j], b[n+j]), F.times(a[n+j],b[j])))
    return s


def is_rb(cols,n,F):
    """Test the defining identity on every pair of Lie basis elements."""
    m=2*n; d=m+1
    assert len(cols)==d and all(len(c)==d for c in cols)
    Z=cols[m]
    for i in range(d):
        basis_i=[int(j==i) for j in range(m)]
        for j in range(i+1,d):
            basis_j=[int(k==j) for k in range(m)]
            lhs=symp(cols[i],cols[j],n,F)
            r=F.plus(symp(cols[i],basis_j,n,F),symp(basis_i,cols[j],n,F))
            r=F.plus(r,symp(basis_i,basis_j,n,F))
            if any(F.times(r,Z[k]) != (lhs if k==m else 0) for k in range(d)):
                return False
    return True


def span_iso_count(n,r,q):
    num=den=1
    for i in range(r):
        num *= q**(2*(n-i))-1
        den *= q**(r-i)-1
    assert num % den == 0
    return num//den


def symplectic_size(n,q):
    answer=q**(n*n)
    for i in range(1,n+1): answer*=q**(2*i)-1
    return answer


def T_count(n,q):
    s=0
    for r in range(n+1):
        surj=1
        for i in range(r):surj*=q**(2*n)-q**i
        s+=span_iso_count(n,r,q)*surj
    return s


def predicted(n,q):
    return q**(2*n)*(2*T_count(n,q)+(q-2)*symplectic_size(n,q))


def exhaustive_full(n,q):
    F=Field(q);d=2*n+1
    total=0; central={c:0 for c in range(q)}
    for entries in product(range(q), repeat=d*d):
        cols=[entries[i*d:(i+1)*d] for i in range(d)]
        if is_rb(cols,n,F):
            total+=1
            assert all(v==0 for v in cols[-1][:-1])
            central[cols[-1][-1]]+=1
    assert total==predicted(n,q), (n,q,total,predicted(n,q))
    factor=q**(2*n)
    for c,v in central.items():
        assert v%factor==0
        expected=T_count(n,q) if c in (0,F.neg[1]) else symplectic_size(n,q)
        assert v//factor==expected,(n,q,c,v//factor,expected)
    print(f'FULL q={q} n={n}: {total} operators; central fibers {central}')


def exhaustive_reduced(n,q):
    F=Field(q); m=2*n; d=m+1
    fibers={}
    for c in range(q):
        total=0
        for entries in product(range(q),repeat=m*m):
            cols=[tuple(entries[i*m:(i+1)*m])+(0,) for i in range(m)]
            cols.append((0,)*m+(c,))
            if is_rb(cols,n,F): total+=1
        expected=T_count(n,q) if c in (0,F.neg[1]) else symplectic_size(n,q)
        assert total==expected, (n,q,c,total,expected)
        fibers[c]=total
    assert sum(fibers.values())*q**(2*n)==predicted(n,q)
    print(f'REDUCED q={q} n={n}: {fibers}, with {q**(2*n)} free central coefficients')


def examples(n,q):
    F=Field(q);m=2*n;d=m+1
    for c in range(q):
        # Singular symplectic multiplier: image in standard isotropic Lagrangian.
        if c in (0,F.neg[1]):
            B=[[int(i==j and i<n) for i in range(m)] for j in range(m)]
        else:
            mu=F.times(c,F.plus(c,1))
            B=[[((1 if j<n else mu) if i==j else 0) for i in range(m)] for j in range(m)]
        cols=[]
        for j in range(m):
            v=[F.plus(B[j][i],c if i==j else 0) for i in range(m)]
            v.append((2*j+1)%q if q!=4 else ((j+1)%4))
            cols.append(tuple(v))
        cols.append((0,)*m+(c,))
        assert is_rb(cols,n,F)
    print(f'EXAMPLES q={q} n={n}: all central scalars checked')



def square_zero(cols,F):
    d=len(cols)
    for j in range(d):
        for i in range(d):
            acc=0
            for k in range(d): acc=F.plus(acc,F.times(cols[j][k],cols[k][i]))
            if acc!=0:return False
    return True


def mat_rank(cols,F):
    d=len(cols)
    rows=[[cols[j][i] for j in range(d)] for i in range(d)]
    rank=0
    for col in range(d):
        pivot=next((r for r in range(rank,d) if rows[r][col]),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        inv=next(t for t in range(1,F.q) if F.times(t,rows[rank][col])==1)
        rows[rank]=[F.times(v,inv) for v in rows[rank]]
        for r in range(d):
            if r==rank:continue
            fac=rows[r][col]
            if fac:rows[r]=[F.minus(rows[r][j],F.times(fac,rows[rank][j])) for j in range(d)]
        rank+=1
        if rank==d:break
    return rank


def expected_poly(n,q):
    # This implementation evaluates the closed rank distribution; brute force
    # below does not use this formula when selecting operators.
    counts=[0]*(n+2)
    for r in range(n+1):
        surj=1
        for i in range(r):surj*=q**(2*n-r)-q**i
        factor=span_iso_count(n,r,q)*surj
        counts[r]+=factor*q**r
        counts[r+1]+=factor*(q**(2*n-r)-q**r)
    return counts


def exhaustive_full_square(n,q):
    F=Field(q);d=2*n+1
    counts=[0]*(n+2)
    for entries in product(range(q),repeat=d*d):
        cols=[entries[i*d:(i+1)*d] for i in range(d)]
        if square_zero(cols,F) and is_rb(cols,n,F):
            rk=mat_rank(cols,F)
            assert rk<len(counts)
            counts[rk]+=1
    exp=expected_poly(n,q)
    assert counts==exp,(n,q,counts,exp)
    print(f'FULL_SQUARE n={n} q={q} rank_counts={counts}')


def exhaustive_reduced_square(n,q):
    F=Field(q);m=2*n;d=m+1
    counts=[0]*(n+2)
    raw=0
    # Every square-zero RB preserves the central line and kills its generator;
    # enumerate every horizontal matrix and all possible central coefficients.
    for entries in product(range(q),repeat=m*m):
        base=[tuple(entries[j*m:(j+1)*m]) for j in range(m)]
        cols=[tuple(base[j])+(0,) for j in range(m)]+[(0,)*d]
        if not square_zero(cols,F) or not is_rb(cols,n,F):continue
        raw+=1
        for phis in product(range(q),repeat=m):
            full=[base[j]+(phis[j],) for j in range(m)]+[(0,)*d]
            if square_zero(full,F) and is_rb(full,n,F):
                counts[mat_rank(full,F)]+=1
    exp=expected_poly(n,q)
    assert counts==exp,(n,q,counts,exp)
    print(f'REDUCED_SQUARE n={n} q={q} tested_horizontal={q**(m*m)} basic_valid={raw} rank_counts={counts}')


if __name__=='__main__':
    for q in (2,3,4): exhaustive_full_square(1,q)
    exhaustive_reduced_square(2,2)
    print('VERIFY_OK')
