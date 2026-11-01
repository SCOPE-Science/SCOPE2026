# A sharp second-derivative Cheeger corner signature for rounded convex polygons

## Finding
Let \(K\subset\mathbb R^2\) be a compact convex polygon with nonempty interior, exactly \(n\ge3\) genuine vertices, area \(A>0\), perimeter \(P>0\), and interior angles \(0<\alpha_i<\pi\). Set \(C=\sum_{i=1}^n\cot(\alpha_i/2)\), let \(B\) denote the unit Euclidean disk, and put \(K_t=K+tB\) for \(t\ge0\). Its Cheeger constant is \(h(t)=\inf_{E\subseteq K_t,\,|E|>0}P(E)/|E|\), with the perimeter interpreted in the finite-perimeter sense. Define \(t_*=\sqrt{A/\pi}\) and \(B_*=P+2\sqrt{\pi A}\).

**Corner-signature theorem.** The outer-parallel Cheeger profile \(h(t)\) is continuously differentiable near \(t_*\), analytic on either side, and **not twice differentiable** at \(t_*\). More precisely, the one-sided second derivatives exist, and
\[
\boxed{h''(t_*+)-h''(t_*-)=\frac{8\pi^2}{B_*^3}\left(\sum_{i=1}^n\cot\frac{\alpha_i}{2}-\pi\right)>0.}
\]
For all \(t\ge t_*\), the entire rounded polygon \(K_t\) is its own Cheeger set and its Cheeger constant is exactly
\[
\boxed{h(t)=\frac{P+2\pi t}{A+Pt+\pi t^2}.}
\]
For \(t<t_*\) sufficiently close to \(t_*\), write \(T(t)=A-\pi t^2>0\), \(B(t)=P+2\pi t\) and \(\Delta=C-\pi>0\). Then
\[
\boxed{h(t)=\left[t+\frac{2T(t)}{B(t)+\sqrt{B(t)^2-4\Delta T(t)}}\right]^{-1}.}
\]
These formulas, including the indicated side, apply to every such polygon, without assuming that the Cheeger set of \(K\) itself meets all the sides of \(K\).

The dimensionless corner signature obeys the **sharp angular inequality**
\[
\boxed{\frac{B_*^3}{8\pi^2}\bigl(h''(t_*+)-h''(t_*- )\bigr)=C-\pi\ \ge\ n\tan(\pi/n)-\pi>0,}
\]
with equality in the first inequality exactly when \(K\) is equiangular. The bound is globally sharp among \(n\)-gons (for example, regular \(n\)-gons attain it).

In particular, a scalar Cheeger response to disk rounding recovers the summed polygonal corner invariant \(C\) once \(A\) and \(P\) are known. Moreover, the response tail \(h(t)\) for large \(t\) determines \(P\) and \(A\) itself, via
\[
h(t)=\frac2t-\frac{P}{\pi t^2}+\frac{P^2/\pi^2-2A/\pi}{t^3}+O(t^{-4}).
\]
Thus the complete profile determines \((A,P,C)\), though it need not determine the polygon.

## Assumptions and scope
Euclidean plane; a closed, full-dimensional convex polygon with only genuine vertices (no consecutive collinear sides); ordinary Euclidean Minkowski dilation by a disk; exact area, perimeter and Cheeger constant. The profile concerns all \(t\ge0\), but the explicit below-threshold branch is claimed only on an unspecified sufficiently short interval \((t_* -\varepsilon,t_*)\), because at smaller offsets the inner polygon may lose sides. The upper branch and sharp threshold are global. A double prime with argument \(t_*\pm\) denotes the corresponding one-sided limit of the second derivative from its analytic branch.

