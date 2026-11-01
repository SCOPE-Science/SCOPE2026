# Fifth-order small-chord law and a sharp curvature-frequency transition for convex plane curves

## Finding

Let \(\Gamma\subset\mathbb R^2\) be any embedded \(C^8\) strictly convex closed curve, parametrized counterclockwise by arclength \(s\in\mathbb R/L\mathbb Z\), of perimeter \(L>0\) and positive curvature \(\kappa(s)\). For independent points \(X,Y\) sampled from normalized arclength on \(\Gamma\), set \(F(t)=\Pr(\|X-Y\|\le t)\). As \(t\downarrow0\),

\[
F(t)=\frac{2t}{L}+\frac{t^3}{12L^2}\int_0^L\kappa(s)^2\,ds
+\frac{t^5}{L^2}\left(\frac3{320}\int_0^L\kappa(s)^4\,ds-\frac1{360}\int_0^L\kappa'(s)^2\,ds\right)+O_\Gamma(t^7).
\]

The cubic coefficient is minimized exactly by the circle at fixed perimeter:
\[
\frac1{12L^2}\int_0^L\kappa^2\,ds\ge\frac{\pi^2}{3L^3},
\]
with equality only at constant curvature.

More surprisingly, write \(\rho=2\pi/L\). For each integer \(n\ge2\) and \(0<a<1\), there exists a closed smooth strictly convex curve with curvature \(\kappa_{n,a}(s)=\rho(1+a\cos(n\rho s))\). Its fifth-order coefficient is
\[
c_5(n,a)=\frac{\rho^4}{L}\left[\frac3{320}\left(1+3a^2+\frac{3a^4}{8}\right)-\frac{n^2a^2}{720}\right].
\]
Relative to the circle of the same perimeter, \(c_5(n,a)>c_5(\mathrm{circle})\) **exactly for** \(n=2,3,4\), and \(c_5(n,a)<c_5(\mathrm{circle})\) **exactly for** \(n\ge5\), throughout \(0<a<1\). At any fixed \(L\) and \(a\in(0,1)\), \(c_5(n,a)\to-\infty\) as \(n\to\infty\). Hence the fifth-order coefficient has no global lower bound over smooth strictly convex curves of fixed perimeter; unlike its cubic predecessor, it is sensitive to high-frequency curvature gradients.

## Assumptions and scope

All distances are ambient Euclidean straight-line distances; they are not intrinsic arclength distances or motion-invariant random-line chords. Both points are independent and uniform **on the curve** (not in the enclosed body). Curvature is positive with the counterclockwise orientation, derivatives are in arclength, and \(O_\Gamma(t^7)\) has a constant depending on the fixed curve. The fifth-order coefficient is the limit
\[
c_5(\Gamma)=\lim_{t\downarrow0}\frac{F(t)-2t/L-c_3(\Gamma)t^3}{t^5},\qquad c_3(\Gamma)=\frac1{12L^2}\int_0^L\kappa^2\,ds.
\]
The asserted unboundedness varies the curve with \(n\), taking the small-\(t\) limit separately for each fixed curve; it makes no uniform error estimate as \(n\to\infty\).

## Proof

**Step 1 (localization and midpoint coordinates).** Since \(\Gamma\) is compact and embedded, for any sufficiently small positive threshold \(t\), the pairs satisfying \(\|\gamma(s')-\gamma(s)\|\le t\) have \(s'-s\) modulo \(L\) near zero. Put \(u=(s+s')/2\) and \(h=s'-s\) on this local neighborhood of the diagonal. The Jacobian of \((u,h)\mapsto(s,s')\) has absolute value one. For each \(u\) there is a unique positive local solution \(H(u,t)\) to
\[
\|\gamma(u+H/2)-\gamma(u-H/2)\|=t
\]
for small enough \(t\), smoothly and uniformly in \(u\). The allowable signed \(h\) interval is \((-H,H)\), hence
\[
F(t)=\frac{2}{L^2}\int_0^L H(u,t)\,du.
\]

**Step 2 (exact local chord Taylor coefficients).** Let \(T=\gamma'\) and \(N\) be the left normal. The Frenet relations \(T'=\kappa N\) and \(N'=-\kappa T\) give
\[
\gamma'''=-\kappa^2T+\kappa'N,
\qquad
T\cdot\gamma^{(5)}=\kappa^4-4\kappa\kappa''-3(\kappa')^2.
\]
Taylor expansion of the symmetric midpoint chord gives
\[
\Delta(u,h)=\gamma(u+h/2)-\gamma(u-h/2)
=hT+\frac{h^3}{24}\gamma'''+\frac{h^5}{1920}\gamma^{(5)}+O_\Gamma(h^7).
\]
Squaring, then taking a positive square root, yields
\[
\|\Delta(u,h)\|=h-\frac{\kappa^2}{24}h^3+
\left(\frac{\kappa^4}{1920}-\frac{\kappa\kappa''}{480}-\frac{(\kappa')^2}{1440}\right)h^5+O_\Gamma(h^7),\qquad h>0.
\]
All functions of curvature in this step are evaluated at \(u\), and the error is uniform on the compact parameter circle. Reversion of the series \(t=\|\Delta(u,H)\|\) gives
\[
H(u,t)=t+\frac{\kappa^2}{24}t^3+
\left(\frac{3\kappa^4}{640}+\frac{(\kappa')^2}{1440}+\frac{\kappa\kappa''}{480}\right)t^5+O_\Gamma(t^7).
\]
Integrating and using periodic integration by parts,
\(\int_0^L\kappa\kappa''\,du=-\int_0^L(\kappa')^2\,du\), proves the displayed expansion. No finite sampling or truncated enumeration enters this argument.

**Step 3 (strict cubic circle extremum).** The turning-angle theorem for a simple positively oriented strictly convex closed curve gives \(\int_0^L\kappa\,ds=2\pi\). Cauchy–Schwarz gives \(\int\kappa^2\ge(2\pi)^2/L\), with equality precisely for constant positive curvature, hence a circle.

**Step 4 (closed, strictly convex harmonic family).** Fix an integer \(n\ge2\), \(0<a<1\) and define the tangent angle
\[
\vartheta(s)=\rho s+\frac a n\sin(n\rho s),\qquad
T(s)=(\cos\vartheta(s),\sin\vartheta(s)).
\]
Integrate \(T\) to form \(\gamma_{n,a}(s)=\int_0^s T(v)\,dv\). Because \(T(s+L/n)\) is the rotation by \(2\pi/n\) of \(T(s)\), the total displacement over \(n\) equal subintervals vanishes as a sum of \(n\)-th roots of unity. Thus \(\gamma_{n,a}(L)=\gamma_{n,a}(0)\). Moreover \(\vartheta'(s)=\rho(1+a\cos(n\rho s))>0\) and \(\vartheta(L)-\vartheta(0)=2\pi\), so the closed unit-speed curve is smooth, embedded, and strictly convex (the positive-curvature turning-angle characterization).

Straight trigonometric averaging gives
\[
\frac1L\int_0^L\kappa_{n,a}^4ds
=\rho^4\left(1+3a^2+\frac{3a^4}{8}\right),\qquad
\frac1L\int_0^L(\kappa_{n,a}')^2ds=\frac12\rho^4n^2a^2.
\]
It follows that
\[
c_5(n,a)-c_5(\mathrm{circle})
=\frac{\rho^4a^2}{L}\left(\frac9{320}-\frac{n^2}{720}+\frac{9a^2}{2560}\right).
\]
The bracket strictly decreases with integer \(n\). For \(n=4\) its value at \(a=0\) is \(17/2880>0\); for \(n=5\) its value at \(a=1\) is \(-71/23040<0\). Thus precisely \(n\le4\) (within \(n\ge2\)) increase the fifth coefficient and all \(n\ge5\) decrease it, for every \(0<a<1\). The term \(-n^2a^2/720\) proves unboundedness below.

## Verification

Run `python verify_curve_tail.py` with Python 3, SymPy, NumPy and SciPy. The program differentiates Frenet frame identities exactly, checks the midpoint-chord expansion and its formal inverse, validates the circle via the independent exact arcsine CDF, and evaluates the Fourier-mode identities symbolically. As additional checks, it numerically integrates the actual parametric chord length for four distinct Fourier frequencies and two small thresholds each, solving the inverse-radius equation. The expected program conclusion is:

`VERIFY_OK Frenet_series=6 inverse_series=1 exact_fourier=2 circle=1 numerical_cases=8`

The full proof is analytic; finite numerical checks are not an infinite proof and do not establish a uniform error bound as the curve varies.

## Relationship to prior work

The Grassberger–Procaccia correlation integral is exactly a pair-proximity statistic of the type \(F(t)\). Hein and Audibert [1] analyze the leading and second-order (curvature-dependent) small-scale correction for kernel-weighted proximity on smooth embedded manifolds. Their Proposition 1 provides a term of order \(h^2\) after dividing by the manifold dimension factor and a remainder of order \(h^3\); it does not specify the present \(t^5\) coefficient, the negative curvature-gradient energy, or the Fourier-frequency transition. Their result gives important prior conceptual coverage of the *cubic* curvature correction, so that term is not separately claimed as novel here.

Bäsel [2] derives random-line chord laws and interior point-distance laws for regular polygons, not independent uniform **boundary** pairs on smooth strictly convex curves. The circle chord law [3] supplies an exact benchmark recovered by this expansion, not a novel special case. Lellouche and Souris [4] review forward random-distance calculations for compact sets and homogeneous spatial sampling, but do not present the fifth-order curve-boundary expansion. Published geometric research [5] treats the near-zero boundary-pair law for polygons, with angle rather than smooth-curvature behavior. The distinction in the present claim is the explicit fifth-order smooth-curve invariant and its non-monotone high-frequency behavior.

## Limitations

No independent novelty audit has been performed. Although the most relevant inspected sources did not state an equivalent fifth-order formula, older distance-correlation integral literature or classical tube/kernel-expansion theory could potentially contain equivalent curvature-derivative terms under different notation. The claim is restricted to embedded positively curved smooth closed planar curves and exact population sampling; it asserts neither finite-sample estimation rates nor global reconstruction of the full curve from \(F\). The \(O_\Gamma(t^7)\) remainder depends on the fixed curve and must not be uniformized over unbounded harmonic frequencies.

## References

[1] M. Hein and J.-Y. Audibert, “Intrinsic Dimensionality Estimation of Submanifolds in \(\mathbb R^d\),” *ICML* (2005), DOI `10.1145/1102351.1102388`. Original published paper text, especially Lemma 1 and Proposition 1, inspected; publicly indexed listing dated 2009-11-17: https://www.sciweavers.org/publications/intrinsic-dimensionality-estimation-submanifolds-rd .

[2] U. Bäsel, “Random chords and point distances in regular polygons,” arXiv `1204.2707`, first posted 2012-04-12, https://arxiv.org/abs/1204.2707 .

[3] E. W. Weisstein, “Circle Line Picking,” *MathWorld*, https://mathworld.wolfram.com/CircleLinePicking.html .

[4] S. Lellouche and M. Souris, “Distribution of Distances between Elements in a Compact Set,” *Stats* 3 (2019), 1–15, DOI `10.3390/stats3010001`, https://doi.org/10.3390/stats3010001 .

[5] “Sharp uniform angular stability for the short-pair distance coefficient of convex polygons,” publicly indexed geometric research, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b .
