# Exact Haar central-chord law of rectangular boxes and its singularity thresholds

## Finding

Let \(a_1,a_2,a_3>0\), let \(B=\prod_{i=1}^3[-a_i,a_i]\subset\mathbb R^3\), and let \(U\) be uniformly distributed on the unit sphere \(S^2\). The unoriented line \(\mathbb RU\) passes through the box's center. Denote its chord length by \(L=\mathcal H^1(B\cap\mathbb RU)\), and write \(R=(a_1^2+a_2^2+a_3^2)^{1/2}\).

For positive \(s,t\), define the elementary overlap function
\[
J(s,t)=\begin{cases}
\displaystyle\frac2\pi\left[\arctan\!\frac{z}{st}-s\arctan\!\frac zt-t\arctan\!\frac zs\right],
&0<s<1,\ 0<t<1,\ s^2+t^2<1,\\[4pt]
0,&\text{otherwise},
\end{cases}
\qquad z=(1-s^2-t^2)^{1/2}.
\]
Then, for every real \(x\), the **complete central-chord distribution function** \(F_B(x)=\mathbb P\{L\le x\}\) is
\[
\boxed{F_B(x)=\begin{cases}
0,&x\le2\min_i a_i,\\
\displaystyle\sum_{i=1}^3\left(1-\frac{2a_i}{x}\right)_+
-\sum_{1\le i<j\le3}J\left(\frac{2a_i}{x},\frac{2a_j}{x}\right),
&2\min_i a_i<x<2R,\\[2pt]
1,&x\ge2R,
\end{cases}}
\]
where \((y)_+=\max\{y,0\}\). In particular the possible chord lengths are exactly \([2\min_i a_i,2R]\).

Every pair of facets creates a **sharp geometric threshold** at its corresponding face diagonal \(x_{ij}=2r_{ij}\), where \(r_{ij}=(a_i^2+a_j^2)^{1/2}\). Independently of coincidences among thresholds,
\[
\boxed{J\left(\frac{2a_i}{x},\frac{2a_j}{x}\right)
=\frac{2\sqrt{r_{ij}}}{3\pi a_ia_j}\,(x-x_{ij})_+^{3/2}
+O\left((x-x_{ij})_+^{5/2}\right)}
\]
in a sufficiently small two-sided neighborhood of \(x_{ij}\), where the error is zero below the threshold. If no other facet or pair threshold coincides, this yields a nonanalytic \(3/2\)-power onset in the distribution itself. At coincident thresholds, the indicated pair contributions add; single-facet terms may also have their own linear positive-part onset.

At the **longest-chord endpoint** the survival function obeys the exact quadratic law
\[
\boxed{\mathbb P\{L>x\}=\frac{R}{4\pi a_1a_2a_3}\,(2R-x)^2+O\bigl((2R-x)^3\bigr),\qquad x\uparrow2R.}
\]
This is a complete all-aspect-ratio law, rather than a cube-only specialization or a law for lines with random offsets.

## Assumptions and scope

The three lengths \(a_i\) are arbitrary strictly positive real numbers, with no ordering or aspect-ratio restrictions. The line passes exactly through the center; its direction has normalized rotation-invariant spherical measure, so \(U\) and \(-U\) give the same chord. This is different from a motion-invariant random line with random offset, a uniform random point-and-direction line, and a random *plane* through the center. Expressions with \(s_i\ge1\) are interpreted by the explicit zero clause of \(J\); endpoints are included as above. The claimed singularity coefficients concern pair-overlap contributions, including when two or more thresholds coincide. All assertions concern Euclidean length and axis-orthogonal rectangular boxes in ambient dimension three.

## Proof

