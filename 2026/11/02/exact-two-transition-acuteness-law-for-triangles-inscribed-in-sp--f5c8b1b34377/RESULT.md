# Exact two-transition acuteness law for triangles inscribed in spherical small circles

## Finding

On the unit sphere, choose three independent points uniformly by arclength on a geodesic circle of radius \(R\), where \(0<R<\pi/2\). Connect them by minimizing spherical geodesics and let \(P(R)\) be the probability that all three intrinsic angles are strictly less than \(\pi/2\). Put \(k=\cos^2R\), \(w=(1-k)/(1+k)\), and
\[
 Q(k)=\frac{\operatorname{Li}_2(w)-\operatorname{Li}_2(-w)}{\pi^2}.
\]
For \(0<k<1/2\), define the explicit overlap integral
\[
 B(k)=\frac1{\pi^2}\int_k^{1-k}
       \frac{\log((1-k)/(u(u+k)))}{1-u^2}\,du,
\]
and set \(B(k)=0\) for \(k\ge1/2\). Then the *complete* law is
\[
 P(R)=\begin{cases}
   \frac14-3Q(k),& 1/2\le k<1,\\
   \frac14-3Q(k)+3B(k),&1/3<k<1/2,\\
   0,&0<k\le1/3.
 \end{cases}
\]
In particular, \(P\) decreases strictly from the limiting Euclidean value \(1/4\) to zero on \((0,R_*)\), where \(R_*=\arccos(1/\sqrt3)\), and vanishes identically on \([R_*,\pi/2)\). A second transition occurs at \(R=\pi/4\), where triangles having at least two nonacute angles first appear with positive probability.

Both nonzero branches are explicit in dilogarithms. To eliminate the one-dimensional integral, for \(0<k<1/2\) put
\[
\begin{aligned}
 \Phi(u)&=\operatorname{Li}_2(1-u)+\log u\log(1+u)+\operatorname{Li}_2(-u),\\
 H_k(u)&=\tfrac12\bigl[-\log(1+k)\log(1-u)
   +\operatorname{Li}_2((1-u)/(1+k))\\
 &\hspace{3.3em}+\tfrac12\log^2(1+u)+\operatorname{Li}_2((1-k)/(1+u))\bigr],\\
 F_k(u)&=\log(1-k)\operatorname{artanh}(u)-\tfrac12\Phi(u)-H_k(u).
\end{aligned}
\]
Then \(B(k)=[F_k(1-k)-F_k(k)]/\pi^2\). All special-function arguments in this formula are real and in their real principal branches.

The endpoint and transition laws are sharp:
\[
\begin{aligned}
 P(R)&=\tfrac14-\frac3{\pi^2}R^2-\frac1{2\pi^2}R^4+O(R^6) &&(R\downarrow0),\\
 P(R)&=\frac{27}{2\pi^2}(R_*-R)^2+O((R_*-R)^3)&&(R\uparrow R_*),\\
 3B(k)&=\frac{24}{\pi^2}(\tfrac12-k)^2+O((\tfrac12-k)^3)&&(k\uparrow\tfrac12).
\end{aligned}
\]
The probability is continuously differentiable across both transitions but not twice differentiable there. For illustration, \(P(\pi/4)=0.0447497197384094\ldots\).

## Assumptions and scope

The sphere has constant curvature \(+1\). The center of the sampling circle is fixed, and the sampling law is normalized one-dimensional *geodesic arclength* along its circumference, which is equivalent to a uniform longitude parameter. The three samples are independent. The geodesic edges are the unique shorter great-circle arcs; with probability one they form a nondegenerate geodesic triangle entirely inside the circle's open containing hemisphere. All angle comparisons are intrinsic, measured using tangent vectors to these spherical geodesics, **not** angles between straight Euclidean chords in the ambient three-space. The radius is restricted to \(0<R<\pi/2\). The degenerate limiting equator and the point-circle limit are excluded from the sampling model; their probability limits are stated explicitly.

## Proof

**1. Gap coordinates.** Parametrize the circle as \(X(\theta)=(\sin R\cos\theta,\sin R\sin\theta,\cos R)\). By invariance under rotation fix one sampled point at longitude zero. In ascending order the other two longitudes are \(2a\) and \(2(a+b)\). Define \(c=\pi-a-b\). Then \(a,b,c>0\) and \(a+b+c=\pi\). The joint density of \((a,b)\) is \(2/\pi^2\) on this open triangle: ordering the two independent longitudes contributes a factor two and the change to half-gaps a Jacobian four. This construction uses an anchored labeled point; no distributional assertion about the minimum of three absolute longitude values is needed.

