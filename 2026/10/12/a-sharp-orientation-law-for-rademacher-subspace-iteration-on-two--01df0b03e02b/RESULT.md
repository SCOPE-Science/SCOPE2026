# A sharp orientation law for Rademacher subspace iteration on two-by-two matrices

## Finding

For every real invertible \(2\times2\) matrix \(A\) with distinct singular values \(a>b>0\), every integer \(q\ge0\), and every integer \(\ell\ge1\), the exact-arithmetic rank-one truncation of the Rademacher randomized subspace-iteration sketch obeys the following sharp, orientation-dependent expected squared Frobenius error law:

\[
\mathbb E\lVert A-\widehat A_1\rVert_F^2
=b^2+\frac{a^2-b^2}{2^\ell}H_\rho(c),\qquad
H_\rho(c)=\rho\left(\frac{1-c}{c+\rho(1-c)}+\frac{c}{1-c+\rho c}\right),
\]
\[
\rho=(b/a)^{4q+2},\quad
c=\left|\left\langle v_1,(1,1)^\top/\sqrt2\right\rangle\right|^2,
\]
where \(v_1\) is a unit leading **right** singular vector. Among all matrices with the given singular values, the exact sharp range is
\[
 b^2+\frac{a^2-b^2}{2^\ell}\frac{2\rho}{1+\rho}
 \ \le\ \mathbb E\lVert A-\widehat A_1\rVert_F^2
 \ \le\ b^2+\frac{a^2-b^2}{2^\ell}.
\]
The lower equality holds precisely at \(c=1/2\), and the upper precisely at \(c\in\{0,1\}\). At an upper extremizer, a probability \(2^{-\ell}\) of choosing only the trailing right-singular sign line causes squared error \(a^2\) instead of the optimal \(b^2\), for **every** \(q\). Consequently no number of power iterations removes the worst-orientation excess risk; for each fixed interior \(0<c<1\) it instead vanishes as \(q\to\infty\). This is an exact distinction, not merely a large-\(q\) bound.

For example, on \(A=\begin{pmatrix}2&1\\1&2\end{pmatrix}\) with \(a=3\) and \(b=1\), the upper-bound configuration is attained. For every power count \(q\) and \(\ell=2\), the squared error is \(9\) with probability \(1/4\) and \(1\) otherwise, yielding the exact mean \(3\). The optimal rank-one squared error is \(1\); a two-column Gaussian sketch attains \(1\) almost surely.

A uniform relative expected-squared-error target \(\mathbb E\lVert A-\widehat A_1\rVert_F^2\le(1+\varepsilon)b^2\) for all orientations, \(\varepsilon>0\), holds **if and only if** \(2^\ell\ge(a^2-b^2)/(\varepsilon b^2)\). For contrast, a real standard-Gaussian \(2\times\ell\) sketch with \(\ell\ge2\) gives the optimal error \(b^2\) almost surely.

## Assumptions and scope

Let \(A=U\operatorname{diag}(a,b)V^\top\) with orthogonal \(U,V\), \(a>b>0\), target rank one, and \(\Omega\in\{-1,+1\}^{2\times\ell}\) with all entries independent and equiprobable. Form
\[
Y=(AA^\top)^qA\Omega.
\]
Let \(Q\) be **any rank-revealing orthonormal basis for the actual range of** \(Y\), even if the columns of \(Y\) are linearly dependent. Set \(B=Q^\top A\), take its best rank-one singular-value truncation \(B_1\), and set \(\widehat A_1=QB_1\). When \(Y\) has rank two, this is exactly the best rank-one SVD of \(A\); when it has rank one, this is \(QQ^\top A\). All operations are in exact arithmetic. The definition permits redundant sketch columns \(\ell>2\), an explicitly stated rank-revealing extension of the small-dimension sample-size convention used in some source theorems. The calculation includes \(\ell=1,2\) without any extension.

## Proof

Let \(s_+=(1,1)^\top/\sqrt2\) and \(s_-=(1,-1)^\top/\sqrt2\). Every sign column, after ignoring its irrelevant overall sign, belongs to exactly one of these orthogonal lines, independently with probability \(1/2\). Each line appears at least once with probability \(1-2^{1-\ell}\) (zero when \(\ell=1\)). Since \(A\) is invertible, \((AA^\top)^qA\) is invertible. Thus the range of \(Y\) is all of \(\mathbb R^2\) exactly when both projective lines are sampled, and its rank-one truncation then has squared Frobenius error \(b^2\).

