"""Independent enumeration of finite commuting-permutation structures and Euler products.
Usage: python check_orbits.py
No external packages.
"""
from itertools import permutations
from collections import Counter
from math import gcd


def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))

def canonical_transitive(p,q):
    # For a transitive commuting action, BFS from a basepoint is independent
    # of the basepoint and gives a canonical enumeration by positive words.
    n=len(p); nodes=[0]; loc={0:0}
    for x in nodes:
        for y in (p[x],q[x]):
            if y not in loc:
                loc[y]=len(nodes);nodes.append(y)
    if len(nodes)!=n:return None
    return (tuple(loc[p[x]] for x in nodes),tuple(loc[q[x]] for x in nodes))


def canonical_action(p,q):
    n=len(p); unseen=set(range(n)); comps=[]
    while unseen:
        root=min(unseen); stack=[root]; orb={root}
        for x in stack:
            for y in (p[x],q[x]):
                if y not in orb:orb.add(y);stack.append(y)
        unseen-=orb
        loc={x:i for i,x in enumerate(sorted(orb))}
        subp=tuple(loc[p[x]] for x in sorted(orb));subq=tuple(loc[q[x]] for x in sorted(orb))
        comps.append(canonical_transitive(subp,subq))
    return tuple(sorted(comps))


def sigma1(n): return sum(d for d in range(1,n+1) if n%d==0)

def polys(nmax,k=None):
    # k=None: unlimited orbit multiplicities / actual isomorphism types.
    # k integer: representative is truncated at k copies per orbit type.
    cur=[1]+[0]*nmax
    for h in range(1,nmax+1):
        for copy in range(sigma1(h)):
            vals=[0]*(nmax+1)
            for v in range(nmax+1):
                if not cur[v]:continue
                maxadd=((nmax-v)//h if k is None else min(k,(nmax-v)//h))
                for j in range(maxadd+1): vals[v+j*h]+=cur[v]
            cur=vals
    return cur


def main():
    classes=[1]; transitive=[0]
    for n in range(1,7):
        perms=list(permutations(range(n)))
        c=set();t=set();tot=0
        for p in perms:
            for q in perms:
                if compose(p,q)!=compose(q,p):continue
                tot+=1
                canonical=canonical_action(p,q)
                c.add(canonical)
                if len(canonical)==1:t.add(canonical)
        assert len(t)==sigma1(n),(n,len(t),sigma1(n))
        classes.append(len(c)); transitive.append(len(t))
        print('n=%d commuting pairs=%d transitive types=%d all isomorphism types=%d' %
              (n,tot,len(t),len(c)))
    expected=polys(6)
    assert classes==expected,(classes,expected)
    print('all isomorphism-type counts agree with lattice Euler product: PASS')
    for k in (1,2,3):
        coeff=polys(12,k)
        print('k=%d canonical minimum-size counts (n=0..12):'%k,coeff)
        assert coeff[0]==1 and coeff[1]==1
    assert polys(6,1)[1:]==[1,3,7,14,28,58],polys(6,1)
    print('subgroup-count and truncated-spectrum polynomial checks: PASS')
if __name__=='__main__':main()
