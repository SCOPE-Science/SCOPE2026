"""Independent exhaustive upper-bound check for n=5, no dependencies.
The locality convention fixes one observer for each coordinate across the code.
All 4^5 recovery dependency digraphs are reduced under S_5 relabeling,
then tested by exact 11-clique exclusion on the permutation compatibility graph.
"""
from itertools import permutations, product

n = 5
P = list(permutations(range(n)))

def relabel(dep, rel):
    d = [0] * n
    for i in range(n): d[rel[i]] = rel[dep[i]]
    return tuple(d)

def neighbors(dep):
    adj = [0] * len(P)
    for i,a in enumerate(P):
        for j in range(i):
            b = P[j]
            if all(a[t] == b[t] or a[dep[t]] != b[dep[t]] for t in range(n)):
                adj[i] |= 1<<j
                adj[j] |= 1<<i
    return adj

def forbidden_clique(adj, minimum=11):
    """Prove no clique of at least 'minimum' using exact coloring upper bound."""
    def colorful_order(vertices):
        order=[]; colors=[]; rest=vertices; color=0
        while rest:
            color+=1
            q=rest
            while q:
                one=q & -q; v=one.bit_length()-1
                order.append(v); colors.append(color)
                rest &= ~one
                q &= ~one
                q &= ~adj[v]
        return order, colors
    def search(possible, current):
        if current >= minimum: return True
        if current + possible.bit_count() < minimum: return False
        order, colors = colorful_order(possible)
        for k in range(len(order)-1,-1,-1):
            if current + colors[k] < minimum: return False
            v=order[k]; one=1<<v
            if search(possible & adj[v],current+1): return True
            possible &= ~one
        return False
    return search((1<<len(adj))-1,0)

def main():
    allmaps=set(product(*([j for j in range(n) if j!=i] for i in range(n))))
    reps=[]
    for dep in list(allmaps):
        if dep not in allmaps: continue
        orbit={relabel(dep, rel) for rel in P}
        allmaps.difference_update(orbit)
        reps.append((dep,len(orbit)))
    assert sum(size for dep,size in reps)==4**5
    assert len(reps)==13
    for dep,multiplicity in reps:
        assert not forbidden_clique(neighbors(dep),11), (dep, multiplicity)
    print('PASS n=5 1024 labeled dependency patterns; 13 orbits; no code of size 11')

if __name__=='__main__':main()
