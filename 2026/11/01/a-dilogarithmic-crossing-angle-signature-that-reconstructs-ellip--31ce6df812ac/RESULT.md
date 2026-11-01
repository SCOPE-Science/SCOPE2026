# A dilogarithmic crossing-angle signature that reconstructs ellipses

## Finding

Fix a Euclidean ellipse with semiaxes \(a\ge b>0\). Independently sample four points from the boundary by the **uniform eccentric-anomaly law**: each sampled point has the form \((a\cos T,b\sin T)\) with independent \(T\sim\operatorname{Unif}[0,2\pi)\). Form two segments from the first pair and the second pair. Condition on the event \(E\) that the segments cross in their relative interiors. This event has probability \(1/3\) for every ellipse. Write \(\alpha\in[0,\pi/2]\) for the smaller Euclidean angle at the crossing, and define the dimensionless orthogonality statistic

\[
Q(a,b)=\mathbb E[\sin^2\alpha\mid E].
\]

Put \(r=a/b\ge1\) and \(x=((r-1)/(r+1))^2\in[0,1)\). The exact formula is

\[
\boxed{Q(a,b)=\frac{1-x}{2}+\frac{3}{2\pi^2}\frac{(1-x)^2}{x}\operatorname{Li}_2(x)},
\qquad
\operatorname{Li}_2(x)=\sum_{k=1}^{\infty}\frac{x^k}{k^2},
\]

where the expression at \(x=0\) means its continuous limit. In particular,

\[
Q(a,a)=\frac12+\frac{3}{2\pi^2}.
\]

The function of \(x\) displayed above is strictly decreasing, with the sharp derivative bound

\[
\frac{dQ}{dx}< -\frac12\quad(0\le x<1),\qquad
\lim_{x\uparrow1}\frac{dQ}{dx}=-\frac12.
\]

Consequently, **the single crossing-angle moment \(Q\) uniquely recovers the ellipse's axis ratio** (up to swapping axes), despite the crossing frequency being identically \(1/3\). Given observed population value \(q\in(0,\frac12+\frac{3}{2\pi^2}]\), solve the strictly monotone displayed equation for its unique \(x\in[0,1)\), then recover

\[
\boxed{\frac ab=\frac{1+\sqrt{x}}{1-\sqrt{x}}.}
\]

There is also sharp near-circular quadratic rigidity. As \(\eta=\log(a/b)\to0\),

\[
\boxed{Q(a,b)=\frac12+\frac{3}{2\pi^2}
-\left(\frac18+\frac{21}{32\pi^2}\right)\eta^2+O(\eta^4).}
\]

For slender ellipses, the order-\(r^{-2}\) term cancels and

\[
\boxed{Q(r)=\frac2r+\frac1{r^3}\left[6+\frac{96}{\pi^2}\left(\log\frac4r-1\right)\right]
+O\!\left(\frac{\log r}{r^4}\right)}\qquad(r\to\infty).
\]

The sharp inequalities and expansions concern the stated population statistic; there is no claim of a finite-sample confidence interval.

## Assumptions and scope

All four eccentric anomalies are independent and uniform; the sampling measure is the affine image of uniform angle on the unit circle, **not** Euclidean arclength measure on the ellipse. Segments are straight Euclidean chords, and the angle is the ordinary Euclidean intersection angle after the ellipse's affine stretching. No coincidence, tangency, or endpoint-crossing event contributes: these have probability zero. Ellipse translations, rotations, and common rescalings do not affect \(Q\). Uniform endpoints, rather than motion-invariant random lines, are essential to the formula.

We measure \(\sin^2\alpha\) rather than the angle itself because this quantity is invariant under interchanging the chords or selecting a supplementary angle and admits a clean determinant expression. It is a natural perpendicularity score: zero for parallel directions, one for perpendicular directions.

## Proof

### 1. Circular crossing gaps

Apply the inverse affine map \((X,Y)\mapsto(X/a,Y/b)\). Straight-line intersection is preserved, so two chords of the ellipse cross precisely when their corresponding four circle endpoints alternate. With four distinct endpoints there are three equally likely pairings and only one crossing pairing, establishing \(\mathbb P(E)=1/3\).

Condition on \(E\). Start at one distinguished endpoint of the first chord and traverse the circle counterclockwise. The other three labeled endpoints then appear in alternating order. The four successive circular gaps \((G_1,G_2,G_3,G_4)\), divided by \(2\pi\), have the \(\operatorname{Dirichlet}(1,1,1,1)\) distribution. This follows directly by conditioning three independent uniform angles on their circular order relative to the distinguished endpoint; conditioning the pairing does not alter the gap lengths.

