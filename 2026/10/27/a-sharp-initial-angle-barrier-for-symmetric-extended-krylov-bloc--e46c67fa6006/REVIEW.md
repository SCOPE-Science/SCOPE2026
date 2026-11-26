# Independent mathematical audit

## correctness

PASS

For T=A⁻¹ and μ=bᵀAb, p=(A−μI)b, one has PTp=−μq and bᵀTp=1−μ(bᵀTb)≠0 by strict Cauchy–Schwarz for a non-eigenvector start. Thus the normalized projected cosine strictly exceeds the cosine between p and Tp. The latter is at least 2√κ/(κ+1) by the spectral secant inequality λ²≤(a+c)λ−ac on [a,c]=[1/M,1/m], completed by the square ((a+c)⟨Tp,p⟩−2ac)² for unit p. The two-column normalized Gram spectrum is 1±t; its condition number and the residual fraction √(1−t²) then follow with strict inequalities. Multiplying a putative dependence among b, Ab and A⁻¹b by the active eigenvalues yields a degree-two polynomial; exactly two active values force rank one in the projected block and t=1. To check sharpness, rescale the three spectral values to {r⁻¹,1,r} with outer weights ε, let d=r+r⁻¹−2, and use the equal laws of X and 1/X. Their common mean is 1+εd, common variance εd(r+r⁻¹−εd), and covariance 1−(1+εd)². This reproduces the exact t and its strict limiting gap. The infimum is over the class allowing at least three dimensions, or any fixed dimension ≥3 by padding; at fixed dimension two t=1 and no full-rank block exists. The stated rank and dimension scope supports this reading. No floating-point conclusion follows. The frozen symbolic and sampled checker was inspected without treating its finite tests as proof.

## originality

PASS

Credit the classical antieigenvalue cosine bound and the extended-Krylov block itself as prior. The supported distinct result is sharp optimization under the coupled centering/projection constraint, with strict nonattainment and an explicit admissible extremal sequence; the Gram and residual formulas are consequences, not separate novelty.

## value

PASS

The motivated quantity is the unavoidable input correlation of the batched initial forward/inverse vectors in a named algorithm. The exact attainable limit, including how it forces normalized block ill-conditioning near κ=1, is more informative than a nonsharp inequality or the fact that orthogonalization may be necessary. It is specifically an exact-arithmetic restriction, not an analysis of completed basis quality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