## Proof
**1. Two exact parallel-body identities.** For any compact convex set \(K\), let \(K\ominus sB=\{x:x+sB\subseteq K\}\) for \(s\ge0\). The support-halfspace characterization of an inner parallel set gives
\[
(K+tB)\ominus rB=\begin{cases}K+(t-r)B,&0\le r\le t,\\K\ominus(r-t)B,&r\ge t,\end{cases}
\]
whenever the right-hand side is nonempty. Indeed, membership is equivalent for every unit vector \(u\) to the support inequality \(x\cdot u\le h_K(u)+t-r\), and convexity provides the converse. Steiner's planar formula gives \(|K+qB|=A+Pq+\pi q^2\) for \(q\ge0\).

**2. The Cheeger radius and the exact cutoff.** The planar convex Cheeger characterization of Kawohl--Lachand-Robert asserts that the unique \(r(t)>0\) satisfying
\[
|(K+tB)\ominus r(t)B|=\pi r(t)^2
\]
is the reciprocal \(r(t)=1/h(t)\). Uniqueness follows also because the left side decreases with \(r\), whereas the right side strictly increases. At \(r=t\) the two sides are respectively \(A\) and \(\pi t^2\). Therefore \(r(t)>t\) exactly when \(t<t_*\), and \(r(t)\le t\) exactly when \(t\ge t_*\). In the latter range, substitute \(q=t-r(t)\ge0\) in Steiner's formula. The quadratic terms in \(r\) cancel, yielding
\[
(A+Pt+\pi t^2)-(P+2\pi t)r(t)=0,
\]
which proves the upper formula. The corresponding Cheeger set is \(((K+tB)\ominus r(t)B)+r(t)B=K_t\). For \(t<t_*\), the same identity shows the Cheeger set is not \(K_t\): its inner polygon has been cut back a strictly positive amount at every genuine corner. Thus the self-Cheeger threshold is exact, not merely sufficient.

**3. The inner-polygon quadratic germ.** Choose \(\varepsilon_0>0\) smaller than every offset at which an inset side of \(K\) disappears. For \(0\le s<\varepsilon_0\), inward shifts of the side-supporting lines produce another polygon with the same sequence of sides. The \(i\)-th corner removes a right-triangle strip correction governed by \(\cot(\alpha_i/2)\). Summing strip areas, or differentiating the inset perimeter, gives exactly
\[
|K\ominus sB|=A-Ps+Cs^2,\qquad
P(K\ominus sB)=P-2Cs.
\]
As \(t\uparrow t_*\) from below, the unique Cheeger radius obeys \(s(t)=r(t)-t\downarrow0\), so this formula applies. The Cheeger equation becomes
\[
T(t)-B(t)s(t)+\Delta s(t)^2=0,
\]
with \(\Delta=C-\pi>0\). The small root is the one displayed in the Finding. Existence, reality and analyticity in a left neighborhood follow from the implicit-function theorem at \((t,s)=(t_*,0)\), since the derivative of the equation with respect to \(s\) equals \(-B_*\ne0\). Its positive branch agrees with the unique geometric Cheeger radius.

**4. The sharp second-derivative jump.** Set \(\eta=t-t_*\) and \(s(t)=a\eta+b\eta^2+O(\eta^3)\). The preceding implicit equation gives
\[
a=-\frac{2\pi t_*}{B_*},\qquad
b=\frac{-\pi-2\pi a+\Delta a^2}{B_*}.
\]
For the analytic continuation of the upper branch, \(r_+(t)=t+T(t)/B(t)\), the corresponding coefficient is \(b_+=(-\pi-2\pi a)/B_*\). Both radii have the same value \(t_*\) and first derivative \(1+a=P/B_*\) at the join; therefore \(h=1/r\) is \(C^1\). Their quadratic coefficients differ by \(b-b_+=\Delta a^2/B_*\). Upon inverting \(r\), the difference between the right and left second derivatives of \(h\) is precisely
\[
\frac{2(b-b_+)}{t_*^2}=\frac{8\pi^2\Delta}{B_*^3}.
\]
The strict positivity below proves failure of \(C^2\).

