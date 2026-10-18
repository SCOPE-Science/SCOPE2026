# Sharp cap-incidence probability for all convex cylinders and constant-width extremizers

## Finding
For an arbitrary right convex cylinder, the probability that an isotropic motion-invariant affine plane intersects exactly one horizontal base face has an exact directional-width formula. At prescribed cylinder height and base perimeter, **precisely** constant-width bases maximize that probability. Moreover, among every positive cylinder height and every convex base, the sharp maximum is approximately \(0.640264922430907\). The theorem also determines the entire three-atom base-incidence law and the exact critical ratio at which zero-base and two-base incidences are equally probable, independently of the base shape.

Let \(w(\phi)\) denote the width of the planar base in direction \((\cos\phi,\sin\phi)\), \(L\) its perimeter, \(H\) the cylinder height, and define
\[
\bar w=\frac1{2\pi}\int_0^{2\pi}w(\phi)\,d\phi=\frac{L}{\pi},\quad
A_H=\frac1{2\pi}\int_0^{2\pi} w(\phi)\arctan\frac{H}{w(\phi)}\,d\phi,\quad
D=\frac H2+\frac L4.
\]
For \(j\in\{0,1,2\}\), the exact probabilities \(p_j=\Pr(N=j)\) are
\[
p_0=\frac{H/2-A_H/2}{D},\qquad
p_1=\frac{A_H}{D},\qquad
p_2=\frac{L/4-A_H/2}{D}.
\]
In particular
\[
p_0-p_2=\frac{2H-L}{2H+L},\qquad
\mathbb E N=\frac{2L}{2H+L}.
\]
The balance \(p_0=p_2\) occurs for every shape **exactly** at \(H=L/2\).

For every fixed \(L,H>0\),
\[
p_1\le\frac{\bar w\arctan(H/\bar w)}{D},
\]
with equality exactly for planar convex bodies of constant width. The entire equality family contains disks and noncircular constant-width bodies. At fixed \(L,H\), these are also precisely the joint minimizers of \(p_0\) and \(p_2\).

Let \(w_-:=\min_\phi w(\phi)>0\), \(w_+:=\max_\phi w(\phi)\), and \(\sigma_w^2=(2\pi)^{-1}\int_0^{2\pi}(w(\phi)-\bar w)^2\,d\phi\). The exact curvature bounds are
\[
\frac{H^3\sigma_w^2}{D(H^2+w_+^2)^2}
\le \frac{\bar w\arctan(H/\bar w)}D-p_1
\le \frac{H^3\sigma_w^2}{D(H^2+w_-^2)^2}.
\]
In the regime of widths uniformly approaching a positive constant, these bounds yield the exact leading quadratic width-variance coefficient \(H^3/[D(H^2+\bar w^2)^2]\). This provides a quantitative rigidity statement away from constant width.

With \(x:=H/\bar w\), the all-cylinder bound reduces to \(p_1\le4\arctan(x)/(2x+\pi)\). This one-variable envelope has its unique global maximizer \(x_*\in(0,\infty)\), characterized by
\[
\frac{x_*+\pi/2}{1+x_*^2}=\arctan x_*.
\]
Its approximate value is \(x_*=1.45729440014087\), and the sharp optimal probability is
\[
p_* = \frac{2}{1+x_*^2}=0.6402649224309067\ldots.
\]
Equality occurs if and only if the base has constant width and \(H=x_*L/\pi\).

## Assumptions and scope
The planar set \(B\subset\mathbb R^2\) is compact, convex and has nonempty interior; smoothness, symmetry and polygonality are not assumed. Its perimeter \(L\) and its Euclidean widths are positive and finite. The height \(H\) is any positive real. The solid is the Cartesian product \(K=B\times[-H/2,H/2]\), with genuine planar horizontal faces \(B\times\{\pm H/2\}\).

The space of *unoriented* affine planes carries the Euclidean-motion-invariant measure: choose a normal direction according to spherical area modulo sign and an offset in Lebesgue measure. Condition this sigma-finite measure on the finite-measure event that the plane intersects \(K\). Count an end face only if its intersection with the plane contains a nondegenerate line segment. Tangencies and coincidences have conditional probability zero and do not affect the law. The theorem does not address random lines, finite-thickness slabs, planes constrained to contain the origin, or non-product prismatoids.

## Proof
**1. Normal and offset geometry.** Represent the unoriented normal by \(u=(s\cos\phi,s\sin\phi,c)\), where \(c\in[0,1]\), \(s=\sqrt{1-c^2}\), and \(\phi\in[0,2\pi)\). Under spherical area modulo sign, \(c\) is uniform on \([0,1]\) and independent of uniform \(\phi\). The corresponding affine plane is \(u\cdot x=t\), with \(t\) having Lebesgue measure.

The horizontal projection of \(B\) along \(u\) is an interval of length \(a=w(\phi)s\). For fixed \(c,\phi\), the allowable offsets for hitting each of the two horizontal faces are two intervals of this same length \(a\), displaced by \(b=Hc\). Their convex hull is precisely the set of offsets for meeting \(K\) and has length \(a+b\). Their overlap length is \((a-b)_+\), while their union has length \(2a-(a-b)_+\). Consequently the offset measures of planes hitting no base, exactly one base, or both bases respectively are
\[
\ell_0=(b-a)_+,\qquad
\ell_1=2\min(a,b),\qquad
\ell_2=(a-b)_+.
\]
These expressions sum to \(a+b\) in both regimes and remain valid for nonsymmetric and nonsmooth bases.

