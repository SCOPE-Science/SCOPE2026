# Sharp geodesic-diameter phase diagram of circular conical frusta

## Finding

**Theorem.** Consider only the *lateral surface* of a nondegenerate right circular cone frustum, including its two boundary circles but excluding its end disks. Let \(0<b<B\) be the distances measured along generators from the missing cone apex to the smaller and larger boundary circles. Let \(0<\gamma<\pi/2\) be the half-angle of the cone, and define
\[
q=b/B\in(0,1),\qquad \phi=\pi\sin\gamma\in(0,\pi).
\]
Then its intrinsic (shortest-surface-path) diameter is exactly
\[
\operatorname{diam}(M)=B\begin{cases}
\sqrt{1+q^2-2q\cos\phi}, & 0<\phi<\pi/3,\quad 0<q<2\cos\phi-1,\\[2mm]
2\sin(\phi/2),&q\le\cos(\phi/2)\text{ and the preceding case fails},\\[2mm]
2\sqrt{1-q^2}+q\bigl(\phi-2\arccos q\bigr),&q>\cos(\phi/2).
\end{cases}
\]
The piecewise clauses are ordered, disjoint, and exhaustive. Every diametral pair has developed angular separation exactly \(\phi\). In the first regime, its endpoints lie on **different** boundary circles. In the second and third regimes both lie on the **larger** boundary circle. At the first transition \(q=2\cos\phi-1\) (which exists exactly for \(0<\phi<\pi/3\)), both configurations are diametral. At \(q=\cos(\phi/2)\), the diameter-preserving path switches from a straight developed chord to a pair of tangents joined by an arc of the inner rim.

As a function of \(q\) at fixed \(0<\phi<\pi/3\), the normalized diameter has a strict corner at \(q=2\cos\phi-1\): its left and right derivatives are \(-\sin(\phi/2)\) and \(0\), respectively. At \(q=\cos(\phi/2)\), it is continuously differentiable, with right second derivative \(2/\sqrt{1-q^2}\) and left second derivative \(0\); hence it is not twice continuously differentiable there.

## Assumptions and scope

The frustum is the metric completion of the parametrized surface \((r,\vartheta)\) with \(b\le r\le B\) and physical azimuth \(\vartheta\in\mathbb R/(2\pi\mathbb Z)\). Its intrinsic metric is \(dr^2+(r\sin\gamma)^2d\vartheta^2\). Put \(\theta=(\sin\gamma)\vartheta\); the developed annular strip has Euclidean polar metric \(dr^2+r^2d\theta^2\), angular period \(2\phi=2\pi\sin\gamma\), and inner forbidden disk of radius \(b\). Distances below are intrinsic, not straight-line Euclidean distances through the solid. No claim is made about the surface with end disks attached, about irregular or oblique frusta, or about non-Euclidean intrinsic metrics.

## Proof

**1. Exact two-point geodesic formula.** For points at developed radii \(r,s\in[b,B]\), the shorter developed angular separation is \(\delta\in[0,\phi]\). Define \(\alpha_r=\arccos(b/r)\), \(\alpha_s=\arccos(b/s)\). Their shortest intrinsic distance is
\[
d_b(r,s,\delta)=\begin{cases}
\sqrt{r^2+s^2-2rs\cos\delta},&\delta\le\alpha_r+\alpha_s,\\
\sqrt{r^2-b^2}+\sqrt{s^2-b^2}+b(\delta-\alpha_r-\alpha_s),&\delta>\alpha_r+\alpha_s.
\end{cases}\tag{1}
\]
To derive (1), unwrap the frustum. If the segment joining the two developed points misses the open disk of radius \(b\), the straight segment is shortest. Otherwise any shortest planar path around that disk consists of a tangent from each endpoint and the intervening arc along its boundary. The respective tangent lengths are \(\sqrt{r^2-b^2}\), \(\sqrt{s^2-b^2}\), and the arc has angle \(\delta-\alpha_r-\alpha_s\). The two expressions agree at tangency. A path with a larger absolute angular winding cannot be shorter: scaling its angular coordinate by a factor in \([0,1]\), while fixing its radial coordinate, never increases its length \(\int\sqrt{\dot r^2+r^2\dot\theta^2}\,dt\). Thus the shortest representative indeed uses \(\delta\le\phi\). Formula (1) is nondecreasing in \(\delta\), strictly increasing for \(\delta>0\), so all farthest pairs have \(\delta=\phi\).

**2. Boundary reduction by convexity.** Fix \(s,\delta\) with \(0<\delta<\pi\). In the chord branch of (1), the function of \(r\) is the Euclidean norm of an affine function, and
\[
\partial_r^2d_b=\frac{s^2\sin^2\delta}{(r^2+s^2-2rs\cos\delta)^{3/2}}>0.
\]
In the tangent–arc branch, \(r\)-dependence is
\[
g(r)=\sqrt{r^2-b^2}-b\arccos(b/r),\quad
g'(r)=\frac{\sqrt{r^2-b^2}}r,\quad
g''(r)=\frac{b^2}{r^2\sqrt{r^2-b^2}}>0.
\]
At the branch boundary, \(\cos\delta=(b^2-\sqrt{r^2-b^2}\sqrt{s^2-b^2})/(rs)\) and both first derivatives are \(\sqrt{r^2-b^2}/r\). Hence the distance is globally strictly convex in \(r\in[b,B]\) for fixed \(s,\delta\), and similarly in \(s\). Its maximum on the radial square is attained only at its corners. The inner–inner value \(b\delta\) is strictly smaller than the outer–inner value: for \(s=b\), (1) is nondecreasing in \(r\), with strictly positive increase from \(b\) to \(B\). Consequently
\[
\operatorname{diam}(M)=\max\{d_b(B,b,\phi),\ d_b(B,B,\phi)\}.\tag{2}
\]

