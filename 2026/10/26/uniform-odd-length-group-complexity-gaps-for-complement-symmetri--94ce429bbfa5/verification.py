"""Small finite checks for group complexity of the Thue--Morse word.

All general assertions are proved symbolically in the accompanying manuscript.
"""
from itertools import permutations


def morse_prefix(depth=13):
    s = '0'
    for _ in range(depth):
        s = ''.join('01' if a == '0' else '10' for a in s)
    return s


def factors(word, length):
    return {word[i:i+length] for i in range(len(word)-length+1)}


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def generated_subgroup(perms, gens):
    identity = tuple(range(len(perms[0])))
    H = {identity}
    changed = True
    while changed:
        old = len(H)
        H |= {compose(h, g) for h in tuple(H) for g in gens}
        changed = len(H) != old
    return frozenset(H)


def subgroup_spectrum(n, F):
    perms = list(permutations(range(n)))
    groups = {frozenset([tuple(range(n))])}
    while True:
        new = groups | {generated_subgroup(perms, tuple(H) + (g,))
                        for H in groups for g in perms}
        if len(new) == len(groups):
            break
        groups = new
    histogram = {}
    for H in groups:
        count = len({min(''.join(w[g[i]] for i in range(n)) for g in H) for w in F})
        histogram[count] = histogram.get(count, 0) + 1
    return histogram


def main():
    w = morse_prefix()
    for n in range(1, 11):
        F = factors(w, n)
        assert {''.join('1' if c == '0' else '0' for c in s) for s in F} == F
        assert len(F) >= 2*n
        if n % 2:
            assert len(F) % 2 == 0
    F2, F3 = factors(w, 2), factors(w, 3)
    assert F2 == {'00', '01', '10', '11'}
    assert F3 == {'001', '010', '011', '100', '101', '110'}
    assert subgroup_spectrum(2, F2) == {3: 1, 4: 1}
    assert subgroup_spectrum(3, F3) == {2: 2, 4: 3, 6: 1}
    print('THUE_MORSE_COMPLEMENT_AND_GROUP_SPECTRUM_OK')
    print('n=2: p=4, p_ab=3, group spectrum {3:1, 4:1}')
    print('n=3: p=6, p_ab=2, group spectrum {2:2, 4:3, 6:1}')
    print('Complement closure and p(n)>=2n checked for 1<=n<=10')

if __name__ == '__main__':
    main()
