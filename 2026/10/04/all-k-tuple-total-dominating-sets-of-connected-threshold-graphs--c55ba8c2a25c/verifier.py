from itertools import product
from math import comb
from collections import Counter


def graph_from_bits(bits):
    n=len(bits)
    adj=[set() for _ in range(n)]
    for j in range(1,n):
        if bits[j]==1:
            for i in range(j):
                adj[i].add(j); adj[j].add(i)
    return adj


def is_ktds(adj,S,k):
    return all(sum((u in S) for u in adj[v])>=k for v in range(len(adj)))


def final_one_block(bits):
    n=len(bits); j=n-1
    while j>=0 and bits[j]==1:
        j-=1
    return set(range(j+1,n))


def formula_counter(n,b,k):
    out=Counter()
    if k>b:
        return out
    for j in range(k,b+1):
        for q in range(0,n-b+1):
            out[j+q]+=comb(b,j)*comb(n-b,q)
    out[k]-=comb(b,k)
    if out[k]==0:
        del out[k]
    return out


def main():
    graphs=0; subset_checks=0; coefficient_checks=0; minimal_checks=0
    max_order=10
    for n in range(2,max_order+1):
        for mid in product([0,1], repeat=max(0,n-2)):
            bits=(0,)+mid+(1,)
            adj=graph_from_bits(bits)
            B=final_one_block(bits); b=len(B)
            graphs+=1
            for k in range(1,n+1):
                brute=Counter()
                valid_sets=[]
                for mask in range(1<<n):
                    S={i for i in range(n) if mask>>i & 1}
                    truth=is_ktds(adj,S,k)
                    pred=(k<=b and len(S & B)>=k and len(S)>=k+1)
                    subset_checks+=1
                    if truth!=pred:
                        raise AssertionError((bits,k,mask,truth,pred,b))
                    if truth:
                        brute[len(S)]+=1; valid_sets.append(S)
                form=formula_counter(n,b,k)
                if brute!=form:
                    raise AssertionError((bits,k,brute,form))
                coefficient_checks+=n+1
                # Inclusion-minimal kTDS are exactly the valid sets of size k+1.
                for S in valid_sets:
                    minimal=all(not is_ktds(adj,S-{v},k) for v in S)
                    expected=(len(S)==k+1)
                    minimal_checks+=1
                    if minimal!=expected:
                        raise AssertionError(('minimal',bits,k,S,minimal,expected))
    print(f'VERIFY_OK graphs={graphs} subset_k_checks={subset_checks} coefficient_checks={coefficient_checks} minimal_checks={minimal_checks} max_order={max_order}')

if __name__=='__main__':
    main()
