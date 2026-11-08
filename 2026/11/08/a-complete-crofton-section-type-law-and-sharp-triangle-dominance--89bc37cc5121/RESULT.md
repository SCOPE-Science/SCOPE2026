# A complete Crofton section-type law and sharp triangle dominance for right rectangular pyramids

## Finding
For arbitrary real \(a,b,h>0\), define the nondegenerate right rectangular pyramid
\[
K(a,b,h)=\operatorname{conv}\{(\pm a,\pm b,0),(0,0,h)\}\subset\mathbb R^3.
\]
Select an unoriented affine plane from Euclidean-motion-invariant measure, conditioned on its meeting \(K(a,b,h)\) in a nondegenerate polygon. Let \(N\) be the number of section vertices. Define
\[
L=\sqrt{a^2+b^2+h^2},\quad
\phi=\arctan\frac{hL}{ab},\quad
D=\pi(a+b)-a\arctan\frac hb-b\arctan\frac ha+L\phi.
\]
For \(0\leq t\leq\pi/2\), put \(c_+(t)=a\cos t+b\sin t\) and \(c_-(t)=|a\cos t-b\sin t|\), and set
\[
J=\int_0^{\pi/2}\left[c_+(t)\arctan\frac{h}{c_+(t)}-c_-(t)\arctan\frac{h}{c_-(t)}\right]dt.
\]
The product \(c\arctan(h/c)\) is defined to be zero at \(c=0\). Then \(N\in\{3,4,5\}\) almost surely, and its **entire law** is
\[
\boxed{\mathbb P(N=5)=\frac JD,\quad
\mathbb P(N=4)=\frac{2\pi(a+b+L)}D-3-\frac{2J}D,\quad
\mathbb P(N=3)=4-\frac{2\pi(a+b+L)}D+\frac JD.}
\]
All three probabilities are positive. The expected section vertex count is
\[
\boxed{\mathbb EN=\frac{2\pi(a+b+L)}D.}
\]
For every fixed \(a,b>0\), this expectation increases **strictly** with \(h>0\), from the limit \(2+2\sqrt{a^2+b^2}/(a+b)\) as \(h\downarrow0\) to the limit \(4\) as \(h\to\infty\). Consequently the sharp universal bounds and strict triangular-section dominance are
\[
\boxed{2+\sqrt2<\mathbb EN<4,\qquad\mathbb P(N=3)>\mathbb P(N=5).}
\]
The lower expectation constant is approached by flat square-based pyramids; the upper one is approached by increasingly tall pyramids. Neither endpoint is attained for a nondegenerate finite pyramid.

## Assumptions and scope
The random-plane law is **not** the law obtained by first choosing a uniform direction and then a uniform offset between the two supporting planes. Write an oriented plane as \(H(u,s)=\{x:\langle u,x\rangle=s\}\), with \(u\in S^2\) and \(s\in\mathbb R\). The motion-invariant measure is \(d\sigma(u)\,ds\), where \(\sigma\) is normalized uniform spherical measure. Conditional on intersection with \(K\), the normal \(u\) is weighted by the directional width of \(K\). Counting each unoriented plane twice cancels in all conditional ratios. Plane cuts through a vertex or an edge form a null set. All angles in the formulas are principal, and all denominators are strictly positive.

## Proof
**1. Width normalization and expected vertex count.** Every generic plane meeting a polyhedron cuts one edge for each vertex in its intersection polygon. For an edge of vector \(v\), integrating over offsets \(s\) gives an intersection interval of length \(|\langle u,v\rangle|\). Because \(\int_{S^2}|\langle u,v\rangle|d\sigma(u)=|v|/2\), and the pyramid has two base edges of length \(2a\), two of length \(2b\), and four lateral edges of length \(L\), the total unnormalized expected section-vertex integral equals \(2(a+b+L)\).

The standard polyhedral mean-width identity (equivalently, the edge form of the Cauchy support-function formula) is
\[
\int_{S^2}w_K(u)\,d\sigma(u)=\frac1{4\pi}\sum_{e}|e|\,\beta_e,
\]
where \(\beta_e\) is the exterior dihedral angle between the outward normals of the two faces incident to edge \(e\). The base-edge exterior angles are \(\pi-\arctan(h/b)\) (for length \(2a\)) and \(\pi-\arctan(h/a)\) (for length \(2b\)). The four lateral edges each have exterior angle
\[
\arccos\frac{ab}{\sqrt{(a^2+h^2)(b^2+h^2)}}
=\arctan\frac{h\sqrt{a^2+b^2+h^2}}{ab}=\phi.
\]
Thus the total edge-angle sum is \(4D\), giving \(\int w_K\,d\sigma=D/\pi\). Dividing the crossing-edge integral by this hit-plane normalizer proves the stated formula for \(\mathbb EN\).

**2. Five-sided sections.** By the coordinate reflection symmetries and reversal of the oriented plane, reduce to the positive octant of a normal with absolute coordinate magnitudes. Put \(X=a|u_x|\), \(Y=b|u_y|\), \(Z=h|u_z|\). The four vertex projections of the base have the ordered values \(-X-Y,-|X-Y|,|X-Y|,X+Y\). The apex projection has magnitude \(Z\), with the appropriate sign. Exactly five edges of the pyramid cross an offset plane precisely when the apex is on the same side as the unique extremal base vertex and the other three base vertices are on the opposite side. The total admissible offset length, for each such normal, is exactly
\[
\ell_5(u)=(Z-|X-Y|)_+-(Z-X-Y)_+.
\]
Indeed the interval starts when the offset passes the second-highest base value \(|X-Y|\) and ends at the smaller of the apex and highest base value, \(\min\{Z,X+Y\}\); the negative-octant counterpart is symmetric.

