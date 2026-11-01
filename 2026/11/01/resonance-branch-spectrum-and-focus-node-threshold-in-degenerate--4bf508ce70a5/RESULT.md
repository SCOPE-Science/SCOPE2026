# Resonance-branch spectrum and focus–node threshold in degenerate border-collision maps

## Finding

Consider the rank-one left and nonsingular right Jacobians of the planar border-collision normal form,
\[
A_L=\begin{pmatrix}a&1\\0&0\end{pmatrix},\qquad
A_R=\begin{pmatrix}t&1\\-d&0\end{pmatrix},\qquad a>0,\ d>0,\ t\in\mathbb R.
\]
For each integer \(n\ge1\), call \(t\) an **\(n\)-right-step collapse resonance** when
\[
P_n(t;a,d):=\operatorname{tr}(A_LA_R^n)=0.
\]
These are the candidate zero-slope loci for the affine right-then-left return branches, *before* itinerary admissibility is imposed.

For every \(a,d>0\) and \(n\ge1\), the equation \(P_n(t;a,d)=0\) has **exactly \(n\) distinct real roots**. All roots vary real-analytically in \(d>0\) at fixed \(a\); roots for consecutive values of \(n\) strictly interlace. Exactly \(\lfloor n/2\rfloor\) roots are negative and \(\lceil n/2\rceil\) are positive. All negative roots and all but possibly the largest positive root are in the right-Jacobian focus band \(|t|<2\sqrt d\). The largest root is inside, on, or outside its positive edge according as
\[
d\ <,\ =,\ >\ a^2\left(1+\frac1n\right)^2.
\]
Thus a single positive hyperbolic collapse branch appears at a **sharp, degree-dependent focus–node crossing**; no negative hyperbolic collapse branch exists.

Writing \(c=\sqrt d/a\) and \(t_{n,\max}\) for the largest root, if \(d>a^2\) then, for all sufficiently large \(n\),
\[
2\sqrt d<t_{n,\max}<a+\frac da,
\qquad
 t_{n,\max}\longrightarrow a+\frac da.
\]
More precisely,
\[
a+\frac da-t_{n,\max}
=\sqrt d\,\frac{(c^2-1)^2}{c^{2n+3}}\left(1+O_c(nc^{-2n})\right).
\]
At the accumulation threshold \(d=a^2\), every root is explicit:
\[
t_{n,j}=2a\cos\frac{(2j-1)\pi}{2n+1},\qquad 1\le j\le n.
\]
For any fixed \(a,d>0\), the empirical distribution of all \(n\) roots tends weakly to the arcsine probability measure
\[
\frac{\mathbf1_{(-2\sqrt d,2\sqrt d)}(t)}{\pi\sqrt{4d-t^2}}\,dt.
\]
The complete set of accumulation points of distinct resonances, as \(n\to\infty\), is the closed focus band \([-2\sqrt d,2\sqrt d]\), with one additional point \(a+d/a\) precisely when \(d>a^2\).

## Assumptions and scope

The result concerns **algebraic collapse resonances of affine itinerary pieces**, not a claim that every algebraic resonance is visited by a genuine orbit. In the full map the left branch has \(x\le0\), the right branch has \(x\ge0\), and the affine forcing \(\mu\) affects orbit locations but not the derivative matrices. For an admissible interval of \(x\)-axis initial conditions following exactly \(n\) right iterations and one left iteration, the derivative of the resulting section map is \(P_n\). Vanishing of \(P_n\) makes that section branch constant. If the constant branch participates in an actual periodic orbit then that orbit is superstable, but no existence, attractivity, or width of a periodicity region follows merely from \(P_n=0\).

The assumptions \(a>0\) and \(d>0\) are essential for the symmetric Jacobi reduction and the stated sign classification. The integer \(n\) is arbitrary but fixed for each algebraic equation; the limiting statements send \(n\to\infty\) with \(a,d\) fixed.

## Proof

