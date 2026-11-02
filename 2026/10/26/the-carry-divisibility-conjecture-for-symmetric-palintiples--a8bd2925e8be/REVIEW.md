# Independent mathematical audit

## correctness

PASS

Given 1<n<b, a genuine nonzero-ended base-b digit reversal multiple of length k+1 and carries c0=c_(k+1)=0 with symmetric c_j=c_(k−j), eliminate the two grade-school equations to obtain (n²−1)d_j=nbc_(k−j+1)−nc_(k−j)+bc_(j+1)−c_j. Symmetry gives c_k=0 and first digit identity (n²−1)d0=bc1, forcing c1>0, and b(nc_(j−1)+c_(j+1))≡(n+1)c_j mod n²−1 for 1≤j≤k−1. For every prime ℓ|n−1, set a=vℓ(n−1), q=vℓ(n+1), t=vℓ(b). If t≤q, the first equation makes c1 multiple ℓ^a and congruence inductively propagates. If t>q, take a carry of globally least ℓ-valuation s<a: left side has valuation ≥t+s and right (n+1)c_j has exactly q+s<a+q, so their difference cannot vanish mod ℓ^(a+q). Thus n−1 divides every carry. Since 0≤c_j≤n−1, all carries are 0 or n−1; c1=n−1 and n+1|b by first identity. Holt 2014 Theorem 6 supplies the converse. This handles ℓ=2, n=2, all k and noncoprime cases; no finite cutoff is used. Independently enumerated 52 actual valid small digit-reversal multiples with symmetric carries and checked all conclusions.

## originality

PASS

The mathematical statement is explicitly Holt 2015 Conjecture 1: symmetric palintiple carries divisible by n−1. Holt 2014 Theorem 6 proves sufficiency n+1|b and Theorem 7 obtains necessity only when gcd(b,n−1)=1. Kendrick 2015 characterizes an associated Young graph as 1089 iff n+1|b but does not establish every symmetric palintiple arises on that graph; its Remark 4 recognizes the conjectural direction. Holt 2025 works on general permutiples and reflected permutiple graph classes, whose symmetry is not carry symmetry. Available inspected full primary sources and scholarly searches reveal no resolution, while later unindexed digit-reversal proofs remain a priority risk. The new two-case local valuation argument resolves the exact historical conjecture without relying on computer enumeration.

## value

PASS

An explicit published all-base, all-length arithmetic conjecture is resolved, including precisely the noncoprime case that blocked Holt 2014. This is substantive and naturally motivated arithmetic structure, not an arbitrary small numerical pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