**2. Exact spherical-angle test.** For unit vectors \(X,Y,Z\) the tangent vectors at \(X\) to minimizing great-circle arcs toward \(Y,Z\) have positive dot product exactly when
\(Y\cdot Z-(X\cdot Y)(X\cdot Z)>0\). For the vertex adjacent to half-gaps \(a,c\), this numerator simplifies *exactly* to
\[
 4\sin^2R\sin^2a\sin^2c\,
     (\cos^2R-\cot a\cot c).
\]
The other two angle tests follow cyclically. Thus all angles are acute if and only if the three products \(\cot a\cot b\), \(\cot b\cot c\), and \(\cot c\cot a\) are strictly smaller than \(k=\cos^2R\).

The elementary identity
\[
\cot a\cot b+\cot b\cot c+\cot c\cot a=1
\]
holds because \(a+b+c=\pi\). If a half-gap is at least \(\pi/2\), its cotangent is nonpositive, while the product of the other two cotangents is at least one. Such a configuration fails the acuteness test for \(k<1\). Hence the event is contained in \(0<a,b,c<\pi/2\).

**3. Positive simplex and its density.** On that subtriangle, put
\(u=\cot a\cot b\), \(v=\cot b\cot c\), \(s=\cot c\cot a\). The preceding identity gives \(u,v,s>0\) and \(u+v+s=1\), and conversely every point of the open probability simplex determines unique positive cotangents by
\[
 \cot a=\sqrt{us/v},\qquad
 \cot b=\sqrt{uv/s},\qquad
 \cot c=\sqrt{vs/u}.
\]
The sum of their arccotangents is \(\pi\) because their pairwise product sum is one and each angle is in \((0,\pi/2)\). Differentiating the inverse map gives
\[
 \left|\frac{\partial(a,b)}{\partial(u,v)}\right|
  =\frac1{2(1-u)(1-v)(1-s)}.
\]
Consequently, the *unconditional* sampling-density mass pushed onto the positive simplex is
\[
 g(u,v)=\frac1{\pi^2(1-u)(1-v)(1-s)},
 \qquad s=1-u-v.
\]
Its total mass equals \(1/4\), as is also seen from its marginal
\[
 g_u(u)=\int_0^{1-u}g(u,v)\,dv
       =\frac{-2\log u}{\pi^2(1-u^2)},\qquad 0<u<1,
\]
and \(\int_0^1 g_u(u)du=1/4\).

