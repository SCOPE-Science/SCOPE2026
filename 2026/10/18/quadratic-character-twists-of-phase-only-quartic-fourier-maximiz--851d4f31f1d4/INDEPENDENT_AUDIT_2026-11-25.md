# Independent mathematical audit

## correctness

PASS

The unnormalized transform with the average over both dual coordinates gives the exact sum of squared phase sums over ordered two-sum fibers. All 19 input values have modulus one. The constant input reaches the triangle-inequality bound, and equality forces product phases to agree in every individual fiber. A separate exhaustive enumeration gave the ordered histogram {1:19,2:99,4:36}, hence 991; the 36 nontrivial comparisons are precisely the two disjoint 18-element dilation orbits of the displayed seeds, with no relation involving the zero coordinate. For normalized nonzero sum the two distinct pair products add to 2 and the simultaneous discriminant test leaves {4,17} and {8,13}. The comparison products have the same quadratic character; multiplying by ζ^(At+Bt⁴) also preserves each comparison. Independently rebuilt from the first seed and multipliers 1,…,17, the 17-square deleted-coordinate minor has exact Bareiss determinant 722. Deleting coordinate 18 is an integral coordinate chart on the degree-zero lattice, so the minor cuts the projective phase characters down to a group of order 722, not merely to dimension zero. All 722 candidate triples give distinct projective characters: an odd-order phase cannot cancel the nonconstant quadratic sign up to a scalar, and a degree-at-most-four polynomial constant at 18 nonzero inputs is constant as a polynomial. All candidates satisfy the remaining relations; hence the upper count is exhausted. Both f(0) and the common nonzero-coordinate phase are arbitrary unit scalars, so each projective nonzero pattern lifts to a disjoint two-torus, or a circle after common-phase quotient. To replay, bucket all 19² pairs by (a+b,a⁴+b⁴) modulo 19, compare their unordered pair classes and quadratic signs, then build the minor from the 17 rows in RESULT.md lines 51–61 and compute its integer determinant. The separate exact replay took 0.009 s. The supplied artifacts/verify.py and recorded output were inspected but not executed. Neither proof nor computation covers other primes or amplitude-unrestricted extension.

## originality

PASS

Pass for the complete phase-only equality classification at 19, especially the order-two character twist and exhaustive 722 projective patterns. The value 991 is already a specialization of the cited quartic additive-energy formula and is explicitly excluded from the novelty claim. The strongest same-object alternative optimizes a different input class and does not cover this equality set.

## value

PASS

Characterizing every extremizing phase on this natural quartic Fourier graph is a structural question not answered by computing its energy. The non-Sidon collisions leave a genuine order-two family beyond additive phases and an independent phase at zero. The exact discrete component count distinguishes this from a generic numerical optimum or an arbitrary small-field test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
