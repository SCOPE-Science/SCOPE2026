# A dimension-three counterexample to the weighted-cosine Hadamard bound

## Statement

Loe, Huang, and Needell (arXiv:2609.17947v1) define, for a positive diagonal matrix
\[
\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n),\qquad U,V\in O(n),
\]
the weighted-cosine matrix
\[
C_\Sigma(U,V)_{ij}
=\frac{u_i^\top\Sigma v_j}
{\sqrt{(u_i^\top\Sigma u_i)(v_j^\top\Sigma v_j)}}
\]
and the effective spectral dimension
\[
\gamma=\frac{\|\sigma\|_1^2}{\|\sigma\|_2^2}.
\]
Their Appendix A reports numerical evidence for the conjectural upper bound
\[
\|C_\Sigma(U,V)\|_F^2\le \frac{n^2}{\gamma},
\]
with equality at a common orthogonally scaled Hadamard frame when such a frame exists.

The bound is false. It already fails for a symmetric choice \(U=V\) in dimension three, and dimension three is minimal: the conjectured inequality is valid for every positive spectrum and every pair \(U,V\in O(n)\) when \(n\le 2\). The failure is robust over an open one-parameter family of spectra. It also yields an order-four counterexample, so the failure persists in a dimension where a real Hadamard frame exists.

## Exact dimension-three counterexample

Take
\[
\Sigma=\operatorname{diag}(3,1,1/3)
\]
and
\[
U=V=
\begin{pmatrix}
1/\sqrt3&\sqrt{2/3}&0\\
-1/\sqrt3&1/\sqrt6&1/\sqrt2\\
1/\sqrt3&-1/\sqrt6&1/\sqrt2
\end{pmatrix}.
\]
The rows are orthonormal. Direct multiplication gives
\[
B:=U\Sigma U^\top=
\begin{pmatrix}
5/3&-2/3&2/3\\
-2/3&4/3&-1\\
2/3&-1&4/3
\end{pmatrix}.
\]
For \(U=V\), the squared weighted cosines are the squared correlations of \(B\):
\[
C_{ij}^2=\frac{B_{ij}^2}{B_{ii}B_{jj}}.
\]
Thus
\[
C_{12}^2=C_{13}^2=\frac15,\qquad C_{23}^2=\frac9{16},
\]
and therefore
\[
\|C_\Sigma(U,U)\|_F^2
=3+2\left(\frac15+\frac15+\frac9{16}\right)
=\frac{197}{40}.
\]
Meanwhile
\[
\gamma
=\frac{(3+1+1/3)^2}{3^2+1^2+(1/3)^2}
=\frac{13}{7},
\]
so the conjectured upper bound is
\[
\frac{9}{\gamma}=\frac{63}{13}.
\]
Hence
\[
\boxed{
\|C_\Sigma(U,U)\|_F^2-\frac9\gamma
=\frac{41}{520}>0.}
\]

## Robust spectral family

Keep the same orthogonal matrix \(U\), but let
\[
\Sigma_t=\operatorname{diag}(t,1,t^{-1}),\qquad t>0.
\]
Exact simplification gives
\[
\|C_{\Sigma_t}(U,U)\|_F^2
=
\frac{9(4t^5+4t^4+9t^3+9t+10)}
{(t+2)(2t^2+t+3)^2}.
\]
Subtracting the conjectured value \(9/\gamma_t\) factors as
\[
\boxed{
\|C_{\Sigma_t}(U,U)\|_F^2-\frac9{\gamma_t}
=
\frac{18(t-1)^2(2t^3-t^2-4)}
{(t+2)(t^2+t+1)(2t^2+t+3)^2}.}
\]
At \(t=3/2\), the cubic factor is \(1/2\), and its derivative is
\(2t(3t-1)>0\) for \(t>1/3\). Consequently the conjecture fails for every
\[
\boxed{t\ge 3/2.}
\]
The counterexample is therefore not an isolated algebraic coincidence.

## Failure also at a Hadamard order

