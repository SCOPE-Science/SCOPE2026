# Exact Crofton polygon-type law for right triangular prisms

## Finding

Let \(T\subset\mathbb R^2\) be any nondegenerate triangle, let \(L>0\) be its perimeter, let \(h>0\), and put \(P=T\times[0,h]\subset\mathbb R^3\). Sample an unoriented affine plane by Euclidean-motion-invariant plane measure, conditional on meeting the interior of \(P\). Write \(N\) for the number of vertices in its polygonal section. Then \(N\in\{3,4,5\}\) almost surely, and **the complete distribution is elementary for every triangular base**. In particular, its triangle–pentagon probability gap is independent of the base triangle's shape:

\[
\boxed{\Pr(N=3)-\Pr(N=5)=\frac{2h}{L+2h}>0.}
\]

The other information needed for the complete law is one explicitly evaluated finite elementary sum. For a unit vector \(e_\theta=(\cos\theta,\sin\theta)\), sort the three numbers \(v_i\cdot e_\theta\) for the vertices \(v_0,v_1,v_2\) of \(T\) as \(a_\theta\le b_\theta\le c_\theta\) and put \(p_\theta=b_\theta-a_\theta\), \(q_\theta=c_\theta-b_\theta\). Define \(g_h(s)=s\arctan(h/s)\) for \(s>0\), and \(g_h(0)=0\). Then

\[
\boxed{\Pr(N=5)=\frac{1}{\pi(L+2h)}\int_0^{2\pi}
\bigl[g_h(p_\theta)+g_h(q_\theta)-g_h(p_\theta+q_\theta)\bigr]d\theta.}
\]

This integral is **not** an unevaluated numerical prescription: a finite, explicit arctangent antiderivative rule below evaluates it without quadrature, using at most the six intervals between directions perpendicular to the sides of \(T\). The remaining probabilities satisfy

\[
\Pr(N=3)=\Pr(N=5)+\frac{2h}{L+2h},\qquad
\Pr(N=4)=1-\Pr(N=3)-\Pr(N=5).
\]

All three probabilities are strictly between zero and one for \(h>0\).

For an equilateral base of side one, set \(s=\sqrt{1+h^2}\) and

\[
J(h)=\frac\pi2\left(1+\frac h3-s\right)
-\arctan\frac{2h}{\sqrt3}
+2s\arctan\frac{h}{\sqrt3s}.
\]

Then \(\Pr(N=5)=12J(h)/(\pi(3+2h))\). At unit height \(h=1\), the complete distribution in increasing order of side count is approximately \((0.485692077742520,\ 0.428615844514960,\ 0.085692077742520)\).

## Assumptions and scope

The triangle may be scalene, obtuse, or arbitrarily thin provided it is nondegenerate. The prism is right: its lateral edges are perpendicular to the triangular base. Generic means the cutting plane misses all six vertices and contains no edge; these exceptions have zero invariant-plane measure. A plane is represented by \(u\cdot x=t\), with \(u\in S^2\), and the invariant measure is a constant multiple of \(d\omega(u)\,dt\). Double counting \((u,t)\) and \((-u,-t)\) cancels under conditioning. This is **not** the Haar measure on planes through a fixed center, nor a uniformly sampled orientation followed by a conditional-uniform offset without width weighting.

## Proof

**1. Offset classification.** Fix \(u=(u_x,u_y,u_z)\) with \(u_z>0\), and sort its three bottom-vertex projection heights as \(a<b<c\). Write \(H=hu_z\), \(p=b-a\), and \(q=c-b\). The two triangular faces are intersected by the plane \(u\cdot x=t\) precisely when \(t\in(a,c)\cap(a+H,c+H)\). The projection ranges of the three rectangular side faces, which correspond to the three pairs of triangle vertices, have common intersection \((b,b+H)\). Thus a generic section has five sides if and only if

\[
\max(a+H,b)<t<\min(c,b+H).
\]

The length of this offset interval is

\[
\ell_5(u)=\bigl[\min(q,H)-\max(0,H-p)\bigr]_+
=H_+-(H-p)_+-(H-q)_++(H-p-q)_+.
\]

Reflection in the horizontal midplane handles \(u_z<0\). A right triangular prism has exactly five facets, so no section can have more than five sides; every nondegenerate planar convex section has at least three.

**2. Integration over orientations.** On the upper hemisphere write \(u=(\sin\phi\,e_\theta,\cos\phi)\), with \(0\le\phi\le\pi/2\). In the preceding expression substitute \(p=\sin\phi\,p_\theta\), \(q=\sin\phi\,q_\theta\), \(H=h\cos\phi\). For \(c\ge0\), direct integration gives

\[
\int_0^{\pi/2}\sin\phi\,\bigl(h\cos\phi-c\sin\phi\bigr)_+\,d\phi
=\frac12\bigl[h-c\arctan(h/c)\bigr],
\]

with the continuous interpretation at \(c=0\). Summing the four terms and both hemispheres yields exactly the numerator integral displayed in the finding. This is an equality of invariant plane measures, not an approximation.

**3. Normalizing measure.** The width of the prism in direction \(u\) is the directional width of its triangular base plus \(h|u_z|\). Cauchy's planar width identity, \(\int_0^{2\pi}w_T(e_\theta)\,d\theta=2L\), and \(\int_0^\pi\sin^2\phi\,d\phi=\pi/2\), give

\[
\int_{S^2}w_P(u)\,d\omega(u)=\pi(L+2h).
\]

This is the total measure of planes meeting the prism, up to the common harmless normalization constant. Division gives the stated pentagon probability.

