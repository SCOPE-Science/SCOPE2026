# A sharp small-scale spindle-absorption law and Euclidean-ball rigidity

## Finding
Let \(d\ge 2\) and let \(K\subset\mathbb R^d\) be a centrally symmetric convex body with center at the origin, positive volume \(V\), and radial function \(\rho_K:S^{d-1}\to(0,\infty)\). Independently sample \(X_\varepsilon,Y_\varepsilon\) uniformly in \(\varepsilon K\). Define their *unit-ball spindle* \([X_\varepsilon,Y_\varepsilon]_1\) to be the intersection of every closed Euclidean unit ball containing both sampled points. Put
\[
P_\varepsilon(K)=\Pr\bigl(0\in[X_\varepsilon,Y_\varepsilon]_1\bigr).
\]
For all sufficiently small \(\varepsilon>0\), these balls exist, and the following precise rare-event limit holds:
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{1-d}P_\varepsilon(K)
=\frac{\kappa_{d-1}J_d}{2^{d-1}V^2}
\int_{S^{d-1}}\rho_K(u)^{3d-1}\,d\sigma(u),}
\qquad
J_d=\sum_{j=0}^{d-1}\frac{\binom{d-1}{j}}{(d+j)(2d-1-j)}.
\]
Here \(\kappa_j=\pi^{j/2}/\Gamma(j/2+1)\) is the unit \(j\)-ball volume and \(\sigma\) is unnormalized spherical area.

Let \(B_R\) be the origin-centered Euclidean ball of the same volume, where \(R=(V/\kappa_d)^{1/d}\). The limiting comparison is exactly
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{P_\varepsilon(K)}{P_\varepsilon(B_R)}
=\frac{1}{d\kappa_d}\int_{S^{d-1}}
\left(\frac{\rho_K(u)}R\right)^{3d-1}\,d\sigma(u)\ge1.}
\]
Equality holds precisely when \(K=B_R\). More quantitatively, put \(M(u)=(\rho_K(u)/R)^d\) and write \(\mathbb E_\sigma\) for averaging over the unit sphere. Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{P_\varepsilon(K)}{P_\varepsilon(B_R)}-1
\ge \left(2-\frac1d\right)\mathbb E_\sigma[(M-1)^2].}
\]
The leading constant is unbounded above among origin-symmetric convex bodies of fixed positive volume. For Euclidean balls, the coefficient is explicitly \(2R/(3\pi)\) in dimension two and \(93R^2/640\) in dimension three.

## Assumptions and scope
The assertion holds for every integer \(d\ge2\) and every compact convex body \(K=-K\) with nonempty interior. No smoothness or strict convexity is assumed; in particular, symmetric polytopes are included. The sampling distribution is Lebesgue-uniform on \(\varepsilon K\), the ambient norm and the balls defining the spindle are Euclidean, and the two samples are independent. The parameter \(\varepsilon\) is a dimensionless homothety factor; take it sufficiently small that \(\varepsilon K\subset B_1\). The center of symmetry must coincide with the queried point \(0\). This result concerns fixed sample count two and the small-body limit, not increasing sample count.

## Proof
**1. Exact angular membership criterion.** For nonzero vectors \(x=r u\), \(y=s v\) with \(0<r,s<1\) and \(u,v\in S^{d-1}\), all centers of unit balls containing \(x,y\) form \(B(x,1)\cap B(y,1)\). Therefore the origin lies in the spindle if and only if this set of centers is contained in \(B(0,1)\). If \(tw\), where \(t>1\) and \(\|w\|=1\), is a center satisfying \(\|tw-x\|\le1\), then
\[
w\cdot u\ge \frac{t^2+r^2-1}{2tr}>\frac r2.
\]
The strict inequality follows because the function on the right increases for \(t\ge1\), provided \(r<1\). The same implication holds with \(y\). Conversely, if there exists \(w\in S^{d-1}\) satisfying both strict inequalities \(w\cdot u>r/2\) and \(w\cdot v>s/2\), then \(w\) is in the interiors of both center balls, so \(tw\) lies in their intersection for some \(t>1\). Thus nonmembership of the origin is equivalent to the overlap of two open spherical caps with angular radii \(\arccos(r/2)\) and \(\arccos(s/2)\), centered at \(u,v\). The caps overlap exactly when their center distance is less than the sum of their angular radii. We obtain the exact criterion
\[
\boxed{0\in[x,y]_1\quad\Longleftrightarrow\quad
\operatorname{dist}_{S^{d-1}}(u,-v)
\le\arcsin(r/2)+\arcsin(s/2).}
\]
The equality case belongs to the spindle because open caps then fail to intersect. Sampling at the origin has probability zero.

**2. Rescale the event.** Write \(X_\varepsilon=\varepsilon X\) and \(Y_\varepsilon=\varepsilon Y\), where \(X,Y\) are independent and uniform on \(K\). In polar coordinates \(X=t u\) and \(Y=s v\), their joint volume element is \(t^{d-1}s^{d-1}\,dt\,ds\,d\sigma(u)\,d\sigma(v)/V^2\), with \(0<t<\rho_K(u)\), \(0<s<\rho_K(v)\). The criterion from step 1 confines \(v\) to a spherical cap of angular radius \(O_K(\varepsilon)\) about \(-u\). In normal coordinates \(v=\exp_{-u}(\varepsilon z)\), with \(z\in T_{-u}S^{d-1}\), spherical area becomes \(\varepsilon^{d-1}(1+o(1))\,dz\), uniformly for bounded \(z\). Moreover
\[
\frac{\arcsin(\varepsilon t/2)+\arcsin(\varepsilon s/2)}{\varepsilon}
\longrightarrow\frac{t+s}{2}.
\]
Since the radial function of a convex body containing the origin is continuous, \(\rho_K(v)\to\rho_K(-u)=\rho_K(u)\). All coordinates \(t,s,z\) stay in fixed bounded sets; dominated convergence applies, including at polytope directions. The tangential \(z\)-ball has volume \(\kappa_{d-1}((t+s)/2)^{d-1}\). Consequently
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{1-d}P_\varepsilon(K)
=\frac{\kappa_{d-1}}{2^{d-1}V^2}
\int_{S^{d-1}}\int_0^{\rho_K(u)}\int_0^{\rho_K(u)}
 t^{d-1}s^{d-1}(t+s)^{d-1}\,ds\,dt\,d\sigma(u).
