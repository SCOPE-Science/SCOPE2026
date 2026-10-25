"""Finite reproducibility checks for the 3,4,5 ideal-product power theorem.

The proof is independent of these finite enumerations. Python 3.10+; no dependencies.
"""

def monomials(k):
    return sorted({3**a * 4**b * 5**(k-a-b) for a in range(k+1) for b in range(k-a+1)})


def predicted(k):
    xs = [3**(k-i)*4**i for i in range(k+1)]
    ys = [3**(k-i)*4**(i-1)*5 for i in range(1,k+1)]
    return sorted(xs+ys)


def reachable(coins, cap):
    table=bytearray(cap+1)
    table[0]=1
    for coin in coins:
        for j in range(coin,cap+1):
            if table[j-coin]: table[j]=1
    return table


def independently_minimal_generators(k):
    # Work from ALL degree-k products rather than from the claimed list.
    raw=monomials(k)
    keep=[]
    for a in raw:
        if not reachable(keep,a)[a]:
            keep.append(a)
    return keep


def check():
    for k in range(1,9):
        raw=monomials(k)
        claim=predicted(k)
        brute=independently_minimal_generators(k)
        assert len(claim)==2*k+1
        assert len(set(claim))==len(claim)
        assert brute==claim,(k,brute,claim)
        table=reachable(claim,max(raw))
        assert all(table[v] for v in raw)
        for g in claim:
            omit=reachable([v for v in claim if v!=g],g)
            assert not omit[g],(k,g)
        print(f'k={k}: raw_products={len(raw)}; generators={len(brute)}; largest_generator={brute[-1]}')
    print('VERIFY_OK')

if __name__=='__main__':check()
