# Self-review

## Correctness — PASS

The proof identifies sequential residual-weighted Cholesky on a diagonal two-plateau matrix with a size-biased permutation. An exponential race gives the exact conditional binomial law; independent spacings of the dominant clocks yield the Laplace factors and full finite probability generating function. The fixed-rank geometric limit and growing-rank conditional-binomial central limit theorem are derived with explicit scaling. The final exact residual trace establishes that the specified near-optimal event is equivalent to capturing every dominant coordinate. The independent rational dynamic recursion in `verify.py` cross-checks the finite formula and the first two moments.

## Originality — PASS, subject to literature limitations

Epperly's 2026 near-optimality bounds, Divan–Gilles's 2026 spectral-decay bounds, and Chen–Epperly–Tropp–Webber's original RPCholesky guarantees do not, in the inspected material, establish the exact two-plateau RPCholesky capture-count law or its high-probability Gaussian critical window. The last paper does use the two-level diagonal motif for DPP sampling in Appendix C.4; this is explicitly credited. Classical exponential races, geometric sums, and central limit methods are acknowledged as proof ingredients, not claimed as new. The possibility of an equivalent result in broader size-biased permutation theory or inaccessible primary material remains.

## Value — PASS

The exact law and sharp logarithmic oversampling threshold quantify the additional pivot budget needed to find a known number of prominent spectral coordinates in a natural structured RPCholesky benchmark. The limiting Gaussian transition supplies numerical high-probability calibration rather than only order bounds, and identifies the fluctuation mechanism. This complements, but does not strengthen, universal worst-case bounds for arbitrary positive-semidefinite matrices.

## Closest literature and limitations

Primary comparison: arXiv:2608.20633v1 (universal RPCholesky bounds; incomplete later-section access), arXiv:2609.06287v1 (spectral-decay bounds), arXiv:2207.06503v6 (foundational algorithm; two-plateau DPP benchmark). The finite law assumes exact sequential sampling. The limiting trace guarantee requires \(a=\lambda n\), \(r=o(n)\), and \(0<\varepsilon<\lambda\). No floating-point or dense-kernel guarantee is established.

Self-review: passed. Independent audit: not yet performed.
