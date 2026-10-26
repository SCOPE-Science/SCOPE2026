# Exact power and essential norms of homogeneous-tree Cesàro backward shifts

## Finding

Let \(b\ge2\) be an integer, let \(1<p<\infty\), and let \(\mathcal T_b\) be the full rooted \(b\)-ary tree. Let \(\lambda\in\mathbb C\setminus\{0\}\). On the tree Cesàro space \(X_p(\mathcal T_b)\) defined below, the constant-edge weighted backward shift is
\[
(B_\lambda f)(v)=\lambda\sum_{u\in\operatorname{Chi}(v)}f(u).
\]
Write \(H_p(s)=\sum_{j=s}^{\infty}j^{-p}\) for integer \(s\ge1\), so \(H_p(1)=\zeta(p)\). For every integer \(m\ge1\),
\[
\boxed{\ \|B_\lambda^m\|=(b|\lambda|)^m\left(\frac{\zeta(p)}{H_p(m+1)}\right)^{1/p},\qquad
\|B_\lambda^m\|_{\mathrm e}=(b|\lambda|)^m.\ }
\]
All nonzero norm-attaining inputs for \(B_\lambda^m\) are **exactly** the functions supported on the \(m\)-th level for which all nonzero values share a common complex argument. Consequently
\[
\lim_{m\to\infty}\frac{\|B_\lambda^m\|}{(b|\lambda|)^m m^{1-1/p}}
=\big((p-1)\zeta(p)\big)^{1/p},\qquad
r(B_\lambda)=r_{\mathrm e}(B_\lambda)=b|\lambda|.
\]
In particular, at the critical weight \(|\lambda|=1/b\) the essential norm of every positive power is \(1\), although its ordinary norm grows with the exact order \(m^{1-1/p}\).

## Assumptions and scope

The level \(D_n=\{v:|v|=n\}\) contains \(b^n\) vertices. For a scalar function \(f\) on the vertices define the mean absolute level mass and cumulative Cesàro mean by
\[
M_n(f)=b^{-n}\sum_{v\in D_n}|f(v)|,\qquad
C_n(f)=\frac1{n+1}\sum_{k=0}^n M_k(f).
\]
The Banach space in the theorem is
\[
X_p(\mathcal T_b)=\left\{f:\ \|f\|_X=\left(\sum_{n=0}^{\infty}C_n(f)^p\right)^{1/p}<\infty\right\}.
\]
All norms are the ordinary operator norms on this complex Banach space. The essential norm is distance to the compact operators on \(X_p(\mathcal T_b)\); \(r_{\mathrm e}\) denotes the spectral radius of the image in the Calkin algebra. Finite branching, fixed branching number, level-average normalization, constant complex edge weight, and \(1<p<\infty\) are required. The result makes no claim for arbitrary edge weights or nonhomogeneous rooted trees.

## Proof

**1. Scalar Cesàro-shift lemma.** Write \(\operatorname{ces}_p\) for sequences \(a=(a_j)_{j\ge0}\) with norm
\[
\|a\|_{\operatorname{ces}_p}^p=\sum_{n\ge0}\left(\frac1{n+1}\sum_{j=0}^{n}|a_j|\right)^p.
\]
Let \(S^m a=(a_{n+m})_{n\ge0}\). Then for every integer \(m\ge1\),
\[
\|S^m\|^p=\frac{H_p(1)}{H_p(m+1)},
\]
and a nonzero input attains this norm precisely if only its coordinate \(m\) can be nonzero.

To prove this, put \(a_j=0\) for \(0\le j<m\); doing so leaves the numerator unchanged and does not increase the denominator. We may replace remaining entries by their moduli. Let \(s_n=\sum_{j=m}^n a_j\), \(u_n=s_n^p\), \(u_{m-1}=0\), and \(d_k=u_k-u_{k-1}\ge0\). Tonelli's theorem gives the two *exact* nonnegative series identities
\[
\|S^m a\|_{\operatorname{ces}_p}^p
=\sum_{k=m}^{\infty}d_k H_p(k-m+1),\qquad
\|a\|_{\operatorname{ces}_p}^p
=\sum_{k=m}^{\infty}d_k H_p(k+1).
\]
For \(r\ge1\), the positive sequence \(H_p(r)\) is strictly log-convex. Indeed,
\[
H_p(r)=\frac1{\Gamma(p)}\int_0^{\infty}\frac{t^{p-1}e^{-rt}}{1-e^{-t}}\,dt,
\]
and strict Cauchy–Schwarz gives \(H_p(r+1)^2<H_p(r)H_p(r+2)\). It follows for each fixed \(m\ge1\) that \(H_p(k-m+1)/H_p(k+1)\) strictly decreases as \(k\ge m\) increases. Thus the numerator-to-denominator ratio is a weighted average bounded by its unique maximum at \(k=m\), namely \(H_p(1)/H_p(m+1)\). The input \(a=e_m\) attains this bound. Strictness and positivity show equality forces \(d_k=0\) for all \(k>m\), hence \(a_k=0\) for all \(k>m\), as well as the already removed lower coordinates being zero. All assertions also hold when some input sums vanish, by continuity or directly from the nonnegative identities.

