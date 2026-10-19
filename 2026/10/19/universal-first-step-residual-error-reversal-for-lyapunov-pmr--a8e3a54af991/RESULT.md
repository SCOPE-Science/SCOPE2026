# Universal first-step residual–error reversal for Lyapunov PMR

## Finding

Consider the stable real symmetric Lyapunov equation
\[
AX+XA+vv^{\mathsf T}=0,\qquad A=-H,\quad H=H^{\mathsf T}\succ0,\quad \|v\|_2=1,
\]
with its unique positive-semidefinite solution \(X\). In the first (one-dimensional) polynomial Krylov subspace \(\operatorname{span}\{v\}\), write every candidate as \(X_y=yvv^{\mathsf T}\), and set
\[
a=v^{\mathsf T}Hv>0,\qquad b^2=v^{\mathsf T}H^2v-a^2\ge0.
\]
The one-step Galerkin, exact Frobenius-minimal-residual (MR), and harmonic pseudo-minimal-residual (PMR) coefficients, with the PMR definition of Lund and Palitta, are respectively
\[
y_{\mathrm G}=\frac1{2a},\qquad
 y_{\mathrm{MR}}=\frac{a}{2a^2+b^2},\qquad
 y_{\mathrm{PMR}}=\frac{a}{2(a^2+b^2)}.
\]
If \(b>0\) (equivalently, \(v\) is not an eigenvector of \(H\)), their **residuals and actual solution errors are strictly ranked in opposite directions**:
\[
\|AX_{y_{\mathrm{MR}}}+X_{y_{\mathrm{MR}}}A+vv^{\mathsf T}\|_F
 <\|AX_{y_{\mathrm{PMR}}}+X_{y_{\mathrm{PMR}}}A+vv^{\mathsf T}\|_F
 <\|AX_{y_{\mathrm G}}+X_{y_{\mathrm G}}A+vv^{\mathsf T}\|_F,
\]
while
\[
\boxed{\quad
\|X-X_{y_{\mathrm G}}\|_F
 <\|X-X_{y_{\mathrm{MR}}}\|_F
 <\|X-X_{y_{\mathrm{PMR}}}\|_F.\quad}
\]
All three approximations are positive semidefinite. If \(b=0\), all three are exactly \(X\).

The reversal admits **no finite universal relative-error bound**. For every integer \(K\ge2\), choose
\[
H_K=\begin{pmatrix}1&0\\0&K\end{pmatrix},\qquad
v_K=\frac1{\sqrt{K^2+1}}\begin{pmatrix}K\\1\end{pmatrix}.
\]
Then
\[
\|X_K-X_{y_{\mathrm G},K}\|_F=\frac{\sqrt3}{2K}+O(K^{-2}),
\qquad \|X_K-X_{y_{\mathrm{PMR}},K}\|_F=\frac14+O(K^{-1}),
\]
so
\[
\boxed{\quad\frac{\|X_K-X_{y_{\mathrm{PMR}},K}\|_F}{\|X_K-X_{y_{\mathrm G},K}\|_F}
=\frac{K}{2\sqrt3}+O(1)\longrightarrow\infty.\quad}
\]
Nonetheless, the PMR-to-Galerkin residual-norm ratio converges to \(\sqrt3/2<1\). The corresponding MR-to-Galerkin residual-norm ratio converges to \(\sqrt{2/3}\), while MR's solution error tends to \(1/6\).

## Assumptions and scope

All dimensions \(n\ge2\) are allowed, with arbitrary real symmetric positive-definite \(H\) and any real unit vector \(v\). The statement concerns exact arithmetic, a **single** rank-one right-hand side \(vv^{\mathsf T}\), and the first Krylov projection dimension \(1\), before subsequent basis vectors are added. It does not assert an analogous ordering at higher Krylov dimensions, for block right-hand sides, or for nonnormal or indefinite drifts. The error is the unweighted Frobenius norm of the difference of solution matrices, **not** the energy norm associated with the Lyapunov operator. PMR is the harmonic low-rank-modified projected Lyapunov method defined by Lund and Palitta; MR is the true Frobenius residual minimizer over this same one-dimensional approximation space.

## Proof

