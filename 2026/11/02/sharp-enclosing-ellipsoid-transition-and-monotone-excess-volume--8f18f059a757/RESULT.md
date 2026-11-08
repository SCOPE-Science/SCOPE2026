# Strict monotonicity and dimensional scaling of enclosing-ellipsoid excess volume for Euclidean ball caps

## Finding
Let \(d\ge2\) be an integer, \(-1<a<1\), and
\[
K_{d,a}=\{(x,z)\in\mathbb R\times\mathbb R^{d-1}:x^2+\|z\|^2\le1,\ x\ge a\}.
\]
Let \(E_{d,a}\) be its unique minimum-volume enclosing ellipsoid and put
\(\mathcal R_d(a)=\operatorname{Vol}_d(E_{d,a})/\operatorname{Vol}_d(K_{d,a})\). Then **the normalized ellipsoidal excess-volume ratio is strictly increasing** as the cutting height \(a\) increases across the *entire* interval \((-1,1)\), including the point \(a=-1/d\) at which the optimal ellipsoid changes shape. Its exact endpoint laws are
\[
\lim_{a\downarrow-1}\mathcal R_d(a)=1,\qquad
\lim_{a\uparrow1}\mathcal R_d(a)=
\frac{\kappa_d}{\kappa_{d-1}}\frac{d^d}{2(d^2-1)^{(d-1)/2}},
\quad\kappa_j=\frac{\pi^{j/2}}{\Gamma(j/2+1)}.
\]
For every fixed \(a\in(0,1)\), as \(d\to\infty\),
\[
\mathcal R_d(a)\sim\sqrt{2\pi d}\,\frac{a}{1+a}.
\]
At the central-limit height \(a=\tau/\sqrt d\), for each fixed real \(\tau\),
\[
\lim_{d\to\infty}\mathcal R_d(\tau/\sqrt d)
=\frac{e^{-(\max\{\tau,0\})^2/2}}{\overline\Phi(\tau)},
\qquad\overline\Phi(\tau)=\frac1{\sqrt{2\pi}}\int_\tau^\infty e^{-s^2/2}\,ds.
\]
**Priority boundary:** The minimum-volume ellipsoid itself, including its entire all-height parameter formula and transition at \(-1/d\), is *not claimed as new*. It is a one-sided-cut specialization of Michael J. Todd's 1982 formula in *On Minimum Volume Ellipsoids Containing Part of a Given Ellipsoid*, Proposition 1 and section 3 (DOI:10.1287/moor.7.2.253). The findings assessed here are the strict ratio monotonicity and its quantitative endpoint and dimensional laws.

## Assumptions and definitions
The caps are full-dimensional Euclidean balls cut by one halfspace, not multiple cuts. All enclosing ellipsoids may have arbitrary center and orientation. Let \(q=(d-1)/2>0\). The cap volume is
\[
\operatorname{Vol}_d(K_{d,a})=\kappa_{d-1}\int_a^1(1-x^2)^q\,dx.
\]
By the known all-height ellipsoid formula of Todd (1982), the optimal ellipsoid has center and semiaxes
\[
(t,u,v)=\begin{cases}
(0,1,1), &-1<a\le -1/d,\\[2pt]
\left(\frac{1+da}{d+1},\frac{d(1-a)}{d+1},\frac{d\sqrt{1-a^2}}{\sqrt{d^2-1}}\right),& -1/d<a<1.
\end{cases}
\]
Here \(u\) is the axial semiaxis and \(v\) the common transverse semiaxis. Thus
\[
\mathcal R_d(a)=\frac{\kappa_d}{\kappa_{d-1}}
\frac{u v^{d-1}}{\int_a^1(1-x^2)^q\,dx}.
\]
The ellipsoid formula and its uniqueness are supplied as an expressly credited prior theorem; their presence as input does not constitute an originality assertion.

## Proof of the ratio and scaling claims
When \(a\le-1/d\), the optimal ellipsoid remains the unit ball. Its volume is constant whereas the cap volume is strictly decreasing, so \(\mathcal R_d(a)\) is strictly increasing on this interval.

