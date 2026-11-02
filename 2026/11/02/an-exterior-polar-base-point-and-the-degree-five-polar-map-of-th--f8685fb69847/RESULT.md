# An exterior polar base point and the degree-five polar map of the Segre cubic in characteristic three

## Finding
Let \(k\) be algebraically closed of characteristic zero or odd characteristic. Write \(s=\sum_{i=0}^{4}x_i\), and let \(e_j\) be the elementary symmetric polynomial of degree \(j\) in \(x_0,\ldots,x_4\). The primitive integral Segre cubic model in \(\mathbb P^4_k\) is \(X=V(F)\), where
\[
F=e_3-se_2.
\]
For its *ambient* polar rational map \(\Phi=[F_{x_0}:\cdots:F_{x_4}]\colon\mathbb P^4\dashrightarrow\mathbb P^4\), the base scheme consists of ten reduced points, all ordinary nodes of \(X\), if \(\operatorname{char}k=0\) or \(\operatorname{char}k\ne2,3\); it consists of eleven reduced points if \(\operatorname{char}k=3\). In characteristic three the ten nodes remain, but the eleventh base point \(P=[1:1:1:1:1]\) lies **outside** \(X\). The map is dominant and separable and its generic degree is
\[
\deg\Phi=\begin{cases}5,&\operatorname{char}k=3,\\6,&\operatorname{char}k=0\text{ or odd characteristic different from }3.\end{cases}
\]

## Assumptions and scope
All varieties and base schemes are over an algebraically closed field \(k\) of characteristic zero or an odd prime. The term *polar degree* means the generically finite degree of the rational map given by the five first partial derivatives in the full ambient projective space, not the degree of the Gauss map of \(X\). Write \(x_5=-s\) to recover the six-label presentation: the integral identity
\[
3F=\sum_{i=0}^{4}x_i^3-s^3=\sum_{i=0}^{5}x_i^3
\]
holds on \(\sum_{i=0}^5x_i=0\). Because the right side vanishes identically in characteristic three, the *primitive cubic* \(F\), rather than an invalid reduction of the divided equation, defines the relevant integral model. This homogeneous primitive equation is flat over \(\mathbb Z\) as a hypersurface family; no assertion about stable reduction is made.

## Proof
**Gradient identity.** The elementary symmetric derivatives satisfy \(\partial_i e_3=e_2-x_i(s-x_i)\) and \(\partial_i e_2=s-x_i\). Thus, over \(\mathbb Z\),
\[
q_i:=\frac{\partial F}{\partial x_i}=x_i^2-s^2 \quad(0\le i\le4).
\]

**Base-point classification.** Suppose all \(q_i\) vanish. If \(s=0\), then every \(x_i^2=0\), impossible in projective space. Rescale to \(s=1\), giving \(x_i=\varepsilon_i\in\{1,-1\}\) in odd characteristic. If exactly \(r\in\{0,1,2,3,4,5\}\) of these five signs are positive, the normalization equation is \(2r-5=1\) in \(k\), equivalently \(2(r-3)=0\). In characteristic zero or odd characteristic other than three this forces \(r=3\), yielding \(\binom53=10\) distinct projective points. In characteristic three, \(r=0\) is the only additional possibility; all signs are negative and this is projectively \(P=[1:1:1:1:1]\). These are *all* geometric base points.

**Reducedness and singularities.** The affine Hessian matrix at a normalized base point is
\[
H=2(D-J),\qquad D=\operatorname{diag}(\varepsilon_0,\ldots,\varepsilon_4),
\]
where \(J\) is the all-ones matrix. Since \(\sum_i\varepsilon_i=1\), the rank-one determinant formula shows that \(D-J\) has rank four and kernel spanned by the projective coordinate vector \(\varepsilon\) (equivalently, \(J\) induces one exceptional direction on the invertible diagonal space). The four projective tangent directions therefore impose four independent linear conditions: every base point is scheme-theoretically reduced. The ten points with three plus signs and two minus signs satisfy \(F=0\) over the integers (direct substitution, or \(3F=\sum x_i^3-s^3=0\) followed by an integral polynomial evaluation), and the restricted quadratic form has rank four: they are ordinary double points on the cubic in every considered characteristic. At the additional point \(P\) in characteristic three,
\[
F(P)=\binom53-5\binom52=10-50=-40\equiv2\pmod3.
\]
Hence \(P\notin X\) and it is not an eleventh node. There are no further singularities since any singular point must be a gradient base point.

