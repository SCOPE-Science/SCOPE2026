# A resonant Poisson-kernel obstruction to curvature decay on the Wasserstein circle
## Finding
For every integer \(n\ge 1\) and every \(0\le r<1\), define the smooth positive probability density
\[
\rho_{r,n}(\theta)=\frac{1-r^2}{2\pi\bigl(1-2r\cos(2n\theta)+r^2\bigr)},
\qquad \mu_{r,n}=\rho_{r,n}(\theta)\,d\theta
\]
on \(S^1\). In the notation of the Fourier-plane curvature formula of Gomes--Rodrigues--San Martin, put
\[
C_\mu=\int_0^{2\pi}\rho(\theta)^{-1}\,d\theta.
\]
Then
\[
C_{\mu_{r,n}}=4\pi^2\frac{1+r^2}{1-r^2},
\qquad
\left|\widehat\mu_{r,n}(2n)\right|=r,
\]
and hence
\[
\overline K_{\mu_{r,n}}(V_{c_n},V_{s_n})
=\frac{3n^2}{1+r^2}.
\]
In particular,
\[
C_{\mu_{r,n}}\longrightarrow\infty
\quad\text{but}\quad
\overline K_{\mu_{r,n}}(V_{c_n},V_{s_n})\longrightarrow\frac{3n^2}{2}
\qquad (r\uparrow1).
\]
Therefore divergence of \(C_\mu\) alone does not imply curvature decay in these equal-frequency Fourier planes. This gives an explicit counterexample to the final degeneration assertion in Corollary 3.12 of arXiv:2610.00625 as inspected in the current public text on 2026-10-05 UTC.

## Assumptions and scope
The statement is entirely inside the smooth positive-density manifold \(P^\infty(S^1)\) used in arXiv:2610.00625: every parameter value satisfies \(0\le r<1\), so \(\rho_{r,n}\) is smooth and strictly positive. The limiting object at \(r=1\) is not asserted to belong to that manifold; only the behavior of the admissible family as \(r\uparrow1\) is used.

The curvature formula used here is the source's exact Corollary 3.10,
\[
\overline K(V_{c_n},V_{s_n})
=\frac{12\pi^2n^2}{C_\mu\bigl(1-|\widehat\mu(2n)|^2\bigr)}.
\]
The source's positivity, sharp upper bound \(\overline K\le 3n^2\), and equality characterization at the uniform measure are not contradicted. Only its additional claim that every family with \(C_\mu\to\infty\) has curvature tending to zero is refuted.

## Proof
The Poisson-kernel identity gives, for \(0\le r<1\),
\[
\frac{1-r^2}{1-2r\cos\varphi+r^2}
=1+2\sum_{j\ge1}r^j\cos(j\varphi).
\]
Taking \(\varphi=2n\theta\) and dividing by \(2\pi\) shows that \(\rho_{r,n}\) has total mass one and that its Fourier coefficient at frequency \(2n\) has modulus \(r\):
\[
|\widehat\mu_{r,n}(2n)|=r.
\]

The reciprocal density is elementary:
\[
\rho_{r,n}(\theta)^{-1}
=\frac{2\pi}{1-r^2}\bigl(1-2r\cos(2n\theta)+r^2\bigr).
\]
Since \(\int_0^{2\pi}\cos(2n\theta)\,d\theta=0\), direct integration gives
\[
C_{\mu_{r,n}}
=\frac{2\pi}{1-r^2}\,2\pi(1+r^2)
=4\pi^2\frac{1+r^2}{1-r^2}.
\]
Substitution into the exact equal-frequency curvature formula yields
\[
\overline K_{\mu_{r,n}}(V_{c_n},V_{s_n})
=\frac{12\pi^2n^2}
{\left(4\pi^2\frac{1+r^2}{1-r^2}\right)(1-r^2)}
=\frac{3n^2}{1+r^2}.
\]
Thus \(C_{\mu_{r,n}}\to\infty\), whereas the curvature tends to \(3n^2/2\).

The failure can also be seen directly in the published proof of the degeneration clause. From \(1-|\widehat\mu(2n)|^2\le1\) and the fact that this factor occurs in the denominator, the displayed curvature formula gives a lower bound
\[
\overline K(V_{c_n},V_{s_n})\ge\frac{12\pi^2n^2}{C_\mu},
\]
not the upper bound used there. The Poisson family shows that the missing factor can decay at exactly the compensating rate.

## Verification
The argument was checked symbolically and by direct integration, but no finite computation is used as a substitute for proof. The only non-elementary premise is the exact curvature formula from Corollary 3.10 of arXiv:2610.00625; its derivation through Theorem 3.8 and the Fourier-plane Gram determinant was inspected in the source. The source text was also checked at Corollaries 3.10 and 3.12 to verify that the refuted limit assertion and the inequality direction used in its proof are actually present in the current public version inspected on 2026-10-05 UTC.

Boundary checks are consistent: at \(r=0\), \(\mu_{0,n}\) is uniform and the formula gives the source's sharp value \(3n^2\); for every \(r<1\), the denominator is positive; and the limit \(r\uparrow1\) is taken only after evaluating the formula on admissible smooth densities.

## Relationship to prior work
Gomes, Rodrigues and San Martin derive the exact sectional-curvature formula on \(P^\infty(S^1)\), prove the sharp upper bound \(3n^2\) in the equal-frequency plane, and then state that curvature tends to zero whenever \(C_\mu=\int\rho^{-1}\) diverges. The present result uses their exact formula but gives a natural harmonic family for which the two denominator factors compensate, producing a nonzero limiting curvature.

A broader 2026 treatment of sectional curvature in Wasserstein geometry by Sturm was compared at the statement level. The focal source itself distinguishes Sturm's one-dimensional torus calculations with different frequencies from the equal-frequency cosine-sine planes responsible for nonzero curvature here. No inspected source or searched research record stated the Poisson-kernel profile above or this correction.

## Limitations
This result does not rederive the full curvature tensor of Wasserstein space and does not alter the source's principal nonflatness theorem, positivity result, or sharp upper bound. It refutes only the universal degeneration-to-zero clause for equal-frequency Fourier planes.

The comparison with the broader Sturm preprint was not an exhaustive line-by-line full-text search of every example, so an older or differently phrased equivalent observation remains a residual originality risk. The claim is specifically about the formal smooth Wasserstein manifold and the curvature normalization used in arXiv:2610.00625.

## References
1. A. Magalhães de Sá Gomes, C. S. Rodrigues, L. A. B. San Martin, *The Wasserstein space of the circle is not flat*, arXiv:2610.00625, first public 2026-09-30; Corollaries 3.10 and 3.12 and Theorem 3.8.
2. K.-T. Sturm, *Sectional Curvature for Kantorovich-Wasserstein and Hellinger-Kantorovich Geometries*, arXiv:2606.14318, 2026.
