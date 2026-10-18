# Exact two-harmonic convexity domain and intrinsic-volume laws for zonal support bodies

## Finding
Fix a unit axis \(e\in\mathbb R^3\). Let \(P_2(t)=(3t^2-1)/2\) and \(P_4(t)=(35t^4-30t^2+3)/8\), and define on \(S^2\)
\[
h_{a,b}(u)=1+aP_2(u\cdot e)+bP_4(u\cdot e),\qquad (a,b)\in\mathbb R^2.
\]
The positively homogeneous extension of \(h_{a,b}\) is the support function of a compact, full-dimensional convex body if and only if
\[
-\frac{27}{217}\le b\le\frac6{49},\qquad L(b)\le a\le U(b),
\]
where
\[
L(b)=\begin{cases}
\dfrac{-55b-5\sqrt{-14b(27+217b)}}{27},&-\dfrac{27}{217}\le b\le-\dfrac{24}{679},\\
\dfrac{57b-8}{20},&-\dfrac{24}{679}\le b\le\dfrac6{49},
\end{cases}
\]
and
\[
U(b)=\begin{cases}
\dfrac{-55b+5\sqrt{-14b(27+217b)}}{27},&-\dfrac{27}{217}\le b\le-\dfrac1{21},\\
\dfrac{1-9b}{2},&-\dfrac1{21}\le b\le\dfrac6{49}.
\end{cases}
\]
Thus the exact admissible coefficient set has two straight boundary portions and two curved portions meeting at different rational parameters. Its extreme \(b\)-sections are single points: \((a,b)=(55/217,-27/217)\) and \((-5/98,6/49)\).

Every admissible body is origin symmetric, rotationally symmetric about \(e\), has mean width \(2\), and is strictly convex (though some principal curvature radii vanish at the boundary of the coefficient region). Its surface area and enclosed volume are respectively
\[
S(a,b)=4\pi\left(1-\frac25a^2-b^2\right),
\]
\[
V(a,b)=\frac{4\pi}{3}\left(1-\frac65a^2-3b^2+\frac47a^3+\frac{18}{35}a^2b+\frac{300}{77}ab^2+\frac{2448}{1001}b^3\right).
\]

## Assumptions and scope
All parameter inequalities include their endpoints. Support functions are interpreted on all of \(\mathbb R^3\) by positive homogeneous extension \(H(v)=\|v\|h(v/\|v\|)\) for \(v\ne0\), \(H(0)=0\). Convexity refers to finite-dimensional Euclidean convexity; the body is uniquely determined by this support function. On the boundary of the admissible region, formulas for curvature-radius tensors are interpreted as nonnegative semidefinite limits. A vanishing radius is not a negative curvature and does not imply a line segment of the body.

## Proof
**1. A single quadratic tests convexity.** For a smooth function on the sphere, the homogeneous extension is convex if and only if its tangential radius tensor \(R=\nabla^2_{S^2}h+hI\) is everywhere positive semidefinite. Set \(z=u\cdot e\) and \(x=z^2\in[0,1]\). The eigenvalues along meridians and parallels are
\[
\lambda_m(x)=Q_{a,b}(x):=1+\frac{5-9x}{2}a+\frac{-525x^2+510x-57}{8}b,
\]
\[
\lambda_p(x)=G_{a,b}(x):=1-\frac{3x+1}{2}a+\frac{-105x^2+30x+3}{8}b.
\]
Here \(\lambda_p(1)=\lambda_m(1)\), with the eigenvalues interpreted by continuity at the poles. Direct differentiation gives
\[
Q(x)=G(x)-2(1-x)G'(x).
\]
Consequently,
\[
\frac{d}{dx}\big(\sqrt{1-x}\,G(x)\big)=-\frac{Q(x)}{2\sqrt{1-x}}.
\]
Integrating from \(x\) to \(1\) and using the finite polynomial endpoint shows
\[
G(x)=\frac{1}{2\sqrt{1-x}}\int_x^1\frac{Q(t)}{\sqrt{1-t}}\,dt\ge0\quad(0\le x<1)
\]
whenever \(Q\ge0\); at \(x=1\) both eigenvalues equal \(Q(1)\). Hence convexity is **equivalent** to \(Q_{a,b}(x)\ge0\) for every \(x\in[0,1]\). The integral also shows \(G(x)>0\) for \(x<1\) whenever \(Q\ge0\), because \(Q\) cannot vanish identically (its constant-one term and the coefficient equations would be inconsistent).

