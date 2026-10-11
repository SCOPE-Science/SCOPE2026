# Scientific review

## Correctness — PASS
The affine-support and modulation reductions preserve the exact zero count for arbitrary complex coefficients. Cyclotomic determinantal rank is characterized algebraically, then every one of the \(194580\) normalized five-zero candidate configurations is checked using exact integer arithmetic; all rank-deficient cases are discharged by an explicit full-support kernel criterion or an essential-column obstruction. Each of the 330 permissible normalized five-zero matrices has an exact full-support cofactor witness with exactly those five zeros; an explicit witness is printed. Double counting gives exactly \(3234\) projective maximizers. The formal finite enumeration is exhaustive for the stated finite field, not a numerical sampling or an extrapolated infinite assertion. Reproduction: `python3 verify_parabola_7.py`.

## Originality — PASS, with access risk
Li's arXiv:2609.16030v1 abstract supplies a bound of six for odd support five, but no exact five-zero count or projective census. The full accessible v2 manuscript (Introduction, Theorem 3.7, Sections 5–6) gives the general bound and classifies global total-support minimizers, which are not the five-supported vectors having total support \(49\). Fiorentino–Weigert's full text, particularly the dimension-seven discussion in Section 5.3, addresses global uncertainty and numerical existence of several basis-support configurations, not this sharp fixed-five-point upper bound and full extremizer census. Published finding searches found neighboring finite Fourier support cases on other groups, not an implication of the present statement. A significant residual risk is the unavailable full v1 text, which could contain a specialized computation not evident in its abstract; no universal absence of unpublished or unindexed work is asserted.

## Value — PASS
The exact maximum is the first five-point odd-support test of the general parabolic Fourier uncertainty framework, and it proves a strict gap at the smallest prime where the test makes sense. The result also classifies the size of the full exact-support extremizer family and its natural modulation orbits, with a reproducible exhaustive algebraic certificate. These naturally associated values are not incidental coefficient substitutions: they distinguish the generic odd-support bound from the actual sharp finite-field behavior. Nothing is asserted for larger primes or for an arbitrary infinite family.

## Constraints on interpretation
Exact rank computations are a proof only because the affine and modulation reductions show that the finite computation exhausts every complex projective vector. The original initial manuscript was not fully accessible; uniqueness of this statement in all literature is unproved. No independent audit has been performed.

Same-model review: passed. Independent audit: not yet performed.
