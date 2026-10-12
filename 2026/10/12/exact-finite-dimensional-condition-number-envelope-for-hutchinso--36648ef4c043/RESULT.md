# Exact finite-dimensional condition-number envelope for Hutchinson variance
## Finding
Let \(A=A^{\mathsf T}>0\) be real \(n\times n\), \(n\ge2\), and let \(\kappa=\lambda_{\max}(A)/\lambda_{\min}(A)\). For independent Rademacher probes, define
\[
\widehat t_m=\frac1m\sum_{s=1}^m z_s^{\mathsf T}Az_s.
\]
The exact worst relative variance among all such matrices with condition number at most \(\kappa\) is
\[
\sup_A\frac{\operatorname{Var}(\widehat t_m)}{\operatorname{tr}(A)^2}
=\frac{\mathcal V_n(\kappa)}m,
\]
where
\[
\mathcal V_n(\kappa)=2\max_{0\le r\le n}\left(\frac{n+r(\kappa^2-1)}{\bigl(n+r(\kappa-1)\bigr)^2}-\frac1n\right).
\]
For \(\kappa>1\), only the two integers adjacent to \(n/(\kappa+1)\) need be tested. Thus the finite-dimensional optimizer has a discrete spectral law: \(r\) eigenvalues sit at the upper endpoint and \(n-r\) at the lower endpoint.

A convenient dimension-only corollary is
\[
\mathcal V_n(\kappa)\le
\min\left\{2\left(1-\frac1n\right),\frac{(\kappa-1)^2}{2\kappa n}\right\}.
\]
The second term is the familiar continuous bounded-ratio envelope; the new finite-dimensional formula records the integer obstruction that it suppresses.

## Assumptions and scope
The matrix is real symmetric positive definite and the probes have independent symmetric \(\pm1\) coordinates. The result concerns exact sampling variance of the ordinary Hutchinson estimator, not tail probabilities, floating-point error, Gaussian probes, probing designs with dependent vectors, or variance-reduced estimators. The condition number is spectral. For \(m\) independent probes, the one-probe variance is divided by \(m\).

## Proof
For one Rademacher vector \(z\), the classical variance identity is
\[
\operatorname{Var}(z^{\mathsf T}Az)
=2\left(\lVert A\rVert_F^2-\sum_{i=1}^n a_{ii}^2\right).
\]
Write the eigenvalues as \(\lambda_1,\ldots,\lambda_n\), and put
\[
S=\sum_i\lambda_i=\operatorname{tr}(A),
\qquad
Q=\sum_i\lambda_i^2=\lVert A\rVert_F^2.
\]
Since the diagonal entries sum to \(S\), Cauchy--Schwarz gives
\[
\sum_i a_{ii}^2\ge \frac{S^2}n.
\]
Hence
\[
\frac{\operatorname{Var}(z^{\mathsf T}Az)}{S^2}
\le2\left(\frac Q{S^2}-\frac1n\right).
\]
This orientation bound is sharp for every prescribed spectrum: the constant vector \((S/n,\ldots,S/n)\) is majorized by the eigenvalue vector, so the real Schur--Horn theorem gives an orthogonal conjugate having constant diagonal. Thus it remains only to maximize \(Q/S^2\) over the admissible eigenvalues.

Scale \(\lambda_{\min}\) to one, so \(1\le\lambda_i\le\kappa\). Fix all eigenvalues except one, say \(t\), and write \(s\) for the sum and \(q\) for the squared-sum of the fixed coordinates. Then
\[
F(t)=\frac{q+t^2}{(s+t)^2},
\qquad
F'(t)=\frac{2(ts-q)}{(s+t)^3}.
\]
Any interior critical point is therefore a minimum. Replacing one coordinate by an endpoint never decreases a global maximum, so some maximizer has every eigenvalue in \(\{1,\kappa\}\). If exactly \(r\) eigenvalues equal \(\kappa\), then
\[
Q=n+r(\kappa^2-1),
\qquad
S=n+r(\kappa-1),
\]
which yields the stated finite maximization.

