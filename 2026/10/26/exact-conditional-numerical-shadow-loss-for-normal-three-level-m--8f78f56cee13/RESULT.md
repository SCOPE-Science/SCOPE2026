# Exact conditional numerical-shadow loss for normal three-level matrices

## Finding

Let \(A\) be **any normal complex \(3\times3\) matrix**, \(B\) any complex \(3\times3\) matrix, and \(X\) Haar-uniform on the complex unit sphere. Define the numerical measurements \(Z_A=X^*AX\) and \(Z_B=X^*BX\). The best nonlinear least-squares prediction error from the single complex numerical value is

\[
\mathcal R_A(B)=\inf_{f:\mathbb C\to\mathbb C\ \mathrm{Borel}}\mathbb E\,|Z_B-f(Z_A)|^2
=\mathbb E\,|Z_B-\mathbb E[Z_B\mid Z_A]|^2.
\]

The following exhaustive spectral classification is exact. All matrix entries mentioned are in an orthonormal eigenbasis of \(A\).

**(i) Three distinct noncollinear eigenvalues.** Writing \(B=(b_{ij})\),
\[
\mathcal R_A(B)=\frac1{12}\sum_{i\ne j}|b_{ij}|^2.
\]

**(ii) Three distinct collinear eigenvalues.** Order them \(a,b,c\) so that \(b=a+r(c-a)\) with \(0<r<1\). Put \(D=b_{22}-(1-r)b_{11}-rb_{33}\). Then
\[
\boxed{\mathcal R_A(B)=\frac1{12}\sum_{i\ne j}|b_{ij}|^2+\frac{|D|^2}{24}.}
\]
For \(t=(z-a)/(c-a)\) in \([0,1]\) set \(L_r(t)=\min\{t/r,(1-t)/(1-r)\}\). An optimal prediction, at each \(z=a+t(c-a)\), is
\[
\mathbb E[Z_B\mid Z_A=z]
=b_{11}(1-t)+b_{33}t+\frac D2L_r(t).
\]
This predictor has a genuine kink at \(t=r\) exactly when \(D\ne0\).

**(iii) One or two distinct eigenvalues.** If \(P_\lambda\) are the distinct spectral projections of \(A\) and \(m_\lambda=\operatorname{rank}P_\lambda\), define
\[
\Pi_A(B)=\sum_{\lambda\in\sigma(A)}\frac{\operatorname{tr}(P_\lambda B)}{m_\lambda}P_\lambda.
\]
Then
\[
\mathcal R_A(B)=\frac1{12}\|B-\Pi_A(B)\|_{\mathrm{HS}}^2,
\qquad
\mathbb E[Z_B\mid Z_A]=X^*\Pi_A(B)X.
\]
The right-hand predictor is a measurable function of \(Z_A\) because there are at most two distinct eigenvalues.

**Sharp nonlinear gain.** In case (ii) put \(H_r=1+r^2+(1-r)^2\), and denote by \(\mathcal R_A^{\mathrm{aff}}(B)\) the minimum over complex affine functions of \(z\) and \(\overline z\). Then
\[
\mathcal R_A^{\mathrm{aff}}(B)=\frac1{12}\sum_{i\ne j}|b_{ij}|^2+\frac{|D|^2}{12H_r},
\quad
\frac34\,\mathcal R_A^{\mathrm{aff}}(B)\le\mathcal R_A(B)\le\mathcal R_A^{\mathrm{aff}}(B).
\]
The constant \(3/4\) is sharp, realized by \(A=\operatorname{diag}(-1,0,1)\) and \(B=\operatorname{diag}(1,-2,1)\): the affine risk equals \(1/2\) and the optimal risk equals \(3/8\). For \(A_\varepsilon=\operatorname{diag}(-1,i\varepsilon,1)\) and every real \(\varepsilon\ne0\), the same diagonal \(B\) has \(\mathcal R_{A_\varepsilon}(B)=0\). Thus this exact-information functional is discontinuous at a collinear spectrum.

## Assumptions and scope

Matrices act on \(\mathbb C^3\) with the standard Hermitian form \(X^*BX\), and the Haar law is invariant under all unitary matrices. \(B\) need not be normal or Hermitian. Errors are complex-modulus squared, the spectral ordering in case (ii) is by position on the line, and the observation has exact/noiseless complex precision. No higher-dimensional or nonnormal classification is asserted. The index \(47A12\) concerns numerical ranges and numerical shadows.

## Proof

**Haar moments and phases.** In an eigenbasis of the normal matrix \(A\), write \(P_j=|X_j|^2\). These variables are uniformly distributed on the probability simplex \(P_1+P_2+P_3=1\), with joint density \(2\) in \((P_2,P_3)\). Conditional on \((P_1,P_2,P_3)\), coordinate phases are independent uniform unit-circle variables. Consequently the off-diagonal numerical form \(\sum_{i\ne j}b_{ij}\overline X_iX_j\) has conditional expectation zero, is orthogonal in \(L^2\) to every function of \(Z_A\), and its unconditional squared norm equals \(\sum_{i\ne j}|b_{ij}|^2/12\). The final identity uses \(\mathbb E[P_iP_j]=1/12\) for distinct \(i,j\); distinct directed phase monomials are orthogonal.

More generally the exact second-moment identity is
\[
\mathbb E[(X^*BX)\overline{(X^*CX)}]
=\frac{\operatorname{tr}(BC^*)+\operatorname{tr}(B)\overline{\operatorname{tr}(C)}}{12}.
\]