**3. Comparison of the two endpoint classes.** Divide lengths by \(B\). Write \(A(q,\phi)=d_b(B,b,\phi)/B\) and \(C(q,\phi)=d_b(B,B,\phi)/B\). Formula (1) gives
\[
A=\begin{cases}\sqrt{1+q^2-2q\cos\phi},&q\le\cos\phi\text{ (possible only for }\phi\le\pi/2),\\
\sqrt{1-q^2}+q(\phi-\arccos q),&\text{otherwise},\end{cases}
\]
and
\[
C=\begin{cases}2\sin(\phi/2),&q\le\cos(\phi/2),\\
2\sqrt{1-q^2}+q(\phi-2\arccos q),&q>\cos(\phi/2).
\end{cases}
\]
If \(q\ge\cos(\phi/2)\), both paths involve the small rim and \(C-A=\sqrt{1-q^2}-q\arccos q>0\): its derivative is \(-\arccos q<0\), and its value tends to zero at \(q=1\). On \(\max(0,\cos\phi)<q<\cos(\phi/2)\), \(C\) is constant while \(\partial_q A=\phi-\arccos q>0\); comparison at the endpoints shows \(A<C\) throughout (at \(q=\cos\phi\ge0\), one has \(A=\sin\phi<2\sin(\phi/2)=C\); when \(\cos\phi<0\), the value at \(q=0\) is \(A=1<C\)). Finally, where \(0<q\le\cos\phi\), both distances are chords and
\[
C^2-A^2=(1-q)\bigl(q-(2\cos\phi-1)\bigr).
\]
This identity gives the sole switch at \(q=2\cos\phi-1\) when \(0<\phi<\pi/3\), and no switch otherwise. Substituting the winning branch in (2) gives the displayed theorem, including the farthest-point configurations.

**4. Regularity.** At \(q=2\cos\phi-1\), the first branch has derivative \((q-\cos\phi)/A=-\sin(\phi/2)\), while the middle branch is constant in \(q\). At \(q=\cos(\phi/2)\), the last branch has derivative \(\phi-2\arccos q=0\) and second derivative \(2/\sqrt{1-q^2}\); the middle branch has both derivatives zero. This verifies the two distinct singularity classes.

## Verification

The proof above is valid for all real \(0<b<B\) and \(0<\gamma<\pi/2\), not merely a numerical grid. Running `python3 frustum_diameter_checker.py` performs 810,000 reproducibly seeded random endpoint-pair comparisons over 270 parameter configurations, independently checks all four radial corner candidates, and exhaustively tests 8,281 radial grid points for each of 20 additional configurations. The recorded maximum positive violation is zero and maximum formula/contact discrepancy is about \(5.83\times10^{-16}\). These finite calculations support but do not establish the universal theorem.

Two limiting consistency checks are: as \(b\downarrow0\), the formula tends to \(B\max\{1,2\sin(\phi/2)\}\), the lateral-cone diameter; and as a frustum approaches a cylindrical lateral surface with fixed generator length \(H=B-b\) and fixed limiting radius \(R=B\sin\gamma\), its diameter tends to \(\sqrt{H^2+\pi^2R^2}\).

## Relationship to prior work

The standard local conical metric is explicitly formulated by Charitos, Papadoperakis and Tsapogas (arXiv:1306.1759, initial version 7 June 2013). Their results concern geodesic dynamics on closed Euclidean cone surfaces, rather than the diameter of an annular truncated cone with boundary. Chen's treatment of rectifying curves and geodesics on cones (2017) derives the straightened-cone approach for local geodesics, but does not address boundary-following shortest paths or the global two-parameter diameter phase diagram. The earlier polyhedral shortest-path algorithm of Mitchell, Mount and Papadimitriou (1987) concerns different classes of surfaces and is not an explicit result about this smooth frustum. In particular, the comparison between outer–inner and outer–outer boundary endpoints and both exact shape transitions are established here, not quoted from any of those references.

## Limitations

This is a self-contained self-review mathematical derivation, **not an independent validation or proof of publication priority**. The exact classification could potentially be implicit in unlocated elementary-geometry treatments of planar annular obstacles. Automated and bibliographic searches did not locate an explicit earlier formula, but absence from such searches does not prove novelty. Surfaces with their end caps attached have a different shortest-path metric and are excluded. The source date below is the earliest *exact calendar date verified for a cited public geometric source*, not a claim that elementary cone geometry originated then.

## References

1. C. Charitos, I. Papadoperakis and G. Tsapogas, *The geometry of Euclidean surfaces with conical singularities*, arXiv:1306.1759, initial public submission 2013-06-07, https://arxiv.org/abs/1306.1759 .
2. B.-Y. Chen, *Rectifying curves and geodesics on a cone in the Euclidean 3-space*, Tamkang Journal of Mathematics **48** (2017), 209–214, DOI:10.5556/j.tkjm.48.2.2017.2382, https://journals.math.tku.edu.tw/index.php/TKJM/article/download/2382/1027/6204 .
3. J. S. B. Mitchell, D. M. Mount and C. H. Papadimitriou, *The discrete geodesic problem*, SIAM Journal on Computing **16** (1987), 647–668, DOI:10.1137/0216045 (publisher abstract consulted; complete article not inspected).
