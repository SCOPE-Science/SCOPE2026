# Independent mathematical audit

## correctness

PASS

For N>5 and 5|N, Kummer/Legendre makes v2 of the restricted binomial gcd equal the least binary carry count among 5|k, 0<k<N. Valuation zero is equivalent to a proper nonempty zero-sum submultiset of the occupied binary digit residues 1,2,4,3 modulo5. Minimal zero-sum multisets of nonzero C5 residues have at most five terms; independent enumeration gives exactly fourteen shapes: 2 length2,4 length3,4 length4,4 length5. Splitting one positive-position power into its two halves gives a one-carry witness for ordinary minimal shapes; parity restrictions obstruct it for odd minimal {1,2,2} (valuation2) and for odd two-term {1,4} (valuation3). Positive even two-term minimal cases have v2=2. The explicit two/three carry constructions in the source prove all remaining upper bounds. Thus maximum v2=3 precisely N=2^(4h+2)+1, h>=1. Independently checked the 14 shape classifications and directly minimized s2(k)+s2(N-k)-s2(N) for every multiple of five from N=10 to 3000 (599 N); no mismatch, max3 at N=65,1025. Infinite proof rests on carry-splitting, not finite brute force.

## originality

PASS

Fairfax-Ball arXiv:2609.37754v1 studies the same restricted gcd, proving special p congruent to -1 mod m and recording prior p=+1 results. For modulus m=5, p=2 has order four and is neither +1 nor -1; the exact v2 branch classification therefore lies outside those theorems. McTague 2017 concerns same-residue congruence classes, and Wu 2026 studies related gcds but only title/abstract-level full coverage could be verified here. No indexed Resultary matching 14-shape binary mod5 case was found; this is best-of-knowledge, not priority certification.

## value

PASS

A fixed-modulus gcd with one prime whose multiplicative order is four is the naturally omitted next nontrivial case of the initiating restricted-binomial theorem. Resolving all residue-pattern branches and the maximal-power family gives an exact infinite arithmetic classification with explicit witnesses; not a routine substitution into the known ±1 congruence formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
