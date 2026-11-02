"""Independent BWT inversion and cyclic-rotation reconstruction of every witness.
Run: python3 verify_inverse.py witnesses.tsv
The check does not rely on the Hamming-distance formula or on verify_direct.py.
"""
import sys


def invert(last):
    # Sort the last-column indices by (symbol, their original position).
    ordered=sorted(range(len(last)), key=lambda j: (last[j], j))
    rank=[0]*len(last)
    for first_row, old_row in enumerate(ordered):
        rank[old_row]=first_row
    index=0
    source=[]
    seen=set()
    for _ in last:
        assert index not in seen
        seen.add(index)
        source.append(last[index])
        index=rank[index]
    assert index==0
    return ''.join(reversed(source))


def bwt_by_sorting_rotations(source):
    shifts=[source[i:]+source[:i] for i in range(len(source))]
    assert len(set(shifts))==len(source)  # primitive necklace
    shifts.sort()
    return ''.join(s[-1] for s in shifts)


def cyclic_runs(word):
    return sum(word[i]!=word[(i+1)%len(word)] for i in range(len(word)))


def main(path):
    with open(path,encoding='utf-8') as handle:
        assert handle.readline().rstrip('\n')=='n\tL'
        sizes=[]
        for line in handle:
            n,last=line.strip().split('\t');n=int(n)
            assert len(last)==n
            source=invert(last)
            assert bwt_by_sorting_rotations(source)==last
            assert all(last[i]!=last[i+1] for i in range(n-1))
            assert cyclic_runs(source)==(n+1)//2
            sizes.append(n)
    assert sizes==list(range(31,65))
    print(f'PASS inverse BWT/primitive-rotation/cyclic-run verification: {len(sizes)} witnesses, n={sizes[0]}..{sizes[-1]}')

if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else 'witnesses.tsv')
