# Quantitative Euclidean dissipation without positivity for two fourth-order nonsymmetric Dirichlet Laplacians

## Finding
For each integer \(n\ge5\), consider the two fourth-order finite-difference Dirichlet matrices \(M_n^{\mathrm{BH}}\) and \(M_n^{\mathrm{OS}}\) defined below. They are nonsymmetric and not symmetrizable by a positive diagonal matrix, yet each has an explicitly coercive symmetric part. Let \(D_n=\operatorname{tridiag}(-1,2,-1)\) and define
\[
\beta_{\mathrm{BH}}=10-\sqrt{14}>0,\qquad
\beta_{\mathrm{OS}}=9-\sqrt{62}>0.
\]
For either choice \(s\in\{\mathrm{BH},\mathrm{OS}\}\) and every \(u\in\mathbb C^n\),
\[
\boxed{\operatorname{Re}(u^*M_n^s u)\ \ge\ \beta_s u^*D_nu+\|D_nu\|_2^2.}
\]
Thus the spatially discretized heat generator \(A_n^s=M_n^s/(12h^2)\), with \(h=1/(n+1)\), satisfies
\[
\|e^{-tA_n^s}\|_2\le e^{-m_{n,s}t},\quad
\|(I+tA_n^s)^{-1}\|_2\le (1+m_{n,s}t)^{-1}\qquad(t\ge0),
\]
where
\[
\lambda_n=4\sin^2\!\left(\frac{\pi}{2(n+1)}\right),\qquad
m_{n,s}=\frac{\beta_s\lambda_n+\lambda_n^2}{12h^2}>0.
\]
The implicit-midpoint/Crank--Nicolson map \((I+tA_n^s/2)^{-1}(I-tA_n^s/2)\) is a strict Euclidean contraction for every \(t>0\). Nevertheless, the exact heat propagator \(e^{-tA_n^s}\) is not entrywise nonnegative for all sufficiently small positive \(t\). The estimate also extends additively to Kronecker-sum discretizations on rectangular Cartesian grids.

## Assumptions and scope
Indices run from \(1\) to \(n\). Each \(M_n^s\) has interior rows indexed \(2\le i\le n-1\) obtained by placing coefficients \((1,-16,30,-16,1)\) at columns \((i-2,i-1,i,i+1,i+2)\) and omitting columns outside \(1,\ldots,n\). The first row has entries \((24,-12,0,0)\) for \(s=\mathrm{BH}\), or \((20,-6,-4,1)\) for \(s=\mathrm{OS}\), followed by zeros. The last row is the reversal of the first row. The matrix of the corresponding negative Laplace operator is \(A_n^s=M_n^s/(12h^2)\). The norm is the unweighted Euclidean operator norm. All conclusions hold over real or complex vectors; no diagonalizability hypothesis is used.

## Proof
Write \(D=D_n\) and \(C=12D+D^2\). The interior rows of \(C\) are exactly the required fourth-order stencil. Its first row is \((29,-16,1,0,\ldots)\), and the last is the reversal. Therefore
\[
M_n^s=C+e_1r_s^\mathsf{T}+e_n(Jr_s)^\mathsf{T},
\quad r_{\mathrm{BH}}=(-5,4,-1,0,\ldots)^\mathsf{T},\quad
r_{\mathrm{OS}}=(-9,10,-5,1,0,\ldots)^\mathsf{T},
\]
where \(J\) reverses coordinates. The first and last row corrections are valid for every \(n\ge5\).

Set \(u_0=u_{n+1}=0\) and \(d_j=u_j-u_{j-1}\) for \(1\le j\le n+1\). The standard Dirichlet identity gives \(u^*Du=\sum_{j=1}^{n+1}|d_j|^2\), while \(u^*D^2u=\|Du\|_2^2\). The real quadratic contribution from the left boundary defect is
\[
q_{\mathrm{BH}}=-2|d_1|^2+3\operatorname{Re}(\overline d_1d_2)-\operatorname{Re}(\overline d_1d_3),
\]
respectively
\[
q_{\mathrm{OS}}=-3|d_1|^2+6\operatorname{Re}(\overline d_1d_2)-4\operatorname{Re}(\overline d_1d_3)+\operatorname{Re}(\overline d_1d_4).
\]
Both are Hermitian rank-two forms (with additional zero eigenvalues) on the indicated difference variables. More generally, the matrix of \(-a|v_1|^2+2\operatorname{Re}(\overline v_1\sum_{j\ge2}c_jv_j)\) has least eigenvalue
\[
-\frac{a+\sqrt{a^2+4\sum_{j\ge2}|c_j|^2}}{2}.
\]
Consequently \(q_s\ge-\tau_s\sum_{j=1}^{k_s}|d_j|^2\), where \(k_{\mathrm{BH}}=3\), \(k_{\mathrm{OS}}=4\) and
\[
\tau_{\mathrm{BH}}=1+\frac{\sqrt{14}}2,\qquad
\tau_{\mathrm{OS}}=\frac{3+\sqrt{62}}2.
\]
Reflection gives the same estimate for the last \(k_s\) edge differences. No difference appears in more than two of the left and right boundary sets, regardless of their overlap when \(n\) is small. Hence the total boundary contribution is bounded below by \(-2\tau_s\sum|d_j|^2\). Combining it with \(C\) proves the claimed estimate with \(\beta_s=12-2\tau_s\). Both constants are strictly positive.

