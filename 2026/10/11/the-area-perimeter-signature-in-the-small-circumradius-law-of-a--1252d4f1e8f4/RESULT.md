# The area–perimeter signature in the small-circumradius law of a random triangle

## Finding
Let \(K\subset\mathbb R^2\) have positive area \(A=A(K)\), perimeter \(P=P(K)\), a \(C^2\) boundary, and everywhere strictly positive curvature. Let \(X_1,X_2,X_3\) be independent uniform points in \(K\), and let \(\rho\) be the radius of the unique circle through them. The collinear case has probability zero. Then
\[
F_K(t):=\Pr(\rho\le t)=\frac{6\pi^2}{A^2}t^4-\frac{512P}{15A^3}t^5+O_K(t^6)\qquad(t\downarrow0).
\]
Equivalently, with \(\alpha=\lim_{t\downarrow0}F_K(t)/t^4\) and \(\beta=\lim_{t\downarrow0}[F_K(t)-\alpha t^4]/t^5\),
\[A=\pi\sqrt{6/\alpha},\qquad P=-15\beta A^3/512.\]
The coefficient pair is therefore an area–perimeter signature. Among equal-area bodies meeting these hypotheses, the disk has the largest \(F_K(t)\) for every sufficiently small positive \(t\) (where the sufficient cutoff may depend on \(K\)); the inequality is strict for each nondisk.

For the unit disk \(B\), the concrete prediction is
\[F_B(t)=6t^4-\frac{1024}{15\pi^2}t^5+O(t^6).\]

## Assumptions and scope
Throughout, \(K\) is a compact planar convex body with nonempty interior and \(C^2\) boundary of curvature bounded away from zero; a fixed body is considered while \(t\) tends to zero. Its perimeter is ordinary Euclidean arclength, and its area is planar Lebesgue measure. The random variable is the **circumradius**, not the minimal-enclosing-ball radius; the corresponding circumcircle is *not* required to be contained in \(K\). The constant in \(O_K(t^6)\) can depend on \(K\); no uniform remainder over all shapes is claimed.

For \(\theta\in[0,2\pi)\), put \(u(\theta)=(\cos\theta,\sin\theta)\). For an angle triple \(\boldsymbol\theta=(\theta_1,\theta_2,\theta_3)\), define the unit-circle triangle \(T_{\boldsymbol\theta}=\operatorname{conv}\{u(\theta_1),u(\theta_2),u(\theta_3)\}\), of area \(a_{\boldsymbol\theta}\) and perimeter \(p_{\boldsymbol\theta}\). Define the translative erosion
\[K\ominus rT:=\{c\in\mathbb R^2:c+ru\in K\text{ for every }u\in T\}.\]
As \(K\) is convex, this equals the intersection of the three translates \(K-ru(\theta_j)\).

## Proof
**1. Exact circumcircle integral.** Except for collinear triples, each ordered triple has a unique representation \(x_j=c+ru(\theta_j)\), where \(c\in\mathbb R^2\), \(r>0\), and the \(\theta_j\) lie on \([0,2\pi)\). A direct six-dimensional Jacobian calculation, subtracting the first point's two coordinate rows from the other two point-row pairs, gives
\[
\left|\frac{\partial(x_1,x_2,x_3)}{\partial(c_1,c_2,r,\theta_1,\theta_2,\theta_3)}\right|=2a_{\boldsymbol\theta}r^3.
\]
Thus the change of variables and the definition of erosion yield the **exact** identity
\[
F_K(t)=\frac1{A^3}\int_0^t r^3\!\int_{[0,2\pi)^3}2a_{\boldsymbol\theta}\,\operatorname{area}(K\ominus rT_{\boldsymbol\theta})\,d\boldsymbol\theta\,dr.\tag{1}
\]
There is no assumption that the entire random circumcircle lies in \(K\): only its three marked points are constrained.

**2. Uniform first variation of erosion.** For every compact convex \(T\subset B\) (and in particular every \(T_{\boldsymbol\theta}\)), write \(h_T(v)=\max_{u\in T}\langle u,v\rangle\) for its support function. For the fixed \(C^2\), positively curved body \(K\),
\[
\operatorname{area}(K\ominus rT)=A-r\int_{\partial K}h_T(n(y))\,ds(y)+O_K(r^2),\tag{2}
\]
where the remainder is **uniform** for all \(T\subset B\). Here is a local justification. For sufficiently small \(r\), the symmetric difference between \(K\) and \(K\ominus rT\) lies in an \(O(r)\)-width tubular neighborhood of \(\partial K\). In tubular normal coordinates \(c=y-sn(y)\), the condition \(c+ru\in K\) is, uniformly for \(u\in B\), equivalent to \(s\ge r\langle u,n(y)\rangle+O_K(r^2)\). Requiring this for all \(u\in T\) gives \(s\ge rh_T(n(y))+O_K(r^2)\). The tubular area element is \((1+O_K(r))\,ds\,dy\). Integrating signed normal strips proves (2), including when \(h_T\) is negative in a particular direction. Compactness and the uniform \(C^2\) Taylor bound supply one error constant independent of the varying triangle.

