# Review of the commuting-idempotent tuple enumerator

## Correctness

PASS. The proof constructs a conjugating unit explicitly: from commuting idempotents it builds orthogonal joint projectors and an invertible incidence-algebra element with diagonal one. The resulting stabilizer count has precisely one free field coordinate for each strict comparable pair carrying equal bit patterns, with nonzero independent diagonal entries. Orbit-stabilizer and a direct edge-subset expansion give both exact formulas, including characteristic two and all finite poset sizes. The bundled direct-convolution checker verifies representative small incidence algebras independently of orbit arguments; its finite range is not used as a general proof.

## Originality

PASS within the checked literature, subject to the explicit risks below. Can–Casimiro–Malheiro (2022) identify **single**-idempotent orbits over an algebraically closed field; Gargate–Gargate (2020) enumerate **single** potent elements over finite fields; Cheraghpour et al. (2024) study all-element commuting graphs of two-by-two triangular rings. Their mathematical statements do not give the joint diagonal classification for arbitrary commuting tuples or its comparability-graph Potts count. Separate searches for incidence-algebra commuting idempotents, triangular finite-field tuple enumeration, simultaneous conjugacy, exact tables, and Potts connections did not identify a stronger covering statement. Ring-theoretic lifting and unindexed enumeration literature remain residual originality risks; failure of a search is not treated as a proof of novelty.

## Value

PASS. Joint idempotent families are naturally finite Boolean projection systems inside incidence algebras. The theorem computes their entire ordered-tuple spectrum uniformly for every finite poset and field size, provides a tractable conceptual parameterization of orbits, and shows that this algebraic census is an antiferromagnetic Potts invariant of the comparability graph. This goes beyond isolated finite tables or the known one-idempotent case. The maximum multiway-cut interpretation also identifies the degree and leading coefficient of the counting polynomial.

## Closest literature and scientific limits

The nearest directly comparable theorem is Can–Casimiro–Malheiro, arXiv:2208.01073v1, Theorem 3.2, whose objects are individual idempotents in incidence monoids. Gargate–Gargate, arXiv:2009.04243v1, treat individual potent elements; the \(k=1\) specialization here is not claimed as new. Cheraghpour et al., arXiv:2402.12619v1, concern the full commuting graph of a particular triangular ring. A differently framed formula for commuting idempotent families might exist outside the accessed records. Neither independence of checking nor priority is established externally.

Self-review: passed. Independent audit: not yet performed.
