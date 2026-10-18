# Independent mathematical audit

## correctness

PASS

Set a=qM+r with 1<=r<M, gcd(r,M)=1. Reconstructed T(a/M)=q(M+r)/M, first reduced denominator d=M/gcd(q,M); exact order two iff d>1 and d divides Q=q+floor(qr/M), where q<=Q<=2q-1. The quotient-exclusion cases for k=2s, k=2s+1 at p odd, and k odd at p=2 rule out every smaller q using p-adic valuation and d>Q. For odd p, the candidate q=p^s(p+1)/2 requires Q=p^(s+1), fixing the minimal r0=ceil[M(p-1)/(p+1)]; modular calculation proves p does not divide r0. Even-exponent and odd binary choices use r=1. Directly checked M=2 special mu=7. An independent fresh exact Fraction enumeration verified candidates and excluded 83714 smaller coprime numerators for 32 prime-power cases <=1000, while the all-prime proof is the quotient/divisibility argument, not this enumeration.

## originality

PASS

Carvalho 2026 explicitly poses determination of mu(M,n) as Question 3.5, gives denominator-two instance and general congruence counting but no inspected uniform prime-power order-two minimum. The assessed formula resolves the natural first nontrivial order and every prime-power denominator with a valuation-parity phase transition. The denominator-two case is explicitly previously known; the separate older x ceil(x) map has different dynamics. Historical unindexed equivalent congruence minimizations remain a priority risk.

## value

PASS

The first admissible numerator for rational-entry time is an explicit open invariant in the exact source, and order two is its first nontrivial stopping case. An all-parameter prime-power solution with minimum witness, coprimality proof and parity/2-adic exceptional transition is a mathematically motivated exact classification. It is not a restatement of how many residue classes exist or a finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
