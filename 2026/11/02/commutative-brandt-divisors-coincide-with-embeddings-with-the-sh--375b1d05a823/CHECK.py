"""Finite exact checks for commutative Brandt-divisor classification.

No external dependencies; symbolic proof is in RESULT.md.
"""
from itertools import combinations, product


def partitions(n):
    if n == 0:
        yield ()
        return
    def visit(labels, maximum):
        if len(labels) == n:
            yield tuple(labels)
        else:
            for new_label in range(maximum + 2):
                yield from visit(labels + [new_label], max(maximum, new_label))
    yield from visit([0], 0)


def brandt2(a, b):
    """The five-element Brandt semigroup over the trivial group."""
    if a == 0 or b == 0:
        return 0
    i, j = divmod(a - 1, 2)
    k, ell = divmod(b - 1, 2)
    return 1 + 2 * i + ell if j == k else 0


def check_shape(multiplication):
    q = len(multiplication)
    if q == 1:
        return True
    zeros = [z for z in range(q) if all(multiplication[z][i] == z and
             multiplication[i][z] == z for i in range(q))]
    if len(zeros) != 1:
        # Without an external zero, the quotient must be a group.
        identities = [e for e in range(q) if all(multiplication[e][i] == i and
                      multiplication[i][e] == i for i in range(q))]
        if len(identities) != 1:
            return False
        e = identities[0]
        return all(any(multiplication[x][y] == e for y in range(q)) for x in range(q))
    zero = zeros[0]
    tags = {}
    for x in range(q):
        if x == zero:
            continue
        if all(multiplication[x][y] == zero and multiplication[y][x] == zero
               for y in range(q)):
            tags[x] = ('nil', x)
            continue
        powers = [x]
        current = x
        for _ in range(q + 1):
            current = multiplication[current][x]
            powers.append(current)
        if x not in powers[1:]:
            return False
        candidate_ids = [e for e in set(powers) if e != zero and
                         multiplication[e][e] == e and multiplication[e][x] == x]
        if len(candidate_ids) != 1:
            return False
        tags[x] = ('group', candidate_ids[0])
    for x in range(q):
        for y in range(q):
            actual = multiplication[x][y]
            if x == zero or y == zero or tags[x][0] == 'nil' or tags[y][0] == 'nil':
                if actual != zero:
                    return False
            elif tags[x][1] == tags[y][1]:
                if actual == zero or tags[actual] != tags[x]:
                    return False
            elif actual != zero:
                return False
    return True


def exhaustive_quotients():
    closed_count = congruence_count = commutative_count = 0
    for mask in range(1, 1 << 5):
        elements = [x for x in range(5) if mask & (1 << x)]
        if any(brandt2(x, y) not in elements for x, y in product(elements, repeat=2)):
            continue
        closed_count += 1
        index = {x: i for i, x in enumerate(elements)}
        for labels in partitions(len(elements)):
            if any(labels[index[brandt2(a, c)]] != labels[index[brandt2(b, c)]] or
                   labels[index[brandt2(c, a)]] != labels[index[brandt2(c, b)]]
                   for a in elements for b in elements
                   if labels[index[a]] == labels[index[b]] for c in elements):
                continue
            congruence_count += 1
            if any(labels[index[brandt2(a, b)]] != labels[index[brandt2(b, a)]]
                   for a, b in product(elements, repeat=2)):
                continue
            commutative_count += 1
            q = max(labels) + 1
            representatives = {labels[i]: elements[i] for i in range(len(elements))}
            mult = [[labels[index[brandt2(representatives[i], representatives[j])]]
                     for j in range(q)] for i in range(q)]
            assert check_shape(mult), (elements, labels, mult)
    return closed_count, congruence_count, commutative_count


def construction(group_orders, number_of_annihilators):
    t = len(group_orders)
    orders = tuple(group_orders) + ((max(1, number_of_annihilators),)
                                     if number_of_annihilators else ())
    elements = ['zero']
    for i, size in enumerate(group_orders):
        elements += [('group', i, a) for a in range(size)]
    elements += [('nil', a) for a in range(number_of_annihilators)]
    def product_s(a, b):
        if a == 'zero' or b == 'zero':
            return 'zero'
        if a[0] == 'nil' or b[0] == 'nil' or a[1] != b[1]:
            return 'zero'
        return ('group', a[1], (a[2] + b[2]) % group_orders[a[1]])
    m = max(1, t + (2 if number_of_annihilators else 0))
    def embedding(a):
        if a == 'zero':
            return None
        if a[0] == 'group':
            i, value = a[1], a[2]
            coord = tuple(value if j == i else 0 for j in range(len(orders)))
            return i, coord, i
        coord = (0,) * t + (a[1],)
        return t, coord, t + 1
    def brandt_product(a, b):
        if a is None or b is None or a[2] != b[0]:
            return None
        result = tuple((x + y) % z for x, y, z in zip(a[1], b[1], orders))
        return a[0], result, b[2]
    images = {a: embedding(a) for a in elements}
    assert len(set(images.values())) == len(elements)
    assert all(brandt_product(images[a], images[b]) == images[product_s(a, b)]
               for a, b in product(elements, repeat=2))
    assert all(brandt_product(images[a], images[b]) ==
               brandt_product(images[b], images[a])
               for a, b in product(elements, repeat=2))
    return len(elements), m

if __name__ == '__main__':
    print('B2(trivial) subsemigroups, congruences, commutative quotients:',
          *exhaustive_quotients())
    for groups, count in [([], 4), ([2], 0), ([2, 3], 3), ([1, 2, 2], 1)]:
        print('explicit embedding', groups, count, construction(groups, count))
    print('VERIFY_OK')
