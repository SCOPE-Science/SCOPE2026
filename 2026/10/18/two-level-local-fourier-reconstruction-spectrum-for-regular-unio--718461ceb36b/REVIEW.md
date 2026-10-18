# Mathematical assessment

## Correctness — PASS

The normalized Fourier integral differentiates into an explicit endpoint matrix. On the fixed-area, fixed-rotation slice, the real discrete Fourier transform decomposes it into conjugate frequency pairs and, for even arc count, one real Nyquist block. Every pair's Gram matrix has the exact two eigenvalues from the cosine of half the interlaced endpoint offset; Parseval supplies the claimed factor \(m/(4\pi^2)\). Both real multiplicities sum to \(2m-2\), and strict positivity holds at every interior duty fraction. A real-analytic Taylor estimate and the inverse function theorem prove the local result with sharp constants. An independently formed Jacobian passed 45 numerical singular-spectrum and finite-difference comparisons; numerical tests are supportive, not the proof.

## Originality — PASS, with historical-priority uncertainty

Courtney's complete primary argument proves qualitative recovery from coefficients through order \(m\) and an algorithm, but does not evaluate the lower-order, fixed-area, rotation-quotient endpoint Jacobian or its sharp full real singular spectrum. Batenkov et al. prove bounds in general partial nonuniform Fourier matrices for node clustering, not this regular interlaced two-grid exact spectrum or its unique half-duty isotropy. Jiang's oscillation theorem concerns lower Fourier-mode uncertainty and sign changes of continuous functions, not inverse endpoint differential conditioning. Targeted searches for exact regular-arc Jacobian singular values, equivalent Vandermonde two-grid reductions, duty-cycle isometry and endpoint-recovery tables found no dominating result. Since database recall is incomplete and elementary DFT diagonalizations can have appeared elsewhere, historical priority is not certified.

## Value — PASS

The mathematical object is the natural endpoint parametrization of regular periodic arc masks, and its low Fourier moments are the observables in interval reconstruction. The answer is sharp for **all** arc counts and interior duty fractions, identifies a dimension-independent optimal condition number, and proves a precise singularity at duty fractions tending to zero or one. It is more than a routine bound: the conjugate-pair real Jacobian could a priori have many angularly dependent singular values, but collapses to two levels; half-duty yields an exact local isometry. This gives quantitative inverse-stability information absent from the qualitative recovery and generic cluster-bound literature.

## Limitations and closest works

The assertion is local and concerns fixed length and a rotation-gauge slice. No statement of global uniqueness, arbitrary arc placements, or globally optimal sampling is included. The closest primary treatments are Courtney (2010), Batenkov–Demanet–Goldman–Yomdin (2018/2019), and Jiang (2026). An independent literature and proof audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
