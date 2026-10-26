#!/usr/bin/env python3
"""Exact finite-group algebra certificate for the ternary characteristic-two symmetry theorem."""
I = (1, 2, 4)
A = (2, 3, 4)
C = (2, 4, 1)
S = (2, 1, 4)


def compose(g, h):
    """Images after substituting h in the triple g."""
    result = []
    for mask in h:
        val = 0
        for j in range(3):
            if (mask >> j) & 1:
                val ^= g[j]
        result.append(val)
    return tuple(result)


def basis_insert(basis, vector):
    while vector:
        pivot = vector.bit_length() - 1
        if pivot in basis:
            vector ^= basis[pivot]
        else:
            basis[pivot] = vector
            return True
    return False


def in_span(basis, vector):
    while vector:
        pivot = vector.bit_length() - 1
        if pivot not in basis:
            return False
        vector ^= basis[pivot]
    return True


def main():
    group = [I]
    index = {I: 0}
    cursor = 0
    while cursor < len(group):
        for gen in (A, C, S):
            next_element = compose(group[cursor], gen)
            if next_element not in index:
                index[next_element] = len(group)
                group.append(next_element)
        cursor += 1
        assert len(group) <= 168
    assert len(group) == 168
    assert all(compose(g, h) in index for g in group for h in group)
    a2 = compose(A, A)
    basis = {}
    for g in group:
        cvec = (1 << index[g]) ^ (1 << index[compose(C, g)])
        avec = ((1 << index[g]) ^ (1 << index[compose(A, g)]) ^
                (1 << index[compose(a2, g)]))
        basis_insert(basis, cvec)
        basis_insert(basis, avec)
    assert len(basis) == 160
    for g in group:
        swap = (1 << index[g]) ^ (1 << index[compose(S, g)])
        assert in_span(basis, swap)
    print('VERIFY_OK group=168 rank=160 swaps=168')


if __name__ == '__main__':
    main()
