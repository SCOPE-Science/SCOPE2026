# Arithmetic–geometric norm staircases for two-sided Forelli–Rudin disk operators

## Finding

For a natural three-parameter family of disk-kernel integral operators, the full singular spectrum and the sharp operator norm admit closed formulas. When the two radial weights differ, the maximizing angular Fourier mode climbs an infinite, explicitly located staircase; the steps accumulate at the exact loss-of-compactness threshold. At that boundary the operator norm is not attained, whereas equal radial weights give a scaled orthogonal projection.

Let \(d\mu(z)=dA(z)/\pi\) be normalized planar area on the open unit disk \(\mathbb D\). Fix real \(a,b>-1/2\) and \(c>0\), and define the (initially pointwise-defined) operator
\[
(T_{a,b,c}f)(z)=(1-|z|^2)^a\int_{\mathbb D}\frac{(1-|w|^2)^b f(w)}{(1-z\overline w)^c}\,d\mu(w).
\]
The branch of the denominator is its analytic binomial expansion at zero. Put
\[
A=2a+2,\qquad B=2b+2,\qquad m=\frac{A+B}{2}=a+b+2.
\]
For every integer \(n\ge0\) set
\[
\sigma_n=\frac{\Gamma(n+c)\sqrt{\Gamma(A-1)\Gamma(B-1)}}{\Gamma(c)\sqrt{\Gamma(n+A)\Gamma(n+B)}}.
\]

**Theorem.** The operator has a bounded extension on \(L^2(\mathbb D,d\mu)\) exactly when \(c\le m\); if bounded, its nonzero singular values, counted with multiplicities before decreasing rearrangement, are precisely \(\sigma_n\) for \(n\ge0\). It is compact exactly when \(c<m\). In that case, with \(\delta=m-c>0\),
\[
\sigma_n\sim C n^{-\delta},\qquad C=\frac{\sqrt{\Gamma(A-1)\Gamma(B-1)}}{\Gamma(c)},
\]
and \(T_{a,b,c}\) belongs to the Schatten class \(S_p\), \(p>0\), exactly when \(p\delta>1\). It is in the weak Schatten class \(S_{1/\delta,\infty}\) but not in \(S_{1/\delta}\).

If \(a\ne b\), define, for integers \(n\ge0\),
\[
c_n=\sqrt{(n+A)(n+B)}-n.
\]
These critical values satisfy \(c_0=\sqrt{AB}<c_1<c_2<\cdots<m\) and tend to \(m\). For \(0<c<c_0\), the unique maximizing angular order is zero. At \(c=c_n\), precisely orders \(n\) and \(n+1\) tie for the sharp norm. For every \(k\ge1\) and \(c_{k-1}<c<c_k\), order \(k\) uniquely attains the norm. Hence the exact norm is \(\|T_{a,b,c}\|=\sigma_k\) with the relevant maximizing index; equality inputs are exactly the linear combinations of the corresponding normalized input modes. As \(c\uparrow m\), the maximizing order obeys
\[
k(c)=\frac{(A-B)^2}{8(m-c)}+O_{a,b}(1).
\]
At \(c=m\) and \(a\ne b\),
\[
\|T_{a,b,m}\|=\|T_{a,b,m}\|_{\mathrm{ess}}
=\frac{\sqrt{\Gamma(A-1)\Gamma(B-1)}}{\Gamma(m)},
\]
and no nonzero input attains the norm. For \(a=b\), every \(0<c<m\) has unique maximizing order zero and sharp norm \(\big((2a+1)(2b+1)\big)^{-1/2}\); at \(c=m\) all nonzero singular values are identically \((2a+1)^{-1}\), and the operator is that multiple of the orthogonal projection onto the radial-weighted analytic monomial subspace.

## Assumptions and scope

