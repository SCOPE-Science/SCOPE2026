# Self-review

**Statement reviewed:** Fixed-modulus optimality and a sharp Gaussian tail penalty in one-vector range finding. The sole accepted claim comprises the all-dimensional aligned one-vector iid fixed-magnitude optimality identity with equality cases, together with its exact one-spike Gaussian-versus-sign power-iteration asymptotics. Source window is anchored by Saibaba–Międlar's arXiv first posting on 2023-08-10.

## Correctness: PASS

The proof specifies \(m\ge d\ge3\), \(q\ge0\), positive singular squares, and nonzero iid centered unit-variance real probes. Projector algebra gives a bounded quotient of weighted squared probe entries. Exchangeability produces the exact pairwise positive gap, including strictness. Independent Gaussian chi-squares yield the beta representation on the spike; an explicit integrable envelope justifies the large-power limit with its exact Gamma constant. A dependency-free Python checker passes 621 exact and numerical test groups. No finite test is treated as an infinite proof.

## Originality: PASS, with priority risk

Saibaba–Międlar (arXiv:2308.05814v1) introduce the relevant beyond-Gaussian randomized low-rank setting, derive broader bounds, and examine sign probes but do not derive the claimed all-iid exact signed-magnitude comparison and power-exponent separation in the inspected full text. Diouane et al. (arXiv:2206.08793v2) provide Gaussian mean/covariance error bounds. Epperly–Webber (arXiv:2605.19096v2) prove sharp rotation-invariant minimax statements over adversarial matrices, not pointwise optimal iid magnitudes on a fixed aligned matrix; their relevant sharp minimax bound moreover excludes a one-column sketch. Related earlier two-dimensional no-power facts are not claimed as new. Exact ratios of exchangeable normalized weights may exist under different terminology; no publication-priority certification is asserted, and a relevant 2018 canonical-angle text was only partly accessible.

## Value: PASS

This gives a reproducible, dimension-uniform design principle for the most basic nontrivial randomized range-finding step, quantifies all competing iid probe laws with one nonnegative certificate, and exhibits an explicit near-gap convergence-exponent difference between signs and Gaussian probes after power iteration. The result cannot be extrapolated to arbitrary singular-vector orientations or multi-column sketches; these restrictions appear in the scientific statement and proof.

## Scope and reproducibility

Reproduce using `python3 verify.py` from the complete package. The exact finite enumeration checks the swap identity and equality cases; sampled Gaussian comparisons and numerical integrals are diagnostics only. The proof establishes all unbounded dimensions, positive singular spectra and power indices. Literature overlap remains a qualified risk; no independent review was undertaken.

Self-review: passed. Independent audit: not yet performed.