\]
Scaling \(t,s\) by \(\rho_K(u)\) produces the power \(3d-1\). Binomial expansion of \((t+s)^{d-1}\) over the unit square gives exactly the stated finite sum \(J_d\).

**3. Sharp ball comparison and quantitative rigidity.** The polar volume identity yields \(V=d^{-1}\int\rho_K^d\,d\sigma\). Thus \(\mathbb E_\sigma M=1\). The ratio of the limiting constants for \(K\) and the equal-volume ball equals \(\mathbb E_\sigma M^q\), where \(q=(3d-1)/d=3-1/d>2\). Strict Jensen convexity gives \(\mathbb E_\sigma M^q\ge1\), with equality only when \(M=1\) almost everywhere. Continuity of \(\rho_K\) then gives \(K=B_R\). For the quantitative claim, convexity of the function \(t\mapsto t^{q-1}\) gives \(t^{q-1}\ge1+(q-1)(t-1)\) for \(t\ge0\). Multiplying by \(t\), averaging, and using \(\mathbb E_\sigma M=1\) yields
\[
\mathbb E_\sigma M^q-1\ge(q-1)(\mathbb E_\sigma M^2-1)
=\left(2-\frac1d\right)\mathbb E_\sigma(M-1)^2.
\]

**4. No shape-independent upper bound.** Fix volume \(2^d\) and let \(K_a=[-a,a]\times[-b,b]^{d-1}\) with \(b=a^{-1/(d-1)}\), as \(a\to\infty\). The spherical cap where all transverse coordinates obey \(|u_j|\le b/(2a)\) has area bounded below by a positive dimension-dependent constant times \((b/a)^{d-1}=a^{-d}\). On that cap \(\rho_{K_a}(u)\ge a\). The radial integral is therefore at least a constant times \(a^{(3d-1)-d}=a^{2d-1}\), while \(V\) is fixed. This proves divergence of the leading constant.

## Verification
The included `verify_standalone.py` runs with the Python standard library. It checks the exact rational values \(J_2=1/3\), \(J_3=31/120\), \(J_4=19/70\); the closed-form small-radius disk probability from the reference; independent three-dimensional radial quadrature; the strict equal-area ellipse comparison and variance bound; and independent point-pair Monte Carlo for disks and a noncircular ellipse. It reports `ALL_CHECKS_PASSED`. These numerical checks corroborate formulas only; the proof above covers all dimensions and all permitted bodies. In particular, testing finitely many shapes does not establish the minimization theorem, which instead follows from the exact limit and Jensen's inequality.

## Relationship to prior work
Fodor, Montenegro Pinzón and Vígh (2022) introduced the directly related two-point Euclidean spindle absorption probability, including an exact triple integral for uniform samples from a ball and a statement that this probability tends to zero with the ball radius. Their results supply the motivating probabilistic model and the relevant angular geometry. The present finding instead evaluates the sharp leading coefficient for every origin-symmetric convex body, identifies its radial moment, and establishes a sharp fixed-volume isoperimetric minimizer with a quantitative shape deficit and absence of a global upper bound. These conclusions are not stated in the inspected reference; the spherical-cap and elementary convexity methods themselves are not claimed as new. Lángi, Naszódi and Talata (2011/2012) develop deterministic ball/spindle convexity, while Fodor, Papvári and Vígh (2020) analyze a different many-sample approximation limit. Historical priority for the specific rare-event shape law is not established absolutely.

## Limitations
The limit is asymptotic as the sampling body shrinks. No assertion of a finite-\(\varepsilon\) inequality or a uniform error bound over all convex bodies is made. Symmetry around the queried point is essential to the single radial-moment expression and minimization proof; nonsymmetric bodies are outside scope. The theorem concerns two independent uniform samples and Euclidean unit-ball spindles only. Although the leading shape coefficient is explicit, the result does not settle finite-sample statistics or corresponding laws for generalized non-Euclidean ball convexity. The historical-priority assessment is provisional.

## References
1. F. Fodor, N. A. Montenegro Pinzón, V. Vígh, *On Wendel's equality for intersections of balls*, Aequationes Mathematicae 97 (2023), 439–451; first publicly verified September 10, 2022. DOI: 10.1007/s00010-022-00912-3.
2. Z. Lángi, M. Naszódi, I. Talata, *Ball and Spindle Convexity with respect to a Convex Body*, arXiv:1110.4823, first submitted October 21, 2011; revised September 5, 2012.
3. F. Fodor, D. I. Papvári, V. Vígh, *On Random Approximations by Generalized Disc-Polygons*, Mathematika 66 (2020), 498–513, DOI: 10.1112/mtk.12027, first published April 9, 2020.
4. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–111 (classical convex-hull context).
