"""Independent finite checks for two-cycle counts in parallel chip firing on full binary trees.

Run with Python 3.10 or later: python verify.py
"""
from itertools import product
from math import log, exp, sqrt


def tree(height):
    n = (1 << (height + 1)) - 1
    edges = [(i, 2*i+j) for i in range((1 << height)-1) for j in (1,2)]
    adj = [[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b); adj[b].append(a)
    return n, edges, adj


def step(state,adj):
    fires = [int(state[i] >= len(neighbors)) for i,neighbors in enumerate(adj)]
    return tuple(state[i] - len(adj[i])*fires[i] + sum(fires[j] for j in adj[i])
                 for i in range(len(adj)))


def matrix_counts(height):
    a,b=0,1
    factor=1
    for j in range(height):
        a,b = 2*b*factor,(a+3*b)*factor
        factor=a+b
    return a


def linear_product(height):
    a,b=0,1
    u=[1]
    for _ in range(height):
        a,b=2*b,a+3*b
        u.append(a+b)
    value=a
    for j in range(1,height):
        value*=u[j]**(1 << (height-1-j))
    return value


def full_cut_enumeration(height, construct=False):
    n,edges,adj=tree(height)
    m=len(edges)
    cycles=0
    verified_states=0
    for mask in range(1<<m):
        c=[0]*n
        spin=[0]*n
        for j,(a,b) in enumerate(edges):
            bit=(mask>>j)&1
            c[a]+=bit
            c[b]+=bit
            spin[b]=spin[a]^bit
        if not all(c):
            continue
        ways=1
        for x in c:ways*=x
        cycles+=ways
        if construct:
            intervals=[]
            for v in range(n):
                d=len(adj[v]);k=c[v]
                start=d if spin[v] else d-k
                intervals.append(range(start,start+k))
            for state in product(*intervals):
                y=step(state,adj);z=step(y,adj)
                assert z==state and y!=state
                assert state[0]<len(adj[0]) and y[0]>=len(adj[0])
                verified_states+=1
    assert not construct or verified_states==cycles
    return cycles,verified_states


def brute_bounded_states(height):
    n,edges,adj=tree(height)
    ranges=[range(2*len(a)) for a in adj]
    total=0; periodic=0; primitive=0; root_wait=0
    for x in product(*ranges):
        total+=1
        y=step(x,adj);z=step(y,adj)
        if z==x:
            periodic+=1
            if y!=x:
                primitive+=1
                root_wait+=int(x[0]<len(adj[0]))
    return total,periodic,primitive,root_wait


def main():
    expected={1:2,2:30,3:9350,4:859413750}
    for h,nexp in expected.items():
        val=matrix_counts(h)
        assert val==linear_product(h)==nexp,(h,val)
        print(f'height={h}, vertices={(1<<(h+1))-1}, primitive_two_cycles={val}')
    for h in (1,2,3):
        val, verified=full_cut_enumeration(h,construct=True)
        assert val==expected[h]
        print(f'height={h}, direct_edge_subset_orbits={val}, independently_updated_orbit_representatives={verified}')
    for h in (1,2):
        total,periodic,primitive,root_wait=brute_bounded_states(h)
        assert primitive==2*expected[h] and root_wait==expected[h]
        print(f'height={h}, enumerated_bounded_chip_states={total}, primitive_period_two_states={primitive}, root_wait_representatives={root_wait}')
    u=[1,5]
    for j in range(2,71):u.append(3*u[-1]+2*u[-2])
    entropy=sum(log(u[j])/2**(j+2) for j in range(1,71))
    prefactor=exp(entropy)*4/(19+5*sqrt(17))
    assert 0.7145<entropy<0.7146 and 0.2063<prefactor<0.2064
    print(f'entropy_per_vertex={entropy:.15f}, asymptotic_growth_base={exp(entropy):.15f}, prefactor={prefactor:.15f}')
    print('FULL_BINARY_CHIPFIRING_VERIFY_OK')

if __name__=='__main__':main()
