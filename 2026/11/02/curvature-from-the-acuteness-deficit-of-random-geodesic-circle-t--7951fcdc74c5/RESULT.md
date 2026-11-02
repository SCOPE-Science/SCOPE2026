# Curvature from the acuteness deficit of random geodesic-circle triangles

## Finding
Let \((M,g)\) be a smooth Riemannian surface, let \(p\in M\), and, for all sufficiently small \(r>0\), choose three independent points uniformly with respect to normalized Riemannian arclength on the geodesic circle \(S_g(p,r)\). Join them by their unique minimizing geodesics and let \(P_p(r)\) denote the probability that every intrinsic triangle angle is strictly less than \(\pi/2\). Then
\[
P_p(r)=\frac14-\frac{3K_g(p)}{\pi^2}r^2+O_p(r^3),
\]
where \(K_g(p)\) is Gaussian curvature, positive on round spheres. In particular, the single Bernoulli observable “the sampled triangle is acute” determines Gaussian curvature at any point:
\[
K_g(p)=\frac{\pi^2}{3}\lim_{r\downarrow0}\frac{\frac14-P_p(r)}{r^2}.
\]
The statement does **not** require constant curvature, global homogeneity, or orientability. If \(K_g(p)>0\) (respectively \(<0\)), then \(P_p(r)<1/4\) (respectively \(>1/4\)) for all sufficiently small \(r\).

## Assumptions and scope
A smooth two-dimensional Riemannian manifold suffices; no completeness assumption is needed. Fix \(p\) in its interior, and take \(r\) smaller than a strongly convex normal-neighborhood radius. The probability law is product normalized arclength measure on the **geodesic circle**, not uniform volume in the enclosed disk and not sampling from an ambient Euclidean sphere. Each angle is formed by the initial tangents of the two minimizing geodesic edges at its vertex. Degenerate triples and right-angle equalities have probability zero for sufficiently small radii. Constants in \(O_p(\cdot)\) can depend on local metric derivatives around \(p\).

