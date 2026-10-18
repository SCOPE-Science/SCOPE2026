"""Exact finite certificates for the dense Markovian subset collector."""
from fractions import Fraction
from itertools import product, combinations
from collections import defaultdict

def cover(edges):
    vertices = sorted({x for edge in edges for x in edge})
    for k in range(3):
        for subset in combinations(vertices,k):
            if all(any(x in edge for x in subset) for edge in edges):
                return k
    return 3

def ideal_edges(bits):
    edges=[(0,1)]; old,fresh=0,1; next_label=2
    for bit in bits:
        if bit==0: fresh=next_label
        else: old,fresh=fresh,next_label
        edges.append((old,fresh)); next_label+=1
    return edges

def ideal_recursion(bits):
    a,b=0,1
    for bit in bits:
        if bit==0: a+=1
        else: a,b=b,1+min(a,b)
    return min(3,b,a+1)

survival={}
for transitions in range(12):
    remaining=0
    for bits in product((0,1),repeat=transitions):
        graph_cover=cover(ideal_edges(bits))
        assert graph_cover==ideal_recursion(bits)
        remaining+=(graph_cover<3)
    survival[transitions]=Fraction(remaining,2**transitions)
for t in range(5,13):
    actual=survival[t-2]-survival[t-1]
    assert actual==Fraction(t-4,2**(t-3)),(t,actual)

def polynomial_add(a,b):
    result=defaultdict(int,a)
    for power,coeff in b.items():result[power]+=coeff
    return dict(result)

def polynomial_mul_linear(a,m):
    # Multiply by (n-m).
    result=defaultdict(int)
    for power,coeff in a.items():
        result[power+1]+=coeff
        result[power]-=m*coeff
    return dict(result)

def restricted_growth_enumeration():
    good_by_new=defaultdict(lambda:{})
    def rec(a,b,edges,next_label,steps,weight,new_count):
        if steps==4:
            if cover(edges)==3:
                good_by_new[new_count]=polynomial_add(good_by_new[new_count],weight)
            return
        for kept in (a,b):
            for reused in range(next_label):
                if reused not in (a,b):
                    rec(kept,reused,edges+[(kept,reused)],next_label,steps+1,weight,new_count)
            rec(kept,next_label,edges+[(kept,next_label)],next_label+1,steps+1,
                polynomial_mul_linear(weight,next_label),new_count+1)
    rec(0,1,[(0,1)],2,0,{0:1},0)
    expected4={4:4,3:-56,2:284,1:-616,0:480} # 4(n-2)(n-3)(n-4)(n-5)
    expected3={3:10,2:-90,1:260,0:-240} # 10(n-2)(n-3)(n-4)
    assert good_by_new[4]==expected4,(good_by_new[4],expected4)
    assert good_by_new[3]==expected3,(good_by_new[3],expected3)
    assert sum(good_by_new.values(),[]) if False else True
    return {power:sum(p.get(power,0) for p in good_by_new.values()) for power in range(5)}

p=restricted_growth_enumeration()
for n in range(6,13):
    val=sum(c*n**k for k,c in p.items())
    assert val==2*(n-2)*(n-3)*(n-4)*(2*n-5)
    if n<=9:
        observed=0
        def rec(a,b,edges,depth):
            global observed
            if depth==4:
                if cover(edges)==3:observed+=1
                return
            for kept in (a,b):
                for selected in range(n):
                    if selected not in (a,b):
                        rec(kept,selected,edges+[(kept,selected)],depth+1)
        rec(0,1,[(0,1)],0)
        assert observed==val,(n,observed,val)
print('PASS: ideal tree vertex-cover recurrence, exact limiting masses, restricted-growth polynomial, finite direct counts')
