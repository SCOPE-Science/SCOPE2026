#!/usr/bin/env python3
"""Independent residue-shortest-path verification of explicit semigroup formulas."""
import heapq

def shortest_paths(x):
    generators=(x+1,2*x-1,2*x+3)
    distances=[10**30]*x
    distances[0]=0
    heap=[(0,0)]
    while heap:
        value,residue=heapq.heappop(heap)
        if value!=distances[residue]:
            continue
        for generator in generators:
            r=(residue+generator)%x
            if value+generator<distances[r]:
                distances[r]=value+generator
                heapq.heappush(heap,(value+generator,r))
    return distances

def predicted_pf(x):
    t,u=divmod(x,4)
    formulas={
        0:((2*t-1)*x-t,(2*t-1)*x+3*t-1),
        1:((2*t-1)*x-t,(2*t-1)*x+3*t-1,(2*t-1)*x+3*t),
        2:((2*t-1)*x+3*t-1,2*t*x+3*t+1),
        3:((2*t-1)*x+3*t-1,2*t*x+3*t+1,(2*t+1)*x-t-1),
    }
    return sorted(formulas[u])

def check():
    tested=0
    for x in range(4,501):
        distances=shortest_paths(x)
        predicted=[0]+[min((r//3)*(2*x+3)+(r%3)*(x+1),(x-r)*(2*x-1)) for r in range(1,x)]
        assert distances==predicted,(x,'Apery',distances,predicted)
        generators=(x+1,2*x-1,2*x+3)
        actual=sorted(distances[r]-x for r in range(1,x) if all(distances[(r+g)%x]!=distances[r]+g for g in generators))
        assert actual==predicted_pf(x),(x,'PF',actual,predicted_pf(x))
        tested+=1
    print('PASS: independent Apéry shortest paths and complete pseudo-Frobenius sets for',tested,'parameters, x=4..500')

if __name__=='__main__':
    check()
