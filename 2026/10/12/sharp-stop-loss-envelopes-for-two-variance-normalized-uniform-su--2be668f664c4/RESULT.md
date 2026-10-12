# Sharp stop-loss envelopes for two variance-normalized uniform summands

## Finding
Let \(U,V\) be independent uniform random variables on \([-1,1]\), let \(d\geq0\), and consider every real coefficient pair satisfying \(a^2+b^2=1\). Define the stop-loss (integrated right-tail) functional
\[
L_d(a,b)=\mathbb E[(aU+bV-d)_+],\qquad (x)_+=\max\{x,0\}.
\]
This normalization fixes \(\operatorname{Var}(aU+bV)=1/3\). Set
\[
q_1=\frac1{2\sqrt2},\quad q_2=\frac1{\sqrt5},\quad q_3=\frac1{\sqrt3},\qquad s_d=\sqrt{d^2+3}-d,\quad b_d=\sqrt{\frac{1+3d^2}{2}}.
\]
For every \(d\ge0\), the exact minimum is
\[
\min_{a^2+b^2=1}L_d(a,b)=
\begin{cases}
(\sqrt2-d)^3/12,&0\le d\le q_1,\\
(s_d-d)^3/[12(s_d^2-1)],&q_1\le d\le q_2,\\
b_d/3-d/2,&q_2\le d\le q_3,\\
(1-d)_+^2/4,&d\ge q_3.
\end{cases}
\]
The exact maximum is
\[
\max_{a^2+b^2=1}L_d(a,b)=
\max\left\{\frac{(1-d)_+^2}{4},\frac{(\sqrt2-d)_+^3}{12}\right\}.
\]
There is a unique \(\delta\in(0,1)\), approximately \(0.4717750532144\), satisfying \(3(1-\delta)^2=(\sqrt2-\delta)^3\). For \(0\le d<\delta\) the maximum uses a single summand; for \(\delta<d<\sqrt2\) it uses equal coefficients. At \(d=\delta\) both orientations maximize; at \(d\ge\sqrt2\), all orientations yield zero. The minimizers pass through **four exact phases**: equal magnitudes, unequal magnitudes parametrized by \(s_d\), unequal magnitudes parametrized by \(b_d\), and one nonzero coefficient. For \(d\ge1\), the minimum is zero, attained exactly when \(|a|+|b|\le d\). The optimizer descriptions before this degeneracy are unique up to signs and permutation; at the joining thresholds adjacent formulas give the same orientation.

## Assumptions and scope
Only independence and exact uniformity of \(U,V\) are assumed; both coefficients may be zero individually but not simultaneously, and the strike is any fixed real \(d\ge0\). Because the summands are symmetric and exchangeable, set \(b=\max\{|a|,|b|\}\), \(c=\min\{|a|,|b|\}\), so \(1/\sqrt2\le b\le1\), \(c=\sqrt{1-b^2}\). In the first interior minimum regime \(q_1<d<q_2\), the minimizing pair is \((b,c)=((s_d+\sqrt{2-s_d^2})/2,(s_d-\sqrt{2-s_d^2})/2)\). In the second interior minimum regime \(q_2<d<q_3\), it is \((b_d,\sqrt{1-b_d^2})\). At \(0\le d<1\), the one-summand minimum in the fourth phase is \((1,0)\). The minimizer at \(d=0\) is exactly balanced.

## Proof
**1. Exact integrated tail.** For \(b\ge c>0\), convolution of the uniform densities gives a trapezoidal distribution for \(bU+cV\). Direct integration, or the two-sided uniform spline identity, gives
\[
L_d(b,c)=\frac{(b+c-d)_+^3-(b-c-d)_+^3}{24bc},\qquad d\ge0.
\]
For \(c=0\), continuity or elementary uniform integration gives \(L_d(1,0)=(1-d)_+^2/4\). This covers every boundary of the coefficient circle.

**2. Two analytic chambers.** In the central chamber \(0\le d\le b-c\), use \(b^2+c^2=1\) to simplify:
\[
L_d(b,c)=\frac b6-\frac d2+\frac{1+3d^2}{12b}=:G_d(b),
\quad G_d'(b)=\frac{2b^2-1-3d^2}{12b^2},\quad G_d''(b)=\frac{1+3d^2}{6b^3}>0.
\]
Thus this chamber has no interior maximum and its sole possible interior minimum is \(b=b_d\).

In the outer chamber \(b-c\le d<b+c\), let \(s=b+c\), so \(1\le s\le\sqrt2\) and \(2bc=s^2-1\). Then
\[
L_d(b,c)=\frac{(s-d)^3}{12(s^2-1)}=:F_d(s),\qquad
F_d'(s)=\frac{(s-d)^2(s^2+2ds-3)}{12(s^2-1)^2}.
\]
The quadratic \(s^2+2ds-3\) is strictly increasing in positive \(s\), and vanishes only at \(s=s_d\). Accordingly this chamber has no interior maximum and has at most one interior minimum. Where \(d\ge b+c\), the functional is zero.

