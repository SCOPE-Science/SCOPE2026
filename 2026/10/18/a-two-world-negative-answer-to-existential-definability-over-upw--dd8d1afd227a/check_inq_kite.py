"""Finite semantic checks for the two-world inquisitive-neighborhood separation.
Run with: python check_inq_kite.py
The unbounded separation follows from the induction in RESULT.md, not testing.
"""
from itertools import product

# Terms are ('p',), ('bot',), (unary, subterm), or (binary, left, right).
A = ('p',)
BOT = ('bot',)
def AND(a,b): return ('and',a,b)
def INQ(a,b): return ('inq',a,b)
def IMP(a,b): return ('imp',a,b)
def E(a): return ('E',a)
def NEG(a): return IMP(a,BOT)
TOP = NEG(BOT)
QUESTION = INQ(A,NEG(A))
TARGET = ('yield',TOP,QUESTION)

worlds=(0,1)
neighborhoods={0:(frozenset([0]),frozenset([0,1])),
               1:(frozenset([1]),frozenset([0,1]))}

def support(term,state,valuation,ns=neighborhoods):
    op=term[0]
    if op=='p':return all(valuation[w] for w in state)
    if op=='bot':return len(state)==0
    if op=='and':return support(term[1],state,valuation,ns) and support(term[2],state,valuation,ns)
    if op=='inq':return support(term[1],state,valuation,ns) or support(term[2],state,valuation,ns)
    if op=='imp':
        return all(not support(term[1],s,valuation,ns) or support(term[2],s,valuation,ns)
                   for bits in product([0,1],repeat=len(state))
                   for s in [frozenset(w for w,bit in zip(sorted(state),bits) if bit)])
    if op=='E':
        return all(any(support(term[1],t,valuation,ns) for t in ns[w]) for w in state)
    if op=='yield':
        return all(all((not support(term[1],t,valuation,ns) or support(term[2],t,valuation,ns))
                       for t in ns[w]) for w in state)
    raise AssertionError(op)

assert support(TARGET,frozenset([0]),(True,True))
assert not support(TARGET,frozenset([0]),(True,False))
assert support(QUESTION,frozenset([0]),(True,False))
assert not support(QUESTION,frozenset([0,1]),(True,False))

# Closure under formation. Full testing of every generated formula through size 6.
terms=[A,BOT]
levels={1:terms}
checks=0
for size in range(2,7):
    new=[]
    new.extend(E(t) for t in levels.get(size-1,[]))
    for i in range(1,size-1):
        for t in levels.get(i,[]):
            for u in levels.get(size-1-i,[]):
                new.extend((AND(t,u),INQ(t,u),IMP(t,u)))
    levels[size]=new
    for term in new:
        for valuation in ((False,False),(True,True),(True,False),(False,True)):
            for w in worlds:
                if valuation[w]:
                    v2=list(valuation); v2[1-w]=not v2[1-w]
                    assert support(term,frozenset([w]),valuation)==support(term,frozenset([w]),tuple(v2))
                    checks+=1
                # Local modal identity for every term.
                assert support(E(term),frozenset([w]),valuation)==support(term,frozenset([w]),valuation)
                checks+=1

# For singleton universe, full reduction of the yields connective to E and implication.
ONE={0:(frozenset([0]),)}
ZERO={0:()}
for ns in (ONE,ZERO):
    for bit in (False,True):
        val=(bit,)
        for size_a in range(1,5):
            for size_b in range(1,5):
                for a in levels[size_a][:30]:
                    for b in levels[size_b][:30]:
                        lhs=support(('yield',a,b),frozenset([0]),val,ns)
                        rhs=support(INQ(NEG(E(TOP)),IMP(a,b)),frozenset([0]),val,ns)
                        assert lhs==rhs
                        checks+=1
print('PASS: two-world strict-conditional separation, kite singleton-locality, one-world reduction; checks:',checks)
