"""Exact arithmetic checks for near-diameter tails of equilateral Johnson networks.
Scientific calculation only; no publication-priority or independent audit claim.
"""
from itertools import combinations
from fractions import Fraction as F
from math import comb

def edges(n,k):
    all_=set(range(n))
    out=[]
    for core in combinations(range(n),k-1):
        S=frozenset(core)
        for a,b in combinations(sorted(all_-S),2):
            out.append((S|{a},S|{b}))
    return out

def cross(e,f,k):
    return [[k-len(set(u)&set(v)) for v in f] for u in e]

def tail_area(matrix,cutoff):
    # area of {(x,y) in [0,1]^2: all endpoint-path routes>cutoff}.
    poly=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
    for i in (0,1):
      for j in (0,1):
        a=1 if i==0 else -1
        b=1 if j==0 else -1
        c=F(matrix[i][j]+(i==1)+(j==1))-cutoff
        if not poly:return F(0)
        nxt=[]
        for p,q in zip(poly,poly[1:]+poly[:1]):
          vp=a*p[0]+b*p[1]+c
          vq=a*q[0]+b*q[1]+c
          if vp>=0:nxt.append(p)
          if (vp<0 and vq>0) or (vp>0 and vq<0):
            t=vp/(vp-vq)
            nxt.append((p[0]+t*(q[0]-p[0]), p[1]+t*(q[1]-p[1])))
        poly=nxt
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1])))/2 if len(poly)>=3 else F(0)

def verify_case(n,k,eps):
    """Exact polygon intersection integral over a complete edge-orbit."""
    ee=edges(n,k)
    M=len(ee)
    assert M==comb(n,k)*k*(n-k)//2
    e=ee[0]
    D=F(k)+(F(1,2) if n==2*k+1 else F(1))
    acc=F(0)
    one_low=0; two_lows_rowcol=0
    for f in ee:
        if f==e:
            continue  # A same-edge distance is <=1, below the near-diameter threshold.
        mat=cross(e,f,k)
        acc+=tail_area(mat,D-eps)
        count_low=sum(x<=k-1 for row in mat for x in row)
        if count_low==1 and sorted(x for row in mat for x in row)==[k-1,k,k,k]:
            one_low+=1
        if count_low==2:
            lows={(i,j) for i in range(2) for j in range(2) if mat[i][j]==k-1}
            if len({i for i,j in lows})==1 or len({j for i,j in lows})==1:
                two_lows_rowcol+=1
    observed=acc/M
    if n==2*k+1:
        expected=F(2*k,M)*(eps+(k-1)*eps**2)
        assert one_low==2*k,(n,k,one_low)
        assert two_lows_rowcol==2*k*(k-1),(n,k,two_lows_rowcol)
    else:
        expected=F(2*comb(n-k-1,k+1),comb(n,k+1))*eps**2
    assert observed==expected,(n,k,eps,observed,expected)
    print(f'PASS J({n},{k}) epsilon={eps}: exact pair-integrated tail {observed}')

if __name__=='__main__':
    # The theorem applies to k>=3. Smaller cases provide external consistency checks.
    for n,k in [(3,1),(5,2),(6,2),(7,3),(8,3),(9,3),(9,4),(10,4)]:
        for eps in (F(1,20),F(1,10),F(2,5)):
            verify_case(n,k,eps)
    print('ALL EXACT RATIONAL CASES PASSED')
