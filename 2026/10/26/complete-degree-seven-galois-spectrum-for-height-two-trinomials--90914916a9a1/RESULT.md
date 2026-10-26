# Complete degree-seven Galois spectrum for height-two trinomials

## Finding

For each integer \(1\le k\le6\), each \(a\in\{-2,2\}\), and each \(b\in\{-1,1\}\), set \(f_{k,a,b}(X)=X^7+aX^k+b\). All \(24\) polynomials are separable over \(\mathbb Q\), and their splitting fields over \(\mathbb Q\) have precisely the following Galois-group classification. The triples in each line are \( (k,a,b) \):

- \(\operatorname{Gal}(f)\cong S_7\): \((1,2,-1)\), \((1,2,1)\), \((2,-2,-1)\), \((2,2,1)\), \((5,2,-1)\), \((5,2,1)\), \((6,-2,-1)\), \((6,2,1)\).
- \(\operatorname{Gal}(f)\cong S_6\): \((1,-2,-1)\), \((1,-2,1)\), \((3,-2,-1)\), \((3,-2,1)\), \((4,-2,1)\), \((4,2,-1)\), \((6,-2,1)\), \((6,2,-1)\).
- \(\operatorname{Gal}(f)\cong S_3\times S_3\): \((2,-2,1)\), \((2,2,-1)\), \((5,-2,-1)\), \((5,-2,1)\).
- \(\operatorname{Gal}(f)\cong S_3\times S_4\): \((3,2,-1)\), \((3,2,1)\), \((4,-2,-1)\), \((4,2,1)\).

In particular, the frequency of each of the four isomorphism types \(S_7\), \(S_6\), \(S_3\times S_3\) and \(S_3\times S_4\) is exactly eight, eight, four and four, respectively. Every occurring Galois group is the full product of symmetric groups allowed by the irreducible factor degrees.

## Assumptions and scope

The ground field is \(\mathbb Q\), the exponent is exactly seven, the middle coefficient has absolute value two, and the constant coefficient has absolute value one. Since seven is prime, each \(1\le k\le6\) is relatively prime to seven. \(\operatorname{Gal}(f)\) means the automorphism group of the entire splitting field, not the group of an individual factor. Each classification applies to all, and only, the twenty-four triples above.

## Proof

**1. Rational factorization.** For every triple, the complete list of primitive monic factors as integer coefficient arrays is given in `CERTIFICATE.json`, under `rows`. Multiplying those arrays as integer polynomials yields \(X^7+aX^k+b\). They are squarefree; the only possible degree multisets are \( (7)\), \((1,6)\), \((1,3,3)\) and \((3,4)\). The certificate includes an exact finite-field irreducibility witness for each of its twenty-eight distinct nonlinear factor polynomials. A monic integral factor remaining irreducible modulo one prime is irreducible over \(\mathbb Q\) by Gauss's lemma, so the decompositions are indeed complete.

**2. Galois groups of the individual irreducible factors.** Let \(g\) be one of the irreducible nonlinear factors. For every listed witness prime \(p\), the reduction of \(g\) modulo \(p\) is squarefree (its discriminant is prime to \(p\)). Dedekind's Frobenius cycle-type theorem gives an element of \(\operatorname{Gal}(g)\) with the degrees of its distinct irreducible modular factors as cycle lengths. The `factor_certificates` array gives the actual primes and degree lists. The following uniform arguments apply to all distinct factors:

- Degree seven: cycle types \((7)\) and \((5,2)\) occur. Taking the fifth power of an element of cycle type \((5,2)\) yields a transposition. Irreducibility gives transitivity in prime degree seven, hence primitivity. A primitive subgroup of a symmetric group containing a transposition is the full symmetric group; therefore \(\operatorname{Gal}(g)=S_7\).
- Degree six: cycle types \((6)\), \((5,1)\), and \((3,2,1)\) occur. The element of type \((5,1)\) rules out a nontrivial invariant system of blocks: a transitive imprimitive action on six letters has blocks of size two or three, but an order-five permutation cannot act nontrivially either on the set of blocks or inside each block. The cube of an element of type \((3,2,1)\) is a transposition. Consequently \(\operatorname{Gal}(g)=S_6\).
- Degree four: cycle types \((4)\) and \((3,1)\) occur. Among transitive subgroups of \(S_4\), only \(S_4\) contains both a four-cycle and a three-cycle: its order must be twelve or twenty-four by Lagrange's theorem; the only index-two subgroup of the symmetric group on four letters is the alternating group, which has no four-cycles. Thus \(\operatorname{Gal}(g)=S_4\).
- Degree three: a modular factor type \((3)\) proves irreducibility. The exact discriminant is either \(-23\) or \(-31\); each is nonsquare. A transitive subgroup of \(S_3\) with nonsquare discriminant is \(S_3\).

