# Exact dilogarithmic acuteness law for random triangles on hyperbolic circles

## Finding

In the hyperbolic plane of constant curvature \(-1\), let three points be sampled independently and uniformly with respect to arclength on the geodesic circle of radius \(R>0\). Join them pairwise by their unique hyperbolic geodesic segments. Let \(P(R)\) be the probability that **all three interior angles of this geodesic triangle are strictly acute**. Put
\[
 z(R)=\frac{\sinh^2R}{2+\sinh^2R}.
\]
Then, for every \(R>0\),
\[
 \boxed{P(R)=\frac14+\frac{3}{\pi^2}\bigl(\operatorname{Li}_2(z(R))-\operatorname{Li}_2(-z(R))\bigr).}
\]
Here the real dilogarithm is \(\operatorname{Li}_2(x)=\sum_{m\ge1}x^m/m^2\) for \(|x|<1\). The function \(P\) is strictly increasing and maps \((0,\infty)\) bijectively onto \((1/4,1)\). Thus this one acuteness probability uniquely determines the sampling circle's hyperbolic radius. The endpoint expansions are
\[
 P(R)=\frac14+\frac{3R^2}{\pi^2}-\frac{R^4}{2\pi^2}+O(R^6)\quad(R\downarrow0)
\]
and
\[
 1-P(R)=\frac{24}{\pi^2}e^{-2R}(2R+1-\log4)+O(Re^{-4R})\quad(R\to\infty).
\]

## Assumptions and scope

Hyperbolic curvature is normalized to \(-1\); \(R\) denotes the **hyperbolic distance** from the common circumcenter, not the Euclidean radius in a model. In the Poincaré disk, the sampling circle is centered at the origin with Euclidean radius \(\rho=\tanh(R/2)\). Hyperbolic arclength along this circle is a constant multiple of Euclidean polar angle, so three independent arclength-uniform vertices have independent uniform arguments in \([0,2\pi)\). Degenerate triangles and right angles have probability zero. We measure intrinsic hyperbolic angles (equivalently, Euclidean tangent angles in the conformal disk model), not the angles between the Euclidean straight chords connecting the plotted points. All assertions concern exactly three independent points on one geodesic circle, not area-uniform points in its enclosed disk.

## Proof

**1. Gaps and the hyperbolic cosine law.** Sort the three sampled angles cyclically, and denote the successive positive circular gaps by \(u,v,w\), so \(u+v+w=2\pi\). Their joint law on the open gap simplex has constant density \(1/(2\pi^2)\) relative to \(du\,dv\); this is the Dirichlet \((1,1,1)\) spacing law. Rotation and cyclic relabeling do not change the event of acuteness.

Write \(s=\sinh R\). For two points of this circle separated by polar angle \(t\), their hyperbolic distance \(d_t\) satisfies
\[
 \sinh(d_t/2)=s\sin(t/2),\qquad \cosh d_t=1+2s^2\sin^2(t/2).
\]
The first identity follows directly from the hyperbolic cosine rule in the isosceles triangle formed with the circumcenter, and is also recorded in Beardon's treatment of circumscribed hyperbolic triangles [1]. Consider the triangle angle opposite the side corresponding to gap \(v\); the adjacent sides correspond to gaps \(u\) and \(w\). Its cosine, by the hyperbolic cosine rule, has the sign of \(\cosh d_u\cosh d_w-\cosh d_v\), whose exact factorization is
\[
 4s^2\sin(u/2)\sin(w/2)
 \bigl[\cos(v/2)+s^2\sin(u/2)\sin(w/2)\bigr].
\]
The factorization uses \(u+v+w=2\pi\) and
\[
 \sin^2(u/2)+\sin^2(w/2)-\sin^2(v/2)
 =2\sin(u/2)\sin(w/2)\cos(v/2).
\]
Since all prefactors are positive, this angle is obtuse exactly when the square bracket is negative. In particular, obtuseness is impossible unless \(v>\pi\). Hence at most one of the three angles can be obtuse; all right-angle boundaries have zero area in the gap simplex.

**2. Recovering the acute fraction of Euclidean-obtuse configurations.** For \(v>\pi\), use the coordinates \(t=(u+w)/2\) and \(x=(u-w)/2\). Then \(0<t<\pi/2\), \(-t<x<t\), \(v=2\pi-2t\), and \(|\partial(u,w)/\partial(t,x)|=2\). Furthermore,
\[
 \sin(u/2)\sin(w/2)=\frac{\cos x-\cos t}{2}.
\]
Consequently the angle opposite \(v\), though Euclidean-obtuse, is hyperbolically acute exactly when
\[
 \cos x>\kappa\cos t,
 \qquad\kappa=1+\frac2{s^2}>1.
\]
This is possible precisely for \(t>\arccos(1/\kappa)\). In this range the allowable \(x\)-interval has length \(2\arccos(\kappa\cos t)\), entirely contained in \((-t,t)\). Thus, if
\[
 J(\kappa)=\int_{\arccos(1/\kappa)}^{\pi/2}
 \arccos(\kappa\cos t)\,dt,
\]
the probability contributed by this *one* gap being larger than \(\pi\) and nevertheless giving an acute hyperbolic angle is \(2J(\kappa)/\pi^2\): the coordinate Jacobian is \(2\), the allowable \(x\)-length is \(2\arccos(\kappa\cos t)\), and the gap density is \(1/(2\pi^2)\).