**Step 1: reconstruct the three extraction rules.** The first Arnoldi relation for \(A=-H\) is \(Av=-av-bw\) with \(w\perp v\), \(\|w\|_2=1\) when \(b>0\). The projected Galerkin Lyapunov equation reads \(-2ay+1=0\), yielding \(y_{\mathrm G}=1/(2a)\). Lund and Palitta's harmonic modification is \(M=H_1^{-*}h_{21}^{\mathsf T}h_{21}\) in scalar notation, where \(H_1=-a\) and \(|h_{21}|^2=b^2\); thus \(M=-b^2/a\). Solving the modified equation gives \(y_{\mathrm{PMR}}=a/[2(a^2+b^2)]\).

For any scalar \(y\), the full residual is
\[
\mathcal R(y)=vv^{\mathsf T}-y(Hvv^{\mathsf T}+vv^{\mathsf T}H),
\quad
\|\mathcal R(y)\|_F^2=(1-2ay)^2+2b^2y^2.
\]
Differentiating this strictly convex quadratic yields the unique exact minimizer \(y_{\mathrm{MR}}=a/(2a^2+b^2)\).

**Step 2: strict residual ordering.** For \(b>0\), direct algebra gives
\[
0<y_{\mathrm{PMR}}<y_{\mathrm{MR}}<y_{\mathrm G},
\qquad
\frac{y_{\mathrm{MR}}-y_{\mathrm{PMR}}}
     {y_{\mathrm G}-y_{\mathrm{MR}}}
=\frac{a^2}{a^2+b^2}<1.
\]
The squared residual is a strictly convex quadratic symmetric about its unique minimizer \(y_{\mathrm{MR}}\). Hence the PMR coefficient lies closer to that minimizer than the Galerkin coefficient, proving the strict residual ordering. Explicitly,
\[
\|\mathcal R(y_{\mathrm G})\|_F^2=\frac{b^2}{2a^2},\quad
\|\mathcal R(y_{\mathrm{MR}})\|_F^2=\frac{b^2}{2a^2+b^2},\quad
\|\mathcal R(y_{\mathrm{PMR}})\|_F^2=
\frac{b^2(a^2+2b^2)}{2(a^2+b^2)^2}.
\]

**Step 3: strict Frobenius solution-error reversal.** Since \(H\succ0\), the exact solution has the convergent Gramian representation
\[
X=\int_0^\infty e^{-tH}vv^{\mathsf T}e^{-tH}\,dt.
\]
Set \(\mu=v^{\mathsf T}Xv\). By the spectral theorem and strict convexity of the exponential,
\[
\mu=\int_0^\infty(v^{\mathsf T}e^{-tH}v)^2\,dt
\ge\int_0^\infty e^{-2at}\,dt=\frac1{2a}=y_{\mathrm G}.
\]
For every \(t>0\), Jensen's inequality is strict if \(b>0\), because the spectral measure of \(H\) induced by \(v\) then charges at least two distinct eigenvalues; hence \(\mu>y_{\mathrm G}\). Now
\[
\|X-yvv^{\mathsf T}\|_F^2=\|X\|_F^2-2\mu y+y^2.
\]
This quadratic is strictly decreasing for \(y\le y_{\mathrm G}<\mu\). Together with the coefficient ordering from Step 2, it proves
\(\|X-X_{y_{\mathrm G}}\|_F<\|X-X_{y_{\mathrm{MR}}}\|_F<\|X-X_{y_{\mathrm{PMR}}}\|_F\). If \(b=0\), \(Hv=av\), so the Gramian integral equals \(vv^{\mathsf T}/(2a)\) and all coefficients coincide.

