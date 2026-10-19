"""Exact independent checks for ear locations in uniform polygon triangulations.

Run: python verify_ears.py
Only the Python standard library is required.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, cos, pi, isclose


def cat(m):
    assert m >= 0
    return comb(2*m, m)//(m+1)


def edge(i,j):
    return (min(i,j),max(i,j))


@lru_cache(None)
def triangulations(vertices):
    if len(vertices)<=3:
        return (frozenset(),)
    a,b=vertices[0],vertices[-1]
    ans=[]
    for i in range(1,len(vertices)-1):
        v=vertices[i]
        left=vertices[:i+1]
        right=vertices[i:]
        forced=set()
        if i>1:forced.add(edge(a,v))
        if i<len(vertices)-2:forced.add(edge(v,b))
        for l in triangulations(left):
            for r in triangulations(right):
                ans.append(frozenset(forced|l|r))
    assert len(ans)==len(set(ans))
    return tuple(ans)


def ear_mask(t,n):
    incident=0
    for i,j in t:
        incident|=(1<<i)|(1<<j)
    return ((1<<n)-1)^incident


def independent(mask,n):
    return not (mask & (((mask<<1)|(mask>>(n-1)))&((1<<n)-1)))


def moments_by_enumeration(n):
    tr=triangulations(tuple(range(n)))
    assert len(tr)==cat(n-2)
    f=[0]*(1<<n)
    for t in tr:
        assert len(t)==n-3
        mask=ear_mask(t,n)
        assert independent(mask,n)
        f[mask]+=1
    # Superset zeta transform of ear masks, independent of theoretical formula.
    z=f.copy()
    for bit in range(n):
        for mask in range(1<<n):
            if not mask&(1<<bit):z[mask]+=z[mask|(1<<bit)]
    count=0
    for mask in range(1<<n):
        k=mask.bit_count()
        expected=cat(n-k-2) if independent(mask,n) else 0
        assert z[mask]==expected,(n,mask,z[mask],expected)
        count+=1
    return count,len(tr),f,z


def exact_covariance(n):
    p=Fraction(cat(n-3),cat(n-2))
    q=Fraction(cat(n-4),cat(n-2))
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:row.append(p-p*p)
            elif (i-j)%n in(1,n-1):row.append(-p*p)
            else:row.append(q-p*p)
        matrix.append(row)
    return matrix,p,q


def rational_rank(matrix):
    a=[x.copy() for x in matrix]
    nr=len(a);nc=len(a[0]);i=0
    for j in range(nc):
        k=next((k for k in range(i,nr) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        f=a[i][j]
        a[i]=[x/f for x in a[i]]
        for k in range(nr):
            if k!=i:
                f=a[k][j]
                if f:a[k]=[x-f*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==nr:break
    return i


def local_moment(n,k):
    return Fraction(cat(n-k-2),cat(n-2))


def assert_spectrum(n,matrix,p,q):
    constant=p+(n-3)*q-n*p*p
    assert sum(matrix[0])==constant
    if n>=5:
        assert constant==Fraction((n-5)*(n-4)*(n-1),2*(2*n-7)*(2*n-5)**2)
        assert q-p*p==Fraction(3*(n-1),4*(2*n-7)*(2*n-5)**2)
    for j in range(1,n):
        ev=float(p-q)-2*float(q)*cos(2*pi*j/n)
        for i in range(n):
            x=sum(float(matrix[i][h])*cos(2*pi*j*h/n) for h in range(n))
            y=ev*cos(2*pi*j*i/n)
            assert isclose(x,y,abs_tol=2e-12,rel_tol=2e-12)
        assert (abs(ev)<1e-12 if n==4 and j%2 else ev>0),(n,j,ev)
    expected=1 if n==4 else (n-1 if n==5 else n)
    assert rational_rank(matrix)==expected,(n,rational_rank(matrix),expected)
    if n>=6:assert constant>0
    else:assert constant==0
    return n


def local_limit_exact(m):
    # For each fixed set of observation sites, probability of all indicated
    # ears converges to (1/4)^k unless a neighboring pair is selected.
    # Independently verify that these are the moments of the fair-bit 01-process.
    z=[0]*(1<<m)
    for bits in range(1<<(m+1)):
        marks=0
        for i in range(m):
            if (bits>>i)&1==0 and (bits>>(i+1))&1:marks|=(1<<i)
        z[marks]+=1
    checks=0
    for s in range(1<<m):
        count=sum(z[mask] for mask in range(1<<m) if mask&s==s)
        expected=Fraction(0) if s&(s<<1) else Fraction(1,4**s.bit_count())
        assert Fraction(count,2**(m+1))==expected
        checks+=1
    return checks


def main():
    checked_subsets=0;tot_triangulations=0;rank_cases=0
    for n in range(4,12):
        ct,num,f,z=moments_by_enumeration(n)
        checked_subsets+=ct;tot_triangulations+=num
        mat,p,q=exact_covariance(n)
        for i in range(n):
            for j in range(n):
                cov=Fraction(z[(1<<i)|(1<<j)],num)-Fraction(z[1<<i],num)*Fraction(z[1<<j],num)
                assert cov==mat[i][j]
        assert_spectrum(n,mat,p,q)
        rank_cases+=1
    assert local_limit_exact(8)==256
    for k in range(1,8):
        vals=[local_moment(n,k) for n in (30,100,1000) if n>=2*k]
        assert abs(float(vals[-1])-4.0**(-k))<abs(float(vals[0])-4.0**(-k))
    print('PASS exact triangulations',tot_triangulations)
    print('PASS all joint ear-event sets',checked_subsets)
    print('PASS covariance entries, Fourier eigenvectors and exact ranks',rank_cases)
    print('PASS independent fair-bit local-moment model',256)
    print('PASS Catalan-ratio convergence samples',7)


if __name__=='__main__':main()