**4. Triangle–pentagon complementarity.** For each generic direction \(u\), the offset measure of planes intersecting a given polyhedral edge \([A,B]\) is \(|u\cdot(B-A)|\). Integrating over the sphere yields \(\int_{S^2}|u\cdot(B-A)|\,d\omega(u)=2\pi\|B-A\|\). The prism has six horizontal edges of total length \(2L\) and three vertical edges of total length \(3h\); a generic section's number of vertices is precisely the number of crossed edges. Hence

\[
\mathbb E N=\frac{2\pi(2L+3h)}{\pi(L+2h)}
=\frac{4L+6h}{L+2h}.
\]

Since \(N\in\{3,4,5\}\), the identity \(\mathbb EN=4-\Pr(N=3)+\Pr(N=5)\) now gives \(\Pr(N=3)-\Pr(N=5)=2h/(L+2h)\), with no base-angle terms.

**5. Finite elementary evaluation.** Split \([0,2\pi]\) at the six directions perpendicular to the three sides of \(T\). Within each open interval \((\alpha,\beta)\), the order of the three projected vertices is fixed, say \(i,j,k\). Thus the two consecutive positive gaps are \((v_j-v_i)\cdot e_\theta\) and \((v_k-v_j)\cdot e_\theta\); their sum is \((v_k-v_i)\cdot e_\theta\). Define, for \(\kappa>0\) and \(-\pi/2\le t\le\pi/2\),

\[
F_\kappa(t)=\sin t\arctan\frac{\kappa}{\cos t}+\kappa t
-\sqrt{1+\kappa^2}\arctan\frac{\kappa\tan t}{\sqrt{1+\kappa^2}},
\]

extended continuously to the endpoints. Direct differentiation proves \(F'_\kappa(t)=\cos t\arctan(\kappa/\cos t)\). For every nonzero directed side difference \(d\) with \(d\cdot e_\theta>0\) throughout such an interval, put \(r=\|d\|\), \(\delta=\arg(d)\), and take the unique continuous lift \(t_\theta=\theta-\delta\pmod{2\pi}\) in \((-\pi/2,\pi/2)\). Then

\[
\int_\alpha^\beta g_h(d\cdot e_\theta)\,d\theta
=r\left[F_{h/r}(t_\beta)-F_{h/r}(t_\alpha)\right].
\]

Apply this rule to \(d=v_j-v_i\), \(v_k-v_j\), and \(v_k-v_i\) with coefficients \(+1,+1,-1\) on each interval and add the at most seven interval contributions. This is an exact finite combination of elementary radicals and arctangents for every right triangular prism, with a fully specified branch convention. For the equilateral triangle, symmetry reduces this sum to \(12[F_h(\pi/2)-2F_h(\pi/6)]\), giving the displayed simplified formula.

**6. Support and strict positivity.** Horizontal cutting planes produce triangular sections on an open set of nearby planes. Slightly tilted vertical-section planes through an interior base chord produce quadrilaterals. Choose any planar direction with three distinct projected triangle vertices and vary \(u_z>0\) so that \(0<H<p+q\) and \(\max(0,H-p)<\min(q,H)\); this is an open set yielding pentagons. Thus each of the three probabilities is positive and, because their sum is one, below one.

## Verification

The standalone `verify.py` is included. Run `python3 verify.py` (standard Python library only). It checks the finite elementary formula against separately integrated trigonometric expressions on 32 triangle/height cases, verifies the **entire pentagonal-offset interval** against all nine prism edges for 3,600 generic directions across scalene and equilateral bases, and independently samples 180,000 motion-invariant random affine planes without omitting the orientation-dependent hitting weight. Its output is `TRIANGULAR_PRISM_CHECK_OK`. These finite checks corroborate, but are not substitutes for, the preceding all-parameter analytic proof.

## Relationship to prior work

Wang's 2011 theorem identifies triangular prisms as universal tilers: every nondegenerate plane section tiles the plane. It concerns tilability, not the invariant-plane **probabilities** of three-, four-, and five-sided sections. Earlier stereological work of Voss (1982) describes exact frequency methods for *some* families of polyhedra; Ohser and Mücklich (1995) study regular-prism ensembles via stereological kernels and computer simulation. Their accessible abstracts give important background but do not themselves state the arbitrary-triangular-base finite elementary law or the perimeter-only triangle–pentagon gap. The full texts of these two historically relevant works were not accessible for a definitive priority comparison; they remain genuine overlap risks. This result is not derived by changing the labels in a five-faced pyramid formula: a triangular prism has six vertices and nine edges rather than five vertices and eight edges, and the probability model explicitly uses affine planes rather than central sections or orthogonal shadows.

## Limitations

The formula assumes right rather than oblique triangular prisms, Euclidean isotropic invariant affine-plane sampling, and nondegenerate bases and positive height. It does not claim a full probability distribution of section areas, angles, or perimeters; it concerns polygon vertex counts only. The sharp structural gap follows from established integral-geometric identities, while the joint closed law requires the offset analysis. Historical priority remains subject to inspection of the full 1982 and 1995 stereological works and older tabulations. No independent mathematical audit has been performed.

## References

1. D. G. L. Wang, *Determining All Universal Tilers*, arXiv:1110.1715, first version 8 October 2011, https://arxiv.org/abs/1110.1715.
2. K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy 128 (1982), 111–120, DOI:10.1111/j.1365-2818.1982.tb00443.x; abstract inspected, full text unavailable.
3. J. Ohser and F. Mücklich, *Stereology for some classes of polyhedrons*, Advances in Applied Probability 27 (1995), 384–396, DOI:10.2307/1427832; abstract and bibliographic references inspected, full text unavailable.
4. L. A. Santaló, *Integral Geometry and Geometric Probability*, Addison-Wesley, 1976; standard invariant-plane and Cauchy width background.