All parameters are real, \(a,b>-1/2\), \(c>0\). The Hilbert spaces on both sides are the same *unweighted* \(L^2(\mathbb D,dA/\pi)\). The input and output weights belong to the kernel rather than to the Hilbert-space measure. A pointwise integral is well-defined for each fixed \(z\in\mathbb D\) and every input in \(L^2\): by Cauchy–Schwarz, \((1-|w|^2)^b\in L^2\), and the analytic kernel factor is bounded in \(w\) for fixed \(z\). Boundedness means extension to a bounded map of this same \(L^2\) space; the unbounded region is not claimed to be pointwise undefined.

## Proof

**Step 1: an exact singular-value decomposition.** Write
\[
U_n(z)=\frac{z^n(1-|z|^2)^a}{\sqrt{\mathrm B(n+1,2a+1)}},\qquad
V_n(z)=\frac{z^n(1-|z|^2)^b}{\sqrt{\mathrm B(n+1,2b+1)}}.
\]
Rotational orthogonality and the substitution \(s=|z|^2\) show that \((U_n)\) and \((V_n)\) are orthonormal systems in unweighted \(L^2(d\mu)\). For fixed \(z\in\mathbb D\), the binomial kernel expansion is absolutely dominated by \((1-|z|)^{-c}\). Therefore Cauchy–Schwarz and dominated convergence give the pointwise expansion
\[
T_{a,b,c} f=\sum_{n=0}^{\infty}\sigma_n\langle f,V_n\rangle U_n,
\qquad
\sigma_n=\frac{(c)_n}{n!}\sqrt{\mathrm B(n+1,2a+1)\mathrm B(n+1,2b+1)}.
\]
Here the complex inner product is linear in its first argument. The beta–gamma identity cancels the factorials and gives the displayed closed formula for \(\sigma_n\). The operator kills the orthogonal complement of the closed span of \((V_n)\). Consequently this is a genuine singular-value decomposition whenever \(\sup_n\sigma_n<\infty\); in the opposite case its action on the unit inputs \(V_n\) rules out any bounded extension.

**Step 2: boundedness, compactness, and Schatten ideals.** The gamma-ratio expansion gives
\[
\sigma_n=C n^{c-m}(1+O_{a,b,c}(n^{-1})).
\]
Thus the singular coefficients are bounded exactly for \(c\le m\), tend to zero exactly for \(c<m\), and, for \(c<m\), their \(p\)-th powers are summable exactly for \(p(m-c)>1\). Decreasing rearrangement changes only a finite initial portion of the eventually decreasing coefficients. It therefore preserves the positive leading power-law constant and yields the stated weak-Schatten boundary.

**Step 3: exact mode ordering.** Division of consecutive gamma values yields the identity
\[
\frac{\sigma_{n+1}}{\sigma_n}=\frac{n+c}{\sqrt{(n+A)(n+B)}}.
\]
For positive parameters this ratio exceeds, equals, or falls below one according as \(c\) exceeds, equals, or falls below \(c_n=\sqrt{(n+A)(n+B)}-n\). If \(A\ne B\), the continuous interpolation \(g(t)=\sqrt{(t+A)(t+B)}-t\) is strictly increasing for \(t\ge0\), since
\[
g'(t)=\frac{2t+A+B}{2\sqrt{(t+A)(t+B)}}-1>0
\]
by strict arithmetic–geometric mean. Moreover \(g(0)=\sqrt{AB}<m\) and \(g(t)\to m\). Therefore the \(\sigma_n\) increase up to exactly the angular degree specified in the theorem and decrease thereafter, with exactly two adjacent maxima at each transition. The singular-value decomposition implies the stated complete equality-input description.

For \(c_0<c<m\), the real crossing of the ratio is
\[
n_*(c)=\frac{c^2-AB}{A+B-2c}=\frac{(A-B)^2}{8(m-c)}-m+\frac{m-c}{2}.
\]
The maximizing integer is its ceiling unless the crossing is integral, in which case that integer and its successor tie. This proves the escape law with bounded rounding error. If \(A=B\), every ratio is less than one for \(c<A=m\), and every ratio is one for \(c=m\).

