#!/usr/bin/env python3
"""Finite-field checks of length-two idempotent products in height-two incidence algebras."""
from itertools import product


def add(a,b,q):
    if q == 4:
        return a ^ b
    return (a+b)%q

def mult(a,b,q):
    if q != 4:
        return (a*b)%q
    out=0
    aa=a
    bb=b
    while bb:
        if bb&1: out ^= aa
        aa <<= 1
        if aa&4: aa ^= 7  # t^2 + t + 1
        bb >>= 1
    return out

def incidence_product(a,b,n,edges,q):
    diagonals=[mult(a[i],b[i],q) for i in range(n)]
    off=[]
    for j,(u,v) in enumerate(edges):
        off.append(add(mult(a[u],b[n+j],q),mult(a[n+j],b[v],q),q))
    return tuple(diagonals+off)

def predicted(a,n,edges):
    if any(x not in (0,1) for x in a[:n]):
        return False
    return all(a[n+j]==0 or not(a[u]==1 and a[v]==1) for j,(u,v) in enumerate(edges))

def check_height_two(name,n,edges,q):
    all_elements=list(product(range(q),repeat=n+len(edges)))
    idem=[x for x in all_elements if incidence_product(x,x,n,edges,q)==x]
    products={incidence_product(x,y,n,edges,q) for x in idem for y in idem}
    classified={x for x in all_elements if predicted(x,n,edges)}
    assert products==classified, (name,q,len(products),len(classified),len(products^classified))
    subset_sum=sum(q**(len(edges)-sum(u in S and v in S for u,v in edges))
                   for choices in product((0,1),repeat=n)
                   for S in ({i for i,c in enumerate(choices) if c},))
    assert len(products)==subset_sum
    # Explicit constructive factors for every element in the predicted set.
    U={u for u,v in edges}; V={v for u,v in edges}
    for h in classified:
        d=h[:n]
        a=[int(i in U or (i not in V and d[i]==1)) if i not in V else d[i] for i in range(n)]
        b=[d[i] if i not in V else 1 for i in range(n)]
        x=[0]*len(edges); y=[0]*len(edges)
        for j,(u,v) in enumerate(edges):
            if d[v]==0:
                x[j]=h[n+j]
            else:
                y[j]=h[n+j]
        ea=tuple(a+x);fb=tuple(b+y)
        assert incidence_product(ea,ea,n,edges,q)==ea
        assert incidence_product(fb,fb,n,edges,q)==fb
        assert incidence_product(ea,fb,n,edges,q)==h
    print(f'OK {name} q={q} n={n} edges={len(edges)} idempotents={len(idem)} products={len(products)}')
    return len(idem),len(products)

def check_chain_three(q):
    n=3; positions=[(i,j) for i in range(n) for j in range(i,n)]
    def m(a,b):
        A=dict(zip(positions,a));B=dict(zip(positions,b))
        return tuple(sum(A[(i,k)]*B[(k,j)] for k in range(i,j+1))%q for i,j in positions)
    elements=list(product(range(q),repeat=6))
    idem=[x for x in elements if m(x,x)==x]
    E2={m(x,y) for x in idem for y in idem}
    J=(0,1,0,0,1,0)
    assert J not in E2
    a=(1,0,0,1,0,0);b=(1,0,0,0,1,1);c=(0,1,0,1,0,1)
    assert all(m(x,x)==x for x in (a,b,c))
    assert m(m(a,b),c)==J
    print(f'OK upper_triangular_chain_3 q={q} J_not_E2=True J_in_E3=True')

if __name__=='__main__':
    check_height_two('single_edge',2,[(0,1)],2)
    check_height_two('star_1_2',3,[(0,1),(0,2)],2)
    check_height_two('star_1_3',4,[(0,1),(0,2),(0,3)],2)
    check_height_two('four_cycle_K22',4,[(0,2),(0,3),(1,2),(1,3)],2)
    check_height_two('edge_plus_isolate',3,[(0,1)],3)
    check_height_two('four_cycle_K22',4,[(0,2),(0,3),(1,2),(1,3)],3)
    check_height_two('star_1_2_GF4',3,[(0,1),(0,2)],4)
    check_chain_three(2)
    check_chain_three(3)
    print('VERIFY_OK')
