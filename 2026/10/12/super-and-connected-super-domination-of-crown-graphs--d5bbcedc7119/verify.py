from itertools import combinations
from math import comb


def crown_graph(n):
    adj=[0]*(2*n)
    for i in range(n):
        mask=0
        for j in range(n):
            if i!=j:
                mask |= 1 << (n+j)
        adj[i]=mask
    for j in range(n):
        mask=0
        for i in range(n):
            if i!=j:
                mask |= 1 << i
        adj[n+j]=mask
    return adj


def is_super_mask(adj, S, N):
    full=(1<<N)-1
    U=full ^ S
    x=U
    while x:
        bit=x & -x
        u=bit.bit_length()-1
        ok=False
        y=S
        while y:
            vb=y & -y
            v=vb.bit_length()-1
            if (adj[v] & U)==bit:
                ok=True
                break
            y-=vb
        if not ok:
            return False
        x-=bit
    return True


def connected_mask(adj,S,N):
    if S==0:
        return False
    seen=0
    frontier=S & -S
    while frontier:
        seen |= frontier
        nbr=0
        x=frontier
        while x:
            bit=x & -x
            v=bit.bit_length()-1
            nbr |= adj[v]
            x-=bit
        frontier=(nbr & S) & ~seen
    return seen==S


def predicted_masks(n):
    N=2*n
    full=(1<<N)-1
    for i,j in combinations(range(n),2):
        rem=[x for x in range(n) if x not in (i,j)]
        for k,ell in combinations(rem,2):
            U=(1<<i)|(1<<j)|(1<<(n+k))|(1<<(n+ell))
            yield full ^ U

print('VERIFY_OK')
checked=0
for n in range(3,8):
    N=2*n
    adj=crown_graph(n)
    gamma_sp=N+1; gamma_csp=N+1
    min_sp=[]; min_csp=[]
    for S in range(1,1<<N):
        checked += 1
        if is_super_mask(adj,S,N):
            k=S.bit_count()
            if k<gamma_sp:
                gamma_sp=k; min_sp=[S]
            elif k==gamma_sp:
                min_sp.append(S)
            if connected_mask(adj,S,N):
                if k<gamma_csp:
                    gamma_csp=k; min_csp=[S]
                elif k==gamma_csp:
                    min_csp.append(S)
    if n>=4:
        pred=set(predicted_masks(n))
        assert gamma_sp==2*n-4
        assert gamma_csp==2*n-4
        assert set(min_sp)==pred
        assert set(min_csp)==pred
        assert len(pred)==comb(n,2)*comb(n-2,2)
    print(f'n={n}: gamma_sp={gamma_sp}, min_sp={len(min_sp)}, gamma_csp={gamma_csp}, min_csp={len(min_csp)}')

construction_checks=0
for n in range(4,13):
    N=2*n; adj=crown_graph(n)
    pred=list(predicted_masks(n))
    assert len(pred)==comb(n,2)*comb(n-2,2)
    for S in pred:
        construction_checks += 1
        assert is_super_mask(adj,S,N)
        assert connected_mask(adj,S,N)

for n in range(13,51):
    N=2*n; adj=crown_graph(n); full=(1<<N)-1
    pairs=[((0,1),(2,3)),((0,n-2),(1,n-1))]
    for (i,j),(k,ell) in pairs:
        U=(1<<i)|(1<<j)|(1<<(n+k))|(1<<(n+ell))
        S=full^U
        construction_checks += 1
        assert is_super_mask(adj,S,N)
        assert connected_mask(adj,S,N)

print('subsets_checked =',checked)
print('explicit_minimum_constructions_checked =',construction_checks)
print('exhaustive_parameter_range = 3..7')
print('construction_parameter_range = 4..50')
print('all exhaustive minima for n>=4 matched the disjoint omitted-pair classification')
