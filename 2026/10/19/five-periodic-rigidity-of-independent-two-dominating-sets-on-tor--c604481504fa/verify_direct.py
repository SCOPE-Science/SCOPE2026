"""Direct graph-bitset verification for small cyclic grid instances.

This program enumerates independent vertex sets without using the column
structure exploited in the proof. Run: python verify_direct.py
"""
from collections import Counter


def neighbors(n):
    v = 5*n
    masks=[]
    for j in range(n):
        for i in range(5):
            nbr={(j*5+(i+1)%5),j*5+(i-1)%5,((j+1)%n)*5+i,((j-1)%n)*5+i}
            assert len(nbr)==4, (n,i,j)
            masks.append(sum(1<<k for k in nbr))
    assert len(masks)==v
    return masks


def enumerate_kernels(n):
    adj=neighbors(n); size=len(adj); masks=[]
    # Branch on inclusion/exclusion, pruning independent vertices upon inclusion.
    def dfs(unseen, selected):
        if not unseen:
            if all((selected >>v)&1 or (selected&adj[v]).bit_count()>=2 for v in range(size)):
                masks.append(selected)
            return
        bit=unseen & -unseen
        v=bit.bit_length()-1
        dfs(unseen^bit, selected)
        dfs(unseen & ~bit & ~adj[v], selected|bit)
    dfs((1<<size)-1,0)
    return masks


def expected(n):
    if n%5:return set()
    ans=set()
    for epsilon in [-1,1]:
        for a in range(5):
            s=0
            for j in range(n):
                for i in range(5):
                    if (i-epsilon*j-a)%5 in (1,4):s|=1 << (5*j+i)
            ans.add(s)
    return ans


if __name__=='__main__':
    for n in range(3,7):
        actual=enumerate_kernels(n)
        assert len(actual)==len(set(actual))
        assert set(actual)==expected(n),(n,len(actual),len(expected(n)))
        print(f'order={n} vertices={5*n} independent_two_dominating_sets={len(actual)}')
    for n in range(5,81,5):
        adj=neighbors(n); e=expected(n)
        assert len(e)==10
        for s in e:
            assert all(not ((s>>v)&1 and s&adj[v]) for v in range(5*n))
            assert all((s>>v)&1 or (s&adj[v]).bit_count()>=2 for v in range(5*n))
        print(f'formula_validation_order={n} constructions={len(e)}')
    print('DIRECT_VERIFICATION_OK')
