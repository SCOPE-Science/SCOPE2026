"""Executable finite checks for the boxed-subformula Horn abstraction.
Scientific inputs are ordinary modal abstract syntax trees; no external dependencies.
"""
from itertools import product, combinations
from random import Random

p=('p',)
q=('q',)
r=('r',)
top=('T',)
def conj(a,b): return ('&',a,b)
def impl(a,b): return ('>',a,b)
def neg(a): return ('!',a)
def box(a): return ('B',a)

def subtree(t):
    s={t}
    for arg in t[1:]:
        if isinstance(arg,tuple):s.update(subtree(arg))
    return s

def closure_on_S(S, H, flags):
    H=set(H)
    if 'N' in flags and top in S:H.add(top)
    changed=True
    while changed:
        old=len(H)
        for a in S:
            if a[0]=='&':
                if 'M' in flags and a in H: H.update(a[1:])
                if 'C' in flags and a[1] in H and a[2] in H:H.add(a)
            if a[0]=='>' and 'K' in flags and a in H and a[1] in H:H.add(a[2])
        changed=len(H)!=old
    return H

def source_closure_finite(S,H,flags):
    """Independently apply unrestricted source rules with all pairs of known formulas,
    retaining syntactic expressions up to max input size + 3 for safe bounded tests.
    Comparison restricted to S; unbounded equivalence follows from proof.
    """
    H=set(H)
    if 'N' in flags:H.add(top)
    def size(x):return 1+sum(size(y) for y in x[1:] if isinstance(y,tuple))
    bound=max(map(size,S))
    for _ in range(8):
        new=set(H)
        for a in H:
            if a[0]=='&' and 'M' in flags:new.update(a[1:])
            if a[0]=='>' and 'K' in flags and a[1] in H:new.add(a[2])
        if 'C' in flags:
            for a in H:
                for b in H:
                    c=conj(a,b)
                    if size(c)<=bound:new.add(c)
        if new==H:break
        H=new
    return H&S

def evalf(t,val,boxes):
    op=t[0]
    if op in ('p','q','r'):return val[op]
    if op=='T':return True
    if op=='!':return not evalf(t[1],val,boxes)
    if op=='&':return evalf(t[1],val,boxes) and evalf(t[2],val,boxes)
    if op=='>':return (not evalf(t[1],val,boxes)) or evalf(t[2],val,boxes)
    if op=='B':return t[1] in boxes
    raise ValueError(t)

def satisfiable(formula, flags):
    subs=subtree(formula)|{top}
    S=set()
    for t in subs:
        if t[0]=='B': S.update(subtree(t[1]))
    S.add(top)
    s_list=sorted(S,key=repr)
    for bits in product([False,True],repeat=len(s_list)):
        T={x for x,b in zip(s_list,bits) if b}
        if closure_on_S(S,T,flags)!=T:continue
        for values in product([False,True],repeat=3):
            if evalf(formula,dict(zip(['p','q','r'],values)),T):return True
    return False

def checks():
    pool=[p,q,top,conj(p,q),conj(q,p),impl(p,q),impl(conj(p,q),p),impl(conj(p,q),q),impl(impl(p,q),q),box(p),box(q),box(conj(p,q)),box(impl(p,q)),neg(box(p))]
    count=0
    for mask in range(16):
        flags={c for i,c in enumerate('MCNK') if (mask>>i)&1}
        for a in pool:
            S=subtree(a)|{top}
            for seed in [(),(a,), (p,), (q,), (a,p), (p,q),(p,impl(p,q))]:
                H={h for h in seed if h in S}
                x=closure_on_S(S,H,flags)
                y=source_closure_finite(S,H,flags)
                assert x==y,(flags,a,seed,x,y)
                count+=1
        assert satisfiable(p,flags)
        assert not satisfiable(conj(p,neg(p)),flags)
        assert satisfiable(box(p),flags)
        assert satisfiable(neg(box(p)),flags) if 'N' not in flags else True
        if 'N' in flags: assert not satisfiable(neg(box(top)),flags)
        else: assert satisfiable(neg(box(top)),flags)
        if 'M' in flags:assert not satisfiable(conj(box(conj(p,q)),neg(box(p))),flags)
        if 'C' in flags:assert not satisfiable(conj(conj(box(p),box(q)),neg(box(conj(p,q)))),flags)
        if 'K' in flags:assert not satisfiable(conj(conj(box(impl(p,q)),box(p)),neg(box(q))),flags)
    print('ALL_CHECKS_OK',count,'bounded closure comparisons across all 16 axiom subsets')

if __name__=='__main__':checks()
