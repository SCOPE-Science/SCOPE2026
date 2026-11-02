# Scientific review: parity-sawtooth conditional Wilcoxon variance

## Correctness — PASS

The claim is an exact all-integer conditional distributional moment statement for \(a,b\geq1\), with feasible run-count boundaries explicitly specified. Uniform positive compositions yield the run-length covariance matrices, and the bilinear inversion count gives the stated even/odd conditional variance formulas. The proof's four difference identities reduce to strictly positive polynomials on precisely the feasible domains. The standalone verifier reproduces the symbolic identities and independent finite word enumeration (87,811 exact checks); finite enumeration is not used as the universal proof.

## Originality — PASS, with historical-priority qualification

The 2009 multiset Mahonian work gives unconditioned inversion laws. The 2014 two-run order-statistic work gives fixed-composition run counts and moments of the extrema of color-specific run counts, not inversion count conditional on total runs. The 2026 systematic study includes fixed-weight run enumeration, but no direct run-conditioned rank-sum variance formula was found in its inspected relevant sections. The earlier marginal covariance between squared rank sum and runs is only a weighted aggregate and cannot determine the complete conditional variance profile or its strict run-parity oscillation. A possible older full joint rank/run enumeration remains a priority risk; a failed literature search alone does not prove novelty.

## Mathematical value — PASS

Both statistics arise naturally from the same two-sample permutation null. Their uncorrelatedness obscures a deterministic, strict sawtooth of conditional dispersion: the even and odd subsequences each shrink, but an odd run count is a strict local minimum whenever both adjacent even counts exist. This structural finite-sample dependence can inform exact joint/stratified testing; no assertion is made about test power, entire conditional tails or distributional alternatives.

## Limits and verification

The assumptions exclude ties, alternative sampling laws and nonuniform word weights. The computational checker has a SymPy dependency; its exact finite outputs corroborate an independent symbolic identity and positive-polynomial proof. Historical coverage may be incomplete, and no external mathematical certification has been obtained.

Self-review: passed. Independent audit: not yet performed.
