# A sharp pair-distance dispersion inequality for circular cone surfaces

## Finding

Let \(C\) be the curved lateral surface (without its base disk) of a nondegenerate finite right circular cone, equipped with its intrinsic shortest-path metric and normalized surface-area measure. If its slant height is \(\ell>0\), its base radius is \(R\in(0,\ell)\), and its total intrinsic cone angle is \(2\alpha=2\pi R/\ell\), then \(0<\alpha<\pi\). The lateral area is \(S=\pi R\ell=\alpha\ell^2\).

For two independent area-uniform points \(P,Q\) on \(C\),
\[
\mathbb E[d_C(P,Q)^2]
=\ell^2\left(1-\frac{8\sin\alpha}{9\alpha}\right).
\]
Consequently every such cone satisfies the *sharp* scale-invariant inequality
\[
\mathbb E[d_C(P,Q)^2]\geq c_* S,
\qquad c_*=\frac{1}{\alpha_*}\left(1-\frac{8\sin\alpha_*}{9\alpha_*}\right)
=0.251412549578138\ldots,
\]
with equality precisely when
\[
\frac R\ell=\frac{\alpha_*}{\pi}=0.294555417678307\ldots.
\]
Here \(\alpha_*\in(0,\pi/2)\) is the **unique** root in that interval of
\[
8(2\sin\alpha-\alpha\cos\alpha)=9\alpha,
\qquad\alpha_*=0.925373136253244\ldots.
\]
There is exactly one further stationary point \(\alpha_+\in(\pi/2,\pi)\) of the normalized dispersion, at \(\alpha_+=2.92216796039813\ldots\); it is a strict local maximum. At fixed slant height, the entire intrinsic squared-distance distribution is strictly increasing with \(\alpha\) under a canonical coupling, despite this nonmonotonicity at fixed lateral area.

## Assumptions and scope

The result concerns the *intrinsic* path distance on the lateral surface, including its apex and boundary circle; it is not the ambient Euclidean chord distance or the intrinsic distance on the solid cone. The base disk is excluded. The two points are independent and uniformly sampled by two-dimensional Hausdorff area. The opening parameter ranges over \(0<\alpha<\pi\), corresponding exactly to nondegenerate right circular cones with positive height and radius. No smoothness at the apex is assumed; it has area zero.

Fixed lateral area means that \(\ell=\sqrt{S/\alpha}\), \(R=(\alpha/\pi)\sqrt{S/\alpha}\), and the axial height is \(\ell\sqrt{1-(\alpha/\pi)^2}\). The minimizer is unique up to congruence at any fixed \(S>0\).

## Proof

**1. The intrinsic distance and probability coordinates.** Develop the conical lateral surface into a Euclidean sector of radius \(\ell\) and angle \(2\alpha\) with its two radial sides identified. A point has slant-radius \(r\in[0,\ell]\) and developed angular coordinate \(\phi\in\mathbb R/(2\alpha\mathbb Z)\). The area form is \(r\,dr\,d\phi\). For two points with coordinates \((r,\phi)\) and \((s,\psi)\), define the shortest circular angular separation
\[
\delta=\min_{k\in\mathbb Z}|\phi-\psi+2k\alpha|\in[0,\alpha].
\]
Since \(\alpha<\pi\), the straight segment in the unfolded wedge of angle \(\delta\) is a shortest path; alternatively this is the metric-cone cosine rule. Thus, including the apex and zero-radius boundary cases by continuity,
\[
d_C(P,Q)^2=r^2+s^2-2rs\cos\delta. \tag{1}
\]
The normalized area measure makes \(r,s\) independent with density \(2u/\ell^2\) on \([0,\ell]\); each angle is independent and uniform modulo \(2\alpha\). Rotational invariance of the angular circle makes \(\delta\) independent of both radii and exactly uniform on \([0,\alpha]\).

**2. Exact dispersion.** The elementary expectations are
\[
\mathbb E[r^2]=\frac{\ell^2}{2},\quad
\mathbb E[r]=\frac{2\ell}{3},\quad
\mathbb E[\cos\delta]=\frac{\sin\alpha}{\alpha}.
\]
Taking expectations in (1) yields the displayed exact formula. After dividing by \(S=\alpha\ell^2\), set
\[
f(\alpha)=\frac{1}{\alpha}-\frac{8\sin\alpha}{9\alpha^2},\qquad 0<\alpha<\pi.\tag{2}
\]

**3. All critical points and global optimality.** Direct differentiation gives
\[
f'(\alpha)=\frac{g(\alpha)}{9\alpha^3},\quad
g(\alpha)=8(2\sin\alpha-\alpha\cos\alpha)-9\alpha,
\]
\[
g'(\alpha)=8(\cos\alpha+\alpha\sin\alpha)-9,
\quad g''(\alpha)=8\alpha\cos\alpha.
\]
The derivative \(g'\) strictly increases from \(-1\) to \(4\pi-9>0\) on \((0,\pi/2)\), then strictly decreases to \(-17\) on \((\pi/2,\pi)\). Hence it has exactly two zeros, one in each half interval. Since \(g(0)=0\), \(g'(0)=-1\), \(g(\pi/2)=16-9\pi/2>0\), and \(g(\pi)=-\pi<0\), it follows that \(g\) has precisely two zeros \(\alpha_*\in(0,\pi/2)\) and \(\alpha_+\in(\pi/2,\pi)\), with respective sign changes negative-to-positive and positive-to-negative. Thus \(f\) has one strict local minimum followed by one strict local maximum.