For \(-1/d<a<1\), the published semiaxes give
\[
u v^{d-1}=C_d(1-a)(1-a^2)^q,\qquad
C_d=\frac{d^d}{(d+1)(d^2-1)^q}.
\]
Put \(h=1-a\in(0,1+1/d)\). The substitution \(x=1-hy\) shows
\[
\int_a^1(1-x^2)^qdx=h^{q+1}
\int_0^1 y^q(2-hy)^qdy.
\]
Therefore \(\mathcal R_d(a)=(\kappa_d/\kappa_{d-1})C_d F(h)\) with
\[
F(h)=\frac{(2-h)^q}{\int_0^1 y^q(2-hy)^qdy}.
\]
Differentiating under the integral sign yields
\[
\frac{d}{dh}\log F(h)=q\left[-\frac1{2-h}+
\frac{\int_0^1 y^q(2-hy)^q\,\frac{y}{2-hy}\,dy}
{\int_0^1 y^q(2-hy)^q\,dy}\right].
\]
For \(0\le y<1\) and \(0<h<1+1/d<2\),
\(y/(2-hy)<1/(2-h)\). The integrating weight is strictly positive for \(0<y<1\), so the derivative is strictly negative. As \(h=1-a\), the ratio increases strictly with \(a\). The formulas agree continuously at \(a=-1/d\), proving strict increase globally.

As \(a\downarrow-1\), the cap becomes the whole ball and the ratio tends to one. As \(a\uparrow1\), \(h\downarrow0\) and \(F(h)\to q+1=(d+1)/2\), giving exactly the displayed thin-cap constant.

For a fixed positive \(a<1\), endpoint Laplace asymptotics give
\[
\int_a^1(1-x^2)^qdx\sim\frac{(1-a^2)^{q+1}}{2qa}
\quad(d\to\infty).
\]
Use \(C_d\to1\), \(\kappa_d/\kappa_{d-1}\sim\sqrt{2\pi/d}\), and \(2q=d-1\) to obtain \(\mathcal R_d(a)\sim\sqrt{2\pi d}\,a/(1+a)\).

Finally, the first coordinate of a volume-uniform random point of \(B_d\), scaled by \(\sqrt d\), converges in law to \(N(0,1)\); hence
\(\operatorname{Vol}(K_{d,\tau/\sqrt d})/\kappa_d\to\overline\Phi(\tau)\). If \(\tau<0\), then \(\tau/\sqrt d<-1/d\) for all sufficiently large \(d\), so the ellipsoid is the unit ball. If \(\tau\ge0\), substitution in the explicit active semiaxes yields \(uv^{d-1}\to e^{-\tau^2/2}\). The quotient proves the stated crossover, including \(\tau=0\). \(\square\)

## Mathematical motivation and limitations
The excess-volume ratio measures the geometric overhead of replacing a one-cut ball by its least-volume enclosing ellipsoid. Strict monotonicity makes the degree of truncation a rigorous ordering of rounding efficiency. The fixed-height and Gaussian-window asymptotics give dimension-dependent benchmarks for convex optimization and approximation. These are quantitative statements about a specific natural one-parameter family; no all-convex-body or multi-cut extension is asserted. The 1982 optimal-ellipsoid formula is an essential cited input rather than an independently novel result. Since the new monotonicity proof is elementary once that formula is available, its priority and perceived value should be considered in that narrow context.

## Verification
The existing `verify_cap_lowner.py` checks rational containment and semiaxis identities, representative strictly ordered ratios, their thin-cap limits, and large-dimensional beta-integral comparisons. The calculations corroborate but do not prove the uniform all-dimensional theorem; the integral derivative and standard asymptotic arguments above are the proof. Independent direct cap integration at dimensions 2, 3 and 7 also confirmed increasing ratios over a grid of heights. The unchanged verifier includes checks of Todd's known semiaxis formula, which do not establish its novelty.

## References
1. M. J. Todd, *On Minimum Volume Ellipsoids Containing Part of a Given Ellipsoid*, Mathematics of Operations Research **7** (1982), 253–261, Proposition 1 and §3; DOI:10.1287/moor.7.2.253. Author-uploaded full text at https://www.researchgate.net/publication/242929698_On_Minimum_Volume_Ellipsoids_Containing_Part_of_a_Given_Ellipsoid .
2. G. Ivanov and M. Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781 (2022), general optimality framework, not claimed as new here.
3. *Smallest volume ellipsoid containing half ball*, Mathematics Stack Exchange question 5040265 (2025), special case \(a=0\), superseded as a priority lead for the general ellipsoid formula by Todd (1982).
