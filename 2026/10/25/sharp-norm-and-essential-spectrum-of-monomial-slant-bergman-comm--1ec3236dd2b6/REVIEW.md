# Review of sharp monomial slant commutator theorem

## Correctness — PASS

The normalized Bergman monomial basis and the ordinary-monomial downsampler yield exact coefficients: both compositions select one congruence class modulo \(r^2\) and telescope to square-root ratios. Every coefficient is strictly less than \(r\) in magnitude and tends to \(r\) on the far tail. If the two residue streams differ, \(CC^*\) is diagonal with all eigenvalues below, and converging to, \(2r^2\). If the streams coincide, their relative output translation is a nonzero integer; \(CC^*\) is compactly equivalent to \(r^2(2I-S^q-S^{*q})\), whose essential spectrum is \([0,4r^2]\). Triangle inequality supplies the sharp finite upper bound in the latter case. This also establishes norm nonattainment, with a separate top-eigenvalue argument for the former case. The standalone checker returned 29,766 deterministic finite assertions passed. Checks are not substituted for the infinite proof.

## Originality — PASS, with remaining priority risk

Cui–Li–Lu (arXiv:2610.09728v1, 2026) analyze commuting, finite-rank commutators, and nonzero products, not their exact norm or positive essential spectrum. The earlier qualitative essential commutativity theorem by Lu–Liu–Yang (2010), and the commuting/product characterizations by Liu–Lu (2013), do not logically imply the congruence-dependent quantitative spectra. Singh–Singh–Singh (arXiv:2507.06546v1, 2025) studies a differently normalized downsampling map and reports spectral information and finite sections for individual operators. Scientific-record and literature searches found no equivalent theorem. The 2010 full text was inaccessible and remains a specific historical-priority risk; lack of access is not treated as proof of novelty.

## Mathematical value — PASS

This is a complete sharp family for natural commutators in a newly active slant-Toeplitz setting. It upgrades qualitative noncommutativity to exact essential-norm rigidity and a discontinuous arithmetic classification of the positive essential spectrum for every order and every distinct monomial pair. The single versus double input residue stream explains the two fundamentally different limiting operator geometries. Neither a renaming nor an isolated finite example, this classification exposes an invariant unavailable from zero-commutator criteria alone.

## Limits and sources

Scope is analytic monomial pairs with monomial-normalized downsampling on unweighted Bergman space. Numerical finite sections provide diagnostics only. Principal full-text comparison: Cui–Li–Lu (2026, arXiv:2610.09728v1, Sections 1–3), and Singh–Singh–Singh (2025, arXiv:2507.06546v1, operator normalization and spectra). Additional historical comparisons: Lu–Liu–Yang (2010, DOI 10.1002/mana.200710100, abstract available; complete text not read), Liu–Lu (2013, DOI 10.1155/2013/473916, indexed statements; direct full-text retrieval unsuccessful). These leave residual priority uncertainty rather than a logical implication of coverage.

Self-review: passed. Independent audit: not yet performed.
