# Review: exact Fibonacci decorrelation cutoff

## Correctness
PASS. The Fibonacci bases \(v_n,w_n\) have determinant \(\pm1\); the stated exact images follow from the Fibonacci matrix-power identity. Two coordinate bounds reduce every putative boundary resonance to \((1+r^2)(a^2+b^2)\le2\), which forces a signed standard basis coefficient vector and gives exactly four minimizers for **all** positive lags. Fourier orthogonality then determines the band-compressed Koopman operator and its rank; a real cosine witness gives a nonzero correlation of \(1/2\). Exact finite enumerations supplement but do not replace this proof.

## Originality
PASS under the inspected comparisons, with priority uncertainty. Hu–Rosenhaus (2022, arXiv:2204.13655) treats cat-map correlations in Fourier series; its abstract does not state the Fibonacci minimax value or rank-four threshold. Moudgalya et al. (2018, arXiv:1808.04889), whose Fourier dynamics sections were inspected in full HTML, gives an evolution mechanism and scaling for a different cat matrix, not this sharp optimization. Fouxon–Gutkin (2022, DOI:10.1088/1751-8121/aca730) reports finite-support decorrelation for coupled cat maps. Public mathematical-result searches did not expose the same operator-bandwidth and complete extremizer result. The complete Hu–Rosenhaus paper and potentially earlier equivalent lattice statements were not available for definitive priority exclusion; the result is not claimed independently confirmed novel.

## Value
PASS. The exact first Fourier-band overlap is a natural, operational finite-resolution version of mixing: it tells precisely which Fourier-Galerkin cutoffs retain any time-lagged signal, provides an optimal latency and characterizes **all** first surviving resonances, not just decay bounds or a selected test pair. The sharp rank-four equality certificate works uniformly at every time and supplies exact finite-dimensional Koopman information not recovered solely from the asymptotic Lyapunov exponent.

## Scope and limitations
The theorem covers the canonical square cutoff and classical Haar cat dynamics, not general anisotropic apertures, smooth perturbations or infinitely many Fourier modes. Prior results might contain the arithmetic optimization in unexamined text; that priority question remains open to external specialist checking.

Self-review: passed. Independent audit: not yet performed.