**2. Global parameter bounds and equality.** The three fixed-angle tests
\[
Q(0)=1+\frac52a-\frac{57}{8}b,\qquad Q(1)=1-2a-9b,\qquad Q(5/9)=1+\frac{217}{27}b
\]
force \(b\ge-27/217\), \(a\ge(57b-8)/20\), and \(a\le(1-9b)/2\). The two last conditions together force \(b\le6/49\). At the lower endpoint \(b=-27/217\), \(Q(5/9)=0\) occurs at an interior point, so \(Q'(5/9)=0\), forcing \(a=55/217\). At the upper endpoint, \(Q(0)=Q(1)=0\), forcing \(a=-5/98\). Both pairs indeed make \(Q\ge0\).

**3. Exact two-parameter boundary.** For \(b\ge0\), \(Q\) is concave in \(x\); its minimum on \([0,1]\) lies at an endpoint. Hence the two straight-line conditions in Step 2 are necessary and sufficient. For \(b<0\), the quadratic is convex. Its stationary point is
\[
x_* = \frac{85b-6a}{175b}.
\]
When \(a\le85b/6\), its minimum lies at \(x=0\); when \(a\ge-15b\), its minimum lies at \(x=1\). For \(85b/6<a<-15b\), the minimum occurs at \(x_*\in(0,1)\), and exact completion of the square gives
\[
Q(x_*)=\frac{27a^2+110ab+2925b^2+350b}{350b}.
\]
Since \(b<0\), the interior positivity condition is the quadratic inequality
\[
27a^2+110ab+2925b^2+350b\le0.
\]
Its boundary roots are
\[
a_\pm(b)=\frac{-55b\pm5\sqrt{-14b(27+217b)}}{27}.
\]
The negative-root boundary first meets the endpoint branch at \(b=-24/679\), where \(a=-340/679\) and \(x_*=0\). The positive-root boundary meets the other endpoint branch at \(b=-1/21\), where \(a=5/7\) and \(x_*=1\). Comparing which vertex or endpoint realizes the quadratic minimum yields precisely the stated functions \(L,U\). Conversely, every point between those graphs passes all applicable endpoint/vertex tests. This proves necessity and sufficiency for all real parameters, not merely sampled coefficients.

**4. Curvature-degeneracy geometry.** On the open curved pieces \(a=a_\pm(b)\), the meridional radius has a double zero at a unique \(x_*\in(0,1)\), giving two opposite latitude circles of zero meridional radius. On the open lower straight piece \(a=(57b-8)/20\), the meridional radius vanishes only at the equator \(x=0\); on the open upper straight piece \(a=(1-9b)/2\), the common polar radius vanishes only at the two poles \(x=1\). At the joining parameters these limits coincide. At \((a,b)=(-5/98,6/49)\), both equatorial and polar degeneracies occur, while at \((55/217,-27/217)\) there is a double zero at \(x=5/9\). The strict positivity of \(G\) away from the poles prevents any other azimuthal degeneracy. Smoothness of the support function gives a unique support point for each outer normal; hence no admissible body has a boundary segment and all are strictly convex. A smooth nonzero, origin-symmetric support function cannot describe a lower-dimensional body: a lower-dimensional non-singleton body would have multiple supporting points at a normal to its affine span, contradicting smoothness. Thus the bodies are full-dimensional.

**5. Intrinsic-volume identities.** For strictly positive curvature radii, the Gauss-map identities for surface area and volume read
\[
S=\int_{S^2}\lambda_m\lambda_p\,d\omega,
\qquad V=\frac13\int_{S^2}h\lambda_m\lambda_p\,d\omega.
\]
Using the even-polynomial expressions above and \(d\omega=2\pi\,dz\) for axially symmetric integrands, exact integration of the two polynomials gives the displayed formulas, with no numerical approximations. Orthogonality of \(P_2,P_4\) gives \(\int_{S^2}h\,d\omega=4\pi\), so the mean width is \(2\). At parameter-domain boundaries, replace \(h\) by \((1-\epsilon)h+\epsilon\) for \(0<\epsilon<1\); this adds \(\epsilon I\) to the curvature-radius tensor and gives strictly positive radii. Letting \(\epsilon\to0\) extends the surface-area and volume identities continuously to all admissible boundary pairs.

## Verification
Run `python check.py` (Python 3 with SymPy/mpmath). The checker uses exact symbolic differentiation and integration to verify both curvature eigenvalues, the meridional–parallel identity, the quadratic discriminant and boundary joins, and the area and volume polynomials. It additionally checks 50,000 independently generated coefficient pairs against the global minimization of a quadratic and compares numerical spherical integrals with the exact formulas at 40-digit precision. These finite numerical comparisons are corroboration only; Steps 1–5 give the all-parameter proof.

## Relationship to prior work
General smooth convex-body support and Gauss-map theory implies the radius-tensor test and area/volume integral formulas used here; neither is claimed as new. Piastra and Virga (2015), especially their Introduction and Appendices A.1–A.2, treat general axially symmetric convex bodies and Legendre-expanded excluded volumes, but do not state a sharp convexity coefficient domain for the particular even two-mode support family above. Garboczi and Bullard (2013) study spherical-harmonic shape descriptions and numerical convexity diagnostics for **radial** representations of star-shaped particles, a different representation from the support parametrization used here. Nearby published mathematical results treat an odd single-mode zonal constant-width family or an octahedrally symmetric quartic support perturbation; neither specifies nor implies the two-parameter even zonal domain or its distinct latitude-degeneracy transitions. The contribution assessed here is the complete exact coefficient-domain and degeneracy classification, with associated explicit intrinsic volumes, not the classical general criterion itself.

## Limitations
The theorem concerns precisely the normalized degree-two and degree-four **zonal** Legendre support family in three Euclidean dimensions. It does not classify arbitrary spherical-harmonic mixtures, off-axis harmonics, other dimensions, or all axisymmetric convex bodies. On the coefficient boundary, support functions remain smooth but their corresponding convex boundaries need not have positive Gaussian curvature everywhere. Priority beyond the compared records is not proved; exact historical novelty remains subject to broader external review. Independent mathematical validation has not been performed.

## References
1. M. Piastra and E. G. Virga, *Explicit excluded volume of cylindrically symmetric convex bodies*, first public preprint 16 March 2015, arXiv:1503.04667, https://arxiv.org/abs/1503.04667. In particular, Introduction, Appendix A.1, Appendix A.2.
2. E. J. Garboczi and J. W. Bullard, *Contact function, uniform-thickness shell volume, and convexity measure for 3D star-shaped random particles*, publicly dated 15 March 2013, Powder Technology 237, DOI:10.1016/j.powtec.2013.01.019, https://www.nist.gov/publications/contact-function-uniform-thickness-shell-volume-and-convexity-measure-3d-star-shaped.
3. *Sharp convexity and volume hierarchy of one-mode zonal constant-width solids*, published mathematical record `2026/10/11/SCOPE-sharp-convexity-and-volume-hierarchy-of-one-mode-zonal-constant--88fd1a426148`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-convexity-and-volume-hierarchy-of-one-mode-zonal-constant--88fd1a426148.
4. *Sharp convexity and volume of the octahedral quartic support family*, geometric research record identifying a distinct one-parameter cubic-symmetry support family.