**1. The trace recurrence.** Define \(f_0=1\), \(f_1=t\), and \(f_k=tf_{k-1}-df_{k-2}\) for \(k\ge2\). Induction on matrix powers gives
\[
(A_R^n)_{11}=f_n,\qquad (A_R^n)_{21}=-df_{n-1},
\]
so, since the second row of \(A_L\) is zero,
\[
P_n=af_n-df_{n-1}.
\]
Writing \(u=t/\sqrt d\) and using the second-kind Chebyshev polynomials \(U_0=1\), \(U_1(v)=2v\), \(U_{k+1}(v)=2vU_k(v)-U_{k-1}(v)\), we have
\[
P_n(t;a,d)=a d^{n/2}\left[U_n(u/2)-cU_{n-1}(u/2)\right],
\qquad c=\frac{\sqrt d}{a}>0.
\]

**2. Real, simple, interlacing zeros.** Let \(J_n(c)\) be the real symmetric tridiagonal matrix with diagonal \((c,0,\ldots,0)\) and every adjacent off-diagonal entry equal to \(1\). The continuant determinant recurrence gives
\[
\det(uI-J_n(c))=U_n(u/2)-cU_{n-1}(u/2).
\]
Its eigenvalues are real. Each eigenspace is one-dimensional: after choosing the first coordinate, the tridiagonal eigenvector recurrence fixes every following coordinate, and a zero first coordinate forces the entire eigenvector to vanish. Symmetry then makes all eigenvalues algebraically simple. The matrices \(J_n(c)\) are successive leading principal submatrices of \(J_{n+1}(c)\); strict Cauchy interlacing follows from the nonzero connecting off-diagonal entry. Simple-root perturbation theory gives real-analytic eigenvalue branches for \(c>0\), and hence for \(d>0\).

**3. Exact sign count and focus boundary.** For \(c=0\), the eigenvalues of \(J_n(0)\) are \(2\cos(j\pi/(n+1))\), \(1\le j\le n\). Increasing \(c>0\) adds a positive rank-one matrix. The zero-eigenvalue determinant is
\[
\det(-J_n(c))=(-1)^n[U_n(0)-cU_{n-1}(0)].
\]
It never vanishes for \(c>0\). For even \(n\), the positive/negative count remains \(n/2\) each. For odd \(n\), the single zero eigenvalue at \(c=0\) moves strictly upwards (the first component of every path eigenvector is nonzero), yielding \((n+1)/2\) positive and \((n-1)/2\) negative eigenvalues.

Because \(J_n(c)\succeq J_n(0)\) and the smallest eigenvalue of \(J_n(0)\) is strictly greater than \(-2\), every root satisfies \(u>-2\). Deleting the first row and column of \(J_n(c)\) leaves the length-\(n-1\) path matrix; its largest eigenvalue is strictly below \(2\). Interlacing therefore puts **all but the largest** eigenvalue strictly below \(2\) (the case \(n=1\) is immediate). At \(u=2\),
\[
\det(2I-J_n(c))=U_n(1)-cU_{n-1}(1)=n+1-cn.
\]
As the other factors \(2-u_j\) are positive, the largest eigenvalue is below, equal to, or above \(2\) exactly when \(c<\), \(=\), or \(>\,(n+1)/n\). Multiplying by \(\sqrt d\) gives the stated threshold. The negative roots are automatically inside the focus band.

