"""Standalone finite cross-check of exact factor and reflection formulas.
The infinite statements are proved separately by combinatorial arguments.
"""
from collections import defaultdict

def sequence_prefix(n):
    return ''.join(c*k for k in range(1,3*n+4) for c in '01')

def count_pairs_by_inequality(n):
    return sum(1 for a in range(1,n) for b in range(a+1,n) if a+2*b <= n)

def count_right_specials(w,n):
    extensions=defaultdict(set)
    for i in range(len(w)-n):
        extensions[w[i:i+n]].add(w[i+n])
    return {f for f, endings in extensions.items() if len(endings)==2}

def expected_specials(n):
    return ({'0'*n,'1'*n}
          | {'0'*a+'1'*(n-a) for a in range(1,n) if a<=n-a}
          | {'1'*a+'0'*(n-a) for a in range(1,n) if a+1<=n-a})

def check(n):
    w=sequence_prefix(n)
    factors={w[i:i+n] for i in range(len(w)-n+1)}
    orbits={min(f,f[::-1]) for f in factors}
    p=n*(n+1)//2+1
    r=(n*(n+1)+2)//3+1
    assert (len(factors),len(orbits))==(p,r),(n,len(factors),len(orbits),p,r)
    assert len(factors)-len(orbits) == (n-1)+count_pairs_by_inequality(n)+count_pairs_by_inequality(n-1)
    if n<=85:
        # Checking all right-special sets from same finite window requires
        # padding, already provided by 3n+3 full paired runs.
        actual=count_right_specials(w,n)
        expected=expected_specials(n)
        assert actual==expected, (n,sorted(actual^expected))

for n in range(1,141):check(n)
for n in range(1,1001):
    T=lambda m:sum(max(0,min(b-1,m-2*b)) for b in range(2,(m-1)//2+1))
    assert (n-1)+T(n)+T(n-1)==n*(n+1)//6
print('VERIFY_OK n=1..140 exact-factors/reversal-orbits n=1..85 right-special-sets n=1..1000 arithmetic-identity')