**4. Inclusion-exclusion and the two transitions.** Inside this simplex all three spherical angles are acute precisely when \(\max\{u,v,s\}<k\). If \(k\le1/3\), this region is empty. For \(k>1/3\), the three one-coordinate failures \(\{u\ge k\},\{v\ge k\},\{s\ge k\}\) have empty triple intersection. Each has probability
\[
 Q(k)=\int_k^1\frac{-2\log u}{\pi^2(1-u^2)}\,du
 =\frac{\operatorname{Li}_2((1-k)/(1+k))
   -\operatorname{Li}_2(-(1-k)/(1+k))}{\pi^2}.
\]
The three equal pair overlaps disappear if \(k\ge1/2\). If \(1/3<k<1/2\), a pair overlap is
\[
\begin{aligned}
 \int_{u=k}^{1-k}\int_{v=k}^{1-u}g(u,v)\,dv\,du
 &=\frac1{\pi^2}\int_k^{1-k}
 \frac{\log((1-k)/(u(u+k)))}{1-u^2}\,du=B(k).
\end{aligned}
\]
Inclusion-exclusion therefore proves the displayed piecewise formula. Direct differentiation using \(\frac{d}{dz}\operatorname{Li}_2(z)=-\log(1-z)/z\) gives \(F_k'(u)=\log((1-k)/(u(u+k)))/(1-u^2)\) and the stated dilogarithmic expression for \(B\).

**5. Strict monotonicity and sharp expansions.** The density \(g\) is strictly positive in the open simplex. If \(1/3<k_1<k_2<1\), the regions \(\max\{u,v,s\}<k_1\) and \(\max\{u,v,s\}<k_2\) differ by positive mass; hence \(P\) is strictly increasing in \(k\), and strictly decreasing in \(R\) up to the critical radius. At \(k\downarrow1/3\), translate \((u,v,s)\) about \((1/3,1/3,1/3)\). The allowed region is an equilateral coordinate-simplex triangle of area \(\frac92(k-1/3)^2\) in the \((u,v)\) plane. Its density at the central point is \(27/(8\pi^2)\). Thus
\[
 P(k)=\frac{243}{16\pi^2}(k-1/3)^2+O((k-1/3)^3).
\]
Since \(k-1/3=(2\sqrt2/3)(R_*-R)+O((R_*-R)^2)\), the critical-radius formula follows. Similarly, the pair-overlap domain near \(k=1/2\) is a triangle with area \((1-2k)^2/2\), and \(g(1/2,1/2)=4/\pi^2\) (interpreting the third coordinate tending to zero); multiplying by the three pairs gives \(3B(k)=24(1/2-k)^2/\pi^2+O((1/2-k)^3)\). Finally the Taylor series of the first branch, noting \(B=0\) for small \(R\), yields the small-radius expansion. These quadratic turn-ons also establish the stated regularity at both transitions.

## Verification

The self-contained program `check.py` numerically tests the cotangent identity, the inverse Jacobian, the single-coordinate tail integral, the independent one-dimensional overlap quadrature and its dilogarithmic antiderivative. It also samples the original three longitude parameters, evaluates all intrinsic angles from ambient tangent-plane dot products (without using the half-gap criterion), and compares observed probabilities at five radii with the formulas. Separate diagnostics test both quadratic transition coefficients and the small-radius series. Execute `python check.py` with Python 3, NumPy, SciPy, and mpmath installed. All random seeds are fixed. These tests corroborate identities but are not a proof of the all-radius statement; the analytic derivation above is the proof.

## Relationship to prior work

The Euclidean probability \(1/4\) for three boundary-uniform circle points is classical. Akopyan, Edelsbrunner and Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere* (arXiv:2007.07783, first public 2020-07-15), §3–4 and Lemma 4, analyze **Euclidean chord-triangle** acuteness for points distributed over the *entire sphere*, obtaining probability \(1/2\). Their §4.1 also carefully distinguishes a uniformly sampled circumcircle from the conditional-on-circumcircle law; neither is the fixed small-circle arclength-uniform *intrinsic geodesic* law here. Huiling Le, *Random spherical triangles II: Shape densities* (1989), studies three points uniformly in a **spherical cap**, not only on its boundary small circle. Maeda, *Seven Types of Random Spherical Triangle in \(S^n\) and Their Probabilities* (2008), studies seven ambient-sphere triangle types, but the available abstract does not establish a fixed-small-circle arclength law. The survey *Geometric Probability on the Sphere* (Maehara and Martini, 2017; chapter 2024) is potentially related, but its complete chapter text was not available for comparison. This result is consequently offered with provisional historical priority, not as a claim of a certified first discovery.

## Limitations

This is a spherical-intrinsic angle law for one-dimensional arclength-uniform boundary sampling only. It does not apply to uniform surface-area sampling inside a cap, full-sphere uniform vertices, Euclidean chord angles, arbitrary curves, or higher-dimensional simplices. The probability vanishes identically past the sharp radius; it does not identify radii beyond that threshold. Sources not available in complete text remain a historical-priority risk. No independent mathematical validation has been performed.

## References

1. A. Akopyan, H. Edelsbrunner, A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere*, arXiv:2007.07783 (2020-07-15 version), especially pp. 4–5, Lemma 4 and §4.1. https://arxiv.org/abs/2007.07783
2. Huiling Le, *Random spherical triangles II: Shape densities*, Advances in Applied Probability **21** (1989), 581–594, https://doi.org/10.2307/1427637. Abstract inspected; complete text unavailable.
3. Y. Maeda, *Seven Types of Random Spherical Triangle in \(S^n\) and Their Probabilities*, Computational Geometry and Graph Theory (2008), 119–126, https://doi.org/10.1007/978-3-540-89550-3_13. Abstract inspected; complete text unavailable.
4. H. Maehara, H. Martini, *Geometric Probability on the Sphere*, in *Circles, Spheres and Spherical Geometry*, 2024, pp. 159–179, https://doi.org/10.1007/978-3-031-62776-7_8. Publisher preview inspected; complete chapter unavailable.
