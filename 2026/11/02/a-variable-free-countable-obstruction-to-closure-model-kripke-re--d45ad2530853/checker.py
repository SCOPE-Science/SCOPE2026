"""Finite-prefix reproducibility for a countable closure-semantics example.
The mathematical proof does not depend on this program.
"""
from dataclasses import dataclass
from random import Random

# (prefix of all exceptional natural-number worlds, eventual value on N,
#  value at the additional world z)
@dataclass(frozen=True)
class Sig:
    prefix: tuple
    tail: bool
    root: bool
    def at(self, n):
        return self.prefix[n] if n < len(self.prefix) else self.tail

BOT = ("bot",)
TOP = ("top",)

def neg(t): return ("not",t)
def box(t): return ("box",t)
def imp(t,u): return ("imp",t,u)
def itbox(k,t):
    for _ in range(k): t=box(t)
    return t

def evaluate(t):
    tag=t[0]
    if tag=='bot': return Sig((),False,False)
    if tag=='top': return Sig((),True,True)
    if tag=='not':
        s=evaluate(t[1]);return Sig(tuple(not v for v in s.prefix),not s.tail,not s.root)
    if tag=='imp':
        a,b=evaluate(t[1]),evaluate(t[2]);cut=max(len(a.prefix),len(b.prefix))
        return Sig(tuple((not a.at(n)) or b.at(n) for n in range(cut)),
                   (not a.tail) or b.tail,(not a.root) or b.root)
    if tag=='box':
        s=evaluate(t[1]); cut=max(1,len(s.prefix)+1)
        p=(True,)+tuple(s.at(0) and s.at(n-1) for n in range(1,cut))
        return Sig(p,s.at(0) and s.tail,s.tail)
    raise ValueError(tag)

def conj(a,b): return neg(imp(a,neg(b)))

def delta(n):return conj(itbox(n+1,BOT),neg(itbox(n,BOT)))
def chi(n):return neg(delta(n))

def test():
    # Explicit infinitely-indexed witnesses, checked at many finite depths.
    for n in range(101):
        d=evaluate(delta(n));c=evaluate(chi(n))
        assert d.root is False and d.tail is False
        assert c.root is True and c.tail is True
        assert d.at(n) and not c.at(n)
        assert sum(d.at(i) for i in range(150))==1
        assert all(c.at(i) for i in range(150) if i!=n)
    t=neg(box(chi(0)));s=evaluate(t)
    assert s.root is False and s.at(0) is False and s.tail is True
    assert all(s.at(i) for i in range(1,150))
    assert evaluate(box(BOT)).root is False
    # Every Boolean/modal formula is eventually constant along N,
    # so every finite list of tested inner formulas has a common successor.
    rng=Random(10379)
    def random_term(depth):
        if depth==0:return TOP if rng.randrange(2) else BOT
        v=rng.randrange(4)
        if v==0:return TOP
        if v==1:return neg(random_term(depth-1))
        if v==2:return box(random_term(depth-1))
        return imp(random_term(depth-1),random_term(depth-1))
    ts=[random_term(6) for _ in range(1000)] + [chi(n) for n in range(21)]+[t]
    S=[evaluate(t) for t in ts]
    cutoff=max(len(s.prefix) for s in S)
    for sig in S: assert sig.at(cutoff)==sig.tail
    for j in range(0,len(S),20):
        local=S[j:j+20]
        n=max(len(s.prefix) for s in local)
        assert all(s.at(n)==s.tail for s in local)
    print('ALL_CHECKS_OK')
    print('point witnesses=101; random modal terms=1000; finite blocks=52')
    print('max tested common tail index=',cutoff)

if __name__=='__main__': test()
