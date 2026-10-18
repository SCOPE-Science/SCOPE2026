# Exact Haar diametral-section law for products of two Euclidean disks

## Finding
For every real \(h>0\), put \(K_h=B_2^2\times hB_2^2\subset\mathbb R^4\), where \(B_2^2\) denotes the closed unit Euclidean disk and the product carries the ordinary Euclidean metric. Let \(E\) be Haar-uniform in the real Grassmannian \(\operatorname{Gr}(2,4)\). The exact probability that a central planar section retains the entire ambient diameter is
\[
\Pr\!\left\{\operatorname{diam}(K_h\cap E)=\operatorname{diam}(K_h)\right\}
=\frac{\pi h}{2(1+h^2)}.
\]
The probability has the unique global maximum \(\pi/4\) at equal factor radii \(h=1\). It is unchanged by exchanging the two factor radii, that is, replacing \(h\) by \(1/h\), and tends to zero linearly at either extreme aspect ratio.

The section dimension matters sharply: when \(E\) is Haar-uniform in \(\operatorname{Gr}(k,4)\), the full-diameter probability is \(0\) for \(k=1\), the displayed expression for \(k=2\), and \(1\) for \(k=3,4\). For \(k=3\), full-diameter preservation holds for *every* three-dimensional linear subspace, not merely almost surely.

## Assumptions and scope
The product consists of two genuine disks of positive radii \(1\) and \(h\). Every section is through the origin and is taken in a linear subspace with rotation-invariant (normalized Haar) law. Diameter means maximal ambient Euclidean distance between points. A uniformly random unoriented plane can equivalently be obtained by forgetting the orientation of a uniformly random oriented plane. No affine offsets or alternative metrics are included.

## Proof
**1. The critical Rayleigh quotient.** The full body is centrally symmetric, so its Euclidean diameter is twice its farthest distance from the origin:
\[
\operatorname{diam}(K_h)=2\sqrt{1+h^2}.
\]
Fix a two-plane \(E\), choose orthonormal column vectors in a matrix \(U\in\mathbb R^{4\times2}\), and set
\[
T=U^{\mathsf T}\begin{pmatrix}I_2&0\\0&0\end{pmatrix}U.
\]
Its eigenvalues \(0\le\lambda_1\le\lambda_2\le1\) are squared principal cosines between \(E\) and the first coordinate two-plane. If \(v\in E\) is unit length and \(t\) is the squared norm of its first two coordinates, then the ray through \(v\) intersects \(K_h\) in a centered segment with half-length
\[
\rho(v)=\min\left\{\frac1{\sqrt t},\frac h{\sqrt{1-t}}\right\},
\]
with the obvious extended interpretation at the endpoints. Equality \(\rho(v)=\sqrt{1+h^2}\) holds if and only if \(t=c:=1/(1+h^2)\), in which case both disk constraints are active. As \(v\) traverses the unit circle in \(E\), its Rayleigh quotient \(t\) assumes every value in \([\lambda_1,\lambda_2]\). Therefore the full-diameter event is exactly
\[
\lambda_1\le c\le\lambda_2. \tag{1}
\]

**2. Two independent uniform coordinates on the oriented Grassmannian.** Lift the random plane to a uniformly oriented plane with orthonormal basis \((u,v)\), and form the unit decomposable bivector \(W=u\wedge v\) in \(\Lambda^2\mathbb R^4\). Let \(*\) denote the Hodge star for the fixed standard orientation. Since \(W\) is simple, \(W\wedge W=0\), equivalently \(\langle W,*W\rangle=0\). Consequently each of its self-dual and anti-self-dual projections \(W_+=(W+*W)/2\) and \(W_-=(W-*W)/2\) has norm \(1/\sqrt2\). The pair \((\sqrt2W_+,\sqrt2W_-)\) lies on the product of the two unit two-spheres in the three-dimensional Hodge eigenspaces.

This map identifies the oriented Grassmannian with those two spheres: conversely, a pair of unit vectors in the Hodge eigenspaces defines a unit bivector with \(\langle W,*W\rangle=0\), hence a simple unit bivector. Rotations in \(\mathrm{SO}(4)\) induce the full \(\mathrm{SO}(3)\times\mathrm{SO}(3)\) action on the two eigenspaces (the differential decomposes as \(\mathfrak{so}(4)=\mathfrak{so}(3)\oplus\mathfrak{so}(3)\)); therefore the invariant probability on the product is the product of the two uniform spherical area laws.

Write \(W_{12}=\langle W,e_1\wedge e_2\rangle\) and \(W_{34}=\langle W,e_3\wedge e_4\rangle\), and define
\[
A=W_{12}+W_{34},\qquad B=W_{12}-W_{34}.
\]
These are fixed coordinate components of \(\sqrt2W_+\) and \(\sqrt2W_-\), respectively. Hence \(A,B\) are *independent*, each uniform on \([-1,1]\).

