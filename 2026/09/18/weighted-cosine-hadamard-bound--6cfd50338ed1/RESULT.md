# Weighted-cosine Hadamard bound fails exactly from dimension three

## Statement

Let \(\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n)\succ0\), let \(U,V\in O(n)\), and write \(u_i,v_j\) for their rows. Define the weighted-cosine matrix
\[
C_\Sigma(U,V)_{ij}
=
\frac{u_i\Sigma v_j^{\mathsf T}}
{\sqrt{u_i\Sigma u_i^{\mathsf T}}\sqrt{v_j\Sigma v_j^{\mathsf T}}}.
\]
Set
\[
\gamma=\frac{\|\sigma\|_1^2}{\|\sigma\|_2^2}.
\]
Appendix A of Loe--Huang--Needell (2026) conjectures
\[
\|C_\Sigma(U,V)\|_F^2\le \frac{n^2}{\gamma}
= n^2\frac{\|\sigma\|_2^2}{\|\sigma\|_1^2},
\tag{1}
\]
with a common normalized Hadamard frame attaining equality whenever such a frame exists.

The dimensional boundary of (1) is exact:

**Theorem.** Inequality (1) holds for every positive diagonal \(\Sigma\) and every \(U,V\in O(n)\) when \(n\le2\). For every \(n\ge3\), there are positive diagonal \(\Sigma\) and an orthogonal matrix \(U\) such that
\[
\|C_\Sigma(U,U)\|_F^2
>
 n^2\frac{\|\sigma\|_2^2}{\|\sigma\|_1^2}.
\]
Thus the conjecture already fails in the common-frame, positive-definite case. In dimension four, where a real Hadamard frame exists, an explicit common frame strictly exceeds the Hadamard value, so the Hadamard frame is not a global maximizer in general.

## A three-dimensional exact counterexample

Take
\[
\Sigma_3=\operatorname{diag}(10,2,1)
\]
and
\[
U_3=
\begin{pmatrix}
 \sqrt{7/20} & -1/\sqrt2 & \sqrt{3/20}\\
 \sqrt{7/20} &  1/\sqrt2 & \sqrt{3/20}\\
 -\sqrt{3/10} & 0 & \sqrt{7/10}
\end{pmatrix}.
\]
Directly, \(U_3U_3^{\mathsf T}=I\). Let
\[
B_3=U_3\Sigma_3U_3^{\mathsf T}
=
\begin{pmatrix}
93/20&53/20&-9\sqrt{42}/20\\
53/20&93/20&-9\sqrt{42}/20\\
-9\sqrt{42}/20&-9\sqrt{42}/20&37/10
\end{pmatrix}.
\]
For a common frame, \(C_{\Sigma_3}(U_3,U_3)\) is the correlation normalization of \(B_3\), so
\[
\|C_{\Sigma_3}(U_3,U_3)\|_F^2
=
\sum_{i,j}\frac{(B_3)_{ij}^2}{(B_3)_{ii}(B_3)_{jj}}
=
\frac{1800677}{320013}
\approx5.6268870327.
\]
The conjectured upper bound is
\[
9\frac{10^2+2^2+1^2}{(10+2+1)^2}
=
\frac{945}{169}
\approx5.5917159763.
\]
The exact violation is
\[
\boxed{
\frac{1800677}{320013}-\frac{945}{169}
=
\frac{1902128}{54082197}>0.
}
\tag{2}
\]
All entries and the final comparison are exact algebraic quantities; no floating-point search is needed to validate the counterexample.

## Failure in every dimension at least three

Let \(r=n-3\ge0\), set
\[
t=\frac{105}{13},
\qquad
\Sigma_n=\operatorname{diag}(10,2,1,\underbrace{t,\ldots,t}_{r\text{ copies}}),
\qquad
U_n=\operatorname{diag}(U_3,I_r).
\]
A simultaneous permutation of the diagonal of \(\Sigma_n\) and the columns of \(U_n\) can be used if decreasingly ordered weights are desired; it does not change the weighted-cosine matrix.

The weighted-cosine matrix is block diagonal:
\[
C_{\Sigma_n}(U_n,U_n)
=
\operatorname{diag}(C_{\Sigma_3}(U_3,U_3),I_r),
\]
so
\[
\|C_{\Sigma_n}(U_n,U_n)\|_F^2
=
\frac{1800677}{320013}+r.
\tag{3}
\]
Moreover,
\[
\|\sigma\|_1=13+rt,
\qquad
\|\sigma\|_2^2=105+rt^2,
\]
and the conjectured right-hand side simplifies to
\[
n^2\frac{\|\sigma\|_2^2}{\|\sigma\|_1^2}
=
\frac{105(r+3)^2}{169+105r}.
\tag{4}
\]
Subtracting (4) from (3) gives
\[
\boxed{
\frac{4(10386273r+475532)}{320013(105r+169)}>0,
}
\tag{5}
\]
for every \(r\ge0\). Hence the conjectured bound fails for every \(n\ge3\).

### A dimension-four witness against an actual Hadamard frame

