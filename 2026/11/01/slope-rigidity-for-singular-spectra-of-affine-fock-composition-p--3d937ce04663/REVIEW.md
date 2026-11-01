# Review of the paired Fock singular-spectrum theorem

## Correctness — PASS

The two bounded products are calculated independently on reproducing kernels, yielding distinct exponential-affine weighted composition forms. For every weight of the form \(e^{\delta+\beta z}\) and strict affine slope \(|v|<1\), the displayed explicit Weyl displacement factorization reduces singular values to those of the diagonal map \(e_n\mapsto v^n e_n\); the logarithmic scalar follows by a fully expanded square identity. This proves all finite and infinite singular values, including rank one when \(v=0\), and all Schatten formulas. The orientation difference is a Hermitian form with determinant \(-|a-c|^2\); positive semidefiniteness occurs precisely at equal slopes. A supplementary independent finite-matrix implementation of the coefficient formula passed 143 checks. No finite truncation is used as an infinite-dimensional proof.

## Originality — PASS (best-knowledge, not a priority guarantee)

Tian's arXiv:2610.29786v1 establishes qualitative compactness equivalence for the same unweighted Fock product orientations (Corollary 3.7), but no singular-value or uniform orientation-order theorem appears in the directly inspected introductions and relevant theorem/proof sections; the extracted full text was additionally searched for “singular”. Barik–Sen–Paul's arXiv:2607.17170v1 provides Hilbert–Schmidt criteria for individual weighted compositions, rather than a paired singular-value order. Leng–Zhao's arXiv:2610.15472v1 covers products on Hardy and Bergman spaces rather than Gaussian Fock space. Claim-specific mathematical-record searches found no implication-equivalent result; the nearest matched affine composition cross-adjoint result concerns weighted Dirichlet essential spectra and cannot yield the present compact Fock singular-value comparison. The classical Weyl displacement decomposition is acknowledged prior technique, not claimed original. A previous article may still encode the calculation as a special case, so priority remains provisional.

## Mathematical value — PASS

The motivating 2026 compactness equivalence does not quantify orientation-dependent approximation cost. The exact singular sequences settle optimal rank approximation and every Schatten norm in the natural affine family. More importantly, the determinant computation proves an if-and-only-if slope-rigidity principle: agreement of two affine derivatives is exactly the condition for a *uniform* orientation comparison over all translations; otherwise both orders fail with unbounded discrepancy. This is a complete natural classification, not an arbitrary numerical instance or a known-table recomputation. It is limited to the normalized one-variable Gaussian Fock space and affine strict contractions.

## Closest literature and outstanding limits

Primary articles: Xianchi Tian, arXiv:2610.29786v1 (2026-10-21); Somdatta Barik, Anirban Sen, and Kallol Paul, arXiv:2607.17170v1 (2026-07-19); Qianrui Leng and Xianfeng Zhao, arXiv:2610.15472v1 (2026-10-11). A known older reference for the underlying Fock weighted-composition framework is Trieu Le, DOI:10.1112/blms/bdu046 (2014). Residual risk: an older Gaussian-operator/Weyl-calculus source might contain the paired orientation result implicitly. The proof does not cover boundary slopes with freely varying translations, nonlinear symbols or higher-dimensional spaces.

Self-review: passed. Independent audit: not yet performed.
