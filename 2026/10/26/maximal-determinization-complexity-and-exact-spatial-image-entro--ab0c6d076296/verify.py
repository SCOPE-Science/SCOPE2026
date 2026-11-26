"""Exact access and continuation certificates for Rule 73's 16-state DFA."""
from itertools import product


def main():
    arcs = [
        (2*a+b, 2*b+c, int((a,b,c) in {(0,0,0),(0,1,1),(1,1,0)}))
        for a,b,c in product((0,1), repeat=3)
    ]
    access = (
        '100111', '111', '1110', '110', '10011', '11', '1100', '11000',
        '11001', '1101', '11010', '10', '1001', '1', '100', '',
    )
    for m,w in enumerate(access):
        dest = set(range(4))
        for b in map(int, w):
            dest = {j for i,j,a in arcs if i in dest and a == b}
        assert sum(1<<i for i in dest) == m, (m,w,dest)

    suffixes = ('111', '11001', '0111', '10011')
    for i,w in enumerate(suffixes):
        origins = set(range(4))
        for b in map(int, reversed(w)):
            origins = {j for j,k,a in arcs if k in origins and a == b}
        assert origins == {i}, (w,origins)
    print('16 reachable masks; backward continuation supports 1, 2, 4, 8')


if __name__ == '__main__':
    main()
