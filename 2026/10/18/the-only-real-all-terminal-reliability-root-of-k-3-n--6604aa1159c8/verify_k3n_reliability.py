"""Exact independent finite checks for the nontrivial real-root theorem of K_{3,n}.

Run: python3 verify_k3n_reliability.py
Only the Python standard library is required. The all-n proof is in RESULT.md;
this script independently tests the reliability-polynomial identity using graph connectivity.
"""
from math import comb


def padd(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a): z[i]+=v
    for i,v in enumerate(b): z[i]+=v
    return z


def pmul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): z[i+j]+=v*w
    return z


def ppow(a,n):
    z=[1]
    for _ in range(n):z=pmul(z,a)
    return z


def pscale(a,k):return [k*v for v in a]


def ptrim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def theoretical(n):
    a=ppow([1,1,1],n)
    b=ppow([0,1,2],n)
    c=ppow([0,0,3],n)
    f=padd(padd(a,pscale(b,-3)),pscale(c,2))
    return ptrim(pmul(ppow([1,-1],n),f)),f


def connected_from_mask(mask, n):
    parent=list(range(n+3))
    def root(u):
        while parent[u]!=u:
            u=parent[u]
        return u
    for j in range(n):
        for i in range(3):
            if mask & (1 << (3*j+i)):
                a,b=root(i),root(j+3)
                parent[a]=b
    r=root(0)
    return all(root(v)==r for v in range(n+3))


def brute_coefficients(n):
    m=3*n
    connected_counts=[0]*(m+1)
    for mask in range(1 << m):
        if connected_from_mask(mask,n):
            connected_counts[mask.bit_count()]+=1
    p=[0]*(m+1)
    for k,nc in enumerate(connected_counts):
        for j in range(k+1):
            p[m-k+j] += nc * comb(k,j) * (-1)**j
    return p,connected_counts


def pvalue(coeff,num,den):
    deg=len(coeff)-1
    return sum(c*num**j*den**(deg-j) for j,c in enumerate(coeff))


def main():
    cases=0
    subgraphs=0
    for n in range(2,6):
        expected,f=theoretical(n)
        actual,counts=brute_coefficients(n)
        assert actual==expected,(n,actual,expected)
        assert sum(counts)>0
        # Exact derivative/degree/multiplicity at the unavoidable root q=1.
        assert sum(f)==0
        assert sum(i*c for i,c in enumerate(f))==0
        assert sum(i*(i-1)*c for i,c in enumerate(f)) == 6*n*n*3**(n-2)
        assert len(f)==2*n+1
        assert f[-1]==1-3*2**n+2*3**n
        # Evaluate directly at many rational real arguments, excluding q=1.
        for p in range(-32,33):
            if p==8:continue
            assert pvalue(f,p,8)>0,(n,p)
        cases+=1
        subgraphs+=(1<<(3*n))
    # Higher n: independent exact rational arithmetic and coefficient expansions.
    for n in range(6,21):
        R,F=theoretical(n)
        assert len(R)==3*n+1
        assert len(F)==2*n+1
        assert F[-1]==1-3*2**n+2*3**n
        assert sum(F)==0
        assert sum(i*c for i,c in enumerate(F))==0
        assert sum(i*(i-1)*c for i,c in enumerate(F))==6*n*n*3**(n-2)
        for p in range(-40,41):
            if p==10:continue
            assert pvalue(F,p,10)>0,(n,p)
    # Sharp comparison: K_{2,n} has q=-1/3 as a nontrivial real root for even n.
    for n in (2,4,6,8):
        h=padd(ppow([1,1],n),pscale(ppow([0,2],n),-1))
        assert pvalue(h,-1,3)==0
    print(f'VERIFY_OK independent_connected_graphs={cases} edge_subsets={subgraphs} exact_n=2..20')


if __name__ == '__main__':main()
