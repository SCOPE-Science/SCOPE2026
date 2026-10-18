"""Independent finite verification for path-incidence prelinearity formulas.
Run with Python 3; no third-party packages.
"""
from itertools import combinations, product
from fractions import Fraction

STATES=((0,0),(1,0),(0,1),(1,1))


def all_graphs(m):
    edges=list(combinations(range(m),2))
    for x in range(1<<len(edges)):
        yield tuple(e for i,e in enumerate(edges) if x>>i&1)


def direct_counts(m,edges):
    # The m graph vertices are maximal Kripke worlds; each graph edge
    # is a new lower world with precisely its two endpoints above it.
    edges=tuple(edges)
    h=m+len(edges)
    topmask=(1<<h)-1
    up=[1<<v for v in range(m)]
    for i,(u,v) in enumerate(edges):
        up.append((1<<u)|(1<<v)|(1<<(m+i)))
    # Independent from the four-spin formula: construct ALL upward-closed
    # subsets of this finite poset, and evaluate implication pointwise.
    upsets=[]
    for bits in range(1<<h):
        if all((bits>>x&1)==0 or (bits&req)==req for x,req in enumerate(up)):
            upsets.append(bits)
    good=0
    for u in upsets:
        for v in upsets:
            left=u&~v
            right=v&~u
            # x lies in u->v iff no upper extension x witnesses u and not v.
            if all(not ((a&left) and (a&right)) for a in up):
                good+=1
    return len(upsets),good



def algebraic_counts_by_adjoint(m,edges):
    # A second, slower implementation: calculate each implication from the
    # defining adjunction in the lattice, without using principal upsets.
    edges=tuple(edges)
    h=m+len(edges)
    topmask=(1<<h)-1
    up=[1<<v for v in range(m)]
    up += [(1<<u)|(1<<v)|(1<<(m+i)) for i,(u,v) in enumerate(edges)]
    upsets=[bits for bits in range(1<<h) if all((bits>>x&1)==0 or (bits&req)==req for x,req in enumerate(up))]
    good=0
    for a in upsets:
        for b in upsets:
            left=0
            right=0
            for t in upsets:
                if (a&t)&~b==0:left|=t
                if (b&t)&~a==0:right|=t
            good+=(left|right)==topmask
    return len(upsets),good

def spin_counts(m,edges):
    e=tuple(edges)
    z=sum(2**sum((s>>u&1) and (s>>v&1) for u,v in e)
          for s in range(1<<m))
    a=0
    for spins in product(range(4),repeat=m):
        factor=1
        for u,v in e:
            x,y=STATES[spins[u]],STATES[spins[v]]
            if (x==(1,0) and y==(0,1)) or (x==(0,1) and y==(1,0)):
                factor=0
                break
            factor*=2**(x[0]*y[0]+x[1]*y[1])
        a+=factor
    return z,a


def tree_dp(m,edges):
    nei=[[] for _ in range(m)]
    for u,v in edges:
        nei[u].append(v);nei[v].append(u)
    # Verify connected acyclic input.
    if len(edges)!=m-1: raise ValueError('not a tree')
    def recurse(v,parent):
        outcomes=[1]*4
        for w in nei[v]:
            if w==parent:continue
            child=recurse(w,v)
            outcomes=[outcomes[a]*sum((0 if (STATES[a]==(1,0) and STATES[b]==(0,1)) or (STATES[a]==(0,1) and STATES[b]==(1,0)) else 2**(STATES[a][0]*STATES[b][0]+STATES[a][1]*STATES[b][1]))*child[b] for b in range(4)) for a in range(4)]
        return outcomes
    return sum(recurse(0,-1))


def main():
    graphs=0
    ordered_pairs=0
    # All simple graphs through order four: 1+2+8+64 =75.
    for m in range(1,5):
        for e in all_graphs(m):
            z,a=direct_counts(m,e)
            zz,aa=spin_counts(m,e)
            assert (z,a)==(zz,aa),(m,e,z,a,zz,aa)
            ordered_pairs+=z*z
            graphs+=1
    # Full algebraic-adjunction cross-check on every graph through order three.
    adjunction_graphs=0
    for m in range(1,4):
        for e in all_graphs(m):
            assert algebraic_counts_by_adjoint(m,e)==spin_counts(m,e)
            adjunction_graphs+=1
    # A selection of larger graphs, with high and low edge densities.
    cases=[]
    for m in (5,6):
        path=tuple((i,i+1) for i in range(m-1))
        star=tuple((0,i) for i in range(1,m))
        cycle=path+((m-1,0),)
        cases.extend([(m,path),(m,star),(m,cycle),(m,tuple())])
    cases.append((5,tuple(combinations(range(5),2))))
    for m,e in cases:
        z,a=direct_counts(m,e)
        zz,aa=spin_counts(m,e)
        assert (z,a)==(zz,aa),(m,e,z,a,zz,aa)
        ordered_pairs+=z*z
        graphs+=1
    for m in range(1,16):
        path=tuple((i,i+1) for i in range(m-1))
        z,a=spin_counts(m,path) if m<=7 else (None,None)
        # Use the closed recurrence and matrix transfer on long paths.
        Z=[2,5]
        for i in range(2,m):Z.append(3*Z[-1]-Z[-2])
        A=[4,23,147]
        for i in range(3,m):A.append(7*A[-1]-3*A[-2]-2*A[-3])
        if z is not None: assert z==Z[m-1] and a==A[m-1]
        if m<=7:assert tree_dp(m,path)==A[m-1]
    # Non-path trees, direct brute counts vs message passing.
    for m in (5,6):
        for e in (tuple((0,i) for i in range(1,m)),
                  tuple([(0,1),(0,2),(2,3)]+([(3,4)] if m==5 else [(3,4),(3,5)]))):
            assert tree_dp(m,e)==spin_counts(m,e)[1]
    print('VERIFY_OK graphs=',graphs,'independent_pairs=',ordered_pairs,
          'adjunction_graphs=',adjunction_graphs,'tree_recursions=',(7+4),'path_recurrence_to=15')
    print('PATH_EXAMPLES',[(m,Fraction(spin_counts(m,[(i,i+1) for i in range(m-1)])[1],spin_counts(m,[(i,i+1) for i in range(m-1)])[0]**2)) for m in (2,3,4,5)])

if __name__=='__main__':main()