**3. Disjoint splitting fields for reducible products.** For cases with two cubic factors, their discriminants are \(-23\) and \(-31\), so their unique quadratic splitting subfields \(\mathbb Q(\sqrt{-23})\) and \(\mathbb Q(\sqrt{-31})\) differ. The only nontrivial proper quotient of \(S_3\) is \(C_2\). The intersection of two Galois splitting fields is Galois over \(\mathbb Q\), hence its Galois group is a common quotient; it must be trivial. The compositum therefore has group \(S_3\times S_3\).

For cases with an irreducible cubic and quartic, the cubic discriminant is \(-23\) and the quartic discriminant is \(257\). The only common nontrivial quotients of \(S_3\) and \(S_4\) are \(C_2\) and \(S_3\); in either case a common quotient entails the same quadratic subfield. The distinct quadratic fields \(\mathbb Q(\sqrt{-23})\) and \(\mathbb Q(\sqrt{257})\) exclude it. The compositum consequently has group \(S_3\times S_4\). Linear factors have rational roots and do not alter splitting fields. This proves every case.

## Verification

The standalone script `verify.py`, executed with Python and SymPy, reads `CERTIFICATE.json`, regenerates the full family, multiplies every recorded integer factorization, checks all \(28\) factor discriminants and the supplied modular splitting types at their actual primes, tests both quadratic-disjointness patterns, and recomputes the four group frequencies. The executed result was `CERTIFICATE_OK rows=24 nonlinear_factors=28 groups={'S7': 8, 'S6': 8, 'S3xS3': 4, 'S3xS4': 4}`. The argument from modular witnesses to infinite-field Galois groups is the theorem proved above, not an extrapolation from experiments.

## Relationship to prior work

Garmi's 2026 Theorem 1.1 establishes maximal permitted Galois groups for small-coefficient trinomials subject to sufficiently large degree, and explicitly gives the bound \(n>8\) when the coefficient product has magnitude two. Its degree-seven boundary is not covered by that theorem; the current classification identifies reducible degree-seven exceptions and computes the entire splitting-field groups, including whether distinct nonlinear factors have entangled splitting fields. Filaseta–Murphy–Vincent (2019) classify reducibility patterns of polynomials of small Euclidean norm; a factorization classification alone does not establish the group structure or splitting-field disjointness here. Cohen–Movahhedi–Salinier (1999) study Galois groups of irreducible trinomials under various hypotheses, which does not directly classify Galois groups of the reducible septics above.

## Limitations

This is a fixed-degree, fixed-coefficient classification; no claim is made for other degrees or coefficients. The factorization cases may already be implicit in earlier work. The absence of a matching full splitting-field catalogue from the accessed references and record searches is not a proof of priority or exhaustive literature coverage. The result has undergone self-review only and has not been independently validated.

## References

1. Hilel Garmi, *Galois Groups of Trinomials with Small Coefficients*, arXiv:2610.22764v1 (first public 16 October 2026), https://arxiv.org/html/2610.22764v1, Theorem 1.1 and Section 4.
2. Michael Filaseta, Robert Murphy and Andrew Vincent, *Computationally classifying polynomials with small Euclidean norm having reducible non-reciprocal parts*, Banach Center Publications 118 (2019), 245–259, DOI 10.4064/bc118-15.
3. S. D. Cohen, A. Movahhedi and A. Salinier, *Galois Groups of Trinomials*, Journal of Algebra 222 (1999), 561–573, DOI 10.1006/jabr.1999.8033.
