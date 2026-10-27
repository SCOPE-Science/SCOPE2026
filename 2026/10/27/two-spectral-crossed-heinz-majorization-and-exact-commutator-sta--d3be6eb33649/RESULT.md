# Two-spectral crossed-Heinz majorization and exact commutator stability

## Finding

Let \(n\geq1\), \(0<t<1\), and let \(A,B\in M_n(\mathbb C)\) be positive definite, each with **at most two distinct eigenvalues**, not necessarily the same eigenvalues for the two matrices. Define the crossed and ordinary Heinz matrices by
\[
C_t=A^tB^{1-t}+B^tA^{1-t},\qquad H_t=A^tB^{1-t}+A^{1-t}B^t.
\]
Then, in every matrix dimension,
\[
\boxed{s(C_t)\prec_w s(H_t).}
\]
Here \(s(T)\) is the descending singular-value list and \(\prec_w\) denotes weak majorization (every leading partial sum is no larger). Therefore **every unitarily invariant norm** satisfies
\[
\boxed{\|C_t\|_{\mathrm{ui}}\leq\|H_t\|_{\mathrm{ui}}\leq\|A+B\|_{\mathrm{ui}}.}
\]
The two-point spectra of \(A\) and \(B\) may be completely independent, as may all spectral multiplicities and orientations of their eigenspaces.

There is also an **exact quantitative identity**. Suppose the (not necessarily occupied) upper and lower spectral levels are \(a_+>a_->0\) for \(A\) and \(b_+>b_->0\) for \(B\). With corresponding spectral projections \(P,Q\), write
\[
A=a_-I+(a_+-a_-)P,\qquad B=b_-I+(b_+-b_-)Q,
\]
and define, for \(x_+>x_->0\),
\[
\kappa_t(x_+,x_-)=\frac{(x_+^t-x_-^t)(x_+^{1-t}-x_-^{1-t})}{(x_+-x_-)^2}>0.
\]
Then
\[
\boxed{\|H_t\|_{\mathrm F}^2-\|C_t\|_{\mathrm F}^2
=\kappa_t(a_+,a_-)\,\kappa_t(b_+,b_-)\,\|[A,B]\|_{\mathrm F}^2.}
\]
For genuinely non-scalar \(A,B\), equality of the two Frobenius norms occurs **exactly when \(A\) and \(B\) commute**. If either matrix is scalar, both expressions coincide and the defect is zero. The unnormalized alternative, valid even when an upper projection vanishes, is
\[
\|H_t\|_{\mathrm F}^2-\|C_t\|_{\mathrm F}^2
=(a_+^t-a_-^t)(a_+^{1-t}-a_-^{1-t})
(b_+^t-b_-^t)(b_+^{1-t}-b_-^{1-t})\|[P,Q]\|_{\mathrm F}^2.
\]

The two-valued condition is a sharp uniform **spectral-cardinality boundary**: a previously published example with a three-valued first factor and a positive-definite two-valued second factor violates even the trace-norm comparison at \(t=1/4\). This counterexample is credited, not claimed new.

## Assumptions and scope

All matrices are finite-dimensional and complex; no common eigenbasis or matching eigenvalue pairs are assumed. Positive definiteness ensures fractional powers are unambiguous by the spectral functional calculus. The weak-majorization conclusion also extends to positive semidefinite inputs by adding \(\varepsilon I\) and taking \(\varepsilon\downarrow0\). All formulas use the unnormalized Frobenius norm \(\|T\|_{\mathrm F}^2=\operatorname{Tr}(T^*T)\). The endpoint cases \(t=0,1\) are excluded from the strictness statement, because the positive coefficient vanishes there.

## Proof

**1. Two-dimensional comparison.** We record the published sharp two-by-two comparison [1, Theorem 3.3] and its critical calculation. For positive \(2\times2\) matrices, simultaneous unitary conjugation makes \(A\) diagonal with decreasing entries and \(B\) real symmetric with nonnegative off-diagonal. Put \(X=A^tB^{1-t}\) and \(Y=A^{1-t}B^t\). Then \(H_t=X+Y\) and \(C_t=X+Y^{\mathsf T}\). The antisymmetric off-diagonal differences \(\Delta_X=X_{12}-X_{21}\) and \(\Delta_Y=Y_{12}-Y_{21}\) are nonnegative: each \(B^u\), for \(0<u<1\), is a positive-slope affine function of \(B\) in dimension two, while the spectral gaps of \(A^u\) are nonnegative. Thus the differences for \(H_t\) and \(C_t\) are respectively \(\Delta_X+\Delta_Y\) and \(\Delta_X-\Delta_Y\).