**Step 4: the unbounded-distortion family.** With \(H_K\) and \(v_K\) above, exact arithmetic gives
\[
a_K=\frac{K^2+K}{K^2+1},\quad
b_K^2=\frac{K^2(K-1)^2}{(K^2+1)^2},\quad
 y_{\mathrm G,K}=\frac{K^2+1}{2K(K+1)},\quad
 y_{\mathrm{PMR},K}=\frac{K+1}{4K}.
\]
The exact Lyapunov solution is
\[
X_K=\begin{pmatrix}
\dfrac{K^2}{2(K^2+1)}&\dfrac{K}{(K^2+1)(K+1)}\\[5pt]
\dfrac{K}{(K^2+1)(K+1)}&\dfrac{1}{2K(K^2+1)}
\end{pmatrix}.
\]
Expanding these rational entries at \(1/K=0\) shows
\[
K^2\|X_K-y_{\mathrm G,K}v_Kv_K^{\mathsf T}\|_F^2\longrightarrow\frac34,
\qquad
\|X_K-y_{\mathrm{PMR},K}v_Kv_K^{\mathsf T}\|_F^2\longrightarrow\frac1{16}.
\]
Indeed, the leading Galerkin error has diagonal entry \(1/(2K)\) and two equal off-diagonal entries \(-1/(2K)\). Meanwhile \(a_K\to1\), \(b_K^2\to1\), and the PMR coefficient tends to \(1/4\) while \(X_K\to\operatorname{diag}(1/2,0)\). The stated ratio and the residual limits then follow by Step 2's formulas. Finally \(y_{\mathrm{MR},K}\to1/3\), so the MR solution error tends to \(1/6\).

## Verification

The standalone `verify.py` uses Python's exact rational arithmetic to reconstruct the scalar coefficients, residual norms, and squared Frobenius errors directly from arbitrary finite diagonal spectra and probability weights. It tests strict orderings on deterministic families in dimensions \(2\) through \(7\), exact rational formulas on \(249\) members of the two-eigenvalue family, and large-parameter asymptotic checks. A completed execution passed **3695 deterministic assertions**. The infinite-dimensional-parameter and all-dimension statements follow from the analytical argument above, not from enumeration.

To reproduce: run `python3 verify.py` from the package directory with Python \(3.10\) or later; there are no third-party dependencies. The script prints the assertion count and exits with failure on the first violated check.

## Relationship to prior work

Lund and Palitta's *Low-rank-modified Galerkin methods for the Lyapunov equation* (arXiv:2312.00463, first public December 1, 2023), especially its Section 3 harmonic correction and projected equation, supplies the PMR method analyzed here. It studies residual behavior, stability, and positive semidefiniteness; those algorithms and their standard formulas are not new. Lin and Simoncini (2013) provide the established Frobenius minimal-residual Lyapunov formulation. Palitta and Simoncini (2019/2020) prove Galerkin's error optimality in the **Lyapunov-operator energy norm**. Their energy-norm theorem is not itself an unweighted Frobenius ordering and does not state the PMR first-step reversal or the unbounded Frobenius-error ratio.

The contribution assessed here is the combined all-symmetric-problem **strict residual-versus-Frobenius-error reversal** for all three first-step extraction rules and an explicit family with an unbounded PMR-to-Galerkin Frobenius-error ratio despite uniformly better PMR residual. Searches of related public mathematics records did not identify a direct covering statement, but a logically equivalent unpublished or unindexed result cannot be excluded.

## Limitations

This result does not mean PMR is inferior across full multi-step Krylov solves: its purpose is to establish a first-projection obstruction to using residual improvement as a general proxy for solution error. The unbounded comparison is relative; it exploits growing spectral conditioning, while the exact solution remains bounded. The matrix is symmetric, the forcing has rank one, and all proofs assume exact arithmetic. The relative-error ratio refers to Frobenius **solution** error, not the residual norm. No claim of independent verification or of priority over unindexed literature is made.

## References

1. K. Lund and D. Palitta, *Low-rank-modified Galerkin methods for the Lyapunov equation*, arXiv:2312.00463 (first submitted 2023-12-01), *Electronic Transactions on Numerical Analysis* 62 (2024), 1–21. https://arxiv.org/abs/2312.00463
2. Y. Lin and V. Simoncini, *Minimal residual methods for large scale Lyapunov equations*, *Applied Numerical Mathematics* 72 (2013), 52–71. https://www.dm.unibo.it/~simoncin/MRlyap1.pdf
3. D. Palitta and V. Simoncini, *Optimality properties of Galerkin and Petrov-Galerkin methods for linear matrix equations*, arXiv:1908.06016 (2019), *Vietnam Journal of Mathematics* 48 (2020), 791–807. https://arxiv.org/abs/1908.06016
