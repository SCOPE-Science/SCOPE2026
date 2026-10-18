# The universal endpoint-chord law for the Steiner inellipse of a triangle

## Finding

Let \(T\) be any nondegenerate Euclidean triangle, let \(E\) be its Steiner inellipse (the maximal-area inscribed ellipse tangent at the side midpoints), and let \(G\) be their common centroid. Let \(X,Y\) be independent points uniformly distributed by Euclidean arclength on \(\partial T\). For \(0\le s\le1\), write \(E_s=G+s(E-G)\), and let \(p_1,p_2,p_3\) be the three side lengths divided by the perimeter. Then
\[
\Pr([X,Y]\cap E_s\ne\varnothing)=\bigl(1-p_1^2-p_2^2-p_3^2\bigr)Q(s),
\]
where the universal function \(Q\) has the following exact closed form. For \(0<s<1\), define
\[
\eta(s)=\frac{\sqrt3\,s}{\sqrt{4-s^2}},\quad a(s)=\frac{1-\eta(s)}2,\quad b(s)=\frac{1+\eta(s)}2,\quad D(t)=t^2-t+1,
\]
\[
F(t)=\left(1-\frac1t\right)\sqrt{D(t)}+\frac12\left[\operatorname{arsinh}\!\left(\frac{2t-1}{\sqrt3}\right)-\operatorname{arsinh}\!\left(\frac{2/t-1}{\sqrt3}\right)\right].
\]
Then
\[
Q(s)=\frac{(8-s^2)(b-a)+(s^2-2)\log(b/a)+(1+s^2)(1/b-1/a)}9
-\frac{2s}{9}\bigl(F(a)+F(b)\bigr),
\]
with \(a=a(s),b=b(s)\). The endpoint values and sharp endpoint asymptotics are
\[
Q(0)=0,\qquad Q(1)=\frac23+\frac{2\log2}{9},
\]
\[
Q(s)=\frac29\bigl(\sqrt3+\log(2+\sqrt3)\bigr)s+O(s^3)\quad(s\downarrow0),
\]
\[
Q(1)-Q(s)=\frac{1-s}{3}\log\frac1{1-s}+O(1-s)\quad(s\uparrow1).
\]
For every fixed \(0<s\le1\), \(Q(s)>0\) and the probability is strictly Schur-concave as a function of the normalized side lengths. It has unique maximum \(2Q(s)/3\), attained by the equilateral triangle, and sharp unattained infimum \(Q(s)/2\), approached by nondegenerate triangles with normalized side lengths tending to a permutation of \((1/2,1/2,0)\). In particular, for the full Steiner inellipse the sharp probability range is
\[
\frac13+\frac{\log2}{9}<\Pr([X,Y]\cap E\ne\varnothing)\le \frac49+\frac{4\log2}{27}.
\]

## Assumptions and scope

The triangle is Euclidean and nondegenerate; side lengths and arclength are ordinary Euclidean quantities. The event uses the *segment* joining two independent boundary points, not a motion-invariant random line. The scale \(s\) is a homothety of the unique Steiner inellipse about the centroid, and \(E_0=\{G\}\). Formulae concern exact probabilities and do not assert that the Steiner inellipse maximizes intersection probability among all possible inscribed ellipses. This result does not apply unchanged to random points selected uniformly by area or to isotropic-uniform lines.

## Proof