For a real \(2\times2\) matrix \(T=(t_{ij})\), set
\[
R_+(T)=\sqrt{(t_{11}+t_{22})^2+(t_{12}-t_{21})^2},\quad
R_-(T)=\sqrt{(t_{11}-t_{22})^2+(t_{12}+t_{21})^2}.
\]
Its largest singular value is \((R_+(T)+R_-(T))/2\), and its trace norm is \(\max\{R_+(T),R_-(T)\}\), as follows by squaring the two singular values and using \(\det T\). The diagonal and symmetric off-diagonal parts of \(H_t,C_t\) agree; hence \(R_-(H_t)=R_-(C_t)\), while \(R_+(H_t)\geq R_+(C_t)\). Both Ky Fan inequalities follow. One-dimensional blocks have \(C_t=H_t\). This proves the ingredient without assuming the two matrices have matching eigenvalues.

**2. Simultaneous reducing blocks of two projections.** Let \(P,Q\) be any two orthogonal projections. Their simultaneous reducing decomposition comprises the four intersection spaces of their ranges and kernels (one-dimensional blocks after choosing bases), plus orthogonal two-dimensional principal-angle blocks. For completeness, diagonalize the contraction \(PQP\) on \(\operatorname{ran}P\). For an eigenvector \(e\) with eigenvalue \(0<\lambda<1\), define
\[
f=(Qe-\lambda e)/\sqrt{\lambda(1-\lambda)}.
\]
Then \(f\in\ker P\), \(\|f\|=1\), and on \(\operatorname{span}\{e,f\}\) the projections take the forms
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q=\begin{pmatrix}\lambda&\sqrt{\lambda(1-\lambda)}\\
\sqrt{\lambda(1-\lambda)}&1-\lambda\end{pmatrix}.
\]
Distinct orthonormal eigenvectors give mutually orthogonal blocks because \(Q\) is an orthogonal projection; eigenvalues zero and one yield the intersection spaces. Orthogonal complements produce the remaining intersections in \(\ker P\). Thus \(P,Q\) reduce to blocks of dimension one or two, without restrictions on their ranks or the ambient dimension.

**3. Passage to arbitrary dimension.** Write \(A=a_-I+(a_+-a_-)P\) and \(B=b_-I+(b_+-b_-)Q\), with the obvious scalar interpretation. Every power of \(A\) is affine in \(P\), and every power of \(B\) is affine in \(Q\). Hence all four powers, \(C_t\), and \(H_t\) have the common block decomposition of Step 2. Apply Step 1 on each two-dimensional block and scalar equality on each one-dimensional block. Weak majorization is preserved by concatenation of singular-value lists: the largest \(k\) entries of a block sum maximize the sum of blockwise largest \(k_j\) entries over all nonnegative integers \(k_j\) with \(\sum k_j=k\). Each such blockwise sum for \(C_t\) does not exceed that for \(H_t\). Maximizing establishes \(s(C_t)\prec_w s(H_t)\) globally. Ky Fan dominance and the classical Heinz inequality give the displayed inequalities for all unitarily invariant norms.

**4. Exact squared-defect identity.** Cyclicity of the trace and adjoint expansion give
\[
\|H_t\|_{\mathrm F}^{2}-\|C_t\|_{\mathrm F}^{2}
=2\operatorname{Re}\operatorname{Tr}\!\left(AB-A^tB^tA^{1-t}B^{1-t}\right).
\]
For \(u\in\{t,1-t\}\), write
\[
A^u=a_-^uI+\alpha_u P,\quad \alpha_u=a_+^u-a_-^u,\qquad
B^u=b_-^uI+\beta_u Q,\quad \beta_u=b_+^u-b_-^u.
\]
Expand the product inside the trace. Every term with fewer than four projection factors cancels: \(\operatorname{Tr}(PQ)=\operatorname{Tr}(QP)=\operatorname{Tr}(PQP)=\operatorname{Tr}(QPQ)\) and \(P^2=P\), \(Q^2=Q\). Only the four-factor difference remains, giving
\[
\operatorname{Tr}(AB)-\operatorname{Tr}(A^tB^tA^{1-t}B^{1-t})
=\alpha_t\alpha_{1-t}\beta_t\beta_{1-t}\operatorname{Tr}(PQ-PQPQ).
\]
All traces in this final expression are real. Direct multiplication and cyclicity show
\[
\|[P,Q]\|_{\mathrm F}^{2}=2\operatorname{Tr}(PQ-PQPQ).
\]
Combining these identities proves the exact projection formula. Since \([A,B]=(a_+-a_-)(b_+-b_-)[P,Q]\), dividing by the squared spectral gaps gives the normalized formula. Its coefficient is positive for strictly distinct positive levels and \(0<t<1\), proving the Frobenius equality classification. Scalar inputs have \(C_t=H_t\) directly.

