"""Independent finite consistency checks for the matching-face-poset theorem."""
from itertools import combinations


def matchings(n):
    edges = list(combinations(range(n), 2))
    out = []
    def visit(pos, occupied, selected):
        if pos == len(edges):
            out.append(frozenset(selected))
            return
        visit(pos + 1, occupied, selected)
        u, v = edges[pos]
        if u not in occupied and v not in occupied:
            selected.append(pos)
            visit(pos + 1, occupied | {u, v}, selected)
            selected.pop()
    visit(0, set(), [])
    return out


def profile(face, faces):
    result=set()
    for other in faces:
        if face==other: result.add('eq')
        elif face < other: result.add('up')
        elif other < face: result.add('down')
        else: result.add('incomp')
    return frozenset(result)


def parity_witness(faces):
    for x in faces:
        extensions = [y for y in faces if x < y]
        if len(extensions)==1: return x,extensions[0]
    return None


def run():
    stable=None
    for n in range(2,10):
        faces=matchings(n)
        types=frozenset(profile(x,faces) for x in faces)
        hit=parity_witness(faces)
        assert bool(hit)==(n%2==0)
        if n>=4:
            if stable is None: stable=types
            assert stable==types
            assert len(types)==3
        elif n==3: assert len(types)==2
        else: assert len(types)==2
        print(f'n={n}, faces={len(faces)}, two_round_pointed_types={len(types)}, parity_witness={bool(hit)}, stable={n>=4}')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':run()