**1. Affine reduction and the incidence test.** The Steiner inellipse is affinely natural, and conditioned on sampling two specified different sides, each sampling point is uniform in the affine coordinate along its chosen side. Relabel the two sides to meet at the origin and map the triangle affinely to the reference triangle \(\Delta=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\). The conditional points become \((u,0)\), \((0,v)\) with independent uniform \(u,v\in(0,1)\). The reference inellipse has center \(c=(1/3,1/3)\) and equation
\[
(x-1/3)^2+(y-1/3)^2+(x-1/3)(y-1/3)\le1/12.
\]
Its semidefinite shape matrix, defined through the support radius \(\sqrt{n^{\mathsf T}Bn}\), is
\[
B=\frac19\begin{pmatrix}1&-1/2\\-1/2&1\end{pmatrix}.
\]
The line through the sample points has equation \(x/u+y/v=1\). As \(E_s\subseteq\Delta\), this *line* meets \(E_s\) if and only if the *segment* meets \(E_s\). The support-function criterion becomes
\[
|1-(u^{-1}+v^{-1})/3|\le\frac{s}{3}\sqrt{u^{-2}+v^{-2}-(uv)^{-1}},
\]
which, upon multiplication by \(3uv\), is exactly
\[
(3uv-u-v)^2\le s^2(u^2+v^2-uv).\tag{1}
\]
There is no positive-probability contribution when both sampled points lie on the same original side, because \(E_s\) is disjoint from that side except for a single tangency at \(s=1\).

**2. Exact conditional law.** The event (1) is symmetric in \(u,v\). On its half-square \(0<u\le v<1\), put \(u=tv\), where \(0<t\le1\) and write \(z=v\). The Jacobian is \(z\), and (1) reduces to
\[
1+t-s\sqrt{D(t)}\le3tz\le1+t+s\sqrt{D(t)}.
\]
Consequently the allowed \(z\)-interval is \([z_-(t),z_+(t)]\cap[0,1]\), where
\[
z_\pm(t)=\frac{1+t\pm s\sqrt{D(t)}}{3t}.
\]
For \(0<s<1\) both endpoints are positive. Solving \(z_-(t)=1\) and \(z_+(t)=1\) gives exactly \(a(s)\) and \(b(s)\) above; the signs imply: no admissible \(z\) for \(t<a\); the interval \([z_-,1]\) for \(a\le t\le b\); and the interval \([z_-,z_+]\) for \(b\le t\le1\). Twice integrating the Jacobian \(z\) over these intervals gives
\[
Q(s)=\int_a^b\!\left[1-\frac{(1+t-s\sqrt{D(t)})^2}{9t^2}\right]dt
+\frac{4s}{9}\int_b^1\!\frac{(1+t)\sqrt{D(t)}}{t^2}dt.\tag{2}
\]
The identity \((1+t)D(t)=1+t^3\) yields
\[
F'(t)=\frac{(1+t)\sqrt{D(t)}}{t^2},\qquad F(1)=0.
\]
Expanding the first integral in (2) shows its polynomial/rational part has antiderivative
\[
\frac19\bigl[(8-s^2)t+(s^2-2)\log t+(1+s^2)/t\bigr],
\]
while its radical part contributes \(\frac{2s}{9}[F(b)-F(a)]\). The second integral contributes \(\frac{4s}{9}[F(1)-F(b)]\). Their sum is precisely the announced closed form.

**3. Endpoint formulae and cusp.** At \(s=0\), equality in (1) constrains \((u,v)\) to a curve and has planar measure zero. At \(s=1\), the left-minus-right side of (1) factors as \(3uv(3uv-2u-2v+1)\). For \(u\ge1/2\) every \(v\in(0,1)\) succeeds; for \(0<u<1/2\), success requires \(v\ge(1-2u)/(2-3u)\). Therefore
\[
Q(1)=1-\int_0^{1/2}\frac{1-2u}{2-3u}\,du=\frac23+\frac{2\log2}{9}.
\]
As \(s\downarrow0\), the roots satisfy \(a,b=1/2\mp\sqrt3\,s/4+O(s^3)\), and \(F(1/2)=-[\sqrt3+\log(2+\sqrt3)]/2\). The nonradical part in the closed form is \(O(s^3)\); the sum \(F(a)+F(b)=2F(1/2)+O(s^2)\). This proves the first expansion. As \(s\uparrow1\), write \(\delta=1-s\). Then \(a=2\delta/3+O(\delta^2)\), \(b=1-a\), and
\[
F(a)=-1/a+(\log a)/2+3/2-\log2+O(a),\qquad F(b)=O(a).
\]
Inserting into the exact closed form, the divergent \(1/a\) and constant \(\log a\) terms cancel, while the residual coefficient of \(\log a\) equals \((2-s^2-s)/9=\delta/3+O(\delta^2)\). Since \(\log a=\log\delta+O(1)\), the second expansion follows. Strict monotonicity and positivity for \(s>0\) follow from the strictly nested homothetic ellipses and a positive-area open family of intersecting chords between any two distinct levels.