**5. Optimal spectral-cardinality boundary.** The published rank-one-input construction [3] has \(A=\operatorname{diag}(1,16,81)\), \(B=uu^*\), \(u=(1,1,1)/\sqrt3\), and \(t=1/4\), with
\[
\|C_t\|_1^2-\|H_t\|_1^2=\frac43(\sqrt{181}-13)>0.
\]
By continuity, replacing \(B\) by \(B+\varepsilon I\) for sufficiently small \(\varepsilon>0\) preserves the strict reversal. That replacement has exactly **two positive eigenvalues**, whereas \(A\) has three. Hence the two-valued assumption cannot be relaxed uniformly to three spectral points in one factor even if the other retains two. The numerical witness and its priority belong to [3], not to the present work.

## Verification

The standalone standard-library file `verify_heinz.py` checks \(486\) exact rational squared-defect identities for explicit noncommuting two-by-two, three-by-three, and four-by-four projection pairs with independent eigenvalue pairs. It also checks \(972\) numerical Ky Fan partial-sum comparisons in one- and two-block configurations. Execute `python3 verify_heinz.py`. A separate randomized diagnostic tested \(840\) positive-definite complex pairs in dimensions two through eight and all Ky Fan sums, with no non-roundoff violation, and checked the Frobenius identity to relative error below \(5\times10^{-13}\). These finite tests corroborate, but do not establish, the general matrix theorem; the proof is analytic and exact.

## Relationship to prior work

Sababheh and Bourin [1] prove the unrestricted dimension-two comparison, including unequal spectra, and a distinct arbitrary-dimensional Loewner bound only for inputs **sharing the same two numerical eigenvalues**. Their two-dimensional comparison is the explicitly cited starting ingredient of the present global two-projection lifting. The new assertion is the fully arbitrary-dimensional, **independently two-valued** singular-value comparison, supplemented by its exact norm-defect commutator formula. The common-spectra Loewner theorem neither supplies the ordinary-Heinz domination for independently chosen levels nor the normalized product defect. No new proof of the already established dimension-two theorem is claimed.

Bottazzi, Elencwajg, Larotonda, and Varela [2] analyze the general inequality in a central exponent interval and produce general-matrix counterexamples; their full text does not assert the all-exponent, two-valued-pair result. The earlier source [3] describes a different rank-one-input trace/Schatten crossover, and its explicit three-level witness supplies the cited boundary sharpness. The separate two-point-spectrum tracial result [4] compares the crossed expression with \(A+B\), not singular-value majorization by the ordinary Heinz expression. Two-projection canonical decomposition and the classical Heinz inequality are standard tools and not claimed new.

## Limitations

The global weak-majorization theorem requires each input to have at most two spectral values. It makes no claim for general positive matrices with three or more eigenvalues. The equality characterization is for the Frobenius norm, not for every unitarily invariant norm. The main lifting uses a published dimension-two theorem and classical two-projection geometry; its novelty is confined to the assembled higher-dimensional spectral family and exact commutator identity. Absolute priority cannot be certified against all older or unindexed literature. No independent external scientific review is represented by the finite checks or the analytic proof.

## References

1. M. Sababheh and J.-C. Bourin, *Crossed-Heinz Inequalities: The Two-Dimensional Threshold and Higher-Dimensional Stability*, arXiv:2610.04567v1 (first posted 2026-10-03), particularly Theorem 3.3 and Section 6. https://arxiv.org/html/2610.04567v1
2. T. Bottazzi, R. Elencwajg, G. Larotonda, and A. Varela, *Inequalities related to Bourin and Heinz means with a complex parameter*, arXiv:1403.7472v1 (2014-03-28), particularly Sections 2 and 3. https://arxiv.org/html/1403.7472v1
3. *Rank-one crossed-Heinz operators have a spectral-support Schatten crossover* (2026-10-11), public mathematical research record. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-rank-one-crossed-heinz-operators-have-a-spectral-support-schatte--e20efd37906d
4. *Sharp tracial crossed-Heinz stability for common two-point spectra* (2026-10-11), public mathematical research record. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-tracial-crossed-heinz-stability-for-common-two-point-spect--20c5e33ff291