For \(n=4\), use
\[
\Sigma_4=\operatorname{diag}\left(10,2,1,\frac{105}{13}\right),
\qquad
U_4=\operatorname{diag}(U_3,1).
\]
Then
\[
\|C_{\Sigma_4}(U_4,U_4)\|_F^2
=
\frac{2120690}{320013}
\approx6.6268870327.
\]
A normalized real Hadamard matrix of order four attains the value asserted in the source paper,
\[
\frac{16}{\gamma}=\frac{840}{137}\approx6.1313868613,
\]
but the above common frame exceeds it by
\[
\boxed{
\frac{21723610}{43841781}\approx0.4955001714.
}
\]
Thus the source paper's Hadamard stationary point need not be a global maximizer even in the first nontrivial order admitting a real Hadamard matrix.

## Why the conjecture is nevertheless correct in dimension two

The two-dimensional case has a clean structural proof. Assume \(\Sigma=\operatorname{diag}(a,b)\) with \(a,b>0\). For an orthonormal basis \(u_1,u_2\), define the normalized transformed vectors
\[
x_i=\frac{\Sigma^{1/2}u_i^{\mathsf T}}
{\sqrt{u_i\Sigma u_i^{\mathsf T}}},
\qquad i=1,2.
\]
Let \(X=[x_1\ x_2]\), and define \(Y\) analogously from the rows of \(V\). Then
\[
C_\Sigma(U,V)=X^{\mathsf T}Y,
\qquad
\|C_\Sigma(U,V)\|_F^2
=
\operatorname{tr}\big((XX^{\mathsf T})(YY^{\mathsf T})\big).
\tag{6}
\]
The two eigenvalues of \(XX^{\mathsf T}\) are \(1\pm |r_U|\), where
\[
r_U=x_1^{\mathsf T}x_2.
\]
Writing \(u_1=(\cos\theta,\sin\theta)\) and taking the orthogonal complement for \(u_2\),
\[
|r_U|^2
=
\frac{(a-b)^2\sin^2\theta\cos^2\theta}
{ab+(a-b)^2\sin^2\theta\cos^2\theta}
\le
\frac{(a-b)^2}{(a+b)^2}.
\tag{7}
\]
The same bound holds for \(r_V\). By the trace form of von Neumann's eigenvalue inequality applied to the two positive semidefinite frame operators in (6),
\[
\|C_\Sigma(U,V)\|_F^2
\le
(1+|r_U|)(1+|r_V|)+(1-|r_U|)(1-|r_V|)
\le
2+2\left(\frac{a-b}{a+b}\right)^2.
\]
Finally,
\[
2+2\left(\frac{a-b}{a+b}\right)^2
=
4\frac{a^2+b^2}{(a+b)^2}
=
\frac{n^2}{\gamma}
\quad(n=2).
\]
A common \(45^\circ\) frame attains equality. The case \(n=1\) is immediate.

## Interpretation

For \(U=V\), the problem is equivalently an extremal question over the orthogonal orbit of a positive-definite matrix: if \(B=U\Sigma U^{\mathsf T}\) and \(D=\operatorname{diag}(B)\), then
\[
C_\Sigma(U,U)=D^{-1/2}BD^{-1/2}.
\]
A Hadamard frame equalizes the diagonal of \(B\), but diagonal equalization does not maximize the Frobenius norm after correlation normalization once dimension is at least three. The explicit witness above shows that allowing unequal diagonal entries can increase the normalized off-diagonal energy enough to beat the equal-diagonal value.

This result concerns Appendix A's weighted-cosine extremal conjecture. It does not invalidate the exterior-algebraic CUR residual identities, the ACA analysis, or the weighted-mass pivoting experiments in the source paper.

## Reproducibility

`artifacts/verify.py` uses exact symbolic arithmetic to verify orthogonality of the three-dimensional frame, the exact correlation-normalized Frobenius value, the all-dimension extension, the dimension-four Hadamard gap, and the algebraic identity underlying the two-dimensional bound. `artifacts/verification.txt` records the executed output. The verification was run with Python 3.13.5 and SymPy 1.14.0.

## References

1. T. Loe, L. Huang, and D. Needell, *A Geometric View of Adaptive Cross Approximation via Exterior Algebra*, arXiv:2609.17947, 2026. https://arxiv.org/abs/2609.17947
2. R. Grone and S. Pierce, *Permanental Inequalities for Correlation Matrices*, SIAM Journal on Matrix Analysis and Applications 9(2), 1988. https://doi.org/10.1137/0609016
3. N. J. Higham, *Computing the Nearest Correlation Matrix---A Problem from Finance*, IMA Journal of Numerical Analysis 22(3), 2002. https://eprints.maths.manchester.ac.uk/232/
4. H. Chen, *Quotient Geometry of Bounded or Fixed-Rank Correlation Matrices*, SIAM Journal on Matrix Analysis and Applications, 2024. https://doi.org/10.1137/24M1630566
5. J. P. Chehab, H. Oviedo, and M. Raydan, *Optimization schemes on manifolds for structured matrices with fixed eigenvalues*, Computational Optimization and Applications, 2024. https://doi.org/10.1007/s10589-024-00630-3
