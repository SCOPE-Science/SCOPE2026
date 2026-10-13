#!/usr/bin/env python3
"""Exact finite checks for one-bit finite bimodal staircases; Python 3 stdlib."""
from itertools import product


def canonical(elements):
    table={}
    return tuple(table.setdefault(x,len(table)) for x in elements)


def refine(n):
    # Enumerate maximal depth-t modal theories by finite partition refinement.
    x=tuple(int(i<=j) for i in range(n) for j in range(n))
    profiles=[]
    for t in range(n):
        row=tuple(frozenset(x[i*n+j] for j in range(n)) for i in range(n))
        col=tuple(frozenset(x[i*n+j] for i in range(n)) for j in range(n))
        profiles.append((x,row,col))
        lo_r=t//2+1
        hi_r=(t+1)//2
        lo_c=(t+1)//2
        hi_c=t//2+1
        def sameclasses(xs):
            return {frozenset(i for i in range(n) if xs[i]==x) for x in xs}
        expected_rows={frozenset({i}) for i in list(range(lo_r))+list(range(n-hi_r,n))}
        if lo_r<n-hi_r:expected_rows.add(frozenset(range(lo_r,n-hi_r)))
        expected_cols={frozenset({i}) for i in list(range(lo_c))+list(range(n-hi_c,n))}
        if lo_c<n-hi_c:expected_cols.add(frozenset(range(lo_c,n-hi_c)))
        assert sameclasses(row)==expected_rows,(n,t,'row')
        assert sameclasses(col)==expected_cols,(n,t,'col')
        expect=(t+1)**2+1 if t<=n-2 else n*n
        assert len(set(x))==expect,(n,t,len(set(x)),expect)
        x=canonical(tuple((x[i*n+j],row[i],col[j]) for i in range(n) for j in range(n)))
    assert len(set(x))==n*n
    return profiles


def directly_defined_atoms(n):
    # Build ALL depth-bounded Boolean-definable subsets via the Boolean closure
    # of the two boxes of ALL unions of previously definable atoms.
    # This independent evaluator DOES NOT use bisimulation refinement.
    cells=list(product(range(n),repeat=2))
    full=(1<<(n*n))-1
    prop=sum((1<<k) for k,(i,j) in enumerate(cells) if i<=j)
    atoms=[prop, full ^prop]
    assert sum(atom.bit_count() for atom in atoms)==n*n
    populations=[]
    for t in range(n):
        populations.append(len(atoms))
        assert len(atoms)==((t+1)**2+1 if t<=n-2 else n*n)
        if t==n-1: break
        def box(mask,axis):
            ans=0
            for k,(i,j) in enumerate(cells):
                positions=(i*n+l for l in range(n)) if axis==0 else (l*n+j for l in range(n))
                if all(mask & (1<<v) for v in positions):ans|=(1<<k)
            return ans
        signatures=[0]*(n*n)
        for number,atom in enumerate(atoms):
            for k in range(n*n):
                if atom&(1<<k):signatures[k] |= 1<<number
        bit=len(atoms)
        for select in range(1<<len(atoms)):
            union=0
            for i,a in enumerate(atoms):
                if select&(1<<i):union|=a
            for axis in (0,1):
                result=box(union,axis)
                for k in range(n*n):
                    if result&(1<<k):signatures[k] |=1<<bit
                bit+=1
        classes={}
        for k,s in enumerate(signatures):classes[s]=classes.get(s,0)|(1<<k)
        atoms=list(classes.values())
        assert sum(atom.bit_count() for atom in atoms)==n*n
    return populations


def explicit_generator(n):
    # Independent evaluation of recursive row and column singleton selectors.
    cells=list(product(range(1,n+1),repeat=2))
    universe=set(cells)
    p={(i,j) for i,j in cells if i<=j}
    def box_row(a):return {(i,j) for i,j in cells if all((i,k) in a for k in range(1,n+1))}
    def box_col(a):return {(i,j) for i,j in cells if all((k,j) in a for k in range(1,n+1))}
    R={0:set()}; C={0:set()}
    for k in range(1,n+1):
        R[k]=box_row(p|C[k-1])
        C[k]=box_col((universe-p)|R[k])
        assert R[k]=={(i,j) for i,j in cells if i<=k}
        assert C[k]=={(i,j) for i,j in cells if j<=k}
    for i,j in cells:
        assert ((R[i]-R[i-1]) & (C[j]-C[j-1]))=={(i,j)}


def main():
    n_checks=0; round_checks=0; direct_checks=0
    for n in range(2,61):
        profiles=refine(n)
        n_checks+=1;round_checks+=len(profiles)
    for n in range(1,31):
        explicit_generator(n)
    for n in range(2,5):
        result=directly_defined_atoms(n)
        assert result==[((t+1)**2+1 if t<=n-2 else n*n) for t in range(n)]
        direct_checks+=sum(1<<(((t+1)**2+1) if t<=n-2 else n*n) for t in range(n-1))
    print('VERIFY_OK staircase_sizes='+str(n_checks)+' modal_depth_levels='+str(round_checks)
          +' row_column_selector_sizes=30 direct_boolean_unions='+str(direct_checks)
          +' Boolean_modal_algebra_cases=3')
if __name__=='__main__': main()
