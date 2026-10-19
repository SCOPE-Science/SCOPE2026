# A logarithmically enhanced Haar conditioning tail for the rank-one factor-analysis tangent solve

## Finding
Let \(u\) be uniform on the real unit sphere \(S^2\), put \(P=I_3-uu^{\mathsf T}\), and define the positive-semidefinite matrix \(M(u)=P\circ P\), where \(\circ\) is the entrywise product. This is precisely the coefficient matrix of the diagonal least-squares solve in the rank-one factor-analysis (low-rank-plus-diagonal) tangent projection. For \(0<t<1\) write \(\lambda_*(u)=\lambda_{\min}(M(u))\) and \(\kappa(u)=\lambda_{\max}(M(u))/\lambda_*(u)\) when \(M(u)\) is invertible.

The exact sharp lower-tail law and condition-number upper-tail law are
\[
\lim_{t\downarrow0}\frac{\Pr\{\lambda_*(u)<t\}}{\sqrt t\,\log(1/t)}
=\frac{3}{\pi\sqrt2},
\qquad
\lim_{R\to\infty}\frac{\Pr\{\kappa(u)>R\}}{R^{-1/2}\log R}
=\frac{3}{\pi\sqrt2}.
\]
In particular, for every real \(s>0\),
\[
\mathbb E\|M(u)^{-1}\|_2^s<\infty
\quad\Longleftrightarrow\quad s<\tfrac12,
\qquad
\mathbb E\kappa(u)^s<\infty
\quad\Longleftrightarrow\quad s<\tfrac12.
\]
The condition number is finite almost surely, yet its mean is infinite. A second exact identity provides an independent check: with \(p_i=u_i^2\),
\[
\det M(u)=2p_1p_2p_3,
\]
and for every \(0<s<\tfrac12\),
\[
\mathbb E[(\det M(u))^{-s}]
=2^{-s}\frac{\Gamma(3/2)}{\Gamma(3/2-3s)}
\left(\frac{\Gamma(1/2-s)}{\Gamma(1/2)}\right)^3.
\]

## Assumptions and scope
All quantities are real and in exact arithmetic. The randomness is only the Haar-uniform choice of the unit rank-one factor direction in dimension three; the diagonal factor in the underlying covariance approximation may be any strictly positive diagonal matrix, and the positive rank-one coefficient may be any strictly positive scalar. Neither affects \(M(u)\). The result analyzes the intermediate diagonal-coefficient Gram solve, not the condition number of the full covariance matrix or the forward accuracy of the final projected tangent matrix. The inverse and condition number are evaluated on the almost-sure event of invertibility.

## Proof
**1. Determinant and support.** Since \(P\) is an orthogonal projector, for \(z\in\mathbb R^3\) one has
\[
z^{\mathsf T}M(u)z=\|P\operatorname{diag}(z)P\|_F^2\ge0.
\]
Writing \(p_i=u_i^2\), direct expansion gives \(M(u)=\operatorname{diag}(1-2p_i)+pp^{\mathsf T}\). The constraint \(p_1+p_2+p_3=1\) reduces its determinant to \(2p_1p_2p_3\). Thus \(M(u)\) is positive definite whenever all coordinates of \(u\) are nonzero. If one coordinate vanishes its determinant is zero. On a coordinate great circle away from the axes, \(M(u)\) has exactly one zero eigenvalue; at an axis it is a permutation of \(\operatorname{diag}(0,1,1)\). These statements follow directly from the displayed matrix with one or two vanishing \(p_i\). Therefore the two larger ordered eigenvalues remain uniformly positive on the compact sphere; equivalently, there exists \(c>0\) with \(\lambda_2(M(u))\ge c\) at every \(u\), when eigenvalues are sorted increasingly.

**2. Spectral and geometric bounds.** The matrix \(M(u)\) has nonnegative entries and row sum \(\sum_j P_{ij}^2=(P^2)_{ii}=1-p_i\). Hence \(0\le\lambda_j(M(u))\le1\). In particular, \(\lambda_*(u)\ge\det M(u)\), because the product of the other two eigenvalues is at most one.

Fix a small \(\rho>0\) and delete radius-\(\rho\) neighborhoods of the six coordinate-axis points on \(S^2\). On the remaining compact region at least two coordinate magnitudes have a positive lower bound depending on \(\rho\). It follows from the determinant inequality that \(\lambda_*(u)<t\) forces at least one coordinate magnitude to be \(O_\rho(\sqrt t)\). Spherical area of these thin great-circle tubes is \(O_\rho(\sqrt t)\), hence outside the six axis neighborhoods the lower-tail probability is \(O_\rho(\sqrt t)\), negligible after dividing by \(\sqrt t\log(1/t)\).

