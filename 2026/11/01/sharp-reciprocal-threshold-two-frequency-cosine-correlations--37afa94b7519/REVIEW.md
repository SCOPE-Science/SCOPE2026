# Scientific review

## Correctness — PASS

The final theorem concerns every reciprocal threshold radius \(1/m\) with integer \(m\ge5\) and every distinct integer pair, not a finite test set. Its proof first removes common factors and derives exact normalized Fourier formulas separately for the odd–odd and mixed-parity pairs. The periodic Bernoulli difference inequality is proved directly on two affine segments. The remaining comparisons are exhaustive: odd–odd with \(b\le L_m\), odd–odd with \(b>L_m\), and mixed parity split by two frequency scales; the single small exceptional case \(m=5\) is calculated exactly. The formulas establish both the optimum and its complete equality list. A separate exact-rational checker compares these formulas with geometric arc intersections and tests many bounded cases, but the all-integer theorem relies on the displayed inequalities. Risks: all strict cases require the stated integer endpoint conventions; these have been cross-checked, and the zero-threshold endpoint is separately identified as known.

## Originality — PASS relative to inspected literature

The focal source, Clément and Steinerberger (arXiv:2412.17466; 2024-12-23), quantifies signed *discrete* Fourier-row correlations, not the sharp *continuous positive-threshold* probability and its optimizer classification. Gonçalves–Oliveira e Silva–Steinerberger (arXiv:1903.06826) and Dou et al. (arXiv:2212.02496) already resolve the zero-threshold two-frequency case, which is expressly excluded from the new contribution. Zang et al. (arXiv:2610.33190) treat zero-threshold four-frequency extremality and general asymptotic frequency-count behavior, not positive thresholds. Giannitsi–Madrid (arXiv:2610.38135, publicly posted 2026-10-28) introduce the general waveform threshold framework and prove the lower bound \(4/m^n\) and asymptotic rates, but their displayed results do not give the exact finite two-frequency constant \(4/(mL_m)\), parity-dependent optimizers, or the additional minimizer at \(m=5\). These are substantive nonimplication comparisons; absence of search results is not treated as uniqueness proof.

A semantic search of relevant published mathematical research records using threshold, alias, Bernoulli, Fourier and correlation phrases found no equivalent claim; close results concern different objectives such as cyclic two-frequency \(L^1\) concentration and sign covariance of Gaussian vectors. Accessible published mathematical statements were compared by their recoverable claims for overlap. Residual risk: an unindexed earlier theorem using alternative arc-intersection or lonely-runner language may contain the same minimization; an independent audit has not been performed.

## Value — PASS

This is an all-parameter exact classification of a naturally arising first nonzero-threshold extremal case, not a one-off numerical example. The universal \(4/m^2\) bound from recent threshold-correlation theory is sharpened to \(4/[mL_m]\); parity of \(m\) changes the optimizer frequency and the small modulus \(m=5\) has a genuine second minimizer orbit. The same argument handles the full family of strictly monotone antipodal wave profiles, providing a reusable two-frequency benchmark for higher-dimensional threshold problems. It does not claim to solve nonreciprocal or larger-cardinality variants.

## Limits and literature

References: arXiv:2412.17466, arXiv:1903.06826, arXiv:2212.02496, arXiv:2610.33190, arXiv:2610.38135. Closest accessible source arXiv:2610.38135 proves a non-sharp lower bound at fixed two-frequency count but provides no stated exact equality classification. Review is not an independent verification.

Self-review: passed. Independent audit: not yet performed.
