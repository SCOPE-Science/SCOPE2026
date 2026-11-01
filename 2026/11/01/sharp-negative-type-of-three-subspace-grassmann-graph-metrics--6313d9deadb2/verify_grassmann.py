#!/usr/bin/env python3
"""Independent exact/finite checks of Grassmann 3-space distance spectra."""
import itertools
import math
from fractions import Fraction


def qint(q, r):
    return (q**r-1)//(q-1)


def qbinom(q, n, k):
    num = math.prod(q**(n-i)-1 for i in range(k))
    den = math.prod(q**(k-i)-1 for i in range(k))
    assert num % den == 0
    return num//den


def rows(q,n):
    k=3
    b=[q**(2*i+1)*qint(q,k-i)*qint(q,n-k-i) for i in range(k)]+[0]
    c=[0]+[qint(q,i)**2 for i in range(1,k+1)]
    a=[b[0]-b[i]-c[i] for i in range(k+1)]
    out=[]
    for j in range(k+1):
        t=b[0]-qint(q,j)*qint(q,n-j+1)
        arr=[Fraction(1),Fraction(t)]
        for i in range(1,k):
            arr.append((t*arr[i]-a[i]*arr[i]-b[i-1]*arr[i-1])/c[i+1])
        assert sum(arr)==(qbinom(q,n,3) if j==0 else 0)
        out.append(tuple(arr))
    return out,b,a,c


def formulas(q,n):
    X=qint(q,n-5)
    R=q*q+q+1
    j1=(Fraction(1), Fraction(q**3*(q+1)*X+q**3+q**2-1),
        Fraction(q**2*(q*X+1)*(q**4*X-q**2-2*q-1),q+1),
        Fraction(-q**6*X*(q*X+1),q+1))
    j2=(1,q**3*X-(q+1),q-q**3*(q+1)*X,q**4*X)
    j3=(1,-R,q*R,-q**3)
    return [j1,j2,j3]


def fval(q,n,p):
    X=qint(q,n-5)
    return q**3*X*(1-(q+1)*2**p+q*3**p)-(q+1)+q*2**p


def cutoff(q,n):
    lo,hi=0.,1.
    for _ in range(80):
        mid=(lo+hi)/2
        if fval(q,n,mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def rref_3spaces_f2_n6():
    n=6
    out=[]
    for piv in itertools.combinations(range(n),3):
        free=[(i,j) for i in range(3) for j in range(piv[i]+1,n) if j not in piv]
        for mask in range(1<<len(free)):
            basis=[1<<p for p in piv]
            for k,(i,j) in enumerate(free):
                if mask>>k&1:basis[i]|=1<<j
            sub=frozenset(a*basis[0]^b*basis[1]^c*basis[2]
                          for a,b,c in itertools.product((0,1),repeat=3))
            out.append(sub)
    assert len(out)==1395 and len(set(out))==1395
    return out


def sample_direct_f2():
    spaces=rref_3spaces_f2_n6()
    n=len(spaces)
    shells=[[] for _ in range(4)]
    # Row-shell distances computed directly from all subspace intersections.
    for j,W in enumerate(spaces):
        k=len(spaces[0]&W)
        dist=3-(k.bit_length()-1)
        shells[dist].append(j)
    assert [len(x) for x in shells]==[1,98,784,512]
    adjacency=[[] for _ in range(n)]
    for i in range(n):
        U=spaces[i]
        for j in range(i+1,n):
            if len(U&spaces[j])==4:
                adjacency[i].append(j)
                adjacency[j].append(i)
    assert all(len(row)==98 for row in adjacency)
    P,b,a,c=rows(2,6)
    for j in [0,2,17,55,319,728,1394]:
        for dist in range(1,4):
            candidate=next(i for i in range(n) if 3-(len(spaces[j]&spaces[i]).bit_length()-1)==dist)
            hist=[0]*4
            for z in adjacency[candidate]:
                t=3-(len(spaces[j]&spaces[z]).bit_length()-1)
                hist[t]+=1
            assert hist[dist-1]==c[dist]
            assert hist[dist]==a[dist]
            if dist<3:
                assert hist[dist+1]==b[dist]
    # Independently compare subspace-intersection distance with graph BFS.
    from collections import deque
    for source in [0,219,1007]:
        graphdist=[-1]*n
        graphdist[source]=0
        queue=deque([source])
        while queue:
            u=queue.popleft()
            for v in adjacency[u]:
                if graphdist[v]<0:
                    graphdist[v]=graphdist[u]+1
                    queue.append(v)
        for v in range(n):
            assert graphdist[v]==3-(len(spaces[source]&spaces[v]).bit_length()-1)
    # Check adjacency minimal polynomial on four independent integer vectors.
    theta=[int(x[1]) for x in P]
    def mv(vec):return [sum(vec[j] for j in nbr) for nbr in adjacency]
    for seed in range(4):
        z=[((i*37+seed*19)**3)%17-8 for i in range(n)]
        for t in theta:
            v=mv(z)
            z=[x-t*y for x,y in zip(v,z)]
        assert not any(z)
    return len(adjacency),sum(map(len,adjacency))//2


def run():
    checks=0
    for q in [2,3,4,5,7,9,11]:
        for n in range(6,13 if q<=4 else 10):
            P,b,a,c=rows(q,n)
            expected=formulas(q,n)
            for j in range(3): assert P[j+1]==tuple(map(Fraction,expected[j]))
            m=[qbinom(q,n,j)-(qbinom(q,n,j-1) if j>0 else 0) for j in range(4)]
            assert sum(m)==qbinom(q,n,3)
            assert all(t>0 for t in m)
            p=cutoff(q,n)
            # Local bracketing of the unique obstruction and remaining modes.
            assert 0<p<1
            assert fval(q,n,max(0,p-1e-5))<1e-7
            assert fval(q,n,min(1,p+1e-5))>-1e-7
            for z in [0,p/3,p, (p+1)/2,1.]:
                f=[sum(float(P[j][i])*(i**z) for i in range(1,4)) for j in range(1,4)]
                assert f[0]<0 and f[2]<0
                assert abs(f[1]-fval(q,n,z))<=1e-7*max(1,abs(fval(q,n,z)))
            checks+=1
    n,edges=sample_direct_f2()
    print('ALGEBRAIC_PARAMETER_CASES_OK',checks)
    print('INDEPENDENT_BINARY_SUBSPACE_GRAPH_OK',n,edges)
    print('BINARY_6_3_CUTOFF',format(cutoff(2,6),'.12f'))
    print('ALL_CHECKS_OK')

if __name__=='__main__':run()