## Proof
**1. Normal-coordinate comparison and sampling measure.** Fix an orthonormal frame at \(p\), and use geodesic normal coordinates \(x\) centered at \(p\). Set \(\kappa=K_g(p)\). In dimension two, uniformly for \(x\) near the origin,
\[
g_{ij}(x)=\delta_{ij}-\frac{\kappa}{3}\bigl(|x|^2\delta_{ij}-x_i x_j\bigr)+O(|x|^3).
\]
The metric of the simply connected constant-curvature \(\kappa\) surface has exactly the same quadratic jet in its corresponding normal coordinates. On the unit disk after \(x=ru\), the two rescaled metrics therefore differ by \(O_p(r^3)\) in \(C^2\). Standard smooth dependence of short minimizing geodesics on their endpoints and on the metric shows that the intrinsic triangle angles differ by \(O_p(r^3)\) uniformly for angular triples near a right-angle configuration. This remains uniform when two of the circle parameters coalesce: the initial geodesic tangent has a smooth one-sided extension after factoring out the vanishing signed endpoint separation. Explicitly, the logarithm map has the form \(\log_x(y)=B(x,y)(y-x)\) with smooth invertible \(B\), and the chord difference of unit-circle parameters factors as \(2\sin((\theta'-\theta)/2)\) times a smooth nonzero direction.

The polar Jacobi field gives the Riemannian arclength element
\[
ds=J(r,\theta)\,d\theta,\qquad J(r,\theta)=r\bigl(1-\kappa r^2/6+O_p(r^3)\bigr).
\]
Hence normalized arclength has density \((2\pi)^{-1}+O_p(r^3)\) with respect to the normal angular coordinate, uniformly in \(\theta\). Its threefold product differs in total variation by \(O_p(r^3)\) from three uniform angles. In a flat circle, after sorting the three angles cyclically and writing the positive successive gaps as \(a,b,c\), the constraints are \(a+b+c=2\pi\), and the joint gap density is \(1/(2\pi^2)\) on the two-dimensional simplex. The Euclidean angle opposite gap \(c\) equals \(c/2\). Thus the three right-angle boundaries are the transverse straight segments \(a=\pi\), \(b=\pi\), \(c=\pi\) of this simplex. For small model curvature and radius, their perturbed counterparts remain uniformly transverse, including their endpoints. The probability that a model angle lies within \(O_p(r^3)\) of \(\pi/2\) is therefore \(O_p(r^3)\). A union bound gives
\[
P_p(r)=P_{\kappa}^{\mathrm{space\ form}}(r)+O_p(r^3).
\]
Here the superscript simply distinguishes the comparison model; no global comparison theorem is asserted.

**2. Exact space-form right-angle boundary.** In the constant-curvature comparison surface set
\[
 s_\kappa(r)=\begin{cases}\sin(\sqrt\kappa r)/\sqrt\kappa,&\kappa>0,\\r,&\kappa=0,\\\sinh(\sqrt{-\kappa}r)/\sqrt{-\kappa},&\kappa<0,\end{cases}\qquad z=\kappa s_\kappa(r)^2=\kappa r^2+O_\kappa(r^4).
\]
Take three cyclically ordered samples with successive angular gaps \(a,b,c>0\) summing to \(2\pi\), and examine the intrinsic angle \(\alpha\) at the vertex between the gaps \(a,b\), opposite \(c\). The generalized cosine law and the equal radial distances \(r\) give, with \(x=a/2\), \(y=b/2\),
\[
\cos\alpha=-\frac{\cos(x+y)+z\sin x\sin y}{\sqrt{(1-z\sin^2x)(1-z\sin^2y)}}.
\]
The denominator is strictly positive for all sufficiently small \(r\). For \(0<a<\pi\), the condition \(\alpha\ge\pi/2\) is equivalent to
\[
0<b\le b_*(a,z):=2\arctan\!\left(\frac{\cot(a/2)}{1-z}\right);
\]
for \(\pi\le a<2\pi\) it cannot hold. Uniformly for \(a\in[0,\pi]\),
\[
b_*(a,z)=\pi-a+z\sin a+O(z^2).
\]
Consequently the probability that this **one specified** angle is nonacute equals
\[
\frac{1}{2\pi^2}\int_0^\pi b_*(a,z)\,da
=\frac14+\frac z{\pi^2}+O(z^2),
\]
using \(\int_0^\pi\sin a\,da=2\).

At the Euclidean reference, two nonacute angles cannot occur together: they would require two of the gaps to be at least \(\pi\). For small \(|z|\), each such event requires the corresponding gap to be at least \(\pi-C|z|\), so every double-overlap is confined to a two-dimensional simplex region of area \(O(z^2)\). Inclusion-exclusion thus yields
\[
P_{\kappa}^{\mathrm{space\ form}}(r)
=1-3\left(\frac14+\frac z{\pi^2}\right)+O(z^2)
=\frac14-\frac{3\kappa}{\pi^2}r^2+O_\kappa(r^4).
\]
This also holds when \(\kappa=0\), in which case the probability is exactly \(1/4\).

**3. Arbitrary surface.** Combining the comparison estimate from Step 1 and the model expansion from Step 2 gives the asserted \(O_p(r^3)\) formula. Dividing by \(r^2\) proves the curvature-recovery identity and its strict sign consequences when curvature is nonzero.

## Verification
The standalone `CHECK.py` requires Python, SymPy, and mpmath; execute `python CHECK.py`. It independently checks the half-angle trigonometric identity, the exact first variation of the nonacute boundary, the Dirichlet-gap normalization, and high-precision constant-curvature integrals for both signs of curvature and shrinking radii. Its final line is `ALL_CHECKS_PASSED`. The analytic normal-coordinate comparison and uniform boundary-transversality arguments above, not finite numerical experiments, establish the theorem for arbitrary smooth metrics.

## Relationship to prior work
The classical Bertrand–Diguet–Puiseux formula recovers curvature from a small circle's length or its disk's area. Abelgas, Carrillo, Palacios, Weisbart, and Yassine recover **constant** Gaussian curvature from a different Buffon-needle intersection probability. The present observable is instead the acuteness of a random intrinsic geodesic triangle and works pointwise without assuming curvature is constant. Akopyan, Edelsbrunner, and Nikitenko treat Euclidean triangles formed by points uniform on a **two-dimensional sphere**, including acute facets; their sampling measure and their Euclidean rather than intrinsic angles differ. Existing exact constant-curvature geodesic-circle calculations are compatible with the quadratic coefficient, but such model formulas alone do not determine what happens for a nonhomogeneous metric. The novelty asserted here is the universal local curvature-recovery law for **all smooth Riemannian surfaces** using this specified Bernoulli event; it does not claim the curvature-recovery paradigm itself is new.

## Limitations
This is a small-radius asymptotic for the exact population probability, not an exact finite-radius law for variable-curvature surfaces. The error estimate is local and nonuniform across unrestricted families of metrics. No finite-sample estimation rate or confidence interval is proved. When \(K_g(p)=0\), the leading correction vanishes; the result alone does not determine the sign of the next term. Alternative geometric probability experiments can also recover curvature, and full historical priority is not independently certified.

## References
- A. Akopyan, H. Edelsbrunner, and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-Sphere*, arXiv:2007.07783 (first public 2020-07-15); *Experimental Mathematics*, online 2021; DOI: 10.1080/10586458.2021.1980459. See Section 4 for the Euclidean acute-facet model and its sampling distinction.
- A. Abelgas, B. Carrillo, J. Palacios, D. Weisbart, and A. M. Yassine, *Buffon's Problem determines Gaussian Curvature in three Geometries*, arXiv:2009.06755 (first public 2020-09-14); *Journal of Applied Probability* 61 (2024), 1127–1138, DOI: 10.1017/jpr.2023.114. See Theorem 1.1 and Sections 2–4 for a different Bernoulli curvature invariant of space forms.
- Bertrand–Diguet–Puiseux's classical local circumference/area curvature formula; recalled and compared explicitly in the preceding Buffon paper, Section 4.3.
