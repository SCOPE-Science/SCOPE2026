"""Finite exhaustive checks of Nash and coalition-blocker formulas.
This tests small cases only; the written proof establishes arbitrary orders.
"""
from itertools import product, combinations
from math import factorial, gcd
from functools import reduce


def partitions(n):
    parts=[[0]]
    def rec(i):
        if i==n:
            yield tuple(tuple(q) for q in parts)
            return
        for p in parts:
            p.append(i)
            yield from rec(i+1)
            p.pop()
        parts.append([i])
        yield from rec(i+1)
        parts.pop()
    yield from rec(1)


def types_for(sizes):
    return sum(([j]*x for j,x in enumerate(sizes)),[])


def score(i,coal,types,enemy):
    friends=sum(types[j]!=types[i] for j in coal if j!=i)
    enemies=sum(types[j]==types[i] for j in coal if j!=i) if enemy else 0
    return friends,-enemies


def actual_nash(part,types,enemy):
    for bi,block in enumerate(part):
        for i in block:
            baseline=score(i,block,types,enemy)
            if score(i,(i,),types,enemy)>baseline: return False
            for bj,other in enumerate(part):
                if bi!=bj and score(i,other+(i,),types,enemy)>baseline:
                    return False
    return True


def predicted_nash(part,sizes,types):
    r=len(part)
    if any(s%r for s in sizes):return False
    req=tuple(s//r for s in sizes)
    return all(tuple(sum(types[i]==j for i in block) for j in range(len(sizes)))==req for block in part)


def predicted_count(sizes):
    g=reduce(gcd,sizes)
    numer=1
    for s in sizes:numer*=factorial(s)
    result=0
    for r in range(1,g+1):
        if g%r:continue
        denom=factorial(r)
        for s in sizes:denom*=factorial(s//r)**r
        result+=numer//denom
    return result


def smallest_blocker(part,types,enemy,weak):
    base={i:score(i,block,types,enemy) for block in part for i in block}
    n=len(types)
    for k in range(1,n+1):
        for s in combinations(range(n),k):
            comps=[(score(i,s,types,enemy),base[i]) for i in s]
            if weak:
                blocking=all(x>=y for x,y in comps) and any(x>y for x,y in comps)
            else:
                blocking=all(x>y for x,y in comps)
            if blocking:return k
    return None


def main():
    tests=0;stable=0;blocker_checks=0;profiles=0
    for t in range(2,5):
        for sizes in product(range(1,4),repeat=t):
            n=sum(sizes)
            if n>9:continue
            profiles+=1
            types=types_for(sizes)
            for enemy in (False,True):
                found=0
                for part in partitions(n):
                    tests+=1
                    calc=actual_nash(part,types,enemy)
                    pred=predicted_nash(part,sizes,types)
                    assert calc==pred,('nash',sizes,enemy,part,calc,pred)
                    if calc:
                        stable+=1;found+=1
                        if n<=7:
                            r=len(part); s=n//r
                            expected_core=None if r==1 else s+2
                            expected_strict=None if r==1 else s+(2 if enemy else 1)
                            assert smallest_blocker(part,types,enemy,False)==expected_core,('core',sizes,enemy,part)
                            assert smallest_blocker(part,types,enemy,True)==expected_strict,('strictcore',sizes,enemy,part)
                            blocker_checks+=2
                assert found==predicted_count(sizes),('count',sizes,enemy,found,predicted_count(sizes))
    print('PASS',profiles,'type-size profiles;',tests,'set partitions;',stable,'Nash instances;',blocker_checks,'blocking minima')
    print('Examples: [2,2,2] ->',predicted_count((2,2,2)),'; [3,3,3] ->',predicted_count((3,3,3)),'; [2,2,2,2] ->',predicted_count((2,2,2,2)))

if __name__=='__main__':main()