**Noncollinear case.** Three noncollinear eigenvalues are affinely independent as points in \(\mathbb R^2\). Since \(Z_A=\sum_j\lambda_jP_j\) and \(\sum_jP_j=1\), its complex value determines all three \(P_j\) uniquely. Thus the diagonal part \(\sum_jb_{jj}P_j\) is measurable from \(Z_A\), leaving precisely the previously computed off-diagonal error.

**Collinear case.** Reparameterize \(Z_A=a+(c-a)T\), where \(T=rP_2+P_3\). For \(0<t<1\), the simplex fiber \(T=t\) is the segment
\[
0\le P_2\le L_r(t),\qquad P_3=t-rP_2,\qquad P_1=1-t-(1-r)P_2.
\]
Its joint density is constant, so conditional on \(T=t\), \(P_2\) is uniform on this segment, with mean \(L_r(t)/2\) and variance \(L_r(t)^2/12\). Its marginal density is \(2L_r(t)\). Therefore
\[
\mathbb E\big[\operatorname{Var}(P_2\mid T)\big]
=\frac16\int_0^1L_r(t)^3\,dt
=\frac16\left(\frac r4+\frac{1-r}{4}\right)=\frac1{24}.
\]
The diagonal part of \(Z_B\) is \(b_{11}(1-T)+b_{33}T+DP_2\). Its conditional mean is the stated kinked predictor, with integrated residual squared \(|D|^2/24\). Phase orthogonality adds the independent off-diagonal contribution.

**Repeated spectra.** When \(A\) has at most two distinct eigenvalues, the numerical value identifies exactly the total squared mass in each eigenspace. Conditional Haar invariance inside each eigenspace implies
\[
\mathbb E[XX^*\mid Z_A]=\sum_{\lambda}\frac{\|P_\lambda X\|^2}{m_\lambda}P_\lambda.
\]
Taking the trace against \(B\) gives \(\mathbb E[Z_B\mid Z_A]=X^*\Pi_A(B)X\). Because \(\Pi_A\) is Hilbert--Schmidt orthogonal projection onto the algebra of matrices scalar on each spectral subspace, its residual has trace zero and is orthogonal to this algebra. The Haar second-moment identity then yields \(\mathcal R_A(B)=\|B-\Pi_A(B)\|_{\mathrm{HS}}^2/12\). This includes scalar \(A\) and multiplicities \((2,1)\).

**Affine optimality gap.** In case (ii), a complex affine function of \(Z_A\) and its conjugate is equivalent, on the supporting line, to a complex affine function of \(T\). Among diagonal matrices the corresponding two-dimensional operator space is \(\operatorname{span}\{I,A\}\). Its one-dimensional orthogonal complement is generated by the diagonal vector \((-(1-r),1,-r)\), of squared Euclidean norm \(H_r\). The Haar covariance identity gives affine diagonal risk \(|D|^2/(12H_r)\), to which the identical off-diagonal contribution is added. Since \(H_r/2=1-r(1-r)\) is in \([3/4,1)\), the global three-quarter inequality follows. Equality at \(r=1/2\) requires vanishing off-diagonal part and nonzero \(D\), as in the displayed example. Finally the noncollinear formula applies to \(A_\varepsilon\) for any nonzero \(\varepsilon\) and gives its zero loss.

## Verification

The accompanying `verify.py` independently generates deterministic-seed Haar samples, computes conditional predictors in all four spectral cases, and checks the empirical mean squared errors against the exact algebraic values. A successful run prints `all finite checks passed`. It uses Python and NumPy; its Monte Carlo tolerances are only consistency checks, not infinite proofs. The proof above gives the exact identities and covers all \(3\times3\) normal matrices and all complex \(B\).

## Relationship to prior work

Kaunisto, O'Loughlin and Virtanen (2026, arXiv:2610.00443, first public 2026-09-30), establish geometric dilation and complete spectral-set results for scaled numerical ranges, including the ordinary numerical-range endpoint. The present result instead asks how accurately one numerical evaluation predicts another under the canonical Haar distribution. Dunkl, Gawron, Holbrook, Puchała and Życzkowski (2010/2011) establish the simplex model and numerical-shadow moments for normal matrices; Gutkin and Życzkowski (2012/2013) develop joint numerical shadows. Their foundational constructions support the probability setting but the inspected theorems do not give the present exact nonlinear conditional-risk classification, its sharp one-quarter affine-prediction saving, or the collinearity discontinuity. A subsequent 2026 preprint on numerical information establishes a qualitative measurability criterion, not the finite positive loss constants.

## Limitations

The result assumes Haar-distributed complex pure states, normal \(3\times3\) input matrices, and noiseless infinite-resolution observation of one complex numerical value. It does not extend the constants to general dimensions, real-Haar spheres, normal matrices with four or more eigenvalues, or nonnormal matrices. Its discontinuity may disappear with positive observation noise; no noisy-measurement theorem is asserted. Literature priority is not independently certified; equivalent formulas may exist in unindexed statistical or quantum-information literature.

## References

1. M. Kaunisto, R. O'Loughlin and J. Virtanen, *Dilation Theory for Scaled q-Numerical Ranges*, arXiv:2610.00443v1 (2026-09-30), MSC2020 47A12.
2. C. F. Dunkl, P. Gawron, J. A. Holbrook, Z. Puchała and K. Życzkowski, *Numerical shadows: measures and densities on the numerical range*, arXiv:1010.4189 (2010), Linear Algebra Appl. 434 (2011).
3. E. Gutkin and K. Życzkowski, *Joint numerical ranges, quantum maps, and joint numerical shadows*, arXiv:1207.1227 (2012), Linear Algebra Appl. 438 (2013).
4. D. M. Johnson, *Numerical Information of Hilbert Space Operators*, arXiv:2610.29826v1 (first public 2026-10-21); qualitative criterion, later than the focal source.
