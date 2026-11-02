#!/usr/bin/env python3
"""Finite cross-check of the exact same-world relational representation census.

Inputs are finite Kripke models (the finite-world normal closure semantic case
has the same truth algebra), independently compared with every alternate relation.
"""
from itertools import product
from random import Random

def refine(edges, atom_bits, n):
    # Partition refinement by modal depth. Any distinction terminates on finite W.
    C = list(atom_bits)
    while True:
        signatures = [(C[i], frozenset(C[j] for j in edges[i])) for i in range(n)]
        keys = {a:k for k,a in enumerate(sorted(set(signatures), key=repr))}
        D = [keys[a] for a in signatures]
        if all((C[i]==C[j])==(D[i]==D[j]) for i in range(n) for j in range(n)):
            return D
        C = D

def edge_lists(mask,n):
    return [tuple(j for j in range(n) if mask >> (i*n+j)&1) for i in range(n)]

def same_modal_theories(e1,e2,atom_bits,n):
    # Independent reference test: refine the disjoint union of both models.
    N=2*n
    E=[tuple(j for j in e1[i]) for i in range(n)] + [tuple(n+j for j in e2[i]) for i in range(n)]
    colors = atom_bits+atom_bits
    sig = list(colors)
    for _ in range(N+2):
        raw = [(sig[i], tuple(sorted({sig[j] for j in E[i]}))) for i in range(N)]
        uniq = {k:t for t,k in enumerate(sorted(set(raw),key=repr))}
        new = [uniq[x] for x in raw]
        if new == sig: break
        sig=new
    return all(sig[i]==sig[n+i] for i in range(n))

def predicted(e,colors,n):
    types = refine(e,colors,n)
    groups = {}
    for v,t in enumerate(types): groups.setdefault(t,[]).append(v)
    out = 1; emin=0; emax=0
    for i in range(n):
        kinds = {types[v] for v in e[i]}
        emin += len(kinds)
        for t in kinds:
            z=len(groups[t]); out *= 2**z-1; emax += z
    return out,emin,emax

def check(n,initial_masks,valuations):
    for val in valuations:
        colors=[bool((val>>i)&1) for i in range(n)]
        for mask in initial_masks:
            e=edge_lists(mask,n)
            predicted_count, lo,hi=predicted(e,colors,n)
            if n<=3:
                real=sum(same_modal_theories(e,edge_lists(a,n),colors,n) for a in range(1<<(n*n)))
                assert predicted_count==real,(n,val,mask,predicted_count,real)
            else:
                # When n=4 the predicted count can be independently enumerated by
                # rowwise compatible successor sets over the modal type classes.
                typ=refine(e,colors,n)
                rows=[]
                for i in range(n):
                    required={typ[j] for j in e[i]}
                    choices=[]
                    for subset in range(1<<n):
                        observed={typ[j] for j in range(n) if subset>>j&1}
                        if observed==required: choices.append(subset)
                    rows.append(choices)
                assert predicted_count==__import__('math').prod(len(x) for x in rows)
                # Compare a deterministic sample of candidate models both inside
                # and outside the rowwise predicted class by joint refinement.
                rng=Random(mask*31+val)
                for _ in range(256):
                    candidate=[rng.randrange(1<<n) for i in range(n)]
                    ec=[tuple(j for j in range(n) if candidate[i]>>j&1) for i in range(n)]
                    expected=all(candidate[i] in rows[i] for i in range(n))
                    observed=same_modal_theories(e,ec,colors,n)
                    assert expected==observed,(n,val,mask,candidate,expected,observed)
    return len(initial_masks)*len(valuations)

if __name__=='__main__':
    rng=Random(4151)
    cases3=check(3,list(range(1<<9)),[0,1,3,5,7])
    cases4=check(4,[0,(1<<16)-1]+rng.sample(range(1<<16),24),[0,1,3,5,7,10,15])
    # Dedicated 3-world model with one singleton atomic type and a duplicate pair.
    E=[(1,), (1,), (1,)]
    assert predicted(E,[True,False,False],3)==(27,3,6)
    print(f'ALL_CHECKS_OK baseline_models={cases3+cases4} all_alternatives_3world={cases3*512} sampled_alternatives_4world={cases4*256} toy_census=27')