**5. Angular optimality and response recovery.** Let \(\beta_i=(\pi-\alpha_i)/2\) be half the exterior turning angles. Each \(\beta_i\in(0,\pi/2)\), \(\sum_i\beta_i=\pi\), and \(C=\sum_i\tan\beta_i\). Strict convexity of \(\tan\) on this interval and Jensen's inequality show \(C\ge n\tan(\pi/n)>\pi\), with equality precisely when the turns (equivalently, interior angles) are equal. Finally, expansion of the rational upper branch at infinity gives the stated coefficients; the coefficient of \(t^{-2}\) recovers \(P\), and that of \(t^{-3}\) then recovers \(A\). The one-sided jump gives \(C\). All assertions follow.

## Verification
The standalone program `checks/check_cheeger_cusp.py` (Python 3, SymPy and mpmath) checks the implicit quadratic expansion symbolically, independently differentiates the implicit equation, verifies rectangle and equilateral-triangle inset formulas, and compares high-precision one-sided numerical limits and direct Cheeger-radius equations. It reports `ALL_CHECKS_PASSED`. The infinite statements are proved above, not inferred from numerical testing.

## Relationship to prior work
Kawohl and Lachand-Robert's 2006 planar convex Cheeger characterization provides the reciprocal-radius equation and explicit inner parallel polygon geometry (their Theorems 1--3 and Section 4). Those are acknowledged inputs, not new claims. Saracco's 2019 public preprint gives a rolling-disk criterion for self-Cheeger sets; it underlies the global self-Cheeger threshold but does not identify the one-sided second-derivative defect. Cañete's 2021 work analyzes symmetric Cheeger sets, including distinctions between ordinary and symmetry-specific regularity, without a rounded-profile corner law. Ftouhi, Masiello and Paoli's 2022 work classifies sharp Cheeger inequalities for planar convex shapes rather than the local corner signature of a rounding response. Ftouhi's December 2024 preprint analyzes monotonicity and first differentiability of Cheeger constants of general parallel bodies; its first-order theorem neither states the discontinuity of the second derivative nor identifies its exact polygonal angle coefficient. No covering formula for the latter was identified in the inspected materials; unlocated earlier equivalent formulas remain possible.

## Limitations
The theorem does not reconstruct individual angles, side lengths, or the polygon from \((A,P,C)\). The formula immediately below \(t_*\) need not hold down to \(t=0\), because inset edges can disappear. The first two ingredients (planar convex Cheeger-radius characterization and polygon inset-area formula) are classical, as is the criterion underlying the universal self-Cheeger threshold; the specific new assertion is the second-order junction law and its sharp angular recovery inequality. No noisy-data stability, finite-sample bounds, nonconvex polygon analogue, or higher-dimensional extension is claimed. Independent validation has not been performed.

## References
- B. Kawohl and T. Lachand-Robert, *Characterization of Cheeger sets for convex subsets of the plane*, Pacific Journal of Mathematics 225 (2006), 103--118; doi:10.2140/PJM.2006.225.103. Full manuscript: https://www.mi.uni-koeln.de/mi/Forschung/Kawohl/kawohl/CheegerConvexR-2.pdf.
- G. Saracco, *A sufficient criterion to determine planar self-Cheeger sets*, arXiv:1906.12101, first public June 28, 2019; https://arxiv.org/abs/1906.12101.
- A. Cañete, *Cheeger Sets for Rotationally Symmetric Planar Convex Bodies*, Results in Mathematics 77, article 9 (published online November 6, 2021), doi:10.1007/s00025-021-01539-7.
- I. Ftouhi, A. L. Masiello and G. Paoli, *Sharp inequalities involving the Cheeger constant of planar convex sets*, arXiv:2206.13158, first public June 27, 2022; https://arxiv.org/abs/2206.13158.
- I. Ftouhi, *The monotonicity of the Cheeger constant for parallel bodies*, arXiv:2412.20917, first public December 30, 2024; https://arxiv.org/abs/2412.20917.