**1. Radial representation and support.** For \(U=(U_1,U_2,U_3)\in S^2\), the furthest permitted parameter on the ray \(tU\), \(t\ge0\), is \(\min_i a_i/|U_i|\), with the usual infinite convention for a zero coordinate. Central symmetry doubles the radius, giving \(L=2\min_i a_i/|U_i|\). Hence \(L\ge2\min_i a_i\). The equality direction of a shortest half-axis realizes the lower endpoint. The Cauchy–Schwarz inequality in the form \(1=\sum_iU_i^2\le\max_i(U_i^2/a_i^2)\sum_i a_i^2\) yields \(L\le2R\), with equality exactly at the eight body-diagonal directions \(U_i=\pm a_i/R\). Continuity of \(L\) on the sphere and connectedness give the complete interval of values.

**2. Inclusion–exclusion for three orthogonal caps.** For \(0<x<2R\) put \(s_i=2a_i/x\), and let \(E_i=\{|U_i|\ge s_i\}\). Then \(\{L\le x\}=\bigcup_iE_i\) up to measure-zero equality boundaries. Each coordinate of a uniform spherical direction is uniform on \([-1,1]\), hence \(\mathbb P(E_i)=(1-s_i)_+\). Since \(\sum_i s_i^2=4R^2/x^2>1\), no three events can occur simultaneously. Thus exact inclusion–exclusion stops after the three pair intersections.

**3. Evaluation of each pair intersection.** The joint density of \((U_i,U_j)=(u,v)\) in the open unit disk is \(1/(2\pi\sqrt{1-u^2-v^2})\). For \(s,t>0\) with \(s^2+t^2<1\), symmetry over four quadrants gives
\[
\mathbb P(E_i\cap E_j)=\frac2\pi\int_s^{\sqrt{1-t^2}}\arctan\!\left(\frac{\sqrt{1-t^2-u^2}}t\right)\,du.
\]
Its partial derivative with respect to \(s\) is \(-2\arctan(\sqrt{1-s^2-t^2}/t)/\pi\). Direct differentiation of the stated elementary expression for \(J(s,t)\) gives the same derivative. Both expressions vanish at \(s=\sqrt{1-t^2}\), hence they coincide throughout the positive chamber. When \(s^2+t^2\ge1\), or either threshold is at least one, the joint event has zero spherical area and the zero branch applies. Substitution proves the displayed distribution for every positive aspect ratio and threshold.

**4. Sharp pair-threshold exponent.** Fix \(i<j\), abbreviate \(r=r_{ij}\), \(s=2a_i/x\), \(t=2a_j/x\), and set \(z=(1-s^2-t^2)^{1/2}\) for \(x>2r\). In a single coordinate-sign quadrant shift the integral variables by \(u=s+\xi\), \(v=t+\eta\). As \(z\downarrow0\), the integration region is a shrinking triangle \(2s\xi+2t\eta\le z^2\), and its density is \((z^2-2s\xi-2t\eta+O(\xi^2+\eta^2))^{-1/2}\). Rescaling \(\xi=z^2A/(2s)\), \(\eta=z^2B/(2t)\) and integrating \(A,B\ge0\), \(A+B\le1\), yields
\[
J(s,t)=\frac{2z^3}{3\pi st}+O(z^5).
\]
The error follows as well by Taylor expanding the explicit arctangent expression at \(z=0\); all singular factors cancel, and the remaining expansion has odd powers beginning at degree three. Since \(z^2=1-(2r/x)^2=(x-2r)/r+O((x-2r)^2)\), and \(st\to a_ia_j/r^2\), the coefficient is \(2\sqrt r/(3\pi a_ia_j)\). The pair probability vanishes identically for \(x\le2r\). Any coincidence of thresholds simply adds the corresponding terms in the exact distribution.

