# Same-model review

## Correctness — PASS

The argument begins from the exact AR(1) phase equation and eigenvector formula stated in arXiv:2609.20221. Rewriting the inverse covariance also gives the exact identity
\[
(1-\rho^2)R_N(\rho)^{-1}=\rho\big(L_N+(1-\rho)E_N\big)+(1-\rho)^2I,
\]
which independently isolates the boundary perturbation responsible for the scaling law.

For fixed mode index \(m\), the phase equation confines \(N\omega_{m,N}\) to a compact interval approaching \([(m-1)\pi,m\pi]\). Under \(N(1-\rho_N)\to c\in(0,\infty)\), the tangent of the boundary phase converges to \(x/c\). Combining this with the phase budget gives the limiting equation
\[
\tan((m\pi-x)/2)=x/c.
\]
Its derivative is strictly negative on the relevant interval, so the root is unique. The limiting eigenvector follows from the exact centered sinusoidal representation and Riemann-sum normalization. The eigenvalue scaling follows directly from the exact rational eigenvalue formula.

The first-row overlap formula was checked algebraically from the normalized cosine profile. The operator-norm lower bound uses only the elementary fact that the spectral norm dominates the Euclidean norm of any row. The endpoint \(c=\infty\) gives overlap \(2\sqrt2/\pi\) and distance \(\sqrt{2-4\sqrt2/\pi}\). The small-\(c\) expansion gives \(D(c)=c/\sqrt{180}+O(c^2)\).

Adversarial checks included direct dense eigendecomposition of the Toeplitz covariance at finite \(N\), verification that the Perron eigenvector agrees with the closed-form first mode to machine precision, checking the \(N\) rather than \(N+1\) scaling in the continuum coordinate, and separating the fixed-low-mode theorem from any unproved claim about all rows of the transform. The numerical artifact reproduces the critical limits for several \(c\), four fixed modes, the DCT-side regime, and the Dirichlet-side regime.

## Originality — PASS, to the best of our knowledge

The following are prior and excluded from the novelty claim: the Kac--Murdock--Szegő/AR(1) eigenproblem; sinusoidal eigenvectors and transcendental frequency equations; the fixed-\(N\) limit \(\rho\to1\) giving DCT-II; continuous exponential-covariance Karhunen--Loève eigenfunctions and their Robin-type transcendental equations; and the recent exact butterfly factorization with DCT-II/DCT-IV cores and orthogonal correction factors.

The accepted contribution is limited to the joint limit in which block length and correlation approach their endpoints together: the critical parameter \(N(1-\rho)\), the resulting fixed-mode profile law, the explicit positive first-row distance from DCT-II for every nonzero critical parameter, the necessary-and-sufficient scale \(N(1-\rho)\to0\) for convergence of the leading KLT row to the DCT DC row, the noncommutation of the fixed-block and large-block limits, and the implication that the correction-to-identity statement in arXiv:2609.20221 is not uniform in block length.

Literature checks covered the motivating arXiv identifier and title, AR(1) KLT/DCT convergence, Kac--Murdock--Szegő eigenvectors with matrix-size-dependent correlation, exponential-covariance KLEs, and correlation-length/block-length formulations. The full relevant eigenproblem and endpoint statements in the recent preprint were inspected. Torun--Akansu (2013) was inspected at the discrete kernel equations and its continuous exponential-covariance analogue. No source located in these checks states the \(N(1-\rho)\) DCT-boundary criterion or the explicit transform-distance obstruction.

The most important residual originality risks are R. J. Clarke's 1981 two-page paper, DOI 10.1049/ip-f-1.1981.0061, and older Kac--Murdock--Szegő asymptotic literature. Clarke's full text was not inspected; bibliographic records and repeated later citations establish that it proves the fixed-block \(\rho\to1\) DCT relation, but it could conceivably contain a remark about block-length dependence. General Toeplitz/KMS asymptotics could also imply the continuum eigenmode limit without phrasing it as a DCT nonuniformity theorem. Those possibilities are residual risks, not evidence of known coverage. The continuous Robin eigenproblem itself is explicitly treated as prior art.

## Value — PASS

The result supplies a sharp condition missing from the usual statement that "highly correlated AR(1) data have a DCT-like KLT." For large blocks, adjacent correlation approaching one is not enough: the correlation defect must be \(o(1/N)\) even for the leading KLT row to approach DCT-II. The critical family gives an explicit continuum of non-DCT limiting modes and an operator-norm lower bound, while the exact boundary-perturbation identity explains the mechanism. This directly qualifies the fixed-\(N\) identity-correction limit in a new exact fast factorization and indicates when dropping its correction stage cannot be justified by high correlation alone.

## Limitations

The analysis fixes the mode number while \(N\to\infty\). It does not establish a uniform error formula across all frequencies, coding gain, transform-coding distortion, or the computational break-even point for applying correction factors. The operator statement is a lower bound obtained from one row, not a full singular-value characterization of the correction stage. Continuous exponential-kernel KLE formulas are not new contributions.

Same-model review: passed. Independent audit: not yet performed.
