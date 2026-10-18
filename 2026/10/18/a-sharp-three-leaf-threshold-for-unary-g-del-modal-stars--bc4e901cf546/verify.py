"""Supplementary finite tests of crisp Gödel-modal star compression (stdlib only)."""
from fractions import Fraction
from itertools import product
from random import Random

Q = tuple(Fraction(i,4) for i in range(5))

def impl(a,b): return Fraction(1) if a<=b else b

def unary_terms():
    # Enumerate all distinct positive-depth-zero leaf interpretations, including modal constants.
    zero = (Fraction(0),)*len(Q); one=(Fraction(1),)*len(Q)
    fs={zero,one,Q}
    while True:
        old=len(fs); values=list(fs)
        for f in values:
            for g in values:
                fs.add(tuple(min(a,b) for a,b in zip(f,g)))
                fs.add(tuple(max(a,b) for a,b in zip(f,g)))
                fs.add(tuple(impl(a,b) for a,b in zip(f,g)))
        if len(fs)==old: break
    return sorted(fs)

def reps(xs):
    r=([Fraction(0)] if Fraction(0) in xs else [])
    pos=[x for x in xs if x>0]
    if pos:
        r.append(min(pos))
        if max(pos)!=min(pos):r.append(max(pos))
    return tuple(r)

def check_core(fs):
    checked=0
    for n in range(1,6):
        for xs in product(Q,repeat=n):
            ys=reps(xs)
            assert 1<=len(ys)<=3
            for f in fs:
                ox=[f[Q.index(x)] for x in xs]
                oy=[f[Q.index(y)] for y in ys]
                assert min(ox)==min(oy) and max(ox)==max(oy),(n,xs,ys,f)
                checked+=1
    return checked

def neg(x):return impl(x,Fraction(0))

def sep_one(xs):
    return impl(max(xs),min(xs))

def sep_two(xs):
    bp=min(xs); dp=max(xs)
    box_disj=min(max(v,neg(v)) for v in xs)
    return impl(neg(bp),impl(dp,box_disj))

def check_sep():
    assert all(sep_one(xs)==1 for xs in product(Q,repeat=1))
    assert sep_one((Fraction(0),Fraction(1)))==0
    assert all(sep_two(xs)==1 for xs in product(Q,repeat=2))
    assert sep_two((Fraction(0),Fraction(1,4),Fraction(3,4)))==Fraction(1,4)
    return (5,25,3)

# Explicit Gödel-modal syntax trees; full nested formula values, not just one-step operators.
B='B';D='D';AND='and';OR='or';IMP='imp'
def ev(f, idx, root, leaf):
    tag=f[0]
    if tag=='p':return root if idx==-1 else leaf[idx]
    if tag=='bot':return Fraction(0)
    if tag in (B,D):
        if idx!=-1:return Fraction(1) if tag==B else Fraction(0)
        vals=[ev(f[1],i,root,leaf) for i in range(len(leaf))]
        return min(vals) if tag==B else max(vals)
    a=ev(f[1],idx,root,leaf);b=ev(f[2],idx,root,leaf)
    return min(a,b) if tag==AND else max(a,b) if tag==OR else impl(a,b)

def random_form(rng, depth):
    if depth==0:return ('p',) if rng.randrange(2) else ('bot',)
    tag=rng.choice([B,D,AND,OR,IMP])
    if tag in (B,D):return (tag,random_form(rng,depth-1))
    return (tag,random_form(rng,depth-1),random_form(rng,depth-1))

def check_nested():
    rng=Random(41391)
    checked=0
    for n in range(1,9):
        for _ in range(500):
            vals=tuple(rng.choice(Q) for _ in range(n));root=rng.choice(Q)
            core=reps(vals)
            f=random_form(rng,rng.randrange(1,8))
            assert ev(f,-1,root,vals)==ev(f,-1,root,core),(n,vals,core,f)
            checked+=1
    return checked

if __name__=='__main__':
    fs=unary_terms()
    print('distinct_unary_leaf_term_functions',len(fs))
    print('all_term_vectors',[[str(x) for x in f] for f in fs])
    print('exhaustive_unary_extremum_comparisons',check_core(fs))
    print('separation_checks',check_sep())
    print('nested_formula_comparisons',check_nested())
    print('VERIFY_OK')