**2. Exact polar integration.** For any \(w>0\), fix \(\phi\) and put \(a=w\sqrt{1-c^2}\), \(b=Hc\). The switching direction is \(c_*=w/\sqrt{w^2+H^2}\). Elementary integration on \([0,c_*]\) and \([c_*,1]\) yields
\[
\begin{aligned}
\int_0^1\ell_0\,dc&=\frac H2-\frac w2\arctan\frac H w,\\
\int_0^1\ell_1\,dc&=w\arctan\frac H w,\\
\int_0^1\ell_2\,dc&=\frac{\pi w}{4}-\frac w2\arctan\frac H w,\\
\int_0^1(a+b)\,dc&=\frac H2+\frac{\pi w}4.
\end{aligned}
\]
Integrate next over uniform \(\phi\). Cauchy's mean-width identity gives \(\mathbb E_\phi w=L/\pi\). The normalization is therefore \(D=H/2+L/4\), and division by \(D\) proves all three probability formulas. Subtracting the formulas and taking the first moment \(p_1+2p_2\) gives the two shape-independent identities.

**3. Fixed-perimeter sharpness and rigidity.** Define \(f_H(w)=w\arctan(H/w)\). Direct differentiation for positive \(H,w\) gives
\[
f_H''(w)=-\frac{2H^3}{(H^2+w^2)^2}<0.
\]
Strict Jensen inequality yields \(A_H\le f_H(\bar w)\), with equality if and only if \(w(\phi)\) is constant almost everywhere. Width is continuous in \(\phi\), so equality is equivalent to \(B\) having constant width in *every* direction. Such bases exist at every positive perimeter (a disk already suffices), establishing sharpness. The formulas for \(p_0,p_2\) imply simultaneous minimization.

For \(w_-\le w\le w_+\), the negative second derivative is bounded above and below by \(2H^3/(H^2+w_-^2)^2\) and \(2H^3/(H^2+w_+^2)^2\), respectively. Apply Taylor's theorem with integral remainder at \(\bar w\), average, and use \(\mathbb E(w-\bar w)=0\). The stated two-sided variance bounds follow. In a uniformly shrinking width neighborhood of \(\bar w\), both coefficients coincide to leading order, verifying the claimed sharp local quadratic coefficient.

**4. Unique global optimum over height.** For constant-width bases, \(x=H/\bar w\) reduces the envelope to \(g(x)=4\arctan(x)/(2x+\pi)\). Its derivative has the sign of
\[
q(x)=\frac{x+\pi/2}{1+x^2}-\arctan x.
\]
Here \(q(0)=\pi/2>0\), \(\lim_{x\to\infty}q(x)=-\pi/2<0\), and
\[
q'(x)=-\frac{2x(x+\pi/2)}{(1+x^2)^2}<0\qquad(x>0).
\]
Thus a unique root \(x_*\) exists, and the envelope increases then decreases. At the root, algebra using the critical equation gives \(g(x_*)=2/(1+x_*^2)\). The fixed-height equality characterization proves that these, and only these, are global maximizers. The decimal values follow from numerical root solving and are not used in the uniqueness proof.

## Verification
The accompanying standalone `check.py` reconstructs the normal-offset formulas independently by Gauss--Legendre numerical integration over the orientation coordinate \(c\), for disks, ellipses, rectangles and triangles at multiple heights, rather than evaluating only the closed expressions. It also checks probability normalization, planar Cauchy perimeter identities, strict Jensen variance bounds, curvature derivatives, and the unique optimum bracket and formula. All tests passed. These finite computations are diagnostic; the proof above establishes the all-convex-bases and all-heights quantifiers analytically.

## Relationship to prior work
Cruz-Orive (2026), *Stereology for the Weibel-Palade Bodies*, Corollary 2 (equation 27, page 99), already derives the cap-incidence distribution for **right circular cylinders** and motion-invariant random affine planes. Setting the present base to a disk of radius \(r\) gives constant width \(2r\), and taking \(H=2h\) reproduces all three formulas of that corollary exactly. The circular formula and the choice of plane probability model are established prior work, not claimed as discoveries here.

Kellerer (1971), *Considerations on the Random Traversal of Convex Bodies and Solutions for General Cylinders*, gives distributions of **line chord lengths** in cylinders with arbitrary convex bases under an isotropic field of straight tracks, rather than the number of faces intersected by random affine planes. Neither that line problem nor the circular 2026 special case implies the constant-width extremal classification without the arbitrary-base width reduction and strict-concavity argument. Classical Cauchy perimeter/mean-width and Jensen inequalities are used as standard tools.

## Limitations
The three-state statistic records incidences with horizontal end faces only; it is not a full section-shape distribution. It does not treat slabs of positive thickness or arbitrary oblique cylinders. The equality class is **all** positive-width constant-width bases, not only circles. No assertion of absolute historical priority against unindexed older stereological literature is made. The local quadratic coefficient is sharp in the small-anisotropy regime; the finite-width sandwich need not have globally attainable equality for nonconstant widths. No external independent validation is claimed.

## References
1. L. M. Cruz-Orive, *Stereology for the Weibel-Palade Bodies*, **Image Analysis and Stereology** 45 (2026), 95--101, DOI: 10.5566/ias.4005, original public publication 2026-06-17, https://ias-iss.org/ojs/IAS/article/download/4005/1267/10162 . Relevant sections: pages 96--99, Corollary 2, equation (27).
2. A. M. Kellerer, *Considerations on the Random Traversal of Convex Bodies and Solutions for General Cylinders*, **Radiation Research** 47 (1971), 359--376, https://websites.umich.edu/~nersb590/CourseLibrary/Kellerer.pdf . Relevant sections: 2 and 4; straight-track model distinguished from plane probes.
3. Cauchy's perimeter projection theorem (classical mean-width identity), applied in the planar convex-body setting; and the classical strict Jensen inequality.