**3. Two exact angular moments.** For three independent uniform angles, root the cyclic order at the first labeled angle and write the three successive *half-gaps* as \(a,b,c>0\), with \(a+b+c=\pi\). The pair \((a,b)\) has uniform density \(2/\pi^2\) on the triangle \(a>0,b>0,a+b<\pi\). Elementary chord geometry gives
\[
a_{\boldsymbol\theta}=2\sin a\sin b\sin c,\qquad
p_{\boldsymbol\theta}=2(\sin a+\sin b+\sin c).
\]
For \(0<a<\pi\), integrate over \(b\in(0,\pi-a)\):
\[
J(a):=\int_0^{\pi-a}\sin b\sin(\pi-a-b)\,db
=\tfrac12[\sin a+(\pi-a)\cos a].
\]
Integration by parts now gives the two exact scalar identities
\[
\int_0^\pi \sin a\,J(a)\,da=\frac{3\pi}{8},\qquad
\int_0^\pi \sin^2a\,J(a)\,da=\frac89.
\]
Consequently, for the random inscribed triangle,
\[
\mathbb E[a_{\boldsymbol\theta}]=\frac{3}{2\pi},\qquad
\mathbb E[a_{\boldsymbol\theta}p_{\boldsymbol\theta}]=\frac{64}{3\pi^2}.\tag{3}
\]
The second expectation follows by symmetry among the three half-gaps, not by assuming the area and perimeter are independent.

**4. Rotation average and final coefficients.** The classical Cauchy perimeter formula is valid for every convex planar triangle, wherever the origin is placed:
\[
\int_0^{2\pi} h_T(u(\phi))\,d\phi=p_T.
\]
Rotational invariance of \(d\boldsymbol\theta\), combined with (3), implies
\[
\int_{[0,2\pi)^3}2a_{\boldsymbol\theta}\,d\boldsymbol\theta=24\pi^2,
\]
\[
\int_{[0,2\pi)^3}2a_{\boldsymbol\theta}
\left(\int_{\partial K}h_{T_{\boldsymbol\theta}}(n(y))\,ds(y)\right)d\boldsymbol\theta=\frac{512}{3}P.
\]
Indeed the latter angular integral, at each fixed normal, is \((2\pi)^3\mathbb E[2ap]/(2\pi)=512/3\), independent of the normal. Substitute these into (1) using (2), and integrate \(r^3\) and \(r^4\). One obtains
\[
F_K(t)=\frac1{A^3}\left(6\pi^2A\,t^4-\frac{512P}{15}t^5+O_K(t^6)\right),
\]
which is the asserted formula. Finally, the Euclidean isoperimetric inequality \(P^2\ge4\pi A\), with equality only for disks, compares the first shape-dependent coefficient at fixed \(A\). Since the remainder is \(O_K(t^6)\), each nondisk has a strict positive difference \(F_B(t)-F_K(t)\) for all sufficiently small positive \(t\), where \(B\) has the same area.

## Verification
The accompanying program `verify_coefficients.py` uses exact symbolic integration to reproduce the two angular moments, both expansion coefficients, and a nondegenerate instance of the six-dimensional Jacobian. It also checks the unit-disk specialization. Independent reproducibility consists of extracting that program and executing `python verify_coefficients.py` with SymPy installed. Numerical simulation of independent uniform points in the unit disk and in a noncircular ellipse was used only to stress-test, not to prove, the theorem. No experiment is substituted for the uniform geometric remainder estimate or for the analytic moment integrals.

## Relationship to prior work
Bakó-Szabó, Besau, and Fodor [1, Sections 1.4 and 5.2] determine the circumradius distribution for three independent uniform points in the unit disk on \([1,\infty)\), using its connection with random ball-convex hulls. Their paper explicitly leaves the portion below radius \(1\) outside that calculation. The present theorem is a separate, **small-radius** statement, valid for every positively curved \(C^2\) planar convex body, and resolves its first two coefficients.

Le Caër [2] analyzes circumspheres constrained to lie entirely within the sampling ball, including conditional beta-type distributions; a circle intersecting the sampling body's boundary is permitted here, so that different probability event cannot supply our full second coefficient. The distinction matters already at the order of the perimeter correction. The Jacobian and Cauchy formula used in the proof are classical tools; the new assertion is their joint consequence for this unconditional shape-sensitive distribution.

## Limitations
Only the first two nonzero powers, \(t^4\) and \(t^5\), are determined; the entire CDF, higher curvature-sensitive terms, and an error bound uniform in all shapes are not claimed. The positive-curvature \(C^2\) hypothesis ensures the stated \(O_K(t^6)\) remainder; no nonsmooth-body extension is established here. The local disk comparison applies separately to each fixed equal-area body, not with one universal positive cutoff across all bodies. Novelty is assessed against inspected accessible sources, not guaranteed against every publication; an unindexed integral-geometric treatment could contain an equivalent expansion.

## References
[1] A. Bakó-Szabó, F. Besau, and F. Fodor, *Sylvester's four point problem for ball-convex bodies*, arXiv:2608.29975, first public August 30, 2026, https://arxiv.org/html/2608.29975v1 .

[2] G. Le Caër, *Circumspheres of sets of n+1 random points in the d-dimensional Euclidean unit ball (0<n<d+1)*, arXiv:1803.08484 (2018), https://arxiv.org/abs/1803.08484 .
