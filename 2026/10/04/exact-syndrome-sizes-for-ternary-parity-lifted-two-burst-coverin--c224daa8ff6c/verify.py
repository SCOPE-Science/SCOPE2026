from itertools import product


def diff_bits(b):
    return tuple((b[i+1]-b[i]) % 2 for i in range(len(b)-1)) + (b[-1],)


def syndrome(b):
    p=len(b)
    return sum((i+1)*u for i,u in enumerate(diff_bits(b))) % (2*p)


def rotate_right(b):
    return (b[-1],)+b[:-1]


def transitions_cyclic(b):
    return sum(b[i] != b[(i+1) % len(b)] for i in range(len(b)))


def expected(p,a):
    if a == 0:
        return (3**p + (p-1)*2**(p+1) + 1)//(2*p)
    if a == p:
        return (3**p + 2*p - 3)//(2*p)
    if a % 2 == 0:
        return (3**p - 2**(p+1) + 1)//(2*p)
    return (3**p - 3)//(2*p)


def class_sizes_from_binary_lifts(p):
    sizes=[0]*(2*p)
    for b in product((0,1), repeat=p):
        sizes[syndrome(b)] += 2**(p-sum(b))
    return sizes


def delete_two_burst(x):
    return {x[:i]+x[i+2:] for i in range(len(x)-1)}


def direct_ternary_classes(p):
    cs=[[] for _ in range(2*p)]
    for x in product(range(3), repeat=p):
        b=tuple(v % 2 for v in x)
        cs[syndrome(b)].append(x)
    return cs


def verify_prime(p):
    # Parity lemma and cyclic-rotation increment modulo p.
    for b in product((0,1), repeat=p):
        s=syndrome(b)
        assert s % 2 == sum(b) % 2
        rb=rotate_right(b)
        assert (syndrome(rb)-s) % p == transitions_cyclic(b) % p
        if b not in ((0,)*p,(1,)*p):
            assert 0 < transitions_cyclic(b) < p

    sizes=class_sizes_from_binary_lifts(p)
    target=[expected(p,a) for a in range(2*p)]
    assert sizes == target, (p,sizes,target)
    mins=[a for a,v in enumerate(sizes) if v == min(sizes)]
    # Exact minimizers are the nonzero even residues modulo 2p.
    assert mins == [a for a in range(2*p) if a != 0 and a % 2 == 0]
    return sizes


def verify_covering(p):
    classes=direct_ternary_classes(p)
    target=set(product(range(3), repeat=p-2))
    for a,C in enumerate(classes):
        covered=set()
        for x in C:
            covered.update(delete_two_burst(x))
        assert covered == target, (p,a,len(target-covered))
    assert [len(C) for C in classes] == [expected(p,a) for a in range(2*p)]


if __name__ == '__main__':
    for p in (3,5,7,11):
        sizes=verify_prime(p)
        print('p=',p,'sizes=',','.join(map(str,sizes)))
    for p in (3,5,7):
        verify_covering(p)
        print('covering_ok p=',p)
    print('VERIFY_OK')