**4. Side-length factorization and shape order.** For side-selection probabilities \(p_1,p_2,p_3\), the chance that the independently selected points lie on two different sides is \(1-\sum_i p_i^2\). Every ordered pair of different sides has the same conditional probability \(Q(s)\) by the affine reduction. This proves the factorization. Triangle inequalities give \(0<p_i<1/2\), \(\sum_i p_i=1\); thus \(1/3\le\sum_i p_i^2<1/2\). Equality in the lower bound occurs exactly for three equal sides, and the upper bound is approached only on the three degenerate boundary vertices \((1/2,1/2,0)\) and permutations. Strict Schur concavity follows from strict convexity of the sum of squares. This proves both sharp probability bounds.

## Verification

Run `python3 checker.py` with Python, NumPy, SciPy and SymPy. It verifies the ellipse support matrix, polynomial factorization, antiderivative, exact endpoint integral, the closed-form formula against independent adaptive quadrature at multiple scales, and low-discrepancy direct geometrical segment-vs-ellipse tests across nonsimilar triangles. These are finite reproducibility checks, not substitutes for the analytic quantifiers. The proof establishes all nondegenerate triangles and all real \(s\in[0,1]\).

## Relationship to prior work

The Steiner inellipse and its maximal-area property are classical. Steinerberger (2022) investigates a kinematic-random-line intersection multiplicity and quadratic Crofton energy; van der Jagt, Jongbloed and Vittorietti (2023) treat chord *length* distributions generated by isotropic-uniform random lines. Those sampling measures differ from independent arclength-uniform boundary endpoints. Yin and Chen (2023) study radial mean bodies of triangles and their relation to the John ellipsoid, not the endpoint-chord distribution in the accessible abstract. The formula here addresses the exact nested-Steiner-inellipse *hitting probability*, its universal separation of side lengths and affine geometry, and its logarithmic endpoint cusp; no result from those sources implies this specific closed form under the different probability law.

## Limitations

This does not optimize over arbitrary inellipses, does not claim a universal law for general convex polygons, and does not give random-line Crofton probabilities. The closed form has cancellation for \(s\) extremely close to \(1\); the integral (2) or high-precision arithmetic is preferable numerically there. A literature search cannot rule out unindexed prior equivalent computations. These are analytic findings with no independent mathematical audit.

## References

1. S. Steinerberger, *Quadratic Crofton and sets that see themselves as little as possible*, arXiv:2211.03259, first posted 2022-11-07, especially the kinematic line measure in Section 1.2; https://arxiv.org/abs/2211.03259.
2. T. van der Jagt, G. Jongbloed and M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, arXiv:2305.02864, first posted 2023-05-04, especially Definitions 1 and 2; https://arxiv.org/abs/2305.02864.
3. L. Yin and Y. Chen, *The radial mean bodies of triangles in the plane*, Journal of Shaanxi Normal University (Natural Science Edition) **51** (2023), 60–65, DOI:10.15983/j.cnki.jsnu.2023110, online 2023-05-06; https://doi.org/10.15983/j.cnki.jsnu.2023110.
4. *Steiner Inellipse*, Wolfram MathWorld, https://mathworld.wolfram.com/SteinerInellipse.html (classical definition, centroid, and side-midpoint tangencies).
