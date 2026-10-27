"""Reproduce exact-degree spherical-harmonic ranks on normalized F4 root directions.
Only standard Python is needed; arithmetic is exact (fractions)."""
from itertools import combinations, product
from fractions import Fraction

def roots():
    long=[]
    for i,j in combinations(range(4),2):
        for a,b in product((-1,1), repeat=2):
            x=[0]*4;x[i]=a;x[j]=b;long.append(tuple(x))
    short=[]
    for i in range(4):
        for a in (-1,1):
            x=[0]*4;x[i]=2*a;short.append(tuple(x))
    short.extend(product((-1,1),repeat=4))
    # long roots are divided by sqrt(2), short roots by 2
    keep=lambda x:next(a for a in x if a!=0)>0
    P=[x for x in long if keep(x)] + [x for x in short if keep(x)]
    assert len(P)==24
    return P

P=roots()

def u(l,i,j):
    t=sum(a*b for a,b in zip(P[i],P[j]))
    if (i<12)==(j<12):
        denom=2 if i<12 else 4
        if t==denom:val=l+1
        elif t==-denom:val=(-1)**l*(l+1)
        elif t==0:val=(1,0,-1,0)[l%4]
        else:
            assert abs(t)*2==denom,(i,j,t)
            val=(1,1,0,-1,-1,0)[l%6]
            if t<0 and l%2:val=-val
        # for odd degree use congruence diag(1^12,sqrt(2)^12)
        if l%2 and i>=12:val*=2
    else:
        if t==0:val=(1,0,-1,0)[l%4]
        else:
            assert abs(t)==2,(i,j,t)
            # U_l(1/sqrt2): 1,sqrt2,1,0,-1,-sqrt2,-1,0
            # for odd degree multiply by sqrt2 due congruence
            val=((1,2,1,0,-1,-2,-1,0) if l%2 else (1,0,1,0,-1,0,-1,0))[l%8]
            if t<0 and l%2:val=-val
    return int(val)

def gram(l):return [[u(l,i,j) for j in range(24)] for i in range(24)]

def rank_q(matrix):
    a=[[Fraction(x) for x in row] for row in matrix]
    rows=len(a); cols=len(a[0]); r=0
    for c in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        p=a[r][c]
        for i in range(r+1,rows):
            if a[i][c]:
                mul=a[i][c]/p
                for j in range(c+1,cols):a[i][j]-=mul*a[r][j]
                a[i][c]=0
        r+=1
        if r==rows:break
    return r

if __name__=='__main__':
    import time
    tic=time.monotonic()
    rr=[]
    for l in range(24):
        M=gram(l)
        assert all(M[i][j]==M[j][i] for i in range(24) for j in range(24))
        rr.append(rank_q(M))
    print('base_ranks_0_to_23=',rr)
    print('elapsed',time.monotonic()-tic)
    EXPECT=(1,4,9,16,13,20,19,24,23,20,22,24,24,24,23,24,23,24,24,24,24,24,23,24)
    assert tuple(rr)==EXPECT
    # For l>=24: 24-periodic values of U_l(t) on distinct projective lines,
    # and exact diagonal U_l(1)=l+1 imply H_{l+24}=H_l+24I.
    # H_l is PSD by the spherical harmonic addition theorem, hence all l>=24 full rank.
    for l in range(24):
        M=gram(l); Q=gram(l+24)
        # for odd degrees the Gram matrices are congruence scaled, so diagonal increments are (24,48).
        assert all(Q[i][j]-M[i][j]==(24 if i==j and (l%2==0 or i<12) else 48 if i==j else 0)
            for i in range(24) for j in range(24))
    print('period_shift_valid=TRUE')

# Each pair below is (eigenvalue, multiplicity) for the 24-line evaluation Gram.
# The zero eigenvalue is included when present.
SPECTRA = {
 0:((0,23),(24,1)), 1:((0,20),(12,4)), 2:((0,15),(8,9)),
 3:((0,8),(6,16)), 4:((0,11),(8,9),(12,4)),
 5:((0,4),(6,16),(12,4)), 6:((0,5),(8,18),(24,1)),
 7:((6,16),(12,8)), 8:((0,1),(8,18),(12,4),(24,1)),
 9:((0,4),(12,20)), 10:((0,2),(8,9),(12,4),(16,9)),
 11:((12,24),), 12:((8,9),(12,4),(16,9),(24,2)),
 13:((12,20),(24,4)), 14:((0,1),(12,4),(16,18),(24,1)),
 15:((12,8),(18,16)), 16:((0,1),(16,18),(24,5)),
 17:((12,4),(18,16),(24,4)), 18:((12,4),(16,9),(24,11)),
 19:((18,16),(24,8)), 20:((16,9),(24,15)),
 21:((12,4),(24,20)), 22:((0,1),(24,23)), 23:((24,24),)
}

def similar_rational(l):
    """Integral matrix similar to the real Gram H_l (not merely congruent).

    For odd l, cross-root entries in H_l have a sqrt(2) factor.
    G=diag(I_12,sqrt(2)I_12)*H_l*diag(I_12,sqrt(2)I_12)
    is the Gram returned by gram(l). Divide the last 12 rows of G by 2:
    this is diag(I_12,1/sqrt(2)I_12)*H_l*diag(I_12,sqrt(2)I_12).
    """
    M=gram(l)
    if l%2:
        for i in range(12,24):
            assert all(v%2==0 for v in M[i])
            M[i]=[v//2 for v in M[i]]
    return M

def times(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b: C[i][j]+=a*b
    return C

def verify_full_spectra():
    """An exact finite characteristic-polynomial certificate via Newton power sums.

    For a 24x24 matrix, traces of powers 1..24 determine its characteristic
    polynomial (Newton's identities). The expected traces on the right are
    the power sums of the asserted 24 roots, with multiplicities. All
    computations are over the integers, with no eigenvalue approximation.
    """
    for l,levels in SPECTRA.items():
        assert sum(m for _,m in levels)==24
        M=similar_rational(l)
        Q=[row[:] for row in M]
        for k in range(1,25):
            observed=sum(Q[i][i] for i in range(24))
            expected=sum(m*v**k for v,m in levels)
            assert observed==expected,(l,k,observed,expected)
            if k<24:Q=times(Q,M)
    return True

if __name__=='__main__':
    print('integer_power_sum_certificates=',verify_full_spectra())
