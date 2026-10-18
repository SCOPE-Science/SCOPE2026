"""Independent finite test of directed Young-diagram counting refinement (stdlib)."""
from collections import Counter, defaultdict


def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None:
        cap = n
    for a in range(min(n, cap), 0, -1):
        for tail in partitions(n-a, a):
            yield (a,) + tail


def conjugate(lam):
    return tuple(sum(r > j for r in lam) for j in range(lam[0]))


def build(lam):
    cells = [(r, c) for r, width in enumerate(lam) for c in range(width)]
    positions = {p: k for k, p in enumerate(cells)}
    incoming = [[] for _ in cells]
    outgoing = [[] for _ in cells]
    for k, (r, c) in enumerate(cells):
        for target in [(r+1, c), (r, c+1)]:
            if target in positions:
                t = positions[target]
                outgoing[k].append(t)
                incoming[t].append(k)
    return cells, incoming, outgoing


def joint_refinement(shapes):
    incoming, outgoing, labels, pieces = [], [], [], []
    for p, shape in enumerate(shapes):
        cells, ins, outs = build(shape)
        offset = len(labels)
        pieces.append((offset, len(cells), cells))
        incoming.extend([[v+offset for v in row] for row in ins])
        outgoing.extend([[v+offset for v in row] for row in outs])
        labels.extend([p]*len(cells))
    color = [0]*len(labels)
    for rounds in range(len(labels)+1):
        patterns = [(color[v], tuple(sorted(color[u] for u in incoming[v])),
                     tuple(sorted(color[u] for u in outgoing[v]))) for v in range(len(labels))]
        dictionary = {pattern: k for k, pattern in enumerate(sorted(set(patterns)))}
        change = [dictionary[pattern] for pattern in patterns]
        if change == color:
            break
        color = change
    else:
        raise AssertionError('colour sequence did not stabilize')
    return color, pieces, rounds


def check(bound=18):
    shapes_tested = 0
    for n in range(1, bound+1):
        shapes = list(partitions(n))
        colors, pieces, rounds = joint_refinement(shapes)
        groups = defaultdict(list)
        for shape, (offset, size, cells) in zip(shapes, pieces):
            internal = defaultdict(set)
            for p, col in zip(cells, colors[offset:offset+size]):
                internal[col].add(p)
            symmetric = shape == conjugate(shape)
            for same in internal.values():
                p = next(iter(same))
                predicted = ({p, (p[1], p[0])} if symmetric else {p})
                assert same == predicted, (shape, same, predicted)
            profile = tuple(sorted(Counter(colors[offset:offset+size]).items()))
            groups[profile].append(shape)
        if n == 8:
            from math import comb
            a, b = (4,3,1), (4,2,2)
            def path_profile(shape):
                return sorted((i+j, comb(i+j, i)) for i,w in enumerate(shape) for j in range(w))
            assert path_profile(a) == path_profile(b)
            signatures = {shape:tuple(sorted(Counter(colors[o:o+size]).items()))
                          for shape, (o,size,_) in zip(shapes,pieces)}
            assert signatures[a] != signatures[b]
        for members in groups.values():
            base = members[0]
            assert set(members) == {base, conjugate(base)}, (n, members)
        shapes_tested += len(shapes)
        print('SIZE', n, 'partitions', len(shapes), 'conjugacy_classes',len(groups),
              'stable_rounds',rounds, 'PASS')
    print('GLOBAL_PASS', 'shapes', shapes_tested, 'maximum_n', bound)

if __name__ == '__main__':
    check()
