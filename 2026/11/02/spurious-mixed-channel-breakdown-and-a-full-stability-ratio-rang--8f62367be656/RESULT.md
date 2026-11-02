# Spurious mixed-channel breakdown and a full stability-ratio range for extended Krylov bases

## Finding
Let \(A\) be a real, nonsingular symmetric matrix and let \(v\) be a unit starting vector. Compare the inverse-leading mixed-channel extended Krylov basis, which orthogonalizes \(A^{-1}v\) followed by \(Av_2\), with the inverse-leading split-channel basis, which orthogonalizes \(A^{-1}v\) followed by \(Av\). Assume both initial vectors are independent. Writing \(\alpha=v^{\mathsf T}A^{-1}v\), the mixed-channel third candidate has zero orthogonal residual while the split-channel candidate is nonzero precisely when \(\alpha=0\) and \(\{v,A^{-1}v,Av\}\) is linearly independent.

A genuine such third-step, non-lucky mixed-channel breakdown is possible for some real starting vector if and only if \(A\) is indefinite and has at least three distinct eigenvalues. It cannot occur for definite symmetric matrices or for matrices with fewer than three distinct eigenvalues.

For the **fixed**, nonsingular, real symmetric matrix
\[
A=\operatorname{diag}(-1,1,2),\qquad \kappa_2(A)=2,
\]
and \(b_r=(3,r,4r)^{\mathsf T}\), \(0<r\le 1\), the three Laurent-Krylov vectors are independent. At \(r=1\) the mixed channel breaks down at its third vector, whereas the split channel continues. For \(0<r<1\), if \(\rho_M\) and \(\rho_S\) are the local normalized third-step orthogonalization residuals of the mixed and split channels, their ratio \(\gamma_3=\rho_M/\rho_S\) satisfies
\[
\gamma_3(r)^2=\frac{81(1-r^2)^2(65r^2+9)}{4r^2(4r^2+9)(5r^2+333)}.
\]
It ranges over **all positive real numbers** even though the underlying matrix, its singular-value condition number and its spectrum never change. Specifically, \(\lim_{r\downarrow0}r\gamma_3(r)=3/(2\sqrt{37})\) and \(\lim_{r\uparrow1}\gamma_3(r)/(1-r)=9\sqrt{481}/169\).

## Assumptions and scope
All calculations are in exact real arithmetic. Starting vectors are normalized to \(v=b/\|b\|_2\). Set \(z=A^{-1}v\), \(\alpha=v^{\mathsf T}z\), and \(\beta=\|z-\alpha v\|_2>0\). The common second orthonormal vector is \(v_2=(z-\alpha v)/\beta\); write \(P\) for the orthogonal projector onto \(\operatorname{span}\{v,z\}\). The third-step candidates are \(Av_2\) (mixed) and \(Av\) (split). Their normalized residual fractions are
\[
\rho_M=\frac{\|(I-P)Av_2\|_2}{\|Av_2\|_2},\qquad
\rho_S=\frac{\|(I-P)Av\|_2}{\|Av\|_2}.
\]
The comparison is meaningful when \((I-P)Av\ne0\) and \(\alpha\ne0\); at \(\alpha=0\) the mixed channel has an exact third-step zero despite a three-dimensional Laurent-Krylov space. No floating-point orthogonality-loss or ultimate approximation-error claim is made.

## Proof
**1. An exact channel identity.** Since \(Az=v\), direct multiplication gives
\[
Av_2=\frac{v-\alpha Av}{\beta},\qquad
(I-P)Av_2=-\frac{\alpha}{\beta}(I-P)Av.
\]
Thus the first residual vanishes and the second does not exactly when \(\alpha=0\) and \((I-P)Av\ne0\). When both are nonzero, cancellation of the common factors yields the exact local ratio
\[
\frac{\rho_M}{\rho_S}=\frac{|\alpha|\,\|Av\|_2}{\|v-\alpha Av\|_2}.
\]
The denominator is positive under three-vector independence: if \(v-\alpha Av=0\) with \(\alpha\ne0\), then \(Av\) is proportional to \(v\), contradicting independence.

