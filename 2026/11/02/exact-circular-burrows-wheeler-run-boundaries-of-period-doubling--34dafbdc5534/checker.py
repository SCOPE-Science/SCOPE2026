#!/usr/bin/env python3
"""Independent finite checks for the dyadic period-doubling circular BWT theorem.
Run with python3 checker.py. No external dependencies.
"""

def morph(w):
    return ''.join('01' if c == '0' else '00' for c in w)


def cyclic_bwt_sort(w):
    n = len(w)
    order = sorted(range(n), key=lambda i: (w+w)[i:i+n])
    assert len({(w+w)[i:i+n] for i in order}) == n
    return ''.join(w[(i-1) % n] for i in order), order


def cyclic_bwt_doubling(w):
    n = len(w)
    classes = [int(c) for c in w]
    span = 1
    order = list(range(n))
    while span < n:
        order.sort(key=lambda i: (classes[i], classes[(i+span) % n]))
        updated = [0] * n
        count = 0
        for i in range(1, n):
            a, b = order[i-1], order[i]
            count += ((classes[a], classes[(a+span) % n]) !=
                      (classes[b], classes[(b+span) % n]))
            updated[b] = count
        classes = updated
        span *= 2
        if count == n-1:
            break
    assert len(set(classes)) == n
    return ''.join(w[(i-1) % n] for i in order), order


def run_boundary_prefixes(w, output, order):
    n = len(w)
    pairs = []
    for j in range(1,n):
        if output[j] == output[j-1]:
            continue
        a, b = order[j-1], order[j]
        t = 0
        while t < n and w[(a+t)%n] == w[(b+t)%n]:
            t += 1
        assert t < n
        pairs.append(''.join(w[(a+s)%n] for s in range(t)))
    return pairs


def bispecial_factors(w):
    n=len(w)
    ext={}
    doubled=w+w
    for d in range(n):
        for i in range(n):
            u=doubled[i:i+d]
            ext.setdefault(u, set()).add((w[(i-1)%n], w[(i+d)%n]))
    return {u for u, e in ext.items()
            if len({a for a,b in e}) == 2
            and len({b for a,b in e}) == 2}


def expected(k):
    a='00'; b='0'
    aa=[a]; bb=[b]
    for _ in range(1,k-1):
        a=morph(a)+'0'; aa.append(a)
        b=morph(b)+'0'; bb.append(b)
    return aa, bb


def main():
    w='0'
    for k in range(1,15):
        w=morph(w)
        assert w.count('1') % 2 == 1
        bwt, order=cyclic_bwt_doubling(w)
        if k<=9:
            bwt2, order2=cyclic_bwt_sort(w)
            assert (bwt2, order2)==(bwt,order)
        if k<2:
            continue
        aa, bb=expected(k)
        theory=set(aa+bb[:-1])
        boundaries=run_boundary_prefixes(w,bwt,order)
        assert len(boundaries)==2*k-3, (k,len(boundaries))
        assert len(boundaries)==len(set(boundaries)), k
        assert set(boundaries)==theory, (k,set(boundaries)^theory)
        runs=1+len(boundaries)
        assert runs==2*k-2, (k,runs)
        if k<=7:
            actual=bispecial_factors(w)
            assert actual == {''}|set(aa)|set(bb), (k,actual ^ ({''}|set(aa)|set(bb)))
        print(f'rank {k}: length={len(w)}, BWT_runs={runs}, boundary_LCPs={len(theory)}, verified')
    print('ALL CHECKS PASSED: complete bispecial languages through rank 7; '
          'two independent BWT constructions through rank 9; '
          'BWT boundary types and runs through rank 14.')


if __name__=='__main__':
    main()