**2. Transfer to a regular tree.** Every vertex at level \(n+m\) descends from exactly one vertex at level \(n\). Consequently, by the triangle inequality,
\[
M_n(B_\lambda^m f)\le(b|\lambda|)^m M_{n+m}(f).
\]
For the scalar nonnegative sequence \(a_n=M_n(f)\), the scalar lemma yields
\[
\|B_\lambda^m f\|_X\le(b|\lambda|)^m\|S^m a\|_{\operatorname{ces}_p}
\le(b|\lambda|)^m\left(\frac{H_p(1)}{H_p(m+1)}\right)^{1/p}\|f\|_X.
\]
If \(f\) is supported at level \(m\) and its nonzero values have one complex phase, the sum defining \(B_\lambda^m f\) is supported at the root and all triangle inequalities are equalities. This attains the operator-norm bound. Conversely, equality in the scalar bound forces \(M_n(f)=0\) for \(n\ne m\), hence \(f\) has support only on \(D_m\). Equality in the root triangle inequality then requires that the nonzero values of \(f\) at this level have a common phase. This establishes the full extremizer classification.

**3. Essential norm.** Let \(P_N\) be projection onto the finitely many vertices at depths at most \(N\), so \(P_NB_\lambda^m\) is finite rank. Put \(c=b|\lambda|\). For all \(r>N\),
\[
C_r((I-P_N)B_\lambda^m f)
\le\frac{c^m}{r+1}\sum_{n=N+1}^r M_{n+m}(f)
\le c^m\frac{r+m+1}{r+1}C_{r+m}(f).
\]
For \(r\le N\), the left-hand side is zero. Hence
\[
\|(I-P_N)B_\lambda^m\|
\le c^m\left(1+\frac{m}{N+2}\right),
\]
and taking \(N\to\infty\) gives \(\|B_\lambda^m\|_{\mathrm e}\le c^m\).

For the reverse bound, the radial inclusion \(J:\operatorname{ces}_p\to X_p(\mathcal T_b)\), \((Ja)(v)=a_{|v|}\), is an isometry. The vectors \(x_j=Je_j/H_p(j+1)^{1/p}\) form a weakly null unit sequence: the normalized coordinate basis of \(\operatorname{ces}_p\) is weakly null because this Banach space is reflexive and its coordinate vectors form a Schauder basis. Therefore \(Kx_j\to0\) for every compact operator \(K\). For \(j\ge m\),
\[
\|B_\lambda^m x_j\|_X
=c^m\left(\frac{H_p(j-m+1)}{H_p(j+1)}\right)^{1/p}\longrightarrow c^m.
\]
Thus \(\|B_\lambda^m-K\|\ge c^m\) for each compact \(K\), completing the essential-norm formula.

**4. Asymptotic and spectral consequences.** The integral test gives
\[
H_p(m+1)\sim\frac{m^{1-p}}{p-1}\qquad(m\to\infty).
\]
Substitution proves the sharp power-growth coefficient. The spectral-radius formula applied to the ordinary and Calkin operator powers yields the two spectral radii stated above.

## Verification

The standalone file `check.py` independently exercises the scalar bound, the strict monotonicity of the Hurwitz-zeta ratios, extremizing coordinate vectors, and radial tree examples for several exponents, powers, and branching numbers. It produced `PASS 2418 finite checks; infinite claims proved analytically`. These finite checks are corroboration, not a substitute for the preceding quantified proof. The analytical proof uses nonnegative-series Tonelli, strict Cauchy–Schwarz, level counting, finite-rank cutoff estimates, and weak-null compactness; no numerical optimization or unverified computer certificate is required.

## Relationship to prior work

Chen, Cheng, Zhang and Zhou (2026, arXiv:2609.21752) introduce and analyze weighted backward shifts on rooted-tree Cesàro spaces. Their boundedness and dynamical criteria motivate asking for the exact norm geometry of a natural homogeneous, constant-weight model; the inspected article does not provide the all-power operator norm, essential norm, or extremizer formulas above. The 2026 study *On the linear dynamics of shift operators on (PLB)-spaces* supplies the classical scalar Cesàro-space setting, basis norms, reflexivity, and dynamical criteria, but does not state the sharp all-power norm and essential-norm comparison. Kumar, Mursaleen and Sharma's work concerns multiplication operators on rooted-tree Cesàro spaces rather than this backward-shift family. Related exact weighted-shift power profiles on distinct sequence spaces do not imply these Cesàro formulas. The novelty assertion is limited to the specific combination of formulas and rigidity established here, under the inspected evidence.

## Limitations

The proof concerns only full homogeneous trees and constant edge weights; it does not solve the exact essential-norm problem for arbitrary rooted trees or edge-weight sequences. It determines norm-attaining vectors, not a quantitative stability modulus for near-extremizers. Existing literature might contain an equivalent scalar Cesàro-shift formula under different terminology; this is a residual publication-priority risk. The comparison does not constitute an exhaustive global novelty certification. No independent audit has been performed.

## References

1. X. Chen, M.-H. Cheng, L. Zhang, Z.-H. Zhou, *Dynamics of Weighted Backward Shifts on Cesàro Spaces of Rooted Trees*, arXiv:2609.21752 (2026), https://arxiv.org/abs/2609.21752 .
2. *On the linear dynamics of shift operators on (PLB)-spaces*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas (2026), DOI:10.1007/s13398-026-01935-0, https://link.springer.com/article/10.1007/s13398-026-01935-0 .
3. V. Kumar, M. Mursaleen, A. Sharma, *Multiplication operators on Cesàro function spaces on rooted trees*, Afrika Matematika 36 (2025), DOI:10.1007/s13370-025-01369-8 .
