#!/usr/bin/env python3
"""Exhaustive finite checks for the lollipop zero-forcing classification."""
from math import comb


def build_graph(k, ell):
    # Vertices: 0 is the clique attachment a; 1..k-1 are X;
    # k..k+ell-1 are p_1..p_ell.
    n = k + ell
    adj = [0] * n
    for u in range(k):
        for v in range(u + 1, k):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    adj[0] |= 1 << k
    adj[k] |= 1 << 0
    for u in range(k, k + ell - 1):
        adj[u] |= 1 << (u + 1)
        adj[u + 1] |= 1 << u
    return adj


def is_zero_forcing(adj, chosen):
    n = len(adj)
    all_mask = (1 << n) - 1
    blue = chosen
    while True:
        move = 0
        work = blue
        while work:
            bit = work & -work
            work -= bit
            u = bit.bit_length() - 1
            white_neighbors = adj[u] & (all_mask ^ blue)
            if white_neighbors and white_neighbors & (white_neighbors - 1) == 0:
                move = white_neighbors
                break
        if not move:
            return blue == all_mask
        blue |= move


def criterion(k, ell, chosen):
    x_mask = sum(1 << u for u in range(1, k))
    white_x = x_mask & ~chosen
    omitted = white_x.bit_count()
    if omitted == 0:
        return True
    if omitted >= 2:
        return False
    if chosen & 1:  # attachment a
        return True
    terminal = k + ell - 1
    if chosen & (1 << terminal):
        return True
    for u in range(k, k + ell - 1):
        if chosen & (1 << u) and chosen & (1 << (u + 1)):
            return True
    return False


def add_coeff(coeff, degree, value):
    coeff[degree] = coeff.get(degree, 0) + value


def predicted_coefficients(k, ell):
    coeff = {}
    # All X selected; attachment and path arbitrary.
    for j in range(ell + 2):
        add_coeff(coeff, k - 1 + j, comb(ell + 1, j))
    # Exactly one X omitted; attachment selected; path arbitrary.
    for j in range(ell + 1):
        add_coeff(coeff, k - 1 + j, (k - 1) * comb(ell, j))
    # Exactly one X omitted; attachment omitted; rooted-good path subset.
    for j in range(ell + 1):
        independent = comb(ell - j, j) if 0 <= j <= ell - j else 0
        good = comb(ell, j) - independent
        add_coeff(coeff, k - 2 + j, (k - 1) * good)
    return {d: c for d, c in coeff.items() if c}


parameter_pairs = 0
subset_checks = 0
criterion_checks = 0
coefficient_checks = 0
minimum_checks = 0
max_order = 0

for k in range(3, 7):
    for ell in range(1, 9):
        adj = build_graph(k, ell)
        n = k + ell
        max_order = max(max_order, n)
        observed = {}
        for chosen in range(1 << n):
            actual = is_zero_forcing(adj, chosen)
            expected = criterion(k, ell, chosen)
            subset_checks += 1
            criterion_checks += 1
            assert actual == expected, (k, ell, chosen, actual, expected)
            if actual:
                size = chosen.bit_count()
                observed[size] = observed.get(size, 0) + 1
        predicted = predicted_coefficients(k, ell)
        all_degrees = set(observed) | set(predicted)
        for d in all_degrees:
            coefficient_checks += 1
            assert observed.get(d, 0) == predicted.get(d, 0), (k, ell, d, observed, predicted)
        z = min(observed)
        minimum_checks += 2
        assert z == k - 1, (k, ell, z)
        assert observed[z] == 2 * k - 1, (k, ell, observed[z], 2 * k - 1)
        parameter_pairs += 1

print(
    'VERIFY_OK '
    f'parameter_pairs={parameter_pairs} '
    f'subset_checks={subset_checks} '
    f'criterion_checks={criterion_checks} '
    f'coefficient_checks={coefficient_checks} '
    f'minimum_checks={minimum_checks} '
    f'max_order={max_order}'
)
