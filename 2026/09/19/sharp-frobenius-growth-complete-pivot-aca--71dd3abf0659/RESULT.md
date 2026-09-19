# Sharp one-step Frobenius growth under complete-pivot ACA

## Statement

Let \(A\in\mathbb R^{n\times m}\) be nonzero, and let \((i,j)\) be a complete-pivot ACA choice,
\[
|A_{ij}|=\|A\|_{\max}.
\]
Define the rank-one ACA residual
\[
E=A-\frac{A(:,j)A(i,:)}{A_{ij}}.
\]
Then
\[
\boxed{
\frac{\|E\|_F}{\|A\|_F}
\le
\sqrt{\frac{nm}{n+m-1}}.
}
\tag{1}
\]
For square matrices of every order \(N\ge4\), this constant is sharp as a supremum even when the complete pivot is required to be unique. Consequently, a single greedy largest-entry ACA step can increase the Frobenius residual by a factor arbitrarily close to
\[
\boxed{\frac{N}{\sqrt{2N-1}}\sim \sqrt{\frac N2}}.
\tag{2}
\]
Thus largest-entry pivoting controls the entrywise pivot but does not make the Frobenius residual monotone.

## Proof of the universal bound

Permute rows and columns so that the pivot is in position \((1,1)\), and scale the whole matrix by the reciprocal of the pivot. Neither operation changes the ratio in (1). We may therefore write
\[
A=
\begin{pmatrix}
1&c^T\\
r&X
\end{pmatrix},
\qquad |A_{pq}|\le1.
\]
The ACA update annihilates the pivot row and column:
\[
E=
\begin{pmatrix}
0&0\\
0&X-rc^T
\end{pmatrix}.
\]
Set
\[
R=\|r\|_2,
\qquad C=\|c\|_2,
\qquad x=\|X\|_F,
\qquad B=1+R^2+C^2.
\]
By the triangle inequality,
\[
\|E\|_F\le x+RC.
\]
For fixed \(R,C\), the elementary identity
\[
\left(1+\frac{R^2C^2}{B}\right)(B+x^2)-(x+RC)^2
=
\frac{(B-xRC)^2}{B}
\]
gives
\[
\frac{\|E\|_F^2}{\|A\|_F^2}
\le
\frac{(x+RC)^2}{B+x^2}
\le
1+\frac{R^2C^2}{1+R^2+C^2}.
\tag{3}
\]
Complete pivoting implies
\[
R^2\le n-1,
\qquad C^2\le m-1.
\]
Since \(uv/(1+u+v)\) is increasing in each nonnegative argument,
\[
1+\frac{R^2C^2}{1+R^2+C^2}
\le
1+\frac{(n-1)(m-1)}{n+m-1}
=
\frac{nm}{n+m-1},
\]
which proves (1).

## Sharpness with a unique largest entry

Fix \(N\ge4\), put \(s=N-1\), and let \(0<\alpha<1\). Define
\[
B_\alpha=1+2s\alpha^2,
\qquad
\beta_\alpha=\frac{B_\alpha}{s^2\alpha^2},
\]
and
\[
A_{N,\alpha}=
\begin{pmatrix}
1&\alpha\mathbf1^T\\
\alpha\mathbf1&-\beta_\alpha\mathbf1\mathbf1^T
\end{pmatrix}.
\tag{4}
\]
For \(\alpha\) sufficiently close to \(1\), one has \(\beta_\alpha<1\), because
\[
\beta_\alpha<1
\iff
\alpha^2>\frac{1}{(N-1)(N-3)}.
\]
Hence \((1,1)\) is the unique largest-magnitude entry of \(A_{N,\alpha}\).

For this family,
\[
R^2=C^2=s\alpha^2,
\qquad
\|X\|_F=s\beta_\alpha
=
\frac{B_\alpha}{s\alpha^2}
=
\frac{B_\alpha}{RC}.
\]
Moreover \(X\) is antiparallel to \(rc^T\), so equality holds in both inequalities leading to (3). Therefore
\[
\boxed{
\frac{\|E_{N,\alpha}\|_F^2}{\|A_{N,\alpha}\|_F^2}
=
1+\frac{s^2\alpha^4}{1+2s\alpha^2}.
}
\tag{5}
\]
Taking \(\alpha\uparrow1\) yields
\[
1+\frac{(N-1)^2}{2N-1}
=
\frac{N^2}{2N-1},
\]
which proves the sharpness claim (2) while preserving a unique complete pivot for every finite member of the sequence.

If ties are permitted, the limiting matrix itself is an exact extremizer: take \(\alpha=1\) and \(\beta=(2N-1)/(N-1)^2<1\), and choose the upper-left entry among the tied unit-magnitude pivots.

## Exact one-step monotonicity certificate

For an arbitrary nonzero pivot \(a=A_{ij}\), write
\[
c=A(:,j),\qquad r=A(i,:).
\]
Direct expansion gives
\[
\boxed{
\|E\|_F^2-\|A\|_F^2
=
\frac{\|c\|_2^2\|r\|_2^2-2a\,c^TAr^T}{a^2}.
}
\tag{6}
\]
Thus the ACA step decreases the Frobenius norm exactly when
\[
2a\,c^TAr^T>\|c\|_2^2\|r\|_2^2.
\tag{7}
\]
The largest-entry condition alone does not imply (7). Formula (6) is also a convenient local diagnostic for pivot rules intended to remove residual mass rather than merely maximize a single entry.

