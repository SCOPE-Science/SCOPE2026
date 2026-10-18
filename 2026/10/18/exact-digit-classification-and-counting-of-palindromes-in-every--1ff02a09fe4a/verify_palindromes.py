"""Standalone exact verification of simultaneous base-power palindrome formulas.

Runs without non-standard modules. The checks are finite tests of an independently
proved classification; they do not establish the universal theorem by themselves.
"""

def digits(n, base):
    assert n >= 1 and base >= 2
    out = []
    while n:
        out.append(n % base)
        n //= base
    return out[::-1]


def palindrome(s):
    return s == s[::-1]


def classified(s, k):
    L = len(s)
    q, r = divmod(L, k)
    if r == 0:
        blocks = [s[j*k:(j+1)*k] for j in range(q)]
        return all(palindrome(x) for x in blocks) and blocks == blocks[::-1]
    payloads = [s[:r]]
    for j in range(q):
        block = s[r+j*k:r+(j+1)*k]
        if block[:k-r] != [0] * (k-r):
            return False
        payloads.append(block[k-r:])
    return all(palindrome(x) for x in payloads) and payloads == payloads[::-1]


def formula(b, k, L):
    q, r = divmod(L, k)
    if r == 0:
        free = ((k + 1) // 2) * ((q + 1) // 2)
    else:
        free = ((r + 1) // 2) * ((q + 2) // 2)
    return (b-1) * (b ** (free - 1))


def symbolic_dimension(k, L):
    """Independent equality-constraint union/find calculation."""
    parent = list(range(L))
    q, r = divmod(L, k)
    if q == 0:
        return (L + 1) // 2
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    def eq(a, b):
        parent[root(a)] = root(b)
    for i in range(L):
        eq(i, L - 1 - i)
    forced_zero = []
    if r:
        # Digit positions are measured from the least significant end.
        forced_zero.extend(range(r, k))
        for t in range(r):
            eq(t, q*k+t)
        for j in range(1, q):
            for t in range(k):
                eq(j*k+t, (q-j)*k+t)
    else:
        for j in range(q):
            for t in range(k):
                eq(j*k+t, (q-1-j)*k+t)
    zeros = {root(t) for t in forced_zero}
    assert root(L-1) not in zeros, (k,L,'leading digit forced zero')
    return len({root(i) for i in range(L)} - zeros)


def verify():
    profiles = 0
    checked_numbers = 0
    accepted_numbers = 0
    for b in (2,3):
        for k in range(2,8):
            max_L = 14 if b == 2 else 9
            for L in range(1, max_L+1):
                count = 0
                for n in range(b**(L-1), b**L):
                    s = digits(n,b)
                    by_conversion = palindrome(s) and palindrome(digits(n,b**k))
                    by_structure = classified(s,k)
                    assert by_conversion == by_structure, (b,k,L,n,by_conversion,by_structure)
                    count += by_conversion
                    checked_numbers += 1
                assert count == formula(b,k,L), (b,k,L,count,formula(b,k,L))
                accepted_numbers += count
                profiles += 1
    symbolic_profiles = 0
    for k in range(2,18):
        for L in range(1, 14*k+1):
            q, r = divmod(L,k)
            if r == 0:
                free = ((k+1)//2)*((q+1)//2)
            else:
                free = ((r+1)//2)*((q+2)//2)
            assert symbolic_dimension(k,L) == free, (k,L)
            symbolic_profiles += 1
    print(f'VERIFY_OK numeric_profiles={profiles} tested_integers={checked_numbers} accepted={accepted_numbers} symbolic_profiles={symbolic_profiles}')

if __name__ == '__main__':
    verify()