**2. Complete existence criterion.** If \(\alpha=0\), \(v^{\mathsf T}A^{-1}v=0\) forces \(A^{-1}\), hence \(A\), to be indefinite. If \(\{v,A^{-1}v,Av\}\) is independent, the minimal polynomial of \(A\) on the span of the spectral components of \(v\) has degree at least three, hence \(A\) has at least three distinct eigenvalues. Conversely, suppose \(A\) is indefinite with three distinct eigenvalues, including both signs. Pick three associated orthonormal eigenvectors, with nonzero amplitudes whose squared amplitudes \(w_j>0\) obey \(\sum_{j=1}^3 w_j/\lambda_j=0\). This is possible because one reciprocal eigenvalue is positive and another negative: choose a sufficiently small positive third weight, and adjust the two opposite-sign weights. Normalize the amplitudes. The resulting vector has \(\alpha=0\). Independence follows by factoring its three nonzero coordinates from the matrix with rows \((1,\lambda_j^{-1},\lambda_j)\): its determinant is nonzero for distinct nonzero \(\lambda_j\), because after row multiplication by \(\lambda_j\) it is (up to column order) a Vandermonde matrix. Thus the mixed third step is spurious while the split third step is not.

**3. A fixed condition-two family and exact range.** Let \(A=\operatorname{diag}(-1,1,2)\) and \(b_r=(3,r,4r)^{\mathsf T}\). Then \(A^{-1}b_r=(-3,r,2r)^{\mathsf T}\), \(Ab_r=(-3,r,8r)^{\mathsf T}\), and
\[
\det[b_r,A^{-1}b_r,Ab_r]=36r^2\ne0,\qquad
\alpha=\frac{9(r^2-1)}{9+17r^2}.
\]
For \(r=1\) the third mixed candidate is proportional to \(b_1\), but the true three-dimensional space remains unexhausted. For \(0<r<1\), substitute these vectors and \(\alpha\) in the exact local ratio of step 1, giving after rational simplification
\[
\gamma_3(r)^2=\frac{81(1-r^2)^2(65r^2+9)}{4r^2(4r^2+9)(5r^2+333)}.
\]
It is positive and continuous for \(r\in(0,1)\). Expanding the displayed rational function at the two endpoints proves
\[
\lim_{r\downarrow0}r\gamma_3(r)=\frac{3}{2\sqrt{37}},\qquad
\lim_{r\uparrow1}\frac{\gamma_3(r)}{1-r}=\frac{9\sqrt{481}}{169}.
\]
The intermediate-value theorem gives the full range \((0,\infty)\) on one fixed matrix. This proves all statements.

## Verification
The standalone Python 3 file `verify.py` uses standard-library `fractions.Fraction` and independently implements both Gram-projection residuals in exact rational arithmetic. It checks the nonzero Laurent determinant, inverse Rayleigh quotient, projected-residual identity, spurious breakdown at the endpoint and the full rational ratio formula over 2,317 deterministic test cases, including values close to both endpoints. Run `python3 verify.py`: the expected output is `EXACT_VERIFY_PASS 2317`. Finite tests are corroboration only; the preceding algebra and Vandermonde argument prove the quantified statements.

## Relationship to prior work
Lund and Schweitzer introduce and compare inverse-leading mixed- and split-channel extended Krylov orthogonalization (Algorithms 1–2) and prove a normalized-residual ordering for symmetric positive-definite matrices (Theorem 8, under no breakdown). Their indefinite experiments show that no simple numerical ordering persists, but do not supply the present exact third-step non-lucky-breakdown criterion, symmetric-matrix existence classification, or fixed \(\kappa_2=2\) complete positive stability-ratio range. Elsworth and Güttel discuss general rational-Arnoldi continuation/deflation, and Schweitzer (2016) discusses biorthogonal breakdown for a different two-sided process; neither inspected analysis implies the explicit Euclidean single-vector channel identity or its quantitative fixed-matrix consequence. The general phenomenon that Krylov recurrences can break down is not claimed as new.

## Limitations
The claim concerns the first three exact-arithmetic vectors, normalized **orthogonalization** residual fractions, and a single-vector symmetric problem. It does not assert that this is the first possible breakdown in any generalized block/deflated algorithm; nor does it assert floating-point loss of orthogonality, error in approximating a matrix function, or improved overall runtime. The three-dimensional family's near-zero parameter limit also makes the input vectors approach a degenerate two-dimensional configuration; each strictly positive parameter still has full Krylov dimension. Although primary works and related records were inspected, earlier specialized literature might contain an equivalent identity or stronger implication; independent review and exhaustive priority confirmation remain outstanding.

## References
1. K. Lund and M. Schweitzer, *On the stability of basis construction in extended Krylov subspace methods*, arXiv:2610.21603v1, first posted 2026-10-15. https://arxiv.org/html/2610.21603
2. S. Elsworth and S. Güttel, *The Block Rational Arnoldi Method*, 2019 preprint. https://eprints.maths.manchester.ac.uk/2685/1/paper.pdf
3. M. Schweitzer, *A two-sided short-recurrence extended Krylov subspace method for nonsymmetric matrices and its relation to rational moment matching*, 2016 preprint. https://imacm.uni-wuppertal.de/fileadmin/imacm/preprints/2016/imacm_16_08.pdf
