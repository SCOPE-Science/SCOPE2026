"""Finite cross-checks for a length-sparse binary-palindrome construction.

The proof of the infinite statements is in the accompanying mathematical note;
this program checks small lengths, arithmetic statements, and finite examples.
"""

def palindromes(length):
    h = (length + 1) // 2
    for prefix in range(1 << (h - 1), 1 << h):
        a = format(prefix, f'0{h}b')
        yield int(a + (a[:-1] if length % 2 else a)[::-1], 2)

for length in range(3, 19):
    a = list(palindromes(length))
    aset = set(a)
    assert len(a) == 1 << ((length + 1)//2 - 1)
    # No three distinct palindromes of equal length form an AP.
    for i, x in enumerate(a):
        for y in a[i+1:]:
            assert 2*y - x not in aset, (length, x, y, 2*y-x)
    if length % 2:
        h = (length - 1)//2
        assert a[0] == 2**(length-1)+1
        assert a[-1] == 2**length - 1
        assert a[1]-a[0] == a[-1]-a[-2] == 2**h
        # Check the small-first-term dichotomy for all ordered pairs.
        for i, y in enumerate(a):
            for z in a[i+1:]:
                x = 2*y-z
                if 0 < x < 2**h:
                    assert x == 3 and y == a[0] and z == a[-1]

# The first two selected odd lengths are 5 and 13.
chosen = sorted(set(palindromes(5)) | set(palindromes(13)))
chosen_set = set(chosen)
for i, x in enumerate(chosen):
    for y in chosen[i+1:]:
        assert 2*y-x not in chosen_set, (x,y,2*y-x)

for h in range(2, 9):
    length = 2*h+1
    count = sum(1 for ell in range(1, length+1) for _ in palindromes(ell))
    assert count == 3*2**h - 2
    assert len(list(palindromes(length))) == 2**h
    assert 2**h/count > 1/3
print('VERIFY_OK')
print('same_length_verified=3..18')
print('small_first_term_verified_odd=3..17')
print('lacunary_first_two_lengths=5,13')
print('relative_count_formula_h=2..8')
print('finite_checks_do_not_prove_infinite_statement=True')
