# Review

## Correctness

**PASS.** The Fano-plane inclusion-exclusion identity gives the exact expected stopping time from point and line masses. Zero columns can be replaced without increasing coverage time. The checker exhausts every weak composition of eight into the seven nonzero binary directions, uses exact rational arithmetic, and identifies all seven minimizing profiles and the next distinct value.

## Originality

**PASS, with a stated access risk.** The inspected coverage-depth paper proves a general lower bound and results for specified code families, but its stated results do not determine the exact integer profile optimum for binary \([8,3]\) codes. Searches for this parameter set and for rank-three binary coverage-depth optimization returned no matching result; the closest surfaced code-theory result concerns dimension two. A related 2026 paper on coverage-depth random variables was identified from a citation but its full text was not inspected, so that remains a residual risk rather than a claim of exhaustive novelty.

## Value

**PASS.** This is the first length immediately beyond the seven-column binary simplex profile and gives an exact optimality and uniqueness statement at a concrete non-MDS parameter set. It also quantifies the non-obvious fact that appending a duplicate direction raises the expected number of with-replacement reads by \(43/420\), despite adding a stored column. The result is a reproducible finite base case for the broader problem of optimizing full-recovery coverage depth.

Closest literature: Gross et al., arXiv:2610.07370, which treats general coverage-depth formulas and selected optimal code families. Limitations: only \((q,n,k)=(2,8,3)\) is settled here; a related 2026 coverage-depth paper was not fully inspected.

Self-review: passed. Independent audit: not yet performed.
