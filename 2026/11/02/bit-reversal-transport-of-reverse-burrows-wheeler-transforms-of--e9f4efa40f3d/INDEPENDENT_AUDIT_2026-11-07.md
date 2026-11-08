# Independent mathematical audit

## correctness

PASS

Unique feedback table for each de Bruijn n-cycle follows from the bijective successor permutation pairing states 0u and 1u. Lexicographically sorting all n-bit prefixes (each appears exactly once) makes consecutive BWT predecessor bits the complementary pair (m_j,1-m_j). Reversal turns each BWT predecessor into the ORIGINAL next bit of the reversed state, replacing suffix j by fixed-width bit-reversal rev_{n-1}(j). Exactly 2^{n-1} within-block letter changes yield run formula r=2^n-T(m); run count is linear, not cyclic. Independent enumeration visited ALL 2^16 order-five Boolean feedback masks, identified 2048 single-cycle tables, computed forward/reverse BWT directly from sorted rotations, checked both full strings against symbolic block transport, and reproduced the claimed nine-class difference spectrum 4,44,216,436,648,436,216,44,4. The all-order transport rests on symbolic proof, not the finite census.

## originality

PASS

Higgins gives complementary BWT two-character blocks for de Bruijn sets (forward direction) and existing classifications tabulate the one-dimensional order-five marginal. Neither the forward-only blocks nor known marginals alone determine the fixed bit-reversal *reverse* permutation or its joint run-count spectrum. Broader reversal-sensitivity work treats other word classes. These prior components are expressly excluded from the novel claim.

## value

PASS

The all-order exact reversal transport gives a structural relation between two transforms, and the complete n=5 joint census quantifies sensitivity that univariate BWT run tables cannot reconstruct. Exact sharp discrepancy and witnesses are natural finite invariants of de Bruijn cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