**5. The terminal quadratic law.** Set \(Y_i=U_i^2\). Then \((Y_1,Y_2,Y_3)\) has the Dirichlet density with parameters \((1/2,1/2,1/2)\), namely
\[
f(y_1,y_2)=\frac1{2\pi\sqrt{y_1y_2y_3}},\quad y_3=1-y_1-y_2.
\]
For \(x<2R\), the event \(\{L>x\}\) is exactly \(Y_i<4a_i^2/x^2\) for all three indices. Write \(p_i=a_i^2/R^2>0\), and \(\delta=4R^2/x^2-1>0\). The variables \(v_i=4a_i^2/x^2-Y_i\) are nonnegative and satisfy \(v_1+v_2+v_3=\delta\), a planar simplex of coordinate area \(\delta^2/2\). As \(\delta\downarrow0\), its points converge uniformly to \((p_1,p_2,p_3)\), at which the density is smooth and equals \(R^3/(2\pi a_1a_2a_3)\). Therefore
\[
\mathbb P\{L>x\}=\frac{R^3}{4\pi a_1a_2a_3}\,\delta^2+O(\delta^3).
\]
Putting \(x=2R-\varepsilon\) gives \(\delta=\varepsilon/R+O(\varepsilon^2)\) and the claimed \(R\varepsilon^2/(4\pi a_1a_2a_3)+O(\varepsilon^3)\). This completes the proof.

## Verification

The companion self-contained Python 3 program `verify.py` implements the elementary CDF and an independent one-dimensional numerical integral for each two-cap overlap, and checks the endpoint and pair-threshold coefficients. It also compares the exact law against seeded Gaussian-sphere Monte Carlo for three distinct boxes. Run `python3 verify.py` from the directory containing the script; a successful run prints `VERIFY_OK`. These finite computations are reproducibility checks only; the preceding measure-theoretic integration and exact asymptotics prove the continuum assertions.

## Relationship to prior work

Guédon, Litvak, Tatarko, and Vritsiou [1] investigate random section diameters of convex bodies and sharp general bounds. Their quantitative estimates motivate exact low-dimensional models, but they do not supply the all-aspect-ratio box distribution, its pair thresholds, or the terminal coefficient. Coleman [2] computes secant-length laws for cubes and other shapes under four **different** random-line sampling mechanisms (random surface or interior point, invariant line, or two random interior endpoints); the full readable original distinguishes each mechanism from the fixed-center Haar law here. Coleman's later article [3] treats three random-probe sampling laws through boxes and is a plausible but not fully accessible comparator. A published result on the Haar probability of hexagonal **central plane** sections of rectangular boxes [4] concerns a different random section dimension and statistic. A published directional-width law of cubes [5] measures one-dimensional **projections**, not intersections. The complete central-chord quantile law of planar regular polygons [6] treats another ambient dimension and geometry. These distinctions compare random objects and mathematical implications, rather than merely different titles.

## Limitations

The asserted exact formula is specific to three-dimensional Euclidean boxes and the centered Haar-direction model; no claim is made for random offsets, nonorthogonal parallelepipeds, general convex bodies, or higher-dimensional joint-cap intersections. The face-diagonal singularity expansion concerns individual pair probabilities; at coincident thresholds the full CDF also contains other terms. The inaccessible full text of Coleman [3] leaves a residual historical-priority risk. The finite verifier cannot prove originality; no independent mathematical audit has been performed.

## References

[1] O. Guédon, A. E. Litvak, K. Tatarko, and B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, first posted 2026-09-21, https://arxiv.org/abs/2609.24131.

[2] R. Coleman, *Random paths through convex bodies*, Journal of Applied Probability 6 (1969), 430–441, DOI 10.1017/S0021900200032939. Readable full text: https://paperzz.com/doc/7321154/random-paths-through-convex-bodies-1.-introduction.

[3] R. Coleman, *Intercept lengths of random probes through boxes*, Journal of Applied Probability 18 (1981), 276–282, DOI 10.2307/3213189 (full text not accessed).

[4] *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, published mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.

[5] *Exact directional width law of the cube and its first spherical-cap transition*, published mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2.

[6] *Parity-resolved central-chord laws for regular polygons*, published mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parity-resolved-central-chord-laws-for-regular-polygons--de9bb055a653.