A real Hadamard matrix does not exist in order three, but that is not the source of the failure. Embed the preceding construction into order four using
\[
\Sigma_4=\operatorname{diag}(3,1,1/3,7/3),\qquad
U_4=V_4=\operatorname{diag}(U,1).
\]
Then the fourth coordinate is orthogonal to the first three in the weighted-cosine matrix, so
\[
\|C_{\Sigma_4}(U_4,U_4)\|_F^2=\frac{197}{40}+1=\frac{237}{40}.
\]
Also
\[
\gamma_4
=\frac{(20/3)^2}{140/9}=\frac{20}{7},
\qquad
\frac{16}{\gamma_4}=\frac{28}{5}.
\]
Thus
\[
\boxed{
\|C_{\Sigma_4}(U_4,U_4)\|_F^2-\frac{16}{\gamma_4}
=\frac{13}{40}>0.}
\]
Order four admits the usual real Hadamard frame, so even in a dimension where the proposed equality benchmark exists, it is not a global upper benchmark.

## Dimension two: the conjectured bound is true

The dimension-three example is minimal over real orthogonal frames.

Let \(n=2\), \(\Sigma=\operatorname{diag}(a,b)\) with \(a\ge b>0\), and \(W\in O(2)\). Write
\[
d_i=w_i^\top\Sigma w_i,\qquad
D_W=\operatorname{diag}(d_1,d_2),\qquad
X_W=D_W^{-1/2}W\Sigma^{1/2}.
\]
Each row of \(X_W\) has Euclidean norm one, and
\[
C_\Sigma(U,V)=X_UX_V^\top.
\]
Set \(G_W=X_W^\top X_W\). Then \(G_W\) is positive definite and
\[
\operatorname{tr}G_W=2.
\]
Moreover,
\[
\det G_W=(\det X_W)^2=\frac{ab}{d_1d_2}.
\]
Since \(d_1+d_2=a+b\), the arithmetic-geometric mean inequality gives
\[
d_1d_2\le\frac{(a+b)^2}{4},
\]
so
\[
\det G_W\ge\frac{4ab}{(a+b)^2}.
\]
Write \(G_W=I+A_W\), where \(A_W\) is symmetric and traceless. Its eigenvalues are \(\pm r_W\), and
\[
r_W^2=1-\det G_W
\le\left(\frac{a-b}{a+b}\right)^2=:\delta^2.
\]
Hence \(\|A_W\|_F=\sqrt2\,r_W\). Using cyclicity of trace and Frobenius Cauchy-Schwarz,
\[
\begin{aligned}
\|C_\Sigma(U,V)\|_F^2
&=\operatorname{tr}(G_UG_V)\\
&=2+\operatorname{tr}(A_UA_V)\\
&\le 2+\|A_U\|_F\|A_V\|_F\\
&\le 2+2\delta^2\\
&=\frac{4(a^2+b^2)}{(a+b)^2}
=\frac{4}{\gamma}.
\end{aligned}
\]
A common \(45^\circ\) Hadamard frame attains equality. The case \(n=1\) is trivial. Therefore the first possible real dimension for failure is exactly \(n=3\).

## Interpretation

For \(U=V\), \(C_\Sigma(U,U)\) is the Gram matrix of the unit vectors obtained by applying \(\Sigma^{1/2}\) to the rows of an orthogonal frame and then normalizing them individually. Its squared Frobenius norm is therefore a frame potential. Classical frame-potential theory identifies tight frames as minimizers of the ordinary frame potential; it does not provide the spectrum-dependent Hadamard upper bound conjectured here. The counterexample shows that, from dimension three onward, row normalization can concentrate enough weighted angular correlation that the flat Hadamard benchmark is exceeded.

This finding concerns only the Appendix A global upper-bound conjecture. It does not contradict the paper's exterior-algebraic CUR residual identity, its proved weighted-cosine propositions, the rank-one angle formula, or the reported ACA experiments.

## Reproducibility

`artifacts/verify_weighted_cosine_counterexample.py` performs exact symbolic checks of the orthogonality, the dimension-three matrix and gap, the order-four gap, and the one-parameter factorization. `artifacts/verified_output.txt` records the executed output.

## References

1. T. Loe, L. Huang, D. Needell, *A Geometric View of Adaptive Cross Approximation via Exterior Algebra*, arXiv:2609.17947v1 (2026). https://arxiv.org/abs/2609.17947
2. D. G. Mixon, T. Needham, C. Shonkwiler, S. Villar, *Three proofs of the Benedetto–Fickus theorem*, arXiv:2112.02916 (2021; later published as a book chapter). https://arxiv.org/abs/2112.02916
3. J. J. Benedetto, M. Fickus, *Finite Normalized Tight Frames*, Advances in Computational Mathematics 18 (2003), 357–385. https://doi.org/10.1023/A:1021323312367
