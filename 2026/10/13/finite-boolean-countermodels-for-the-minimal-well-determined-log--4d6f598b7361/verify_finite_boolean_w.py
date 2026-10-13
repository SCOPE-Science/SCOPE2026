"""Finite Boolean separation for the minimal well-determined logic.

All computations use exact finite sets/integers. Run: python verify_finite_boolean_w.py
"""
from functools import lru_cache
from itertools import product
from random import Random

# Formula ASTs: ('p',name), ('m',left,right), ('i',left,right)

@lru_cache(None)
def blocks(formula):
    if formula[0] == 'm':
        return blocks(formula[1]) | blocks(formula[2])
    return frozenset((formula,))

@lru_cache(None)
def theorem(formula):
    tag = formula[0]
    if tag == 'p':
        return False
    if tag == 'm':
        return theorem(formula[1]) and theorem(formula[2])
    a,b = formula[1:]
    return all(theorem(c) or c in blocks(a) for c in blocks(b))

@lru_cache(None)
def subformulas(f):
    return frozenset((f,)) if f[0] == 'p' else frozenset((f,)) | subformulas(f[1]) | subformulas(f[2])

def atom_set(f):
    return frozenset(g for g in subformulas(f) if g[0] != 'm' and not theorem(g))

def canonical_test(f):
    atoms = atom_set(f)
    top = atoms
    def evaluate(g):
        if g[0] == 'p':
            return top - {g}
        if g[0] == 'm':
            return evaluate(g[1]) & evaluate(g[2])
        a,b=evaluate(g[1]), evaluate(g[2])
        # Fallback mu(g)= top \\ {g} when g is non-theorem.
        return top if a <= b else top - {g} if g in atoms else top
    for g in subformulas(f):
        wanted=top - frozenset(t for t in blocks(g) if not theorem(t))
        actual=evaluate(g)
        assert actual == wanted, (f,g,actual,wanted)
    assert (evaluate(f)==top)==theorem(f)
    return len(atoms),int(not theorem(f))

# Independently check the implication order test and valuation recursion.
def truth_test(f,carrier,variable_values,mu):
    top=carrier[-1]
    values={}
    def run(g):
        if g in values:return values[g]
        if g[0]=='p': ans=variable_values[g[1]]
        elif g[0]=='m':ans=run(g[1]) & run(g[2])
        else:
            a,b=run(g[1]),run(g[2])
            ans=top if a & b == a else mu.get(g,top)
        values[g]=ans
        return ans
    return run(f)

def generated(max_leaves=5):
    by_n={1:{('p','p'),('p','q')}}
    for n in range(2,max_leaves+1):
        s=set()
        for i in range(1,n):
            for a,b in product(by_n[i],by_n[n-i]):
                s.add(('m',a,b));s.add(('i',a,b))
        by_n[n]=s
    return by_n

if __name__=='__main__':
    counts={}; nonths=0; largest=0
    for n,forms in generated(5).items():
        counts[n]=len(forms)
        for f in forms:
            size,is_no=canonical_test(f)
            nonths+=is_no
            largest=max(largest,size)
    assert counts=={1:2,2:8,3:64,4:640,5:7168},counts

    rng=Random(260715664)
    atoms=[('p',k) for k in 'pqr']
    random_forms=[]
    for _ in range(5000):
        f=rng.choice(atoms)
        for _ in range(rng.randrange(1,16)):
            other=rng.choice(atoms)
            f=(rng.choice(('m','i')),f,other) if rng.randrange(2) else (rng.choice(('m','i')),other,f)
        random_forms.append(f)
        canonical_test(f)

    # Independent exhaustive semantic checks on the 2-element powerset algebra,
    # with every variable and each syntactically distinct fallback assigned arbitrarily.
    semantics_cases=0
    short=list(generated(3)[3])
    for f in short:
        impl=[g for g in subformulas(f) if g[0]=='i']
        for vp,vq in product(range(2),repeat=2):
            for mus in product(range(2),repeat=len(impl)):
                result=truth_test(f,[0,1],{'p':vp,'q':vq},dict(zip(impl,mus)))
                if theorem(f):assert result==1,(f,vp,vq,mus)
                semantics_cases+=1
    # A two-element carrier cannot separate every non-theorem; the 3-chain can.
    p=('p','p');q=('p','q')
    inner=('i',p,q);middle=('i',inner,p);outer=('i',p,middle)
    assert not theorem(outer)
    chain3=truth_test(outer,[0,1,2],{'p':1,'q':0},{inner:2,middle:0,outer:0})
    assert chain3==0
    for pv,qv in product((0,1),repeat=2):
        for mi,mm,mo in product((0,1),repeat=3):
            assert truth_test(outer,[0,1],{'p':pv,'q':qv},{inner:mi,middle:mm,outer:mo})==1
    print('EXACT PASS')
    print('all_distinct_binary_formulas_by_leaf_count',sorted(counts.items()))
    print('canonical_checks',sum(counts.values())+len(random_forms))
    print('max_nontheorem_atoms_in_exhaustive',largest)
    print('two_element_semantic_cases',semantics_cases)
    print('formula_nontheorems_in_exhaustive',nonths)
    print('two_element_separation_failure_3_chain_counterexample','PASS')