The event that every column belongs to the \(s_+\) line has probability \(2^{-\ell}\), as does the analogous \(s_-\) event. Put \(m=2q+1\) and \(\rho=(b/a)^{2m}\). On the \(s_+\) event, the unit range direction \(Q\) has squared left-singular coordinates proportional to \(a^{2m}c\) and \(b^{2m}(1-c)\). Its captured squared Frobenius norm is
\[
\lVert Q^\top A\rVert_2^2
=\frac{a^{2m+2}c+b^{2m+2}(1-c)}{a^{2m}c+b^{2m}(1-c)}.
\]
Subtracting this from \(\lVert A\rVert_F^2=a^2+b^2\) yields the event's error
\[
b^2+(a^2-b^2)\frac{\rho(1-c)}{c+\rho(1-c)}.
\]
On the \(s_-\) event exchange \(c\) and \(1-c\). Combining these disjoint cases gives the claimed expectation exactly for every finite \(\ell,q\).

For the sharp bounds, let \(g(t)=t/(\rho+(1-\rho)t)\) on \([0,1]\). Because \(0<\rho<1\), \(g\) is strictly concave: \(g''(t)=-2\rho(1-\rho)/(\rho+(1-\rho)t)^3<0\). Algebra yields \(H_\rho(c)=2-g(c)-g(1-c)\). Strict concavity and symmetry imply that \(g(c)+g(1-c)\) is maximal at \(c=1/2\), with value \(2/(1+\rho)\), and minimal only at \(c=0\) or \(1\), with value \(1\). Therefore \(H_\rho\) has the claimed extremizers and values. Every \(c\in[0,1]\) occurs for some orthogonal right singular frame, so both bounds are sharp over the stated class.

If \(c=0\) or \(1\), one sign line coincides with the trailing singular direction; sampling only it leaves the leading direction entirely absent, independently of \(q\). If \(0<c<1\), both fractions defining \(H_\rho(c)\) tend to zero as \(\rho\downarrow0\), establishing the power-iteration dichotomy. The orientation-uniform tolerance criterion is immediate from the attained upper bound. Finally, a Gaussian \(2\times\ell\) sketch for \(\ell\ge2\) has rank two almost surely, so its post-truncation error equals \(b^2\). These arguments cover all quantified sizes without an asymptotic or probabilistic approximation.

## Verification

The accompanying `verify.py` is a standalone standard-library Python program using exact rational arithmetic. It directly forms both symmetric and nonsymmetric matrices with prescribed rational singular values and independent rational left/right singular frames, enumerates all projective sign-line sequences for \(1\le\ell\le5\), and compares the direct projected-error computation against the formula for \(0\le q\le3\) at generic and central orientations. It additionally verifies the extremal Hadamard orientation through \(0\le q\le4\). The program produces the diagnostic result `Verified 410 exact-rational identities and inequality cases.` Its finite checks supplement, but do not substitute for, the preceding proof for all \(\ell,q\).

To reproduce: run `python3 verify.py` with a modern Python 3 standard library. No data files or third-party packages are required.

## Relationship to prior work

Saibaba and Międlar's non-Gaussian randomized-SVD framework [1, §2.2, §2.3, Theorem 3.3, Appendix B] explicitly includes Rademacher sampling and provides structural and distributional *bounds*. It does not state this exact rank-two **rank-one-truncated** expected-risk law, the sharp right-singular-frame extremizers, or the all-power-step obstruction from a positive-probability omitted singular direction. Their bounds concern the untruncated range projection and work under different dimension or sketch-regularity conventions.

Saibaba's earlier subspace-iteration analysis [2, §§2–4 and Appendix] treats target-rank truncation and deterministic canonical-angle/norm bounds, with Gaussian specializations and full-row-rank assumptions for its structural arguments. Such bounds do not imply this unconditional sign-sketch expectation on rank-deficient events. Diouane et al. [3, §§3–4] derive generalized deterministic error bounds and Gaussian expectations rather than an exact Rademacher orientation distribution. Dereziński et al. [4] study approximate expressions for projection residuals under other dimensional/rank regimes, not this two-dimensional truncated finite-sample identity. Different sketch distributions and different loss/output operators are not interchangeable.

## Limitations

The result concerns exactly two nonzero distinct singular values, **the expected squared Frobenius error**, iid equiprobable dense sign entries, and a rank-one SVD truncation after a rank-revealing range finder. No high-dimensional generalization, floating-point stability guarantee, runtime claim, tail estimate away from the stated extremizers, or universal claim for other discrete sketches follows. The \(\ell>2\) statement uses the declared redundant-column extension rather than the \(\ell\le2\) sample-size convention in the source's analysis. Exact priority beyond the inspected publications and searched records remains subject to unindexed or specialized treatments of this elementary two-dimensional case.

## References

[1] A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814v1 (public 2023-08-10), https://arxiv.org/abs/2308.05814.

[2] A. K. Saibaba, *Randomized subspace iteration: Analysis of canonical angles and unitarily invariant norms*, arXiv:1804.02614 (first posted 2018-04-08), https://arxiv.org/abs/1804.02614.

[3] Y. Diouane et al., *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793, https://arxiv.org/abs/2206.08793.

[4] M. Dereziński, F. Liang, Z. Liao, and M. W. Mahoney, *Precise expressions for random projections: Low-rank approximation and randomized Newton*, arXiv:2006.10653, https://arxiv.org/abs/2006.10653.
