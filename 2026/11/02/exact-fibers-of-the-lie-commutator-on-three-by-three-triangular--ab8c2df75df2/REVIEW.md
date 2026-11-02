# Assessment of the triangular commutator fiber theorem

## Correctness — PASS

The matrix-entry calculation gives the exact dot-product/determinant identity, with two independent scalar diagonal degrees of freedom. Separating the nonzero and zero sum of the two coefficient vectors gives independent, exhaustive disjoint cases. Counts for dot-product constraints and fixed determinants in \(k^2\) yield the formula in every characteristic; boundary cases \(u=v=0\), \(w=0\), and \(q=2\) were checked explicitly. The probability statement follows from cancelling the correction upon summation. The standalone program directly checks all output fibers for \(q=2,3\) and uses a separate exhaustive intermediate-level enumeration for \(q=4,5\). Nonstandard steps have complete derivations in RESULT.md, so numerical logs are not a replacement for the proof.

## Originality — PASS (historical risk retained)

A search of the available research records for exact nonzero Lie-commutator fibers on triangular \(3\)-by-\(3\) algebras found no matching record. The closest previously catalogued scientific statements concern rank distributions of commutators on rectangular-band semigroup algebras, Lie commutators of rank-one nilpotent matrices, and all-arity involution commutation in unitriangular groups. None logically supplies the present fixed-target, four-stratum distribution. Full or relevant original sections of the main primary sources were inspected: Britnell–Wildon study existence of commuting full-matrix similarity classes; Goodwin–Röhrle study zero-bracket nilradical components; Wang–Zhu–Rou study commutativity preservers; Kaur–Sharma–Singh study commuting *invertible groups* and branching matrices, not this singular-inclusive additive-bracket distribution. The closest unrestricted prior theme is commuting probability, which determines only the zero fiber. De Mello (arXiv:1910.05469, Theorem 6) and Gargate–de Mello (arXiv:2106.12726, Theorem 4.3) already determine the images of multilinear polynomials on triangular algebras over infinite fields: surjectivity of the commutator onto the radical in that setting is **not novel**. Neither theorem supplies target-conditioned finite-field fiber sizes or the sharp output-distribution defect. An equivalent earlier formula under a different commutator-distribution terminology remains possible, and an independent comprehensive priority audit has not been performed.

## Value — PASS

The problem is the complete finite-field pushforward distribution of a natural bilinear word map on the smallest triangular algebra whose radical is nonabelian. Unlike computing only the number of commuting pairs, the result determines every nonzero target fiber, proves exactly which coordinates are independent, and pinpoints a single exceptional simple-root stratum that accounts for all central-coordinate nonuniformity. The exact total-variation identity \((q-1)/q^5\) quantifies a mixing phenomenon across every finite extension and in characteristic two. The four-stratum invariant is an input for studying additive commutator equations and their convolution measures; it is not a numerical observation for an arbitrary subfamily.

## Limitations and closest literature

The theorem does not imply higher-size analogues, the corresponding multiplicative group commutator distribution, or geometric fiber irreducibility. Full-matrix similarity-class results and triangular group branching results do not directly imply the fixed-target law, but could conceivably be combined with further arguments to derive parts of it. Sources and comparison details are in RESULT.md and AUDIT.json. No independent mathematical review has been performed.

Self-review: passed. Independent audit: not yet performed.