Treating \(r\) temporarily as real, differentiation gives
\[
\frac{d}{dr}\frac{n+r(\kappa^2-1)}{\bigl(n+r(\kappa-1)\bigr)^2}
=
-\frac{(\kappa-1)^2\bigl((\kappa+1)r-n\bigr)}{\bigl(n+r(\kappa-1)\bigr)^3}.
\]
Thus the continuous maximizer is \(r=n/(\kappa+1)\), and the integer maximizer must be one of its floor or ceiling. Evaluating at the continuous maximizer gives
\[
\mathcal V_n(\kappa)\le\frac{(\kappa-1)^2}{2\kappa n}.
\]
The universal bound \(Q/S^2\le1\) gives \(\mathcal V_n(\kappa)\le2(1-1/n)\). Schur--Horn applied to the endpoint spectrum proves attainability of the exact finite-dimensional envelope.

For a concrete equality case, take \(n=4\), \(\kappa=3\), and
\[
A=I+\frac12\mathbf 1\mathbf 1^{\mathsf T}.
\]
Its spectrum is \(\{3,1,1,1\}\), every diagonal entry is \(3/2\), and direct substitution gives
\[
\frac{\operatorname{Var}(z^{\mathsf T}Az)}{\operatorname{tr}(A)^2}=\frac16
=\mathcal V_4(3).
\]
Averaging \(m\) independent probes divides the variance by \(m\).

## Verification
The accompanying `verify.py` checks the endpoint formula by exact rational arithmetic on a grid of dimensions and rational condition numbers, verifies that the integer optimizer is always one of the two integers adjacent to \(n/(\kappa+1)\), checks the continuous upper envelope, and reconstructs the exact \(n=4\), \(\kappa=3\) equality witness. These finite checks supplement, but do not replace, the analytic proof.

## Relationship to prior work
Hutchinson introduced the Rademacher trace estimator and its variance analysis. Avron and Toledo emphasized that one-sample variance depends on off-diagonal energy and developed probabilistic sample-complexity bounds. Roosta-Khorasani and Ascher gave sharper and matrix-dependent sample bounds; their Hutchinson parameter is based on columnwise off-diagonal energy relative to the diagonal. Their paper is explicitly classified under MSC 65C20 and does not state a sharp spectral-condition-number envelope for the exact Rademacher variance. Later work gives stable-rank and tail bounds for stochastic trace estimation.

The continuous inequality
\[
\frac{(\kappa-1)^2}{2\kappa n}
\]
is a Kantorovich-type consequence of bounding the relative spread of numbers in a fixed interval and is not claimed here as a new scalar inequality. The contribution is the exact finite-\(n\) Hutchinson envelope, including the floor/ceiling spectral multiplicity law, basis-orientation attainability, and its realization by SPD matrices.

## Limitations
The exact envelope is basis-sensitive through the Rademacher variance and uses the freedom to orient eigenvectors; a particular application matrix can have much smaller variance, especially if it is nearly diagonal in the probing basis. The theorem does not assert optimal tail constants from variance alone. The originality assessment retains risk from older coefficient-of-variation inequalities or trace-estimation literature using different terminology for the same finite-dimensional extremal problem.

## References
1. M. F. Hutchinson, “A Stochastic Estimator of the Trace of the Influence Matrix for Laplacian Smoothing Splines,” *Communications in Statistics—Simulation and Computation* 18 (1989), 1059–1076. DOI: 10.1080/03610918908812806.
2. H. Avron and S. Toledo, “Randomized Algorithms for Estimating the Trace of an Implicit Symmetric Positive Semi-Definite Matrix,” *Journal of the ACM* 58 (2011), Article 8. DOI: 10.1145/1944345.1944349.
3. F. Roosta-Khorasani and U. Ascher, “Improved Bounds on Sample Size for Implicit Matrix Trace Estimators,” arXiv:1308.2475; *Foundations of Computational Mathematics* 15 (2015), 1187–1212. DOI: 10.1007/s10208-014-9220-1.
4. A. Cortinovis and D. Kressner, “On Randomized Trace Estimates for Indefinite Matrices with an Application to Determinants,” *Foundations of Computational Mathematics* (2022). DOI: 10.1007/s10208-021-09525-9.