Since the smallest eigenvalue of \(D\) is \(\lambda_n\), the coercivity inequality implies \(\operatorname{Re}(u^*A_n^su)\ge m_{n,s}\|u\|_2^2\). For \(v(t)=e^{-tA_n^s}v(0)\), differentiating \(\|v(t)\|_2^2\) and applying Gronwall proves exponential Euclidean contraction. For any \(w\), Cauchy--Schwarz applied to \(\operatorname{Re}\langle w,(I+tA_n^s)w\rangle\) yields \(\|(I+tA_n^s)w\|_2\ge(1+tm_{n,s})\|w\|_2\), proving the resolvent bound and invertibility. The identity
\[
\|(I-aA_n^s)w\|_2^2=\|(I+aA_n^s)w\|_2^2-4a\operatorname{Re}(w^*A_n^sw)
\]
for \(a=t/2>0\) proves strict contraction of the implicit-midpoint map. More explicitly, for each integer \(d\ge1\) and dimension sizes \(n_1,\ldots,n_d\ge5\), let \(\mathcal A=\sum_{j=1}^d I\otimes\cdots\otimes A_{n_j}^{s_j}\otimes\cdots\otimes I\) with either boundary choice in each coordinate. Summing the one-axis inequalities yields \(\operatorname{Re}(U^*\mathcal A U)\ge(\sum_{j=1}^d m_{n_j,s_j})\|U\|_2^2\), and hence the same semigroup and implicit-step bounds with decay rate \(\sum_jm_{n_j,s_j}\).

Finally, for \(n\ge5\) the interior entry \((M_n^s)_{2,4}=1\). Thus \((e^{-tA_n^s})_{2,4}=-t/(12h^2)+O(t^2)<0\) for all sufficiently small \(t>0\), so the propagator is not positivity-preserving. For a hypothetical positive diagonal symmetrizer \(H\), the equation \(HM_n^s=(M_n^s)^\mathsf{T}H\) would require \(H_{11}(M_n^s)_{1,3}=H_{33}(M_n^s)_{3,1}\). These entries are \((0,1)\) in the Bramble--Hubbard scheme and \((-4,1)\) in the one-sided scheme. Both violate the equation for positive \(H_{11},H_{33}\).

## Verification
Run \(\texttt{python3 verify.py}\) using Python's standard library. It checks the boundary-rank corrections, the Dirichlet energy identities, exact rational local square completions, and the claimed rational coercivity consequence on integer test vectors. The program passed \(1096\) exact-arithmetic checks with dimensions \(5\le n\le35\). The stronger irrational constants follow from the explicit eigenvalue calculation above, not from the finite checks. A rational subcertificate is \(\operatorname{Re}(u^*M_n^su)\ge u^*Du+\|Du\|_2^2\): for either boundary form \(q_s\ge-(11/2)\sum_{j\le k_s}|d_j|^2\), shown by the exact square completions in the verifier and by \(\tau_s<11/2\); the two boundary sets count each difference at most twice.

## Relationship to prior work
Feng, Gao and Shao (2026) define precisely these Bramble--Hubbard and one-sided fourth-order Dirichlet matrices and prove that all their eigenvalues are real and strictly positive. Their displayed decomposition of the Bramble--Hubbard matrix by a symmetric pentadiagonal core informs the present direct energy proof. Positive-real eigenvalues alone do not imply Euclidean accretivity or contraction: for example, the real upper-triangular matrix \(\left(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\right)\) has positive-real spectrum but an indefinite symmetric part. The claim here concerns explicit numerical-range coercivity, Euclidean semigroup and implicit-step bounds, and simultaneous failure of positivity and positive diagonal symmetrizability. Older literature on Bramble--Hubbard elliptic methods and general discrete stability motivates caution about priority; equivalent energy estimates have not been ruled out exhaustively.

## Limitations
The constants \(\beta_s\) are certified lower bounds, not asserted to be optimal. The statement is restricted to the displayed two Dirichlet boundary closures, \(n\ge5\), and their Cartesian Kronecker sums; no claim is made for arbitrary higher-order or variable-coefficient stencils. The small-time sign failure does not classify all larger times. Numerical replay covers a finite range and is not a proof for untested sizes. Comparison with older specialized elliptic stability literature remains a historical-priority risk.

## References
1. Y. Feng, W. Gao, M. Shao, *Spectral Reality for Certain Fourth-Order Nonsymmetric Finite-Difference Laplacians*, arXiv:2609.32410, v1 first submitted 26 September 2026, https://arxiv.org/abs/2609.32410 .
2. J. H. Bramble and B. E. Hubbard, *On a Finite Difference Analogue of an Elliptic Boundary Problem which is Neither Diagonally Dominant Nor of Non-negative Type*, Journal of Mathematics and Physics 43 (1964), DOI:10.1002/sapm1964431117.
3. H. J. van Linde, *High-order finite-difference methods for Poisson's equation*, doctoral thesis, University of Groningen (1971).