The limits are \(f(\alpha)\sim1/(9\alpha)\to+\infty\) as \(\alpha\downarrow0\), and \(f(\alpha)\to1/\pi\) as \(\alpha\uparrow\pi\). The strict comparison
\[
f(\pi/3)=\frac3\pi-\frac{4\sqrt3}{\pi^2}<\frac1\pi
\]
follows from \(\pi<2\sqrt3\). Therefore the first local minimum lies below either endpoint limit, and it is the unique global minimizer. This proves the sharp constant and its equality case. The displayed numerical values come from ordinary bisection on the two rigorously isolated root intervals, not from assumptions about root counts.

**4. Strict stochastic ordering at fixed slant height.** Couple cone point pairs using independent \(U,V\) with density \(2u\) on \([0,1]\) and an independent uniform \(T\in[0,1]\), putting \(r=\ell U\), \(s=\ell V\), \(\delta=\alpha T\). Formula (1) then reads
\[
\frac{d_C(P,Q)^2}{\ell^2}=U^2+V^2-2UV\cos(\alpha T).
\]
For \(0<\alpha_1<\alpha_2<\pi\), \(\cos(\alpha_1T)>\cos(\alpha_2T)\) whenever \(T>0\), while \(UV>0\) almost surely. Hence the coupled squared distances strictly increase almost surely. This concerns fixed \(\ell\), not the fixed-area optimization of (2).

## Verification

The proof is entirely analytic, including existence, global uniqueness and sharpness. `verification/cone_dispersion_verify.py` is a standalone Python 3 supplementary check: 2,400,000 randomly sampled point pairs over eight opening angles agreed with the exact squared-distance means to at most \(0.001912\) for unit slant height; 200,000 common-randomness configurations satisfied the strict monotonic coupling. Bisection yielded \(\alpha_*=0.925373136253242\ldots\) and \(c_*=0.251412549578139\ldots\). Simulation is not offered as proof of an inequality for all angles or of stationary-point uniqueness.

Run reproducibly with `python3 verification/cone_dispersion_verify.py` from the extracted package root. No nonstandard Python modules are needed.

## Relationship to prior work

Bacher and Sturm, *Ricci Bounds for Euclidean and Spherical Cones* (arXiv:1003.2114v1, March 10, 2010), give the metric-cone cosine law and its natural radial measure (Introduction, Section 1.1). This supplies a standard geometric foundation but does not optimize pairwise squared-distance dispersion for fixed-area circular cone surfaces. Tu and Fischbach, *Random Distance Distribution for Spherical Objects* (arXiv:math-ph/0201046v1, January 22, 2002), develop geometric-probability methods for ambient distances in spherical balls, not intrinsic distances on conical surfaces. Kimberling, *Mean distances on a sphere* (2011, DOI 10.4171/EM/172), studies spherical point-to-region means rather than squared random-pair cone distances. Mayrand, *Particle Motion in Monopoles and Geodesics on Cones* (arXiv:1407.7919v1, July 30, 2014), analyzes geodesic motion on cones, not the present sharp statistical shape inequality.

The metric formula and independent-coordinate integration are standard ingredients; the claimed contribution is specifically the entire sharp fixed-area cone inequality, its unique optimizer and the two-stationary-point classification. This is not a universal inequality for all metric cones or all surfaces. Historical priority beyond the inspected sources remains open to independent assessment.

## Limitations

The theorem applies only to Euclidean right circular cone lateral surfaces, not oblique cones, frusta, arbitrary polyhedral cone metrics or cones with base disks included. The optimizer is for the quadratic intrinsic pair-distance functional at fixed lateral area, not for expected (unsquared) distance, diameter, embedding distortion or area under a fixed volume constraint. The strict stochastic ordering holds at fixed slant height only. The flat-disk limit \(\alpha\uparrow\pi\) and collapsed-angle limit \(\alpha\downarrow0\) are excluded from the equality domain. Novelty has been assessed against accessible literature and records, not independently certified.

## References

1. S.-J. Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046v1 (2002-01-22), https://arxiv.org/pdf/math-ph/0201046.
2. K. Bacher and K.-T. Sturm, *Ricci Bounds for Euclidean and Spherical Cones*, arXiv:1003.2114v1 (2010-03-10), https://arxiv.org/pdf/1003.2114.
3. C. Kimberling, *Mean distances on a sphere*, Elemente der Mathematik 66 (2011), 63–73, https://doi.org/10.4171/EM/172.
4. M. Mayrand, *Particle Motion in Monopoles and Geodesics on Cones*, arXiv:1407.7919v1 (2014-07-30), https://arxiv.org/pdf/1407.7919.
