# Unbounded analytic turning multiplicity alongside an attracting equilibrium and chaos

## Finding

Fix \(a=13/4\), \(b=61/100\), \(c=4167/10000\), and
\[ W(x)=\frac1x+\frac1{1-x}-c\left(\frac1{(11/10-x)^2}+\frac1{(x+1/10)^2}\right). \]
For each positive integer \(L\), put \(m=100L\) and define the strictly increasing analytic potential \(P_L:(0,1)\to\mathbb R\) by \(P_L(1/2)=0\) and
\[P_L'(x)=W(x)\left[1+\frac{99}{100}\cos(2\pi m x)\right].\]
Let \(F_L(x)=P_L^{-1}(P_L(x)-a(x-b))\) on \((0,1)\), continuously extended by \(F_L(0)=0\), \(F_L(1)=1\). Then for every \(L\ge3\), \(F_L\) is real analytic on \((0,1)\), has exactly one interior fixed point \(b\) which is attracting, and has at least \(2L-4\) distinct strict local turning points in \((0,1)\). For all sufficiently large integers \(L\), \(F_L\) additionally has positive topological entropy (indeed a period-six or period-three orbit), simultaneously with the attracting fixed point. Every finite interior periodic orbit of every \(F_L\) has arithmetic mean exactly \(b\). All parameters \(a,b\) and the oscillation amplitude remain fixed as the turning-point count tends to infinity. No uniform explicit cutoff in \(L\) for the entropy conclusion is asserted.

## Assumptions and scope

Write \(a=13/4\), \(b=61/100\), \(c=4167/10000\), \(m=100L\), \(\epsilon=99/100\), with integer \(L\ge3\). The potential \(P_L\) is defined only up to an additive constant; we fix \(P_L(1/2)=0\). The map is analytic on the open interval; continuity, rather than analyticity, at the endpoints is asserted. A *strict local turning point* is a critical point across which the derivative changes sign. The entropy and non-power-of-two-period assertions hold for all sufficiently large \(L\), not necessarily every \(L\ge3\).

## Proof

**Convex potentials and interval self-maps.** Let \(u=x(1-x)\). Algebra gives
\[
W(x)=\frac{(916700u^2-144187u+6050)}{500000u(u+11/100)^2}.
\]
The quadratic written in the following sentence has positive leading coefficient and discriminant \(-1394249031/250000000000\), hence \(W(x)>0\) for all \(0<x<1\). Equivalently, the quadratic \((9167/5000)u^2-(144187/500000)u+121/10000\) has that negative discriminant. Also \(W(x)\sim1/x\) at zero and \(W(x)\sim1/(1-x)\) at one. Since \(1-\epsilon>0\), each \(P_L\) increases bijectively from \(-\infty\) to \(+\infty\), and is real analytic. Its inverse is analytic. The formula defining \(F_L\) consequently defines an analytic interior self-map and extends continuously by the endpoints. Furthermore \(F_L(x)>x\) for \(x<b\) and \(F_L(x)<x\) for \(x>b\), so \(b\) is the unique interior fixed point.

**Fixed-point attraction.** Because \(m b=61L\) is integral, \(P_L'(b)=(199/100)W(b)\). The exact rational value \(W(b)=47259683494/28794086139\) gives \(P_L'(b)>a\). By implicit differentiation,
\[F_L'(x)=\frac{P_L'(x)-a}{P_L'(F_L(x))},\qquad F_L'(b)=1-\frac a{P_L'(b)}\in(0,1).\]
Thus the equilibrium is locally attracting for all \(L\).

**Unbounded modality.** Let \(J=[121/200,123/200]\). On \(J\), direct differentiation and rational interval bounds yield
\[
W'(x)\le -\frac1{(123/200)^2}+\frac1{(77/200)^2}-\frac{2c}{(99/200)^3}+\frac{2c}{(141/200)^3}<0.
\]
In particular \(W(x)\ge W(123/200)=271156663016/165660395901\), so
\[
\frac{199}{100}W(x)-a\ge\frac{120547272359}{16566039590100}>0\quad(x\in J).
\]
On the other hand \(W(x)<1/x+1/(1-x)<5\) throughout \(J\), hence \(W(x)/100-a<0\). At the points \(x=k/m\) in \(J\), \(P_L'(x)-a>0\), while at \(x=(k+1/2)/m\) in \(J\), \(P_L'(x)-a<0\). These alternate through at least \(L-2\) complete oscillation blocks of \(J\), giving at least \(2L-4\) separate sign-changing zeros. As the denominator of \(F_L'\) is everywhere positive, each zero is a strict turning point of \(F_L\).

**Uniform convergence despite nonconvergent derivatives.** Let \(P_0'(x)=W(x)\), \(P_0(1/2)=0\), and let \(F_0=P_0^{-1}(P_0(x)-a(x-b))\). On every compact subinterval of \((0,1)\), integration by parts gives
\[P_L(x)-P_0(x)=\epsilon\int_{1/2}^x W(t)\cos(2\pi m t)\,dt=O(m^{-1}).\]
Strict monotonicity and the derivative lower bound \(P_L'\ge(1-\epsilon)W\) therefore give local-uniform convergence \(F_L\to F_0\). This convergence extends uniformly to \([0,1]\): for any \(\eta\in(0,b)\), choose \(\delta<\eta\) such that \((1-\epsilon)\int_\delta^\eta W(t)\,dt>ab\). If \(x\le\delta\) then \(F_L(x)<\eta\) for every \(L\), since otherwise \(P_L(F_L(x))-P_L(x)=a(b-x)\le ab\) would contradict that integral bound. The analogous argument near one uses \(a(1-b)\). It follows that \(F_L^{k}\to F_0^{k}\) uniformly for each fixed positive integer \(k\).

**Preserving a robust period obstruction.** The published six-step interval certificate for \(F_0\), with \(a=3.25\) and \(b=0.61\), gives for \(I=[0.9559,0.956]\):
\[F_0^2(I)\subset[0.990,0.991],\qquad F_0^6(I)\subset[0.65,0.80].\]
These enclosures have strict margins from \(I\), so uniform convergence of the second and sixth iterates implies for all sufficiently large \(L\) that \(F_L^6(x)<x<F_L^2(x)\) for every \(x\in I\). The standard period-three criterion applied to \(F_L^2\) yields a point of least period three under \(F_L^2\). Its least period under \(F_L\) is therefore either three or six, neither a power of two. The interval-map period/entropy theorem then gives \(h_\mathrm{top}(F_L)>0\), while \(b\) remains an attractor.

**Exact periodic centroid.** For any interior orbit \(x_0,\ldots,x_{n-1}\) of period \(n\), the defining equation gives \(P_L(x_{j+1})-P_L(x_j)=-a(x_j-b)\). Summing around the cycle yields \(\sum_{j=0}^{n-1}x_j=nb\). This identity holds for every \(L\), with no assumptions on the orbit's stability.

## Verification

The rational discriminant, derivative comparison, and endpoint values in the proof were independently evaluated with exact arithmetic. Numerical high-precision substitution in the unperturbed map, via monotone inverse bisection, gave \(F_0^2(0.9559)\approx0.990634218650167\), \(F_0^6(0.9559)\approx0.725939389868557\), \(F_0^2(0.956)\approx0.990634061365128\), and \(F_0^6(0.956)\approx0.725947568874807\); finite samples do not certify an interval enclosure. The needed full-interval bounds were inspected in the original published supplementary proof (proof of Proposition 6.4, figure and interval iterations, page 4). All nonfinite conclusions are proved by positivity, oscillatory integration, uniform convergence and the period-three criterion, not numerical extrapolation.

## Relationship to prior work

Bielawski and collaborators proved the existence of a *single* analytic regularizer with coexistence of an attracting Nash equilibrium and positive entropy, at the specific parameters used here. Their supplementary proof supplies the strict two-/six-step interval certificate used above. They also established periodic-orbit averaging to the equilibrium for the whole underlying learning family; that averaging identity is included here as context, not as a new discovery. The new statement is the simultaneously preserved attractor, positive entropy, and **unbounded strict turning-point multiplicity at fixed parameters** within explicit symmetric, steep, strictly convex analytic potentials. The high-frequency curvature construction converges in \(C^0\) but not \(C^1\), so the conclusion does not follow merely from perturbative structural stability. The earlier multiplicative-weights paper supplies related periodic-centroid context. No claim is made about topological conjugacy, metric basins of the chaotic set, the exact number of turning points, or robust chaos for every \(L\).

## Limitations

The integer cutoff after which the positive-entropy assertion holds is not quantified. The exact number of critical points, entropy values, and global basin geometry are not determined. A strictly positive entropy value does not imply a positive-measure chaotic attractor. Although focused literature and research-index comparisons found no covering statement, independent publication-priority certification has not been performed.

## References

1. J. Bielawski, T. Chotibut, F. Falniowski, G. Kosiorowski, M. Misiurewicz, G. Piliouras, *Follow-the-Regularized-Leader Routes to Chaos in Routing Games*, arXiv:2102.07974 (first public version 2021-02-16), PMLR 139 (2021), 925–935, especially Proposition 6.4 and its supplementary proof, https://proceedings.mlr.press/v139/bielawski21a.html ; https://proceedings.mlr.press/v139/bielawski21a/bielawski21a-supp.pdf.
2. T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Family of Chaotic Maps from Game Theory*, arXiv:1807.06831 (2018), periodic-orbit mean property and related interval dynamics.
3. T.-Y. Li, M. Misiurewicz, G. Pianigiani, J. A. Yorke, *No division implies chaos*, Trans. Amer. Math. Soc. 273 (1982), 191–199; period-three criterion used in reference 1.
