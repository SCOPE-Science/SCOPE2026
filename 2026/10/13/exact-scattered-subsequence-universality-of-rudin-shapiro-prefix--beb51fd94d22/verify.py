#!/usr/bin/env python3
"""Finite algebraic verification of a Rudin--Shapiro arch-cocycle identity.

The symbolic checks compare identities of affine polynomials in an
indeterminate, so they verify the induction step for every integer level,
not only for sampled levels. Direct scans are independent consistency checks.
"""
SUB = {'a': 'ab', 'b': 'ac', 'c': 'db', 'd': 'dc'}
COD = {'a': 0, 'b': 0, 'c': 1, 'd': 1}

# profile maps three input arch states to (output state, #completed arches)
# input state 0 = empty, 1 = only 0 seen, 2 = only 1 seen.
def symbol(bit):
    return [((1 if bit == 0 else 2), 0),
            ((0, 1) if bit == 1 else (1, 0)),
            ((0, 1) if bit == 0 else (2, 0))]

def compose(p, q):
    return [(q[s][0], k + q[s][1]) for s, k in p]

def nxt(profiles):
    return {letter: compose(profiles[pair[0]], profiles[pair[1]])
            for letter, pair in SUB.items()}

def direct_profiles(k):
    p = {letter: symbol(bit) for letter, bit in COD.items()}
    for _ in range(k):
        p = nxt(p)
    return p

# affine-polynomial profiles: (exit_state, coeff, constant) for coeff*q + constant,
# q = 5*2^(m-4); base m=4, and q doubles whenever m increments.
E = {
 'a': [(2,1,-1),(2,1,-1),(2,1,0)],
 'b': [(1,1,0),(1,1,0),(1,1,1)],
 'c': [(2,1,0),(2,1,1),(2,1,0)],
 'd': [(1,1,-1),(1,1,0),(1,1,-1)],
}
O = {
 'a': [(1,1,0),(1,1,0),(1,1,1)],
 'b': [(2,1,-1),(2,1,-1),(2,1,0)],
 'c': [(1,1,-1),(1,1,0),(1,1,-1)],
 'd': [(2,1,0),(2,1,1),(2,1,0)],
}

def symbolic_compose(p, q):
    return [(q[s][0], a+q[s][1], b+q[s][2]) for s,a,b in p]

def symbolic_next(profiles):
    return {letter:symbolic_compose(profiles[image[0]],profiles[image[1]])
            for letter,image in SUB.items()}

def expect_double(profile):
    return {letter:[(s,2*a,b) for s,a,b in values] for letter,values in profile.items()}

assert direct_profiles(4) == {
 letter:[(s,5*a+b) for s,a,b in values] for letter,values in E.items()}
assert symbolic_next(E) == expect_double(O)
assert symbolic_next(O) == expect_double(E)
# The four small block sizes satisfy the uniform per-block discrepancy.
for k in range(4):
    expected = 5 * (1 << k) / 16
    for entry in direct_profiles(k).values():
        assert all(abs(count - expected) <= 1 for _,count in entry)

# Independent RS sequence oracle from overlapping digit 11 occurrences.
def rs(n):
    return ((n & (n >> 1)).bit_count() & 1)

# Morphism coding equals the digit oracle for a substantial finite prefix.
w = 'a'
for k in range(1,18):
    w = ''.join(SUB[x] for x in w)
    if k <= 12:
        assert all(COD[ch] == rs(i) for i,ch in enumerate(w))

# A scan of binary prefixes, independent of symbolic composition.
NMAX = 1 << 18
state = 0
arches = 0
exact_levels = 0
for i in range(NMAX):
    bit = rs(i)
    if state == 0:
        state = 1 + bit
    elif (state == 1 and bit == 1) or (state == 2 and bit == 0):
        arches += 1
        state = 0
    n = i + 1
    assert abs(16*arches-5*n) <= 16*n.bit_count(), (n, arches)
    if n & (n-1) == 0:
        m = n.bit_length()-1
        target = ({0:0,1:0,2:1,3:2}[m] if m < 4 else
                  5*(1 << (m-4)) - int(m%2 == 0))
        assert arches == target, (m, arches, target)
        if m >= 4:
            assert arches == direct_profiles(m)['a'][0][1]
        exact_levels += 1

# An additional independent brute-force subsequence test at small lengths.
def embeds(w, pattern):
    p=0
    for bit in w:
        if p<len(pattern) and bit==pattern[p]:
            p+=1
    return p==len(pattern)

def brute_univ(w):
    k=0
    while k<=len(w)+1:
        if any(not embeds(w,tuple((x>>j)&1 for j in range(k)))
               for x in range(1<<k)):
            return k-1
        k+=1
    raise AssertionError('invalid')
for n in range(0,23):
    word=[rs(j) for j in range(n)]
    state=0;cnt=0
    for bit in word:
        if state==0:state=1+bit
        elif (state==1 and bit==1) or (state==2 and bit==0):cnt+=1;state=0
    assert brute_univ(word)==cnt

print('VERIFY_OK symbolic_induction=even_to_odd_and_odd_to_even'
      ' small_block_bounds=yes morphism_prefix=2^12 direct_prefixes=262144'
      ' exact_dyadic_levels=19 brute_subsequences_lengths=0..22')