**Polar-map degree.** At \(a=[1:1:1:1:-4]\), \(s=0\), so \(H(a)=\operatorname{diag}(2,2,2,2,-8)\) and \(\det H(a)=-128\). This is invertible in characteristic zero and in every odd characteristic. The affine gradient is therefore locally full-rank at a nonzero vector; by homogeneity its induced projective rational map is dominant and generically separable. Take four sufficiently general independent linear combinations of the five polar quadrics cutting out the inverse image of a general target point. Their intersection is proper of degree \(2^4=16\) by Bézout, and includes the polar base scheme. Since the four polar combinations meet transversely at each reduced base point, each contributes intersection multiplicity exactly one. Away from the base, all residual points form the generic fiber of \(\Phi\) and are reduced because \(\Phi\) is separable. Removing the base lengths \(10\) and \(11\) from \(16\) gives degrees \(6\) and \(5\), respectively.

## Verification
Run `python3 verification/verify_polar.py`. The standalone standard-library program expands the defining polynomial and its five partial derivatives over \(\mathbb Z\), verifies the integral six-label symmetry, enumerates all projective base points independently over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), checks Hessian ranks and which base points lie on \(X\), and recomputes the integer Hessian determinant witness. Its expected output is embedded at `verification/verify_polar_output.txt`. The finite-field enumerations are consistency tests; the characteristic-independent proof is the sign argument and Bézout calculation above.

## Relationship to prior work
The six-coordinate Segre cubic and its ten nodes are classical; Hulek and Sankaran provide a modern discussion of the six-variable equation, and Dolgachev reviews the nodal cubic's geometry. Dimca develops gradient-map methods over complex numbers. Their inspected discussions concern classical characteristic-zero settings and do not supply the specific characteristic-three comparison of the *primitive integral* cubic's ambient polar base scheme and polar degree. The claim here concerns the extra off-hypersurface base point and consequent degree change; it does not assert novelty of the classical node coordinates, polar maps, Bézout's theorem, or the general principle that a characteristic dividing the degree can break Euler's implication from gradient vanishing to hypersurface membership.

## Limitations
The claim excludes characteristic two. The unique exterior base point is a feature of the specified primitive integral model in characteristic three; reducing the nonprimitive six-cube sum modulo three would give the zero polynomial and is not a valid alternative model. The result concerns only the ambient gradient map, not the dual variety or Gauss map. Priority is qualified because early literature on polarities and modern positive-characteristic polar-degree classifications may contain equivalent implicit consequences; no exhaustive historical uniqueness claim is made. In particular, Baker's 1936 note on polarities of the nodes was available only as an abstract and bibliographic extract.

## References
1. K. Hulek and G. K. Sankaran, *The Geometry of Siegel Modular Varieties*, arXiv:math/9810153, first public version October 27, 1998; section on the Segre cubic.
2. A. Dimca, *Hypersurface complements, Milnor fibers and minimality of arrangements*, arXiv:math/0011222, November 27, 2000; gradient-map framework.
3. I. Dolgachev, *Corrado Segre and Nodal Cubic Threefolds*, author-hosted version, https://math.lsa.umich.edu/~idolga/segre15.pdf.
4. H. F. Baker, *Polarities for the nodes of a Segre cubic primal in space of four dimensions*, Math. Proc. Cambridge Philos. Soc. 32 (1936), 507–520, DOI:10.1017/S0305004100019253; bibliographic extract consulted, not the full article.
