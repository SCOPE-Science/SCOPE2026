#!/usr/bin/env python3
"""Check exact rank polynomials for finite functional cycle-and-leaves frames.
Standalone, pure standard library, no external data or packages.
"""
from collections import Counter
from itertools import product
from math import comb


def polynomial_product(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def leaf_occupancy_polynomial(p, q):
    return [comb(q,j) * sum((-1)**(j-b)*comb(j,b)*(b+1)**p
                             for b in range(j+1)) for j in range(q+1)]


def formula_e(s):
    c = len(s)
    result = [0]*(sum(s)+1)
    for a in range(c):
        term = [1]
        for i in range(c):
            term = polynomial_product(term, leaf_occupancy_polynomial(s[i], s[(i+a)%c]))
        for j, value in enumerate(term):
            result[j] += value
    return result


def formula_i(s):
    term = [1]
    for p in s:
        term = polynomial_product(term,
                 [comb(p,j)*(j+1)**(p-j) for j in range(p+1)])
    return term


def formula_hom(source, target):
    c=len(source); d=len(target)
    if c%d:
        return [0]*(sum(target)+1)
    result=[0]*(sum(target)+1)
    for a in range(d):
        term=[1]
        for j in range(d):
            p=sum(source[i] for i in range(c) if (i+a)%d==j)
            term=polynomial_product(term, leaf_occupancy_polynomial(p,target[j]))
        for k,v in enumerate(term): result[k]+=v
    return result


def direct_hom(source, target):
    nxts,_=make_frame(source)
    nxtt,_=make_frame(target)
    ns=len(nxts);nt=len(nxtt);d=len(target)
    ranks=Counter(); checked=0
    for f in product(range(nt), repeat=ns):
        checked+=1
        if all(f[nxts[x]]==nxtt[f[x]] for x in range(ns)):
            rank=len(set(f))-d
            ranks[rank]+=1
    expectation=formula_hom(source,target)
    assert [ranks[k] for k in range(sum(target)+1)]==expectation, (source,target,ranks,expectation)
    return checked, sum(ranks.values())


def make_frame(s):
    c=len(s); nxt=list(range(1,c))+[0]; fibres=[]
    for i, q in enumerate(s):
        fibre=[]
        for j in range(q):
            fibre.append(len(nxt)); nxt.append(i)
        fibres.append(tuple(fibre))
    return tuple(nxt), tuple(fibres)


def direct_histogram(s, complete=True):
    nxt, _ = make_frame(s)
    n=len(nxt); c=len(s)
    endom=Counter(); idempot=Counter(); tested=0
    for f in product(range(n),repeat=n):
        tested += 1
        if any(f[nxt[x]]!=nxt[f[x]] for x in range(n)):
            continue
        rank=len(set(f))-c
        assert rank>=0
        endom[rank]+=1
        if all(f[f[x]]==f[x] for x in range(n)):
            idempot[rank]+=1
    expectE=formula_e(s); expectI=formula_i(s)
    assert [endom[j] for j in range(sum(s)+1)] == expectE, (s,endom,expectE)
    assert [idempot[j] for j in range(sum(s)+1)] == expectI, (s,idempot,expectI)
    return tested,sum(endom.values()),sum(idempot.values())


def modal_test(s):
    nxt, _ = make_frame(s)
    n=len(nxt); subsets=tuple(range(1<<n))
    # Box(S) consists of the points whose unique successor belongs to S.
    def box(mask):
        return sum((1<<x) for x in range(n) if mask & (1<<nxt[x]))
    all_boxes=[box(mask) for mask in subsets]
    tested=0; matches=0
    for f in product(range(n),repeat=n):
        tested+=1
        is_bounded=all(f[nxt[x]]==nxt[f[x]] for x in range(n))
        # The modal-algebra homomorphism associated to f is preimage.
        # Boolean operations are automatically preserved, so test Box.
        preserves_box=True
        for mask in subsets:
            premask=sum((1<<x) for x in range(n) if mask & (1<<f[x]))
            lhs=box(premask)
            rhs=sum((1<<x) for x in range(n) if all_boxes[mask] & (1<<f[x]))
            if lhs!=rhs:
                preserves_box=False
                break
        assert preserves_box==is_bounded, (s,f,preserves_box,is_bounded)
        matches+=is_bounded
    return tested,matches


def normal_form_histogram(s):
    nxt, fibres=make_frame(s)
    c=len(s); n=len(nxt)
    E=Counter(); I=Counter(); tested=0
    for a in range(c):
        options=[]
        for i in range(c):
            options.extend([(i+a-1)%c]+list(fibres[(i+a)%c]) for _ in fibres[i])
        for choices in product(*options):
            f=list((i+a)%c for i in range(c))+list(choices)
            tested+=1
            assert all(f[nxt[x]]==nxt[f[x]] for x in range(n))
            rank=len(set(f))-c
            E[rank]+=1
            if all(f[f[x]]==f[x] for x in range(n)):
                I[rank]+=1
    assert [E[j] for j in range(sum(s)+1)]==formula_e(s)
    assert [I[j] for j in range(sum(s)+1)]==formula_i(s)
    return tested,sum(I.values())


def test():
    hist_shapes=0; full_function_tables=0; bounded_maps=0; idempotents=0
    modal_shapes=0; modal_function_tables=0; comparisons=0
    for c in range(1,5):
        for s in product(range(7-c),repeat=c):
            if sum(s)>6-c:continue
            tested,ne,ni=direct_histogram(s)
            hist_shapes+=1;full_function_tables+=tested; bounded_maps+=ne; idempotents+=ni
            comparisons += 2*(sum(s)+1)
            # An entirely separate algebra-preservation check for small frames.
            if c+sum(s)<=4:
                a,b=modal_test(s)
                modal_shapes+=1;modal_function_tables+=a
                assert b==ne
            reflected=tuple(s[(-i)%c] for i in range(c))
            assert formula_e(s)==formula_e(reflected)
            assert formula_i(s)==formula_i(reflected)
            comparisons+=2*(sum(s)+1)
    witness=(1,2,3); reversed_witness=(1,3,2)
    assert reversed_witness not in [tuple(witness[(i+a)%3] for i in range(3)) for a in range(3)]
    assert formula_e(witness)==formula_e(reversed_witness)==[3,66,397,806,564,120,12]
    assert formula_i(witness)==formula_i(reversed_witness)==[1,17,74,107,62,14,1]
    a,b=normal_form_histogram(witness)
    assert a==1968 and b==276
    a2,b2=normal_form_histogram(reversed_witness)
    assert a2==a and b2==b
    comparisons += 4*(sum(witness)+1)
    tiny=[]
    for c in range(1,5):
        for s in product(range(5-c),repeat=c):
            if sum(s)<=4-c:
                tiny.append(s)
    hom_pairs=0; hom_function_tables=0; hom_maps=0
    for source in tiny:
        for target in tiny:
            checked, matches=direct_hom(source,target)
            hom_pairs+=1;hom_function_tables+=checked;hom_maps+=matches
            reflected_source=tuple(source[-i%len(source)] for i in range(len(source)))
            reflected_target=tuple(target[-i%len(target)] for i in range(len(target)))
            assert formula_hom(source,target)==formula_hom(reflected_source,reflected_target)
            comparisons+=sum(target)+1
    print(f'VERIFY_OK {hist_shapes} finite frames; {full_function_tables} brute function tables; '
          f'{bounded_maps} bounded maps; {idempotents} idempotents; '
          f'{modal_shapes} modal-algebra checks ({modal_function_tables} candidate maps); '
          f'{hom_pairs} hom-pairs ({hom_function_tables} direct function tables, {hom_maps} bounded homomorphisms); '
          f'{comparisons} coefficient/reversal assertions; two 9-world normal-form witnesses ({a} maps each)')

if __name__=='__main__':test()
