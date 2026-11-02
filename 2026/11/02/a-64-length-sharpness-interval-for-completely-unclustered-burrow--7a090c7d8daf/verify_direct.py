"""Independently verify the finite witness conditions via LF cycles and Hamming distance.
Run: python3 verify_direct.py witnesses.tsv
Only the standard-library is needed.
"""
import sys


def confirm(n, last):
    assert len(last) == n and set(last) <= set('012')
    assert last.count('2') <= 6
    assert any(all(c == '2' or c == str((start + i) % 2)
                   for i, c in enumerate(last)) for start in (0,1))
    assert all(last[i] != last[i + 1] for i in range(n - 1))
    first = ''.join(sorted(last))
    assert sum(a != b for a,b in zip(first,last)) == (n + 1)//2
    counts = [last.count(str(a)) for a in range(3)]
    offsets = [0, counts[0], counts[0] + counts[1]]
    seen_occurrences = [0, 0, 0]
    permutation = []
    for character in last:
        a = int(character)
        permutation.append(offsets[a] + seen_occurrences[a])
        seen_occurrences[a] += 1
    assert sorted(permutation) == list(range(n))
    visited = set()
    state = 0
    while state not in visited:
        visited.add(state)
        state = permutation[state]
    assert state == 0 and len(visited) == n
    return tuple(counts)


def main(path):
    rows=open(path, encoding='utf-8').read().splitlines()
    assert rows.pop(0) == 'n\tL'
    observed=[]
    for line in rows:
        left,right=line.split('\t')
        n=int(left)
        counts=confirm(n,right)
        observed.append(n)
    assert observed == list(range(31,65))
    print(f'PASS direct LF-cycle/Hamming verification: {len(observed)} witnesses, n={min(observed)}..{max(observed)}')

if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else 'witnesses.tsv')