Parameterize the positive octant by \(u=(\sin\theta\cos t,\sin\theta\sin t,\cos\theta)\), where \(0\le\theta,t\le\pi/2\). For \(c\ge0\) one has the elementary identity
\[
\int_0^{\pi/2}(h\cos\theta-c\sin\theta)_+\sin\theta\,d\theta
=\frac12\left(h-c\arctan\frac hc\right),
\]
with its continuous value \(h/2\) at \(c=0\). The eight octants together carry spherical measure factor \(2/\pi\), so integration of \(\ell_5\) gives \(J/\pi\). Division by the total hit measure \(D/\pi\) proves \(\mathbb P(N=5)=J/D\).

**3. The remaining law and positivity.** A generic plane section has 3, 4 or 5 sides because the pyramid has five faces, each met in at most one side. Thus \(p_3+p_4+p_5=1\) and \(3p_3+4p_4+5p_5=\mathbb EN\), giving the two remaining probabilities by linear algebra. Pentagonal sections occur on an open set of normals and offsets with \(Z>|X-Y|\), hence \(p_5>0\). Four-sided sections occur for normals sufficiently close to vertical and offsets in a compact subinterval of \((0,h)\), hence \(p_4>0\). The proof below gives \(p_3-p_5=4-\mathbb EN>0\), hence \(p_3>0\).

**4. Strict height monotonicity and sharpness.** Differentiation of the explicitly given \(D\), including cancellation of the two base-edge derivatives against the angle derivative, yields the exact identity
\[
D'(h)=\frac hL\phi,\qquad L'(h)=\frac hL.
\]
It follows that the sign of the derivative of \(\mathbb EN=2\pi(a+b+L)/D\) is the sign of
\[
D-(a+b+L)\phi
=a\left(\pi-\arctan\frac hb-\phi\right)
+b\left(\pi-\arctan\frac ha-\phi\right).
\]
Both brackets are positive since \(\pi-\arctan(h/a)>\pi/2\), \(\pi-\arctan(h/b)>\pi/2\), whereas \(0<\phi<\pi/2\). Therefore the expectation is strictly increasing in height. Substituting \(h\downarrow0\) gives \(D\to\pi(a+b)\), \(L\to\sqrt{a^2+b^2}\); dividing leading \(h\to\infty\) terms gives \(\mathbb EN\to4\). Finally \(\sqrt{a^2+b^2}/(a+b)\ge1/\sqrt2\) with equality only when \(a=b\), proving the sharp universal interval by the indicated degenerations. The identity \(p_3-p_5=4-\mathbb EN\) proves strict triangle dominance, and completes the proof.

## Verification
The included `verify.py` is a standalone standard-library Python 3 script. Run `python3 verify.py`. It independently computes section vertex counts by intersected edges for five different parameter triples, with isotropic random normals and a **common fixed offset interval followed by rejection** to implement the invariant hit-conditioned plane measure. It compares those empirical frequencies to the exact quadrature formulas, differentiates the width normalizer by central differences to check \(D'(h)=(h/L)\phi\), checks all probability signs, and numerically approaches both sharp expectation boundaries. The deterministic run used 450,000 proposed orientations and retained 241,034 meeting planes; it reported `RECTANGULAR_PYRAMID_CROFTON_LAW_OK`. Finite numerical tests corroborate but cannot establish any universally quantified claim; the proof above is analytic.

## Relationship to prior work
Kim, Yaskin and Zvavitch (2015) investigate distribution functions of section **area** and projection **area**, including noncentral sections, but not the combinatorial polygon-type law under stationary random affine planes. The published right-rectangular-pyramid five-vertex shadow formula concerns **orthogonal projection**, where the sampling is of target-plane directions rather than affine section offsets; it does not imply this three-point random-section distribution, the hit-conditioned normal bias, or the triangular dominance. Ohser and Mücklich (1995) discuss stereological profiles of regular prisms and random polyhedra, but their complete text was unavailable for comparison; priority relative to that source is a residual risk. These comparisons distinguish scientific statements, not merely their names. The integral-geometric edge and mean-width identities used in the proof are classical and not claimed as original.

## Limitations
The pyramid must have an apex directly above the center of a rectangle, and the sampling measure must be invariant under all Euclidean motions. The formula for \(p_5\) is an exact one-dimensional elementary quadrature, not a claim of an antiderivative in elementary functions. The result neither covers skew pyramids nor arbitrary polyhedra, and it does not address distributions of section areas or perimeters. Indexed and accessible sources do not prove absolute historical uniqueness; an inaccessible stereology source remains a priority risk. Independent mathematical validation has not been performed.

## References
1. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 2015-12-22, https://arxiv.org/html/1512.07289v1 .
2. J. Ohser and F. Mücklich, *Stereology for some classes of polyhedrons*, *Advances in Applied Probability* **27** (1995), 384–396, DOI:10.2307/1427832, https://doi.org/10.2307/1427832 .
3. *Exact five-vertex shadow law and unique height optimum for right rectangular pyramids*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-five-vertex-shadow-law-and-unique-height-optimum-for-right--2273575e8a0a .
