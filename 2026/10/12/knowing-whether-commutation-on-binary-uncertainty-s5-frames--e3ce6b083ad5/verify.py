#!/usr/bin/env python3
"""Independent finite checks for the two-sparse knowing-whether commutation theorem."""
from fractions import Fraction
from math import factorial


def matching_partitions(n):
    """All partitions into blocks of size at most two, exactly once."""
    if n == 0:
        yield ()
        return
    def recurse(rem):
        if not rem:
            yield ()
            return
        a = rem[0]
        for rest in recurse(rem[1:]):
            yield ((a,),) + rest
        for j in range(1,len(rem)):
            b=rem[j]
            for rest in recurse(rem[1:j]+rem[j+1:]):
                yield ((a,b),) + rest
    yield from recurse(tuple(range(n)))


def delta(part, mask):
    ans=0
    for block in part:
        bit=sum(1<<i for i in block)
        if not (mask & bit) or mask & bit == bit:
            ans |= bit
    return ans


def predicted(part1,part2,n):
    # Component decomposition of the equivalence-relation join.
    edges=[]
    for part in (part1,part2):
        edges.append({frozenset(b) for b in part if len(b)==2})
    graph=[set() for _ in range(n)]
    for color in range(2):
        for edge in edges[color]:
            a,b=tuple(edge)
            graph[a].add(b)
            graph[b].add(a)
    visited=set()
    for u in range(n):
        if u in visited:continue
        comp={u};front=[u]
        while front:
            x=front.pop()
            for y in graph[x]-comp:
                comp.add(y);front.append(y)
        visited|=comp
        e1={edge for edge in edges[0] if edge <= comp}
        e2={edge for edge in edges[1] if edge <= comp}
        if len(comp)==1:
            assert not e1 and not e2
        elif len(comp)==2:
            if len(e1|e2)!=1:return False
        elif len(comp)==4:
            if not (len(e1)==len(e2)==2 and not e1&e2):return False
        else:
            return False
    return True


def count_formula(n):
    # Independent coefficient extraction for exp(z + (3/2) z^2 + z^4/4).
    acc=Fraction(0)
    for b in range(n//2+1):
        for c in range(n//4+1):
            a=n-2*b-4*c
            if a>=0:
                acc+=Fraction(3,2)**b *Fraction(1,4)**c / (factorial(a)*factorial(b)*factorial(c))
    out=acc*factorial(n)
    assert out.denominator==1
    return out.numerator


def main():
    for n in range(1,8):
        p=list(matching_partitions(n))
        accepted=0
        tested=0
        for i,a in enumerate(p):
            for j,b in enumerate(p):
                # n=7 exhaustive too: 53,824 pairs * 128 valuations.
                condition=predicted(a,b,n)
                direct=all(delta(a,delta(b,x))==delta(b,delta(a,x))
                           for x in range(1<<n))
                if condition!=direct:
                    raise AssertionError(('counterexample',n,a,b,condition,direct))
                accepted+=int(direct)
                tested+=1
        expected=count_formula(n)
        assert accepted==expected,(n,accepted,expected)
        print('n=%d matchings=%d ordered_pairs=%d commuting=%d formula=%d'
              %(n,len(p),tested,accepted,expected))
    print('VERIFY_OK')

if __name__=='__main__':main()