**3. Sharp minima and phase boundaries.** For \(0\le d<1\), the chamber interface \(d=b-c\) occurs at
\[
b=\frac{\sqrt{2-d^2}+d}{2},\qquad s=\sqrt{2-d^2}.
\]
The candidate \(s_d\) first enters the outer chamber through \(s=\sqrt2\) at \(d=q_1\), and meets the interface at \(d=q_2\). In the central chamber, \(b_d\) first becomes admissible at the same \(q_2\) and reaches \(b=1\) at \(d=q_3\). The signs of the derivatives displayed above show, successively: the global minimum is the balanced endpoint until \(q_1\); it is the unique outer-chamber stationary point until \(q_2\); it is the unique central-chamber stationary point until \(q_3\); and then it is the one-summand endpoint until \(d=1\). The displayed formulas result by substitution. For \(d\ge1\), the one-summand value is zero, hence the global minimum is zero; the nonnegative integrand vanishes almost surely exactly when its maximum possible argument satisfies \(b+c\le d\).

**4. Sharp maxima and switching point.** The derivative signs and convexity in Step 2 exclude a strict interior maximum in either chamber. The outer chamber can only maximize at its equal-weight end or its common interface; the central chamber can only maximize at that same interface or at \(b=1\). Since the derivative crosses the interface consistently, the interface cannot create a strict maximum: for \(d<q_2\), the outer derivative with respect to \(s\) is negative at the interface and the central derivative with respect to \(b\) is positive there (note that \(s=b+c\) decreases with \(b\)); for \(q_2<d<1\), the outer derivative with respect to \(s\) is positive at the interface and the central derivative with respect to \(b\) is negative there. At \(d=q_2\), both derivatives vanish. For \(d\ge1\), there is no central chamber and the positive part is nondecreasing in \(s\). Equivalently, direct comparison on each chamber gives the maximal endpoint pair \((1,0)\) or \((1/\sqrt2,1/\sqrt2)\). Their values are exactly the two terms in the asserted maximum formula. For \(d<1\), their ratio is \((\sqrt2-d)^3/[3(1-d)^2]\); its logarithmic derivative has the sign of \(d+2\sqrt2-3\), so the ratio first decreases and then increases, starts below one at \(d=0\), and diverges as \(d\uparrow1\). There is precisely one crossing \(\delta\in(0,1)\). On \(1\le d<\sqrt2\), only the equal-weight endpoint can yield the maximum; for \(d\ge\sqrt2\), all values vanish. This proves the asserted sharp envelopes and optimizer classifications.

## Verification
The standalone standard-library Python program `verify_stoploss.py` checks the two analytic chamber identities and their derivatives by exact rational arithmetic on multiple coefficient/strike triples, the closed formulas at the three transition strikes, independent direct integrations of the triangular/trapezoidal uniform density, and deterministic numerical optimization against the analytic envelopes. Run `python3 verify_stoploss.py`. These finite checks supplement, rather than replace, the analytic proof above.

## Relationship to prior work
He, Tkocz, and Wyczesany (first made public on 10 May 2023) establish a sharp Gaussian tail comparator for variance-normalized sums of independent uniforms; their main object is the **probability** of exceeding a given threshold, not the integrated exceedance (stop-loss) functional optimized exactly over two weights. Barthe and Koldobsky (2003) prove extremality of certain cube-slab volumes for a range of widths; König and Koldobsky (2011) compute volume formulas and study critical directions for slabs in two and three dimensions. Such pointwise slab statements or evaluation formulas do not state the four-regime optimal integrated-tail envelope. Brandenburg, De Loera, Luo, and Meroni (2026) give a general algorithm for polynomial moments of slices and slabs and study selected critical-point systems, but do not state this variance-normalized stop-loss minimax and its transition constants. The exact optimizer classification here is the distinctive assertion.

## Limitations
This theorem concerns exactly two summands, a fixed quadratic coefficient normalization, and nonnegative strikes. It does not classify arbitrary numbers of summands or prove a single convex-order comparison for all strikes. The older slab-geometry literature is extensive and some relevant primary full texts were not accessible in full for priority comparison; bibliographic priority is therefore not independently certified. No independent mathematical audit has been conducted.

## References
1. X. He, T. Tkocz, K. Wyczesany, *A Sharp Gaussian Tail Bound for Sums of Uniforms*, arXiv:2305.06235 (first publicly posted 10 May 2023), https://arxiv.org/abs/2305.06235.
2. F. Barthe, A. Koldobsky, *Extremal slabs in the cube and the Laplace transform*, Advances in Mathematics 174 (2003), 89–114, https://doi.org/10.1016/S0001-8708(02)00055-5.
3. H. König, A. Koldobsky, *Volumes of low-dimensional slabs and sections in the cube*, Advances in Applied Mathematics 47 (2011), 894–907, https://doi.org/10.1016/j.aam.2011.05.001.
4. M.-C. Brandenburg, J. A. De Loera, Y. Luo, C. Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, arXiv:2603.25643 (2026), https://arxiv.org/html/2603.25643v2.
