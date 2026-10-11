# Optimal dangling-edge refinement and nonattainment of dual-edge product suprema

## Finding

Let \(X\subset\mathbb R^3\) be a finite extremal set of unit diameter: its \(m\ge4\) distinct points determine exactly \(2m-2\) pairs at distance one. The ball polyhedron of \(X\) has exposed dual circular-edge pairs. Write
\[
J_q(X)=\sum_{(e,e')\ \mathrm{dual}}q(e)q(e'),
\qquad q\in\{L,\theta\},
\]
where \(L(e)\) is the Euclidean endpoint distance and
\[
\theta(e)=2\arcsin(L(e)/2).
\]

Fix any exposed pair \((e,e')\). Put
\[
s=L(e)\in(0,1],\qquad
\rho=\sqrt{1-s^2/4}\in[\sqrt3/2,1),
\]
and let \(\varphi\in(0,\pi)\) be the central angle of the exposed minor circular arc \(e'\), lying on the intersection of the unit spheres centered at the two endpoints of \(e\). Define
\[
\begin{split}
c_L(s)&=s,&f_L(t)&=2\rho\sin(t/2),\\
c_\theta(s)&=2\arcsin(s/2),&f_\theta(t)&=2\arcsin(\rho\sin(t/2)).
\end{split}
\]

For every integer \(r\ge1\), add \(r-1\) distinct points in the relative interior of \(e'\), partitioning it into \(r\) consecutive nondegenerate arcs with angles
\[
t_1,\ldots,t_r>0,\qquad\sum_{i=1}^rt_i=\varphi.
\]
The enlarged configuration \(X_r\) remains extremal, and
\[
\boxed{J_q(X_r)-J_q(X)
=c_q(s)\left(\sum_{i=1}^rf_q(t_i)-f_q(\varphi)\right).}
\]
Among all such \(r\)-subdivisions, there is a **unique optimal central-angle partition**:
\[
\boxed{t_1=\cdots=t_r=\frac\varphi r.}
\]
Its exact gain is
\[
\boxed{\Delta^*_{q,r}
=c_q(s)\left(rf_q(\varphi/r)-f_q(\varphi)\right).}
\]
The quantity \(\Delta^*_{q,r}\) is strictly increasing in \(r\), and it is strictly positive for every \(r\ge2\).

The limiting gain and precise approach to it are
\[
\boxed{\Delta^*_{q,\infty}
=c_q(s)\left(\rho\varphi-f_q(\varphi)\right),}
\]
\[
\boxed{\begin{aligned}
\Delta^*_{L,\infty}-\Delta^*_{L,r}
&=\frac{s\rho\varphi^3}{24r^2}+O_{s,\varphi}(r^{-4}),\\
\Delta^*_{\theta,\infty}-\Delta^*_{\theta,r}
&=\frac{\theta(e)\rho(1-\rho^2)\varphi^3}{24r^2}
+O_{s,\varphi}(r^{-4}).
\end{aligned}}
\]
Both leading coefficients are strictly positive.

Consequently **neither product functional has a global finite extremal-set maximizer**:
\[
\boxed{\sup_{X\ \mathrm{finite\ extremal}}J_L(X)
\ \text{and}\ \sup_{X\ \mathrm{finite\ extremal}}J_\theta(X)
\text{ are finite but unattained}.}
\]
Thus the supremal formulation of the spherical dual-edge product, used in the constant-width area problem, cannot be replaced by a maximum over finite configurations.

## Assumptions and scope

The geometric data are those of a finite extremal unit-diameter set in \(\mathbb R^3\), with *exposed* dual circular edges of its unit-ball intersection. A prospective four-endpoint pattern with all cross distances one does not suffice unless the relevant arcs are exposed. The subdivision adds only points of the designated exposed arc, which lies in the original ball polyhedron. It is not an arbitrary modification of the diameter graph.

The angle \(\varphi\) is the angle subtended by the arc on its circle of radius \(\rho\), **not** the endpoint spherical distance \(\theta(e')\). The exposed arcs are minor: in the source's geometry one may take
\[
0<\varphi\le2\arcsin(1/\sqrt3)<\pi.
\]
For \(r=1\), no point is inserted and \(\Delta^*_{q,1}=0\). The \(O_{s,\varphi}(r^{-4})\) remainders hold for a fixed starting edge; no uniform error over degenerating configurations is claimed.

The theorem optimizes only the positions of newly inserted dangling points **on a fixed exposed arc** and fixes their number. It does not claim that these subdivisions maximize the product among all extremal sets with the same total number of vertices or a prescribed global diameter graph.

## Proof

**1. Exact subdivision identity and validity.** For one point in the relative interior of \(e'\), the dangling-insertion theorem for extremal ball polyhedra says that the new point has exactly the two endpoints of \(e\) as diameter neighbours; the point set stays of diameter one, and exactly two diameter pairs are added. The original dual-pair incidence is replaced by the two subarc incidences, both opposite the same geometric edge \(e\). The associated change of a product summand is the product of \(q(e)\) with the difference between the two new and one old subarc sizes. Repeating for successive subarcs proves extremality after \(r-1\) insertions and shows that all other product contributions remain unchanged.

The two unit spheres centered at the endpoints of \(e\), which are distance \(s\) apart, meet in a circle of radius
\[
\rho=\sqrt{1-s^2/4}.
\]
A subarc of central angle \(t\) has endpoint chord
\[
L=2\rho\sin(t/2)
\]
and endpoint spherical distance
\[
\theta=2\arcsin(\rho\sin(t/2)).
\]
Summing the changed contributions gives exactly
\[
J_q(X_r)-J_q(X)
=c_q(s)\left(\sum_{i=1}^rf_q(t_i)-f_q(\varphi)\right).
\]
The arcs are all on the same exposed minor circle, so no pair of inserted points can exceed unit distance: their central separations do not exceed that of the original endpoints, whose chord is at most one.

**2. Strict concavity and finite refinement optimum.** On \(0<t<\varphi<\pi\), direct differentiation gives
\[
f_L''(t)=-\frac\rho2\sin(t/2)<0,
\]
\[
f_\theta''(t)
=-\frac{\rho(1-\rho^2)\sin(t/2)}
{2(1-\rho^2\sin^2(t/2))^{3/2}}<0.
\]
Both functions are strictly concave and vanish at zero. Jensen's inequality therefore gives
\[
\sum_{i=1}^r f_q(t_i)
\le r f_q\!\left(\frac1r\sum_{i=1}^r t_i\right)
=r f_q(\varphi/r).
\]
For \(r\ge2\), strict concavity makes equality possible only if all \(t_i=\varphi/r\). This gives the stated unique optimum. Since \(f_q(t)/t\) is strictly decreasing in \(t>0\) whenever \(f_q\) is strictly concave and \(f_q(0)=0\),
\[
r f_q(\varphi/r)
=\varphi\frac{f_q(\varphi/r)}{\varphi/r}
\]
increases strictly with \(r\). In particular, relative to \(r=1\), every \(r\ge2\) gives a strictly positive gain.

**3. Limiting gain and sharp rate.** Taylor expansion at zero yields
\[
f_L(t)=\rho t-\frac{\rho t^3}{24}+O_{s}(t^5)
\]
and
\[
f_\theta(t)=\rho t
-\frac{\rho(1-\rho^2)t^3}{24}+O_s(t^5).
\]
Consequently
\[
r f_L(\varphi/r)
=\rho\varphi-\frac{\rho\varphi^3}{24r^2}
+O_{s,\varphi}(r^{-4})
\]
and
\[
r f_\theta(\varphi/r)
=\rho\varphi
-\frac{\rho(1-\rho^2)\varphi^3}{24r^2}
+O_{s,\varphi}(r^{-4}).
\]
Multiplying by the positive factor \(c_q(s)\) proves both sharp leading terms and the limit. Their coefficients are positive because \(s>0\) implies \(\rho<1\) and \(\varphi>0\).

**4. Global nonattainment.** Every finite extremal unit-diameter set has exposed dual edge pairs with positive lengths. Choose one and subdivide its dual arc at its midpoint. Step 2 gives a strictly larger value of either \(J_L\) or \(J_\theta\), while Step 1 keeps the new set in the class of finite extremal configurations. Hence no finite set can globally maximize either functional.

The global spherical-product supremum is finite by the source's constant-width area-deficit theorem (its Theorem 15), which bounds \(J_\theta\) from above. Since
\[
0\le L(e)\le\theta(e)
\]
for every edge, the Euclidean-product sum satisfies
\[
J_L(X)\le J_\theta(X).
\]
Therefore its global supremum is finite as well. This completes the proof.

## Verification

The standalone symbolic checker verifies the two strict-concavity derivative formulas and the cubic Taylor coefficients, which give the sharp inverse-square discretization errors. It also checks an explicit equal-angle split on a regular-tetrahedron dual arc, including strict improvement in both product channels. Those checks are supplementary: strict concavity, Jensen's inequality, and the geometric dangling-insertion theorem prove the statement for every finite extremal set and all integers \(r\ge1\).

The sample calculation is not used to infer global nonattainment. Nonattainment is a direct contradiction argument using an arbitrary exposed pair.

## Relationship to prior work

Bogosel's study of extremal diameter graphs defines both dual-edge product functionals and proves the exact change under one dangling insertion in Proposition 11. It establishes *nondecrease* under insertion, convergence of fine spherical subdivision sums to circular arc length, and the exact equality between the global spherical-product supremum and the unit-width surface-area-deficit supremum in Theorem 15. The source does not assert a strict gain for every nontrivial subdivision of either product, a unique optimal subdivision for a prescribed finite count, a sharp inverse-square error, or global nonattainment over finite extremal sets.

A related earlier preprint by the same author, *Dangling points in area-minimizing Meissner polyhedra*, studies changes in the **optimally smoothed surface area** under dangling-point deletion. Its curvature-circle formula uses the same arc coordinate, but its additivity/monotonicity results concern a different functional. They do not imply the two exact product-refinement optima or their nonattainment result.

The new statement pinpoints the distinction between maxima on a **fixed diameter graph** (a question separately considered in the literature) and the global **supremum over all finite extremal graphs**. It shows why arbitrary finite truncation and any fixed vertex-budget computation cannot attain that global supremum. It also supplies the optimal local placement and precise convergence order for the iterative subdivisions underlying the discrete approximation of the constant-width area problem.

## Limitations

No value for either global supremum is computed. In particular, the three-dimensional Blaschke--Lebesgue conjecture is neither proved nor disproved.

The unique subdivision optimum fixes the original configuration, one exposed dual arc, and the number of new points. It does not compare arbitrary graph changes or modifications of other edges.

The inverse-square coefficients depend on the initial edge length and arc angle; no uniform coefficient for all geometrically degenerating extremal configurations is asserted.

The conclusion that the spherical supremum is not attained among *finite extremal configurations* says nothing against attainment of the corresponding geometric area minimum by a general constant-width body.

## References

1. Beniamin Bogosel, *Isoperimetric problems related to extremal diameter graphs in 3D: theoretical and numerical aspects*, arXiv:2608.26395v1, first submitted 26 August 2026. In particular, Proposition 11, equations (3.3) and (3.8), and Theorem 15.
2. Beniamin Bogosel, *Dangling points in area-minimizing Meissner polyhedra*, arXiv:2608.19747v1, first submitted 20 August 2026, especially the circular-arc parametrization and Propositions 2.1--2.3.
