# Strict central-cut profile for regular odd polygons
## Finding
For every odd integer \(n\ge 3\), let \(P_n\subset\mathbb{R}^2\) be a regular \(n\)-gon with center \(O\). For an unoriented line \(L\) through \(O\), let \(\theta(L)\in[0,\pi/(2n)]\) be its angular distance from the nearest side direction, reduced by the dihedral symmetries of \(P_n\). Let \(d_n(\theta)\) be the smaller of the two area fractions of \(P_n\) cut by \(L\). Writing \(p=\pi/n\), one has
\[
d_n(\theta)=\frac12-\frac1{2n}+\frac{\tan(\theta+p/2)-\tan(\theta-p/2)}{2n\tan p},
\qquad 0\le\theta\le\frac p2.
\]
The function \(d_n\) is strictly increasing on \((0,p/2)\). Consequently, modulo the dihedral symmetries, the unique minimizing central cuts are the lines parallel to polygon edges. The opposite endpoint \(\theta=p/2\) consists of symmetry-axis cuts and gives an exact bisection.

At the minimizing direction,
\[
d_n(0)=\frac12-\frac{\tan^2(\pi/(2n))}{2n}.
\]
This endpoint value was already published by Rousseeuw and Ruts; their derivation explicitly states that edge-parallel optimality had been verified numerically. The contribution here is the closed directional profile, an analytic proof of optimality for every odd order, and uniqueness of the minimizing orientations.

## Assumptions and scope
The polygon is Euclidean, regular, nondegenerate, and has odd order \(n\ge3\). The line \(L\) is required to pass through the center. Area means ordinary planar Lebesgue area. No assertion is made here about noncentral cutting lines beyond the published fact that the Tukey depth of the uniform distribution on a regular polygon is maximized at its center.

The result is scale-invariant, so the proof normalizes the circumradius of \(P_n\) to \(1\). The angle \(\theta\) is an unoriented line angle: a side-parallel line has \(\theta=0\), and a reflection-axis line has \(\theta=\pi/(2n)\).

## Proof
Set \(p=\pi/n\) and \(c=\cos p\). Choose an outward normal to one side as polar angle \(0\). On the angular sector \(-p\le u\le p\), the ray at angle \(u\) meets that side on the line whose distance from the origin is \(c\). Hence the radial function satisfies
\[
r(u)=c\sec u,
\qquad
r(u)^2=c^2\sec^2u.
\]
Extending by rotational symmetry, the function \(g(u)=r(u)^2\) is \(2p\)-periodic. Its one-period integral is
\[
I=\int_{-p}^p g(u)\,du
 =2c^2\tan p.
\]
Therefore
\[
\operatorname{area}(P_n)=\frac12 nI.
\]

Write \(n=2m+1\). A halfplane through \(O\) corresponds in polar coordinates to an angular interval of length \(\pi=np=m(2p)+p\). Its radial-area integral therefore consists of \(m\) complete \(2p\)-periods plus one residual interval of length \(p\). The complementary halfplane has the complementary residual interval; their two residual integrals sum to \(I\).

After applying a dihedral symmetry and choosing the smaller of the complementary halfplanes, the residual interval can be written
\[
[\theta-p/2,\,\theta+p/2],
\qquad 0\le\theta\le p/2.
\]
Its integral is
\[
J(\theta)
 =c^2\int_{\theta-p/2}^{\theta+p/2}\sec^2u\,du
 =c^2\bigl(\tan(\theta+p/2)-\tan(\theta-p/2)\bigr).
\]
The corresponding smaller halfplane area is \(\frac12(mI+J(\theta))\), and division by \(\frac12nI\) yields
\[
d_n(\theta)
 =\frac{mI+J(\theta)}{nI}
 =\frac12-\frac1{2n}+\frac{\tan(\theta+p/2)-\tan(\theta-p/2)}{2n\tan p}.
\]

For \(0<\theta<p/2\), differentiation gives
\[
J'(\theta)
 =c^2\left(\sec^2(\theta+p/2)-\sec^2(\theta-p/2)\right)>0,
\]
because both arguments lie in \((-p,p)\) and the first has larger absolute tangent. Thus \(J\), and hence \(d_n\), is strictly increasing in the interior of the chamber. At \(\theta=p/2\),
\[
J(p/2)=c^2\tan p=I/2,
\]
so \(d_n(p/2)=1/2\). This also proves retrospectively that the chosen residual interval is indeed the smaller one throughout the chamber. Therefore \(\theta=0\) is the unique minimizing orientation modulo dihedral symmetry.

Finally,
\[
\frac{J(0)}I
 =\frac{2\tan(p/2)}{2\tan p},
\]
and the identity
\[
1-\frac{2\tan(p/2)}{\tan p}=\tan^2(p/2)
\]
gives
\[
d_n(0)=\frac12-\frac{\tan^2(p/2)}{2n}.
\]
This is exactly the published endpoint value.

## Verification
The proof is symbolic and uses only the radial representation of a regular polygon, periodic decomposition of a central halfplane, and elementary trigonometry. Endpoint checks give \(d_n(0)=4/9\) for the equilateral triangle and \(d_n(p/2)=1/2\) for every odd \(n\), as required by reflection symmetry. For the regular pentagon and heptagon the endpoint formula gives approximately \(0.489443\) and \(0.496279\), matching the values reported by Rousseeuw and Ruts.

As a non-probative consistency check, direct polygon clipping at sampled orientations for odd orders from \(3\) through \(31\) agreed with the displayed formula to floating-point precision. No finite computation is used to infer the all-orders theorem.

## Relationship to prior work
Rousseeuw and Ruts study halfspace depth for the uniform distribution on a regular polygon. In their odd-order calculation they state that they numerically verified that an optimal halfplane through the center has boundary parallel to an edge, and from that orientation derive the maximal-depth value
\[
\frac12-\frac{\tan^2(\pi/(2n))}{2n}.
\]
The present result does not claim that endpoint value as new. It replaces the stated numerical optimization step by an all-orders proof, determines the entire central directional profile, and proves uniqueness of the minimizing orientations modulo dihedral symmetry.

Szarek's convex-geometric asymmetry parameter \(\rho(K)\) is defined from the worst volume ratio of hyperplane cuts through an optimally chosen point, and his floating-body parameter satisfies \(\phi(K)=(\rho(K)+1)^{-1}\). Thus the same central-cut geometry is a canonical convex-geometric symmetry question. Combining the published center-depth fact with the known endpoint value translates routinely to the corresponding value of \(\rho(P_n)\); that translation is not asserted as original here.

## Limitations
Only odd regular polygons and cuts constrained to pass through the center are classified by the new directional formula. The already-published maximal Tukey-depth value is not a novelty claim. Literature searches did not locate a later analytic proof of the same edge-parallel optimality, strict uniqueness, or the full angular profile, but an unindexed or differently phrased proof remains a residual originality risk.

## References
1. P. J. Rousseeuw and I. Ruts, *The depth function of a population distribution*, Metrika 49 (1999), 213--244, DOI 10.1007/PL00020903. Section 5.5 treats the uniform distribution on a regular polygon and explicitly describes edge-parallel optimality as numerically verified before deriving the odd-order endpoint formula.
2. S. J. Szarek, *On measures of symmetry and floating bodies*, arXiv:1302.2076v1, first public version 2013-02-08. The paper defines \(\rho(K)\), relates it to convex floating bodies, and is classified under MSC 52A20 and 52A40.
