#!/usr/bin/env python3
"""Independent finite tests for symbol-window distances of a full-field twisted evaluation family.
Public reproducibility artifact; standard-library Python 3.9+ only.
"""
from itertools import product, permutations
from collections import Counter


def wcount(sequence, k, p, target):
    return sum(sum(sequence[(i+j) % p] for j in range(k)) % p == target
               for i in range(p))


def cyclic_weight(vector, b):
    p = len(vector)
    return sum(any(vector[(i+j) % p] != 0 for j in range(b))
               for i in range(p))


def code_minima(p, k, eta, order):
    # Directly enumerate the entire k-dimensional message space, without
    # using any root-set or window-sum criterion.
    basis = [tuple(pow(x, j, p) for x in order) for j in range(k-1)]
    basis.append(tuple((pow(x,k-1,p) + eta*pow(x,k,p)) % p
                       for x in order))
    minima = {b:p+1 for b in range(1,k+2)}
    first_count = {b:0 for b in range(2,k+1)}
    count = 0
    for msg in product(range(p), repeat=k):
        if not any(msg):
            continue
        word = tuple(sum(msg[j]*basis[j][i] for j in range(k)) % p
                     for i in range(p))
        count += 1
        for b in minima:
            wt=cyclic_weight(word,b)
            if wt < minima[b]:
                minima[b]=wt
                if b in first_count: first_count[b]=1
            elif wt == minima[b] and b in first_count:
                first_count[b]+=1
    return minima,first_count,count


def predicted(p,k,eta,order):
    t=wcount(order,k,p,-pow(eta,-1,p)%p)
    minimum={1:p-k}
    for b in range(2,k+2):
        minimum[b]= p if b>k else p-k+b-(1 if t>0 else 0)
    return t,minimum


def swap_order(p,k,eta):
    t=(((k-1)*pow(2,-1,p))-pow(k*eta,-1,p))%p
    return [(i+t)%p for i in [1,0]+list(range(2,p))]


def run():
    windows=0
    for p in [5,7,11,13,17,19,23,29]:
        for k in range(2,p):
            for eta in range(1,p):
                s=(-pow(eta,-1,p))%p
                base=list(range(p))
                shifted=swap_order(p,k,eta)
                a=wcount(base,k,p,s)
                b=wcount(shifted,k,p,s)
                assert a==1,(p,k,eta,'arithmetic',a)
                assert b==(1 if k==p-1 else 0),(p,k,eta,'adjacent-swap',b)
                windows+=2

    full=0
    cases=0
    for p, ks, etas in [(5,[2,3,4],[1,2,3,4]),
                         (7,[2,3,4,5,6],[1]),
                         (11,[2,3,4],[1,2]),
                         (13,[2,3],[1,2])]:
        for k in ks:
            for eta in etas:
                for order in (list(range(p)),swap_order(p,k,eta)):
                    t,expect=predicted(p,k,eta,order)
                    got,counts,nwords=code_minima(p,k,eta,order)
                    assert got==expect,(p,k,eta,order,t,expect,got)
                    if t:
                        assert all(counts[b]==(p-1)*t for b in counts), (p,k,eta,counts,t)
                    full+=nwords
                    cases+=1

    # Every cyclic permutation at p=5, including ones with multiple or zero
    # matching k-intervals, receives an independent all-codeword check.
    ordered=0
    for k in [2,3,4]:
        eta=1
        for order in permutations(range(5)):
            t,expect=predicted(5,k,eta,order)
            got,counts,nwords=code_minima(5,k,eta,order)
            assert got==expect,(k,order,t,got,expect)
            if t:
                assert all(counts[b]==4*t for b in counts)
            ordered+=1

    print('TWISTED_B_SYMBOL_VERIFY_OK',
          'window_test_cases='+str(windows),
          'complete_code_instances='+str(cases),
          'enumerated_nonzero_codewords='+str(full),
          'all_p5_coordinate_orders='+str(ordered))

if __name__=='__main__':
    run()