## Consequence for later ACA steps

After \(k\) successful complete-pivot ACA steps, the previously selected rows and columns of the residual are zero. Applying (1) to the active \((n-k)\times(m-k)\) block gives the per-step estimate
\[
\boxed{
\|E_{k+1}\|_F
\le
\sqrt{
\frac{(n-k)(m-k)}{n+m-2k-1}
}
\,\|E_k\|_F.
}
\tag{8}
\]
This is a one-step bound only; no claim is made that the sharp examples for successive active dimensions can be realized simultaneously by a single matrix.

## Positive-semidefinite contrast

For a symmetric positive-semidefinite residual, a largest-magnitude entry can be chosen on the diagonal because
\[
|A_{ij}|^2\le A_{ii}A_{jj}.
\]
A diagonal ACA pivot then produces the positive-semidefinite Schur residual
\[
E=A-\frac{A(:,i)A(i,:)}{A_{ii}},
\qquad 0\preceq E\preceq A.
\]
Consequently
\[
\|E\|_F\le\|A\|_F.
\]
The \(\Theta(\sqrt N)\) one-step amplification is therefore an obstruction for general/asymmetric complete-pivot ACA, not for the diagonal positive-semidefinite pivoted-Cholesky setting.

## Context and direction of improvement

Loe, Huang, and Needell (2026) analyze ACA through exterior algebra and emphasize that greedy largest-entry pivoting can perform poorly. They formulate the standard update used above and connect it to Gaussian elimination with complete pivoting; their new rank-one analysis is geometric and singular-vector dependent. The present result supplies a complementary dimension-only statement: it identifies the exact worst possible one-step Frobenius amplification scale and shows that the scale is genuinely attainable by a unique greedy pivot.

Classical complete-pivoting theory instead centers on entrywise growth factors. Cortinovis, Kressner, and Massei (2020) explicitly analyze ACA with complete pivoting through the max-norm growth factor \(\rho_k\), following Wilkinson's complete-pivoting theory. Bound (1) is different: it is a sharp one-step Frobenius-residual factor relative to the *current Frobenius residual*, rather than an entrywise growth factor relative to the initial max norm or a global approximation-to-SVD estimate.

## Verification

`artifacts/verify_aca_frobenius_growth.py` evaluates the explicit family (4), checks the identity (6) on deterministic pseudorandom matrices, tests the dimension bound on those matrices, and verifies positive-semidefinite monotonicity on Gram matrices. The supplied output shows, for example,
\[
N=100:\qquad
\frac{\|E\|_F}{\|A\|_F}=7.088805067425,
\qquad
\frac{N}{\sqrt{2N-1}}=7.088812050083
\]
for \(\alpha=0.999999\). These computations are supplementary checks; the theorem is proved algebraically above.

## Limitations

The theorem concerns one exact-arithmetic rank-one ACA update under complete largest-entry pivoting. It does not provide a multi-step global Frobenius growth factor, a backward-error theorem for floating-point LU, or an average-case prediction for kernel matrices. The sharp family is adversarial and highly structured. The result also does not imply that weighted-mass or other alternative pivot rules are globally optimal; it only quantifies what largest-entry pivoting alone cannot prevent.

## Originality scope

To the best of our knowledge, the new claim is the sharp dimension-dependent factor (1), together with the unique-largest-pivot sharpness construction (4)-(5) and its ACA interpretation. The general ACA update, its equivalence to complete-pivot Gaussian elimination, classical max-entry growth factors, maximum-volume cross approximation, and positive-semidefinite pivoted-Cholesky monotonicity are prior knowledge and are not claimed as new. Formula (6) is an elementary norm expansion and is included primarily as a useful certificate rather than as a broad standalone novelty claim.

The principal residual originality risk is the large classical literature on Gaussian-elimination growth and Schur complements: a norm-growth result under different terminology could contain an equivalent one-step Frobenius estimate. The checked complete-pivoting and cross-approximation sources focus on max-entry growth, global approximation bounds, or structure-specific results; no equivalent sharp factor was located in the material inspected.

## References

1. T. Loe, L. Huang, and D. Needell, *A Geometric View of Adaptive Cross Approximation via Exterior Algebra*, arXiv:2609.17947v1, 2026. https://arxiv.org/abs/2609.17947
2. A. Cortinovis, D. Kressner, and S. Massei, *On maximum volume submatrices and cross approximation for symmetric semidefinite and diagonally dominant matrices*, Linear Algebra and its Applications 593 (2020), 251-268. https://doi.org/10.1016/j.laa.2020.02.010
3. J. H. Wilkinson, *Error Analysis of Direct Methods of Matrix Inversion*, Journal of the ACM 8 (1961), 281-330. https://doi.org/10.1145/321075.321076
4. V. A. Yastrebov and C. Nous, *Adaptive Cross Approximation with a Geometrical Pivot Choice: ACA-GP Method*, arXiv:2502.03886, 2025. https://arxiv.org/abs/2502.03886
