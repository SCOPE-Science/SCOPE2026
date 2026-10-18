# Independent mathematical audit

## correctness

PASS

Inspected frozen RESULT.md SHA 4779918cb6fbf978d8239d4f445e00972b32ce0b and verify.py SHA bd2831ec18767ad478e1279b3d7d20642f63a9ed. For n≥2, Fourier inverse of −i sgn(k)(1−|k|/n), with DC/Nyquist zero, is Q_n(r)=2Σ_{k=1}^{n−1}(1−k/n) sin(πkr/n). Finite geometric derivative gives [sin t−n^-1 sin(nt)]/(1−cos t). Critical grid t=πr/n kills sin(nt); Q= cot(πr/2n) except original sine-sum zero at r=0,n. Normalized circulant row L1 mass and sign-vector/point-mass witnesses prove both endpoint ℓ¹/ℓ∞ norms C_n=(1/n)Σ_{r=1}^{n−1}cot(πr/2n). Partition even and odd terms in C_(2n) to derive 2C_(2n)−C_n=(1/n)Σ_{j=0}^{n−1}cot((2j+1)π/(4n))=untapered cyclic Hilbert L_(4n). Subtract (2/πx) singularity from cot(πx/2) and apply Euler–Maclaurin with H_(n−1) to yield (2/π)log n+(2/π)(γ+log(2/π))−π/(36n²)+O(n^-4). Separately recomputed exact cot sum vs direct multiplier for representative n and high-precision n² residual near −π/36; numerical tests corroborate, not prove, infinite claims.

## originality

PASS

Boche–Pohl 2015 already has stronger continuous conjugate Fejér kernel, so its exact pointwise cotangent collapse at the Nyquist grid is a direct published corollary, NOT novel by itself. After explicitly excluding that covered component, best-of-knowledge extra contribution is the *sharp finite cyclic endpoint norm sequence*, its exact dyadic relation to the untapered Hilbert norm, and explicit n^-2 correction. These are not explicitly proved in the inspected primary slides/papers; the overlap is serious and equivalent prior summation remains a substantial risk. Failed Resultary conveys no absence conclusion.

## value

PASS

Critical-grid first-Cesàro Hilbert regularization is a natural finite Fourier stability problem. A sharp all-n endpoint amplification law, exact comparison to unsmoothed transform and finite-size correction are potentially useful precise invariants. The value rests on the *operator norm classification and two-scale comparison*, not on the pre-existing cotangent kernel identity or mere computational reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