**4. The exceptional positive root.** For \(c>1\), the root beyond \(u=2\) exists for all sufficiently large \(n\). Put \(u=\lambda+\lambda^{-1}\) with \(\lambda>1\). The equation for this root becomes
\[
\lambda^{2n+1}(\lambda-c)=1-c\lambda.
\]
Equivalently \(c-\lambda=(c\lambda-1)\lambda^{-2n-1}>0\). The variational principle applied to \(v=(1,c^{-1},\ldots,c^{-(n-1)})\) yields
\[
0\le c+c^{-1}-u_{n,\max}
\le \frac{(c^2-1)c^{-2n-1}}{1-c^{-2n}}.
\]
The upper inequality uses the exact identity
\[
(c+c^{-1})\|v\|^2-v^T J_n(c)v=c^{-2n+1};
\]
and \(c+c^{-1}\) is a genuine global upper bound on the top eigenvalue because
\[
(c+c^{-1})\|w\|^2-w^T J_n(c)w
=\sum_{j=1}^{n-1}(\sqrt c\,w_{j+1}-w_j/\sqrt c)^2+c^{-1}w_n^2\ge0.
\]
Therefore \(\lambda\to c\), and expansion of the preceding exact hyperbolic-root equation gives
\[
 c-\lambda=(c^2-1)c^{-2n-1}(1+O_c(nc^{-2n})).
\]
Since \(u=\lambda+\lambda^{-1}\), this proves the stated sharp exponential difference. If \(c\le1\), the largest eigenvalue lies below \(2\) for every \(n\) and tends to \(2\) by comparison with \(J_n(0)\). At \(c=1\), the trigonometric identity \(\sin((n+1)\phi)=\sin(n\phi)\) gives the displayed half-odd-grid roots.

**5. Limiting density and accumulation set.** The rank-one perturbation \(J_n(c)-J_n(0)\) alters each empirical spectral cumulative distribution by at most \(1/n\). The eigenangles \(j\pi/(n+1)\) of \(J_n(0)\) become equidistributed on \((0,\pi)\), yielding the arcsine law after multiplication by \(\sqrt d\). Strict interlacing, or the same rank-one counting bound in every interval, supplies roots arbitrarily close to each point of the closed focus band for increasing \(n\). There is at most one root outside it, and its unique possible additional accumulation point when \(c>1\) is \(\sqrt d(c+c^{-1})=a+d/a\). For \(c\le1\), no such additional point exists.

## Verification

The accompanying standalone script `verify_resonance.py` uses only Python's standard-library exact rational arithmetic. It independently calculates matrix powers and checks the trace recurrence, independently evaluates tridiagonal continuants against Chebyshev recurrences, applies exact Sturm sign-change counts at the two focus edges and at zero, and rechecks the previously published four-right-step polynomial. It reports 2,450 passing exact comparisons. These finite checks corroborate the formulas but do **not** establish the all-degree assertions, which are proved above.

## Relationship to prior work

D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant* (first arXiv release August 8, 2024, arXiv:2408.04790), §6.6, derives and interprets the four-right-step zero-trace resonance as the cause of local flat return branches; it explicitly leaves broader resonance-curve geometry open. Simpson's *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant* (first arXiv release June 8, 2026, arXiv:2606.08901), §5.3, gives a general first-return slope formula, plots a finite selection of zero-slope loci, and cautions that a zero-slope piece may be unvisited by an attractor. The present result starts with that **known slope mechanism** and proves an additional all-degree spectral classification: exact real-simple root counts, sign split, a degree-dependent focus/node threshold, strict interlacing, limiting density and an exponentially approached hyperbolic accumulation locus. The classical Jacobi/Chebyshev reduction is expressly part of the proof, not claimed as an independently novel method.

## Limitations

Algebraic roots do **not** by themselves imply an admissible \(R^nL\) itinerary, a periodic orbit, a positive-width stability tongue, or a chaotic-to-periodic transition. The resonance of the full Jacobian product is only a necessary zero-slope condition for a candidate return branch. Realization and basin questions remain separate. All claims require \(a>0\), \(d>0\); they do not address negative determinants, singular right Jacobians, or other symbolic words. The result is analytically checked but has not received independent scientific validation. The literature search is finite; equivalent unindexed spectral specializations remain possible.

## References

1. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790, first public version August 8, 2024; especially §6.6. https://arxiv.org/abs/2408.04790
2. D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901, first public version June 8, 2026; especially §5.3. https://arxiv.org/abs/2606.08901
3. D. J. W. Simpson, *The Two-Dimensional Border-Collision Normal Form with a Zero Determinant*, SIAM J. Appl. Dyn. Syst. 24 (2025), 2205–2245, doi:10.1137/24M1683548 (journal version of reference 1).
4. Classical results used: Cauchy eigenvalue interlacing, Sturm's tridiagonal inertia theorem and second-kind Chebyshev polynomial recurrences.