**3. An ellipse exactly inscribed in a diamond.** The squared determinant of the first two rows of \(U\) is \(W_{12}^2\), whereas the analogous determinant for the last two rows is \(W_{34}^2\). Since \(T\) is the first-block Gram matrix and \(I_2-T\) the second-block Gram matrix,
\[
\lambda_1\lambda_2=W_{12}^2,
\qquad (1-\lambda_1)(1-\lambda_2)=W_{34}^2,
\qquad\lambda_1+\lambda_2=1+AB.
\]
Condition (1) is equivalent to \((\lambda_1-c)(\lambda_2-c)\le0\), or
\[
\frac{(A+B)^2}{4}-c(1+AB)+c^2\le0.
\]
Under the linear change \(x=(A+B)/2\), \(y=(A-B)/2\), this becomes precisely
\[
\frac{x^2}{c}+\frac{y^2}{1-c}\le1. \tag{2}
\]
The original square \((A,B)\in[-1,1]^2\) maps to the diamond \(|x|+|y|\le1\), carrying constant probability density \(1/2\) with respect to planar Lebesgue measure (the inverse Jacobian has absolute determinant \(2\)). Ellipse (2) is contained in this diamond: by Cauchy--Schwarz, every point of the ellipse satisfies
\[
|x|+|y|\le\sqrt{c+(1-c)}\sqrt{\frac{x^2}{c}+\frac{y^2}{1-c}}\le1.
\]
Thus the desired probability equals one half of the area of the ellipse with semiaxes \(\sqrt c\) and \(\sqrt{1-c}\):
\[
\frac12\pi\sqrt{c(1-c)}
=\frac{\pi h}{2(1+h^2)}.
\]
For completeness, this equals the direct integral obtained from the ordered real Jacobi principal-angle density
\[
\frac{\lambda_2-\lambda_1}
{2\sqrt{\lambda_1(1-\lambda_1)\lambda_2(1-\lambda_2)}}
\mathbf 1_{0<\lambda_1<\lambda_2<1}.
\]
The density is background information, not an unproved input into the preceding geometric proof.

**4. Extremality and other section dimensions.** The symmetry \(h\mapsto1/h\) is evident in the formula. The inequality \(2h\le1+h^2\), with equality only at \(h=1\), proves the unique maximum \(\pi/4\). For a random one-dimensional subspace, the squared first-block norm of a uniformly random unit vector is continuously distributed on \((0,1)\); the full-radius condition forces it to equal the single constant \(c\), a null event. Every three-dimensional subspace is a hyperplane \(\{(x,y):a\cdot x+b\cdot y=0\}\), for some \(a,b\in\mathbb R^2\). Choose unit \(x\perp a\) and unit \(y\perp b\), with arbitrary unit choices if a component vanishes. Then \((x,hy)\) belongs simultaneously to the hyperplane and to \(K_h\), and its length is \(\sqrt{1+h^2}\). This proves deterministic preservation for all three-planes. The four-dimensional assertion is immediate. \(\square\)

## Verification
The included standalone `CHECK.py` checks the event identity in independent coordinate representations: Gaussian-QR random two-planes versus the Hodge ellipse, random points in the uniform square/diamond, deterministic construction of diametral witnesses in three-planes, and the aspect-ratio symmetry and sharp maximum. Its exact command is `python CHECK.py` using Python 3 and NumPy. These finite numerical tests check implementation and normalizations; the all-parameter probability and sharp extremum rest on the preceding proof.

## Relationship to prior work
Guedon, Litvak, Tatarko, and Vritsiou (arXiv:2609.24131, first public September 21, 2026) study random Euclidean diameters of central sections of general convex bodies, obtaining probability estimates and applications to \(\ell_p\)-ellipsoids. Their theorem statements and applications provide bounds rather than the exact four-dimensional diameter-preservation probability for the nonsmooth Cartesian product \(B_2^2\times hB_2^2\). The 2019 preprint by Hinrichs, Krieg, Novak, Prochno, and Ullrich (arXiv:1901.06639) concerns random sections of individual quadratic ellipsoids, whose defining constraint is a sum of weighted squares, not the intersection of two independent block-ball constraints. The self-dual/anti-self-dual representation of oriented four-dimensional planes and the real Jacobi principal-angle law are standard ingredients; neither is claimed as new. The finding is the explicit aspect-ratio law for diametral intersection of this product body, together with the dimension-stratified preservation statement.

## Limitations
The proof is specific to a product of exactly two planar Euclidean disks, full-diameter preservation, and central Euclidean sections. No complete distribution of smaller diameters, dimension-uniform asymptotic, noncentral-section statement, or universality for other product factors is claimed. Although searches of accessible published results found no direct statement of this exact law, an equivalent older result may exist under principal-angle or Clifford-torus terminology; no independent historical-priority certification has been performed.

## References
1. O. Guedon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, first posted September 21, 2026, https://arxiv.org/abs/2609.24131.
2. A. Hinrichs, D. Krieg, E. Novak, J. Prochno, M. Ullrich, *Random sections of ellipsoids and the power of random information*, arXiv:1901.06639, first posted January 20, 2019, https://arxiv.org/abs/1901.06639.
3. S. Mendelson, *A remark on the diameter of random sections of convex bodies*, arXiv:1312.3608, first posted December 12, 2013, https://arxiv.org/abs/1312.3608.