**Step 4: nonattainment at the asymmetric boundary.** For \(c=m\) and \(A\ne B\), strict arithmetic–geometric mean shows \(n+m>\sqrt{(n+A)(n+B)}\) for all integers \(n\ge0\). Hence \(\sigma_n\) increases strictly toward \(C\), and the singular-value decomposition implies \(\|Tf\|<C\|f\|\) for every nonzero \(f\). The tail normalized inputs \(V_n\) are weakly null and their images have norms tending to \(C\); hence the essential norm equals \(C\). In the symmetric case \(A=B=c=m\), all \(\sigma_n=(A-1)^{-1}\); the decomposition is an explicit multiple of an orthogonal projection.

## Verification

Run `python3 CHECK.py` with the Python standard library. It checks the exact ratio-sign identity with rational arithmetic, the critical asymmetric example \(a=0,b=1,c=3\), the symmetric projection case, the location of a compact-regime maximizing mode, monotonicity of hundreds of staircase thresholds, and independent polar-quadrature comparisons against the analytical action of the integral kernel. These finite checks test normalization and indexing but do not replace the universal arguments in the proof.

An explicit benchmark at \(a=0,b=1,c=3\) is
\[
\sigma_n^2=\frac{n+2}{2(n+3)},\qquad
\|T\|=\frac1{\sqrt2},
\]
which displays a nonattained critical norm. At \(a=0,b=1,c=29/10\), the unique maximizing order is three.

## Relationship to prior work

Hu, Wang, Zhang and Zhou's September 2026 work treats the same three-parameter Forelli–Rudin kernels, emphasizing weak and restricted weak mapping in the hypersingular regime with input exponent strictly greater than output exponent. The present theorem instead concerns the exact singular-value and norm-attainment theory for the equal Hilbert exponent \(2\), with a newly exposed arithmetic–geometric staircase. Only their public abstract could be accessed for this comparison; its full text was not inspected.

Ding's 2020 study, examined in its open full text (notably Theorems 3.1–3.2 and the diagonalization proof), completely treats Schatten membership for the *single-weight* Bergman-type operator on bounded symmetric domains. After unitary identification, its disk specialization corresponds to the symmetric case \(a=b\), and therefore does not imply the asymmetric norm-maximizer staircase or critical nonattainment. Bai and Zhu's 2021 work addresses the unweighted kernel subfamily; available text confirms its scope \(a=b=0\), but the complete article was not accessible. These older results remain relevant antecedents for the spectral method and for the symmetric slice; this finding does not claim to originate the monomial diagonalization technique.

## Limitations

The theorem is for the disk, equal unweighted Hilbert input/output measure, real \(a,b>-1/2\), and positive real kernel power \(c\). It does not extend the endpoint weak-type classification of the motivating paper, cover the positive absolute-kernel operator, or determine analogous staircases on higher-dimensional balls. The available-source originality assessment is not independent review; unread full texts of the 2026 paper and the 2021 Bai–Zhu article leave an explicit residual overlap risk. An earlier unindexed treatment of the full asymmetric norm staircase cannot be categorically excluded.

## References

1. B. Hu, Z. Wang, K. Zhang and X. Zhou, *Cancellation of complex kernels and sharp critical lines and endpoint theory for the Forelli–Rudin operators I: the purely hypersingular case*, arXiv:2609.14552 (first posted 2026-09-13), https://arxiv.org/abs/2609.14552.
2. L. Ding, *Schatten class Bergman-type and Szegö-type operators on bounded symmetric domains*, arXiv:2009.09613 (first posted 2020-09-21), https://arxiv.org/abs/2009.09613.
3. X.-J. Bai and J.-F. Zhu, *Norm estimates for a class of operators related to the Bergman projection*, *Complex Variables and Elliptic Equations* **67** (2022), 1801–1816, DOI:10.1080/17476933.2021.1900136 (first online 2021-04-14).
