# A sharp affine-preconditioning barrier for inverse-square-root Arnoldi on a three-dimensional Jordan block

## Finding
For the real nilpotent shift \(N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}\), put \(A_K=I+KN\), \(K\geq0\). Consider every normalized real affine polynomial \(q_t(z)=1-t(z-1)\), \(t\in\mathbb R\), and the left inverse-square-root preconditioned matrix \(B_{K,t}=A_Kq_t(A_K)^2\).

**Sharp threshold.** There is a real slope \(t\) for which every first Arnoldi Rayleigh quotient \(v^*B_{K,t}v\), \(\|v\|_2=1\), lies in the *open* right half-plane if and only if \(0\leq K<\sqrt3\). The unique slope maximizing this admissible \(K\)-range is \(t=1/3\). At and above \(K=\sqrt3\), **every** such affine polynomial admits a real nonzero input \(b\) for which the first projected matrix in left polynomially preconditioned Arnoldi is the singular scalar \(H_1=[0]\). Yet for every \(K,t\), \(A_K\), \(q_t(A_K)\), and \(B_{K,t}\) all have spectrum \(\{1\}\): eigenvalue clustering and the square-root branch condition on \(q_t(A_K)\) do not exclude this singular compression.

The slope from the first-order Taylor approximation, \(t=1/2\), has the strictly smaller sharp safety range \(K<\sqrt{8/3}\). At \(K=\sqrt3\), \(t=1/3\), the input \(b=(1,0,1)^{\mathsf T}\) yields \(H_1=[0]\). In contrast, the degree-two polynomial \(q_2(z)=1-\tfrac12(z-1)+\tfrac38(z-1)^2\) obeys \(A_Kq_2(A_K)^2=I\) for **every** \(K\). Three dimensions are minimal for this degree-one-versus-degree-two obstruction: on the two-dimensional Jordan shift the degree-one Taylor polynomial gives the identity exactly.

## Assumptions and scope
All matrices and polynomial coefficients are real and all algebra is exact. Here \(K\geq0\) controls the superdiagonal size. The affine class is normalized by \(q(1)=1\), consistent with approximating \(z^{-1/2}\) at the sole eigenvalue. Allowing an arbitrary positive constant \(q(1)\) only multiplies the preconditioned matrix by a positive scalar and does not change whether its numerical range contains zero. The left preconditioned one-step Arnoldi starting vector is \(c=q_t(A_K)b\), as in the first step of the polynomial inverse-square-root method. A ``safe'' polynomial means that \(\operatorname{Re}(v^*B_{K,t}v)>0\) for every unit complex vector \(v\), a sufficient uniform criterion that every one-dimensional Arnoldi compression avoids the inverse-square-root branch cut and pole. Failure of this condition here is strengthened to **existence of an exactly zero compression**, not a claim that all starting vectors fail.

## Proof
Let \(X=KN\). Because \(X^3=0\), exact multiplication gives
\[
q_t(A_K)=I-tX,\qquad B_{K,t}=(I+X)(I-tX)^2=I+aN+b_2N^2,
\]
where \(a=K(1-2t)\) and \(b_2=K^2(t^2-2t)\). These matrices are upper triangular with diagonal entries one, proving their claimed spectra and invertibility.

The real symmetric part \(S=(B_{K,t}+B_{K,t}^{\mathsf T})/2\) is
\[
S=\begin{pmatrix}1&a/2&b_2/2\\a/2&1&a/2\\b_2/2&a/2&1\end{pmatrix}.
\]
On the antisymmetric vector \((1,0,-1)^{\mathsf T}\) it has eigenvalue \(1-b_2/2\). On the orthonormal symmetric subspace spanned by \((1,0,1)^{\mathsf T}/\sqrt2\) and \((0,1,0)^{\mathsf T}\), it has the matrix
\[
T=\begin{pmatrix}1+b_2/2&a/\sqrt2\\a/\sqrt2&1\end{pmatrix},\qquad
2\det T=2-K^2(1-2t+3t^2).
\]
Therefore \(S\) is positive definite precisely when \(b_2<2\) and \(2-K^2(1-2t+3t^2)>0\). But
\[
1-2t+3t^2=\frac23+3\left(t-\frac13\right)^2.
\]
For \(K\geq\sqrt3\), every \(t\) gives \(\det T\leq0\), so \(S\) has a nonpositive eigenvalue. Conversely, \(t=1/3\) gives \(b_2=-5K^2/9<2\) and \(2\det T=2-(2/3)K^2>0\) for \(K<\sqrt3\). The strict minimum in the displayed quadratic establishes uniqueness of the globally extremal slope.

