"""Exact finite checks for heat-kernel Lipschitz transport on multipartite graphs.

The proof for arbitrary part sizes and real times is analytic; these checks
independently enumerate all integer-valued Lipschitz potentials on small graphs.
"""
from fractions import Fraction as Q
from itertools import product
from math import lcm


def profiles_of_sum(n, minimum=1):
    if n >= minimum:
        yield (n,)
    for first in range(minimum, n // 2 + 1):
        for rest in profiles_of_sum(n-first, first):
            yield (first,) + rest


def check_profile(parts, q):
    N = sum(parts)
    if len(parts)<2:
        return 0
    label = tuple(i for i, count in enumerate(parts) for _ in range(count))
    edges = tuple((u,v) for u in range(N) for v in range(u) if label[u]!=label[v])
    b = q**N
    aa = tuple(q**(N-m) for m in parts)
    # Directly assemble the heat matrix from its three spectral levels.
    H=[]
    for u in range(N):
        i=label[u]; ni=parts[i]
        row=[]
        for v in range(N):
            value = (1-b)/N
            if label[v]==i:
                value += (b-aa[i])/ni
                if u==v: value += aa[i]
            row.append(value)
        assert sum(row)==1
        H.append(row)
    # Direct graph constraint enumeration: integer potentials suffice since
    # the oriented incidence constraint matrix is totally unimodular.
    potential=[]
    for tup in product(range(-2,3), repeat=N-1):
        f=(0,)+tup
        if all(abs(f[u]-f[v])<=1 for u,v in edges):
            potential.append(f)
    assert potential
    for u in range(N):
      for v in range(u):
        diff=[H[u][j]-H[v][j] for j in range(N)]
        w=max(sum(d*x for d,x in zip(diff,f)) for f in potential)
        def F(z):
            a=q**(N-z)
            return b+2*Q(z-1,z)*(a-b)
        predicted=(max(F(parts[label[u]]),F(parts[label[v]]))
                   if label[u]!=label[v] else 2*aa[label[u]])
        assert w==predicted, (parts, q, u,v,w,predicted)
    return N*(N-1)//2


def main():
    graphs=edges=0
    for n in range(2,8):
        for prof in profiles_of_sum(n):
            if len(prof)<2:continue
            for q in (Q(1),Q(1,2),Q(2,3)):
                edges+=check_profile(prof,q)
                graphs+=1
    print(f'CERTIFICATE_OK rational_instances={graphs} pair_tests={edges}')

if __name__=='__main__':main()