The probability that none of the three gaps exceeds \(\pi\), equal to the Euclidean inscribed-circle acuteness probability, is \(1/4\): the three disjoint events that a specified gap exceeds \(\pi\) each have probability \(1/4\). Therefore, using disjointness of the three converted-obtuse events,
\[
 P(R)=\frac14+\frac6{\pi^2}J(\kappa).
\]

**3. Evaluation of the non-elementary integral.** Differentiating under the integral sign for \(\kappa>1\) is valid because the endpoint term vanishes and the resulting square-root singularity is integrable. It gives
\[
 J'(\kappa)=-\int_{\arccos(1/\kappa)}^{\pi/2}
 \frac{\cos t\,dt}{\sqrt{1-\kappa^2\cos^2t}}
 =-\frac{\operatorname{artanh}(1/\kappa)}{\kappa}.
\]
The last integral is elementary under \(y=\sin t\). Since \(J(\kappa)\to0\) as \(\kappa\to\infty\), set \(z=1/\kappa=s^2/(s^2+2)\) and integrate:
\[
 J(\kappa)=\int_0^z\frac{\operatorname{artanh}u}{u}\,du
 =\frac12\bigl(\operatorname{Li}_2(z)-\operatorname{Li}_2(-z)\bigr).
\]
Substitution proves the asserted formula with its exact normalization.

**4. Strictness and endpoints.** The map \(R\mapsto z(R)\) increases strictly from \(0\) to \(1\). Moreover,
\[
 \frac{d}{dz}\bigl(\operatorname{Li}_2(z)-\operatorname{Li}_2(-z)\bigr)
 =\frac{\log((1+z)/(1-z))}{z}>0
 \quad(0<z<1).
\]
Its endpoint values are \(0\) and \(\pi^2/4\), hence \(P\) strictly increases from \(1/4\) to \(1\). The Taylor expansion \(z(R)=R^2/2-R^4/12+O(R^6)\) and the odd-power expansion \(\operatorname{Li}_2(z)-\operatorname{Li}_2(-z)=2z+O(z^3)\) give the small-radius formula. For large \(R\), put \(\delta=1-z=8e^{-2R}+O(e^{-4R})\); direct integration of the displayed derivative yields
\[
 \operatorname{Li}_2(1)-\operatorname{Li}_2(-1)
 -\bigl(\operatorname{Li}_2(1-\delta)-\operatorname{Li}_2(-1+\delta)\bigr)
 =\delta\bigl(\log(2/\delta)+1\bigr)
 +O\bigl(\delta^2\log(1/\delta)\bigr).
\]
This implies the claimed large-radius asymptotic with the stated error. No numerical experiment is used to establish the assertions for all \(R\).

## Verification

The standalone standard-library checker `verify_hyperbolic_acuteness.py` evaluates the one-dimensional spacing integral by Simpson quadrature, independently evaluates the dilogarithm difference by a convergent odd-power series, and simulates hyperbolic geodesic angles using the oriented tangent vectors to Euclidean circles orthogonal to the Poincaré disk boundary. It tests five radii for the exact-integral identity, four radii with 25,000 direct geometric triangles each, and three small-radius expansion cases. All checks passed on the embedded file. The proof above, rather than these finite checks, establishes the universal formula, strict monotonicity, and both asymptotics.

## Relationship to prior work

Beardon's 2022 article [1] studies precisely which hyperbolic triangles admit a circumcircle and derives the half-chord distance geometry used above; it does not evaluate random acuteness probabilities for fixed-radius circumcircles. Lv and Guo's 2016 work [2] computes a hyperbolic acuteness probability \(5/8\) using *uniform triangle-angle coordinates* in the feasible angle simplex (their Section 1 specifies this probability convention, and Section 3.3 performs the calculation). That distribution differs from independent, arclength-uniform vertices of a fixed circumcircle and does not imply a nonconstant function of \(R\). Besau, Rosen, and Thäle [3] study random inscribed polytopes in projective geometries, particularly many-vertex volume asymptotics; their stated results do not imply the exact three-point acuteness law. The standard hyperbolic cosine law and dilogarithm identities are not presented as new.

The claimed contribution is only the fixed-radius *arclength-uniform circumcircle* acuteness law, its strict radius determination, and the two endpoint transition formulas. Although targeted literature and public-archive comparisons found no dominating statement, historical priority remains provisional and cannot be certified by search alone.

## Limitations

The theorem is for curvature \(-1\), independent arclength-uniform boundary vertices and intrinsic angles. Other sampling laws, arbitrary shapes, spherical geometries, disks with area-uniform points, and higher-point polygons are not covered. For curvature \(-k^2\), the result reparametrizes by the dimensionless radius \(kR\), but such substitutions are not treated as separate results. It does not establish a complete angle distribution or an independent historical-priority certification.

## References

[1] A. F. Beardon, *Circumscribed hyperbolic triangles*, Archiv der Mathematik **119** (2022), 439–448, first published 8 August 2022. https://doi.org/10.1007/s00013-022-01761-x

[2] Z. Lv and Y. Guo, *Probability of an Acute Triangle in the Two-dimensional Spaces of Constant Curvature* (2016), Section 1 and Section 3.3. https://archive.ymsc.tsinghua.edu.cn/pacm_paperurl/20160813215159148123192

[3] F. Besau, D. Rosen, C. Thäle, *Random inscribed polytopes in projective geometries*, Mathematische Annalen (2021). https://doi.org/10.1007/s00208-021-02257-9