The circle chord through angles \(u\) and \(v\) is parallel to
\[
(-\sin((u+v)/2),\cos((u+v)/2)).
\]
Thus the difference between the two unoriented chord directions may be taken as
\[
\Delta=(G_1+G_3)/2\in(0,\pi).
\]
The aggregation property of the Dirichlet law gives
\[
\frac{\Delta}{\pi}\sim\operatorname{Beta}(2,2),\qquad
f_\Delta(t)=\frac{6t(\pi-t)}{\pi^3},\quad 0<t<\pi.
\]
A common rotation of the four endpoints is uniform and independent of \(\Delta\). Hence, conditionally on \(\Delta=t\), the pair of chord directions can be written \(v_\theta=(\cos\theta,\sin\theta)\) and \(v_{\theta+t}\), where \(\theta\) is uniform modulo \(\pi\).

### 2. Integrating the affine distortion of crossing angles

Let \(A=\operatorname{diag}(a,b)\) and \(c=(a^2-b^2)/(a^2+b^2)\). The determinant formula for the angle between two nonzero vectors gives
\[
\sin^2\alpha=
\frac{a^2b^2\sin^2t}{\|Av_\theta\|^2\|Av_{\theta+t}\|^2}
=\frac{(1-c^2)\sin^2t}{(1+c\cos2\theta)(1+c\cos(2\theta+2t))}.
\]
Set \(w=(a-b)/(a+b)\), so \(c=2w/(1+w^2)\), and write \(x=w^2\). For \(0\le w<1\), the absolutely convergent Poisson expansion is
\[
\frac{1}{1+c\cos u}=
\frac{1+w^2}{1-w^2}
\left(1+2\sum_{j=1}^{\infty}(-w)^j\cos(ju)\right).
\]
Multiply the two expansions, integrate over uniform \(\theta\), and use \(1-c^2=((1-w^2)/(1+w^2))^2\). Orthogonality of Fourier modes yields
\[
\mathbb E_\theta[\sin^2\alpha\mid\Delta=t]
=\sin^2t\frac{1-x^2}{1-2x\cos(2t)+x^2}
=\sin^2t\left(1+2\sum_{j=1}^{\infty}x^j\cos(2jt)\right).
\]
The expansion remains valid at \(x=0\) by continuity.

### 3. Evaluating the beta-weighted Fourier series

Direct integration by parts twice yields, for each positive integer \(j\),
\[
I_j:=\int_0^\pi\frac{6t(\pi-t)}{\pi^3}\cos(2jt)\,dt
=-\frac{3}{\pi^2j^2},\qquad I_0=1.
\]
Using \(\sin^2t=(1-\cos2t)/2\) and the identity
\[
\cos(2t)\cos(2jt)=\tfrac12\bigl[\cos(2(j-1)t)+\cos(2(j+1)t)\bigr],
\]
absolute convergence permits termwise beta integration. The result is
\[
Q(x)=\frac12\left\{1-I_1+\sum_{j=1}^\infty x^j
\left[2I_j-I_{j-1}-I_{j+1}\right]\right\}.
\]
For \(0<x<1\), recognize \(\sum_{j\ge1}x^j/j^2=\operatorname{Li}_2(x)\), and use the two index shifts
\[
\sum_{j\ge1}x^jI_{j-1}=x-\frac{3x}{\pi^2}\operatorname{Li}_2(x),\qquad
\sum_{j\ge1}x^jI_{j+1}=-\frac3{\pi^2x}(\operatorname{Li}_2(x)-x).
\]
Substitution and simplification give exactly
\[
Q(x)=\frac{1-x}{2}+\frac3{2\pi^2}\frac{(1-x)^2}{x}\operatorname{Li}_2(x).
\]
The same identity at \(x=0\) follows from \(\operatorname{Li}_2(x)/x\to1\).

### 4. Global inverse rigidity