For \(K\geq\sqrt3\), choose a unit real vector with nonpositive Rayleigh quotient of \(S\). Since \(e_2^{\mathsf T}Se_2=1\), continuity on the real unit sphere gives a nonzero real vector \(v\) with \(v^{\mathsf T}B_{K,t}v=v^{\mathsf T}Sv=0\). Since \(q_t(A_K)\) is invertible, the input \(b=q_t(A_K)^{-1}v\) generates this normalized first Arnoldi vector, and \(H_1=[v^{\mathsf T}B_{K,t}v]=[0]\). For the explicit endpoint, taking \(K=\sqrt3\), \(t=1/3\), \(b=(1,0,1)^{\mathsf T}\) gives \(q_t(A_K)b=(1,-1/\sqrt3,1)^{\mathsf T}\), a zero-Rayleigh vector. For \(t=1/2\), \(a=0\) and \(b_2=-3K^2/4\); the symmetric-part eigenvalues are \(1\), \(1+3K^2/8\), \(1-3K^2/8\), giving \(K<\sqrt{8/3}\).

Finally, \(q_2(A_K)=I-X/2+3X^2/8\); direct squaring gives \(q_2(A_K)^2=I-X+X^2\), so multiplication by \(I+X\) yields \(I\), since \(X^3=0\). For \(K>0\), no affine \(q_t\) gives \(B_{K,t}=I\), since the coefficient of \(N\) forces \(t=1/2\), leaving the nonzero coefficient \(-3K^2/4\) of \(N^2\). In dimension two, \(N^2=0\), so \(t=1/2\) already gives identity.

## Verification
The standalone script `checker.py` re-derives \(B_{K,t}\), diagonalizes the symmetric part into the antisymmetric and symmetric invariant blocks, checks the determinant and sharp quadratic identity symbolically, verifies the explicit zero compression, and verifies the exact degree-two identity. It also compares direct matrix products at eighteen rational parameter pairs. Run with `python checker.py` using Python and SymPy. The inequalities and the existence statements above are proved algebraically; finite checks corroborate but do not replace their proofs.

## Relationship to prior work
Frommer, Ramirez-Hidalgo, Schweitzer, and Tsolakis (2024) introduce left/right polynomially preconditioned Arnoldi for the inverse square root, including the expression \(Aq(A)^2\), a branch condition on \(q(A)\), and the possibility that ordinary Ritz values near zero obstruct inverse-square-root computations. Those mechanisms are **prior**. The new claim is the *sharp optimization over all normalized real affine slopes* on a minimal nonnormal Jordan test, the exact threshold \(\sqrt3\), the explicit singular first projection despite spectrum \(\{1\}\), and the degree-two rescue. Carden and Embree (2012) investigate Ritz localization for non-Hermitian matrices including a three-dimensional Jordan block; general numerical-range facts are prior. Embree, Loe, and Morgan (2021) discuss stability control for polynomially preconditioned Arnoldi eigenvalue calculations. No priority over these general principles is asserted.

## Limitations
The sharp threshold applies only to the specified three-dimensional Jordan family, real affine polynomials normalized at eigenvalue one, exact arithmetic, and one-dimensional standard Arnoldi compressions in the *left* inverse-square-root method. The source does not claim all spectral preconditioners preserve the field of values; no such statement is attributed to it. Singular projected matrices occur for selected starting vectors, not generically for all starting vectors. A quadratic polynomial is exact here because the minimal polynomial has degree three; no general degree-two remedy is claimed for larger matrices. The available text of Carden and Embree's plausible related Ritz-localization study was limited to its abstract, so unseen specialized calculations are a residual publication-priority risk. No independent external validation has been performed.

## References
1. A. Frommer, G. Ramirez-Hidalgo, M. Schweitzer, M. Tsolakis, *Polynomial Preconditioning for the Action of the Matrix Square Root and Inverse Square Root*, arXiv:2401.06684v1 (12 January 2024), https://arxiv.org/html/2401.06684v1.
2. R. L. Carden and M. Embree, *Ritz Value Localization for Non-Hermitian Matrices*, SIAM Journal on Matrix Analysis and Applications 33 (2012), 1320–1338, https://doi.org/10.1137/120872693.
3. M. Embree, J. A. Loe, R. B. Morgan, *Polynomial Preconditioned Arnoldi with Stability Control*, SIAM Journal on Scientific Computing 43 (2021), A1–A25, https://doi.org/10.1137/19M1302430.
