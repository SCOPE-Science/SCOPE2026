#!/usr/bin/env python3
"""Checks an exact edge open packing theorem against the original definition.
Run: python3 verify_eop_tree.py (Python 3.9+, standard library only).
The finite tests verify specified base cases and recurrence identities, not
unbounded validity, which follows from the supplied mathematical proof.
"""
from math import comb


def rooted_edges(b,h):
    next_id=1
    level=[(0,0)]  # vertex,depth
    edges=[]
    while level:
        nxt=[]
        for u,d in level:
            if d==h: continue
            for unused in range(b):
                v=next_id
                next_id+=1
                edges.append((u,v,d))
                nxt.append((v,d+1))
        level=nxt
    return edges


def original_conflict(e,f,edges):
    if e==f: return False
    e_end=set(edges[e][:2]);f_end=set(edges[f][:2])
    return any(g!=e and g!=f and u in e_end and v in f_end or
               g!=e and g!=f and v in e_end and u in f_end
               for g,(u,v,d) in enumerate(edges))


def exact_brute(b,h):
    ed=rooted_edges(b,h)
    m=len(ed)
    conflict=[0]*m
    for i in range(m):
        for j in range(i):
            if original_conflict(i,j,ed):
                conflict[i] |= 1<<j
                conflict[j] |= 1<<i
    n=1<<m
    valid=bytearray(n)
    valid[0]=1
    best=-1;count=0;chosen=-1
    for mask in range(n):
        if mask:
            low=mask&-mask
            i=low.bit_length()-1
            rest=mask ^ low
            valid[mask]=valid[rest] and not (conflict[i] & rest)
        if valid[mask]:
            k=mask.bit_count()
            if k>best:best=k;count=1;chosen=mask
            elif k==best:count+=1
    selected_levels={h-1-3*j for j in range((h+2)//3) if h-1-3*j>=0}
    expected=sum(1<<i for i,(_,_,d) in enumerate(ed) if d in selected_levels)
    assert best==expected.bit_count()==sum(b**(h-3*j) for j in range((h+2)//3) if h-3*j>=1)
    assert count==1 and chosen==expected
    return m,n,best,count


def dp_table(b,H):
    # State (x,j): parent edge selected x, j chosen child edges, excluding
    # the parent edge from objective. Multiplicity truncated to 2.
    D={(0,0):(0,1),(1,0):(0,1)}
    for h in range(1,H+1):
        T={}
        for x in (0,1):
            for j in range(b+1):
                degree=x+j
                if degree==0:
                    vals=[(v,c) for (xx,jj),(v,c) in D.items() if xx==0]
                    m0=max(v for v,c in vals)
                    c0=min(2,sum(c for v,c in vals if v==m0))
                else:
                    m0,c0=D[(0,0)]
                if j:
                    vals=[(v,c) for (xx,jj),(v,c) in D.items()
                          if xx==1 and (degree-1)*jj==0]
                    m1=max(v for v,c in vals)
                    c1=min(2,sum(c for v,c in vals if v==m1))
                else:m1,c1=0,1
                val=j+j*m1+(b-j)*m0
                cnt=min(2,comb(b,j)*c1**j*c0**(b-j))
                T[(x,j)]=(val,cnt)
        D=T
        A=sum(b**(h-3*t) for t in range((h+2)//3) if h-3*t>=1)
        for x in (0,1):
            for j in range(b+1):
                if h%3==1:formula=A-b+j
                elif h%3==2:
                    if x==0 and j==0:formula=A
                    elif x==0 and j==1:formula=A-(b*b-b-1)
                    else:formula=A-b*b+j
                else:
                    if x==0 and j==0:formula=A
                    elif x==0 and j==1:formula=A-(b*b-b-1)
                    else:formula=A-j*(b*b-1)
                assert D[(x,j)][0]==formula,(b,h,x,j,D[(x,j)],formula)
        largest=max(v for (x,j),(v,c) in D.items() if x==0)
        count=min(2,sum(c for (x,j),(v,c) in D.items() if x==0 and v==largest))
        assert largest==A and count==1,(b,h,largest,count,A)
    return True


def main():
    checks=[(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,1)]
    total=0
    for b,h in checks:
        m,n,value,count=exact_brute(b,h)
        total+=n
        print('BRUTE_OK',b,h,'edges',m,'subsets',n,'optimum',value,'count',count)
    for b in range(2,11):
        assert dp_table(b,18)
    print('CERTIFICATE_OK','brute_cases',len(checks),'subsets',total,'DP_instances',9*18,
          'all_boundary_states_and_uniqueness=PASS')

if __name__=='__main__':main()