The power-series identity \(\int_0^1 t^j(-\log t)\,dt=(j+1)^{-2}\) shows
\[
H(x):=\frac{(1-x)^2}{x}\operatorname{Li}_2(x)
=(1-x)^2\int_0^1\frac{-\log t}{1-xt}\,dt.
\]
Differentiating under the integral for \(0\le x<1\) gives
\[
H'(x)=(1-x)\int_0^1\frac{(-\log t)[-2+(1+x)t]}{(1-xt)^2}\,dt<0.
\]
Indeed \(-\log t>0\) and \(-2+(1+x)t<0\) for \(0<t<1\) and \(0\le x<1\). Consequently \(Q'(x)=-1/2+(3/(2\pi^2))H'(x)<-1/2\). Since \(\operatorname{Li}_2(x)\to\pi^2/6\) and \(H'(x)\to0\) as \(x\uparrow1\), the derivative bound is sharp in the limiting sense. Also \(Q(0)=1/2+3/(2\pi^2)\) and \(Q(x)\to0\). The axis-ratio inversion now follows because \(x=((r-1)/(r+1))^2\) maps \([1,\infty)\) increasingly onto \([0,1)\).

### 5. Both endpoint regimes

Near the circle, \(\operatorname{Li}_2(x)=x+x^2/4+O(x^3)\) gives
\[
Q(x)=\frac12+\frac3{2\pi^2}-\left(\frac12+\frac{21}{8\pi^2}\right)x+O(x^2).
\]
Since \(x=\tanh^2((\log r)/2)=(\log r)^2/4+O((\log r)^4)\), this is the claimed quadratic rigidity.

For slender ellipses set \(s=1/r\) and \(\delta=1-x=4s/(1+s)^2\). The standard dilogarithm endpoint identity, obtained by integrating \(\operatorname{Li}_2'(z)=-\log(1-z)/z\), is
\[
\operatorname{Li}_2(1-\delta)=\frac{\pi^2}{6}+\delta\log\delta-\delta+O(\delta^2|\log\delta|).
\]
Substitute into \(Q=\delta/2+(3/(2\pi^2))\delta^2\operatorname{Li}_2(1-\delta)/(1-\delta)\) and expand \(\delta=4s-8s^2+12s^3+O(s^4)\). The coefficients of \(s^2\) cancel, leaving precisely the stated logarithmically corrected \(s^3\) term with remainder \(O(s^4|\log s|)\).

## Verification

A standalone standard-library Python program, `checker.py`, performs checks independent of the algebraic simplifications: beta-density Fourier integrals by quadrature, a separate one-dimensional beta–Poisson quadrature at eight aspect ratios, direct rejection sampling of the original four labeled endpoints (not merely simulated beta gaps), and numerical shape-order diagnostics. Run with `python3 checker.py` in the same directory as this file. Its deterministic seed and test tolerances are included in the code. It reports `ALL_CHECKS_PASSED` when successful. Analytical derivations in the preceding sections, not finite computations, establish the all-parameter conclusions.

## Relationship to prior work

Barahona Torres, Manrique-Mirón, and Treviño-Aguilar (2019), arXiv:1911.05576, study the intersection-angle density under a different model: one chord joins **two points uniform in the disk interior**, and the other is a horizontal chord with independently uniform height. Their sine law does not give the endpoint-uniform chord angular law used here and does not imply the ellipse inversion formula. Bortolotto and Ramos (2024), arXiv:2406.06771, investigate extremal probabilities for intersections of chords with arbitrary endpoint distributions on a circle; the primary outputs are crossing-location probabilities rather than angular moments. Bortolotto and Souza (2025), arXiv:2504.12866, give a full radial law of intersection points for endpoint-uniform circle chords; they explicitly derive the chord offset–orientation parametrization and an associated dilogarithm. Their radial marginal neither determines the conditional crossing-angle moment nor the present ellipse shape response. The common appearance of a dilogarithm is acknowledged, not presented as a new special function identity.

The claimed addition is the shape-injective, exact orthogonality moment of crossing **affinely sampled ellipse chords**, including the global derivative bound and two sharp degeneration regimes. The usual circle crossing probability \(1/3\), individual chord orientation uniformity, Dirichlet gap facts, and Poisson kernel are classical ingredients rather than novel standalone claims. Searches of closely related public literature and mathematical research records found no equivalent or stronger angular-shape formula; absence from searched records does not prove historical uniqueness.

## Limitations

The result is for uniform eccentric anomaly on ellipses and conditioned on interior intersections. Euclidean arclength-uniform endpoints, random line-sampling conventions, nonelliptical convex curves, and noisy finite-data inverse estimation are not covered. It determines axis ratio but cannot determine absolute size or orientation. The theorem gives a population identity and exact deterministic inversion, not a statistical estimator or sampling-error guarantee. Historical priority remains provisional pending wider specialist review. The analytical proof and the reproducibility program do not constitute independent certification.

## References

1. J. I. H. Barahona Torres, P. C. Manrique-Mirón, and E. Treviño-Aguilar, *Angle distribution of two random chords in the disc: A sine law*, arXiv:1911.05576, publicly posted 2019-11-13. https://arxiv.org/abs/1911.05576
2. C. Bortolotto and J. P. G. Ramos, *On Extremal Problems Associated with Random Chords on a Circle*, arXiv:2406.06771, publicly posted 2024-06-10. https://arxiv.org/abs/2406.06771
3. C. Bortolotto and V. Souza, *Intersections of Random Chords of a Circle*, arXiv:2504.12866, publicly posted 2025-04-17. https://arxiv.org/abs/2504.12866
