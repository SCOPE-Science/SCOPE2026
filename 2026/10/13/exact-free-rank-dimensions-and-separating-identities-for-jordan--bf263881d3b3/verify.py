"""Direct finite-field term-function checks for affine Jordan Lie algebras.

Python 3 standard library only. No imported mathematical classification data.
The calculations enumerate every input tuple for the listed prime fields.
"""
from itertools import product


def check(p, s, n):
    """Close the generator span under pointwise Lie brackets on all inputs."""
    evaluations = list(product(range(p), repeat=(s + 1) * n))
    number = len(evaluations)
    width = s + 1
    span_length = number * width
    generators = []
    for i in range(n):
        generators.append(tuple(t[(width * i):(width * i + width)]
                                for t in evaluations))

    def bracket(left, right):
        ans = []
        for lrow, rrow in zip(left, right):
            a, c = lrow[0], rrow[0]
            diff = [(a * rrow[j] - c * lrow[j]) % p
                    for j in range(1, width)]
            image = [(diff[j] + (diff[j + 1] if j + 1 < s else 0)) % p
                     for j in range(s)]
            ans.append((0,) + tuple(image))
        return tuple(ans)

    def flatten(function):
        return [x for row in function for x in row]

    pivots = {}

    def add(function):
        vec = flatten(function)
        k = 0
        while True:
            while k < span_length and vec[k] == 0:
                k += 1
            if k == span_length:
                return False
            old = pivots.get(k)
            if old is None:
                scale = pow(vec[k], -1, p)
                pivots[k] = [(scale * t) % p for t in vec]
                return True
            coeff = vec[k]
            for j in range(k, span_length):
                vec[j] = (vec[j] - coeff * old[j]) % p

    for generator in generators:
        assert add(generator)
    queue = []
    for i in range(n):
        for j in range(i + 1, n):
            candidate = bracket(generators[i], generators[j])
            if add(candidate):
                queue.append(candidate)
    processed = 0
    while processed < len(queue):
        next_term = queue[processed]
        processed += 1
        for generator in generators:
            candidate = bracket(generator, next_term)
            if add(candidate):
                queue.append(candidate)
    observed = len(pivots)
    predicted = n + s * (n - 1) * (p ** n - 1)
    assert observed == predicted, (p, s, n, observed, predicted)
    print(f"field={p} jordan_size={s} rank={n} dimension={observed} "
          f"evaluations={number}")


def check_separating_identity(p, s):
    """Test the separating Lie-polynomial action on top Jordan vectors."""
    def act_J(v):
        return tuple((v[j] + (v[j + 1] if j + 1 < len(v) else 0)) % p
                     for j in range(len(v)))

    def polynomial(v):
        term = v
        for _ in range(p):
            term = act_J(term)
        first = act_J(v)
        return tuple((a - b) % p for a, b in zip(term, first))

    for dimension, should_be_zero in [(s, True), (s + 1, False)]:
        vector = (0,) * (dimension - 1) + (1,)
        vector = act_J(vector)
        for _ in range(s):
            vector = polynomial(vector)
        assert (not any(vector)) == should_be_zero, (p, s, dimension)
    print(f"field={p} separation_level={s} IDENTITY_OK")


if __name__ == "__main__":
    cases = [(2, 1, 1), (2, 1, 2), (2, 2, 2), (2, 3, 2),
             (2, 2, 3), (3, 1, 2), (3, 2, 2)]
    for case in cases:
        check(*case)
    separations = [(p, s) for p in (2, 3) for s in (1, 2, 3, 4)]
    for case in separations:
        check_separating_identity(*case)
    print(f"DIMENSION_CHECKS={len(cases)} IDENTITY_CHECKS={len(separations)} VERIFY_OK")
