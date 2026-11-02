# Self-review

## Correctness
PASS. The proof identifies \(S_m\) as a genuine singular component at generic normal rank three, verifies \(4\det M=D\), proves irreducibility and degree eight by Gauss's lemma and a prime quotient, and proves the line-component double cover is nontrivial by independent square classes of \(u\) and \(4q-1\). Exact symbolic identities are checked in `verify_normal_conic.py`. The result does not assert a global singular-locus classification.

## Originality
PASS, subject to the normal residual risk of unlocated equivalent calculations. Baily–Danelon (arXiv:2610.28792v1, §3) establish the strength-two degeneration and its finite truncations, but do not give the conic discriminant, irreducibility, degree or connected component cover. The earlier Ballico–Bik–Oneto–Ventura quartic is a different construction. The general determinant and splitting-cover formalism is classical; the explicit global identification and nonsquareness statement for this model are not implied without further computation. No relevant previously published equivalent statement was identified in the searches described in AUDIT.json.

## Value
PASS. The normal-conic discriminant is the natural equisingularity wall along the singular component of a canonical strength-boundary degeneration. Its irreducibility, invariant degree eight, and nontrivial line-component monodromy provide a geometric feature of the degeneration beyond its strength rank. This is not a classification of all strength-boundary quartics and does not solve the effective finite-variable threshold.

## Risks and limits
The two quadrics may have additional singular components away from the specified locus, and no claim is made about them. The published work supplies the quartic construction, not the field-theoretic result recorded here. General conic-bundle technology exists and other unstated treatments may cover the same exact instance. Only a self-review has been carried out.

Self-review: passed. Independent audit: not yet performed.