Near \(+e_1\), use local coordinates \(u=(\sqrt{1-x^2-y^2},x,y)\), with \(x^2+y^2<\rho^2\). The normalized surface measure has density \((4\pi)^{-1}(1-x^2-y^2)^{-1/2}\,dx\,dy\). The other two eigenvalues of \(M(u)\) tend uniformly to one as \(\rho\downarrow0\). By the exact determinant,
\[
\frac{\lambda_*(u)}{2x^2y^2}=
\frac{1-x^2-y^2}{\lambda_2(M(u))\lambda_3(M(u))}
=1+O(\rho^2)
\]
uniformly in this chart wherever \(xy\ne0\), with constants independent of \(t\). Thus, with arbitrarily small relative error as \(\rho\downarrow0\), the desired event is \(\{|xy|<\sqrt{t/2}\}\). For any fixed small \(\rho\), the planar area inside a disk of radius \(\rho\) of \(\{|xy|<a\}\) equals \(4a\log(1/a)+O_\rho(a)\) as \(a\downarrow0\). The disk-to-square discrepancy contributes only \(O_\rho(a)\). Substituting \(a=\sqrt{t/2}\), the leading contribution of one axis point is
\[
\frac1{4\pi}\cdot4\sqrt{t/2}\cdot\frac12\log(1/t)
=\frac{\sqrt t\log(1/t)}{2\pi\sqrt2}.
\]
There are six congruent axis neighborhoods. Squeeze first as \(t\downarrow0\), then \(\rho\downarrow0\), obtaining the coefficient \(6/(2\pi\sqrt2)=3/(\pi\sqrt2)\).

**3. Condition number and moments.** The top eigenvalue tends to one uniformly as a neighborhood shrinks to any coordinate axis, and is globally at most one. Hence the same local-area squeezing gives the stated upper-tail constant for \(\kappa(u)\); the complement of the axis neighborhoods is again of order \(O_\rho(R^{-1/2})\). The layer-cake integral \(\mathbb E Z^s=s\int_0^\infty t^{s-1}\Pr(Z>t)\,dt\) applied to \(Z=\lambda_*^{-1}\) and \(Z=\kappa\), together with the exact tails, gives the strict moment cutoff \(s=1/2\). Equality diverges logarithmically.

**4. Exact determinant moment.** Haar invariance gives \((p_1,p_2,p_3)\sim\operatorname{Dirichlet}(1/2,1/2,1/2)\). Integrating the monomial \(2^{-s}\prod_i p_i^{-s}\) against this beta-simplex density yields the displayed gamma ratio, finite exactly for \(s<1/2\). This confirms the moment threshold independently for the determinant; the theorem's eigenvalue tail is established in step 2 rather than inferred from the determinant moment alone.

## Verification
The accompanying standalone `verify.py` checks the exact determinant identity with rational arithmetic on a finite barycentric grid and against a separately constructed projected-Hadamard matrix on a large positive grid. It checks positive definiteness, the unit spectral upper bound, and the local eigenvalue-to-determinant relation at six positive scales. The program also evaluates the explicit gamma-moment and leading tail constants. Numerical sampling of 700,000 Haar directions confirmed the predicted slow approach to the asymptotic coefficient, but sampling is not relied upon as a proof. Reproduce the embedded deterministic checks with `python verify.py` (requires NumPy). The mathematical proof covers all real thresholds and all admissible random directions except a null event.

## Relationship to prior work
Bonnabel, Lambert and Bach (arXiv:2407.03373v1, 1 July 2024), Proposition 3 and equation (26), derive this particular Hadamard-square coefficient matrix and its Moore–Penrose inverse as part of the low-rank-plus-diagonal tangent projection. The present contribution concerns its previously unspecified Haar orientation conditioning law, its sharp logarithmic coefficient, and the full inverse-moment threshold—not the tangent-projection formula itself. Borsdorf, Higham and Raydan (SIAM J. Matrix Anal. Appl. 31 (2010), Theorem 3.6) establish a related three-support-rank criterion for a *different* factor-structure Hessian, \(\operatorname{diag}(\|x\|^2-2x_i^2)+xx^{\mathsf T}\). That older support criterion does not determine this Gram matrix's random smallest-eigenvalue or condition-number distribution. Classical Dirichlet integrals provide a component of the proof but do not alone give the eigenvalue asymptotic.

## Limitations
The logarithmic constant and moment threshold are proved only in the smallest nontrivial ambient dimension three, with a *real Haar-uniform* rank-one direction. No claims are made for nonuniform directions, higher-dimensional factor rank, floating-point error, discrete numerical stability of a Riccati integrator, or ill-conditioning of the final full tangent projector. The inferred instability concerns amplification of arbitrary perturbations in the intermediate diagonal solve's right-hand side. The probability law was not independently audited and could have an equivalent treatment under different terminology in older factor-analysis or random-Gram literature.

## References
1. S. Bonnabel, M. Lambert, F. Bach, *Low-rank plus diagonal approximations for Riccati-like matrix differential equations*, arXiv:2407.03373v1 (first public arXiv version 2024-07-01), Section 3.3, Proposition 3 and equation (26). https://arxiv.org/html/2407.03373v1
2. R. Borsdorf, N. J. Higham, M. Raydan, *Computing a Nearest Correlation Matrix with Factor Structure*, SIAM Journal on Matrix Analysis and Applications 31 (2010), 2603–2622, Theorem 3.6. https://eprints.maths.manchester.ac.uk/1523/1/SML002603.pdf
