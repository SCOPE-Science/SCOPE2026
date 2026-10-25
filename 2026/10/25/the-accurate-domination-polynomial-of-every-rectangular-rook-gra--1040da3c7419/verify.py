"""Independent exact finite checks for accurate domination on rook graphs.

Runs without third-party dependencies: python3 verify.py
"""
from itertools import combinations
from collections import Counter
from math import comb


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def proposed_coeffs(p, q):
    n = p*q
    out = []
    for k in range(n+1):
        if 2*k <= n:
            val = sum((-1)**(i+j)*comb(p,i)*comb(q,j)*binom((p-i)*(q-j),k-(i*q+j*p-i*j))
                      for i in range(1,p+1) for j in range(1,q+1))
        else:
            val = binom(n,k) - sum((-1)**(i+j)*comb(p,i)*comb(q,j)*binom((p-i)*(q-j),k)
                                   for i in range(1,p+1) for j in range(1,q+1))
        assert val >= 0, (p,q,k,val)
        out.append(val)
    return out


def direct_dom(mask, p, q):
    # Original graph domination condition, not an occupancy shortcut.
    for r in range(p):
        for c in range(q):
            v=r*q+c
            if mask >> v & 1:
                continue
            if not any((mask >> (r*q+j)) & 1 for j in range(q) if j != c) and not any(
                (mask >> (i*q+c)) & 1 for i in range(p) if i != r):
                return False
    return True


def has_competitor(mask,p,q):
    n=p*q
    k=mask.bit_count()
    missing=[i for i in range(n) if not (mask>>i)&1]
    if len(missing)<k:
        return False
    for cc in combinations(missing,k):
        candidate=sum(1<<i for i in cc)
        if direct_dom(candidate,p,q):
            return True
    return False


def claimed_structural(mask,p,q):
    n=p*q
    k=mask.bit_count()
    if 2*k>n:
        return direct_dom(mask,p,q)
    full_row=any(all((mask >> (r*q+c))&1 for c in range(q)) for r in range(p))
    full_col=any(all((mask >> (r*q+c))&1 for r in range(p)) for c in range(q))
    return full_row and full_col


def run():
    tested = 0
    accurate = 0
    for p,q in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)]:
        observed=Counter()
        for mask in range(1<<(p*q)):
            defined = direct_dom(mask,p,q) and not has_competitor(mask,p,q)
            predicted=claimed_structural(mask,p,q)
            assert defined==predicted,(p,q,mask,defined,predicted)
            observed[mask.bit_count()]+=defined
            tested+=1
            accurate+=defined
        exp=proposed_coeffs(p,q)
        assert [observed[k] for k in range(p*q+1)]==exp,(p,q,observed,exp)
        assert next(k for k,v in enumerate(exp) if v) == p+q-1
        print('DIRECT',p,q, 'n_masks',1<<(p*q), 'accurate',sum(exp), 'minimum_count',exp[p+q-1], 'OK')
    # Exhaustively verify coefficient counts from original adjacency-based domination
    # and independently formulated row/column claim on larger boards (no competitor enumeration).
    fast_total=0
    for p,q in [(3,5),(4,4),(3,6),(4,5)]:
        observed=[0]*(p*q+1)
        for mask in range(1<<(p*q)):
            dom=direct_dom(mask,p,q)
            prediction=claimed_structural(mask,p,q)
            if prediction:
                assert dom
                observed[mask.bit_count()]+=1
            fast_total+=1
        exp=proposed_coeffs(p,q)
        assert observed==exp,(p,q,observed,exp)
        print('STRUCTURAL',p,q,'n_masks',1<<(p*q),'minimum_count',exp[p+q-1],'OK')
    parameter_pairs=0
    for p in range(2,12):
        for q in range(p,16):
            parameter_pairs += 1
            exp=proposed_coeffs(p,q)
            m=p+q-1
            want=binom(2*q,q+1) if p==2 else (binom(9,5) if p==q==3 else p*q)
            assert exp[m]==want and all(x==0 for x in exp[:m]),(p,q,m,want,exp[m])
    print('COEFFICIENT AND MINIMUM CROSS-CHECKS:',parameter_pairs,'parameter pairs OK')
    print('DIRECT_MASKS',tested,'DIRECT_ACCURATE',accurate,'LARGE_STRUCTURAL_MASKS',fast_total)
    print('VERIFY_OK')

if __name__=='__main__':
    run()
