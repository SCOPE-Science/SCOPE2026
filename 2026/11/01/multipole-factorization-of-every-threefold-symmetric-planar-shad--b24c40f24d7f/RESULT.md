# Multipole factorization of every threefold-symmetric planar-shadow area deficit

## Finding
Consider a compact convex body \(K\subset\mathbb R^3\) with nonempty interior. Assume that for **every** two-dimensional linear subspace \(E\), its orthogonal projection \(K\mid E\) has threefold rotational symmetry after a possible translation within \(E\). Then the complete directional projection-area function factors through exactly three unoriented axes.

More precisely, the support function is necessarily
\[
h_K(u)=r+a\cdot u+P(u),\quad u\in S^2,
\]
where \(r>0\), \(a\in\mathbb R^3\), and \(P\) is a real homogeneous harmonic cubic, subject to the usual convex-support condition. If \(P\ne0\), there are three uniquely determined unoriented unit axes \(\pm v_1,\pm v_2,\pm v_3\) (allowing repetitions) and a nonzero real coefficient \(\kappa\) such that
\[
P(x)=\kappa\operatorname{Harm}\!\left[\prod_{j=1}^{3}(v_j\cdot x)\right].
\]
Here \(\operatorname{Harm}\) denotes harmonic projection of homogeneous cubics. The **exact planar-shadow area law** for every unit normal \(n\) is
\[
\boxed{\pi r^2-\operatorname{area}_2(K\mid n^\perp)
=\frac{\pi\kappa^2}{4}\prod_{j=1}^{3}\bigl(1-(n\cdot v_j)^2\bigr).}
\]
The area equals \(\pi r^2\) exactly at the listed axes. Those and only those unoriented normals give a **circular** projection; after a planar translation it is the radius-\(r\) disk. Thus a nonball has **exactly three circular projection planes counted with algebraic multiplicity**, or one, two, or three distinct planes. Generically all three are distinct. Conversely, **every multiset** of three unoriented planes is realized, with exactly those multiplicities, by a smooth strictly convex nonball whose planar projections are threefold symmetric.

For \(P=0\), the body is a translated ball and every projection is a circle. The three-axis uniqueness and finite-circle count are restricted to \(P\ne0\). The word “generic” means outside the proper real algebraic discriminant locus of harmonic cubics with repeated Maxwell axes.

## Assumptions and scope
A convex body is compact, convex, and has nonempty interior. A “projection plane” is an unoriented linear two-plane; its normals \(n\) and \(-n\) describe the same plane. “Threefold symmetry after translation” means that for each projected body some planar translation makes it invariant under rotation by \(2\pi/3\). No common translation center is presumed across the planes. The condition requires threefold, not merely the existence of some unrelated symmetry.

The homogeneous cubic \(P\) satisfies \(\Delta_{\mathbb R^3}P=0\), and its restriction to \(S^2\) is used in the support function. For a twice differentiable support function, the exact support constraint is \(\nabla_{S^2}^2h_K+h_K I\succeq0\) at every unit direction; positivity makes the body strictly convex with positive principal radii. As \(P\) and the linear term are odd, every such body has constant width \(2r\), and therefore \(r>0\).

For a homogeneous cubic \(L\) define
\[
\operatorname{Harm}[L](x)=L(x)-\frac{|x|^2}{10}\Delta L(x).
\]
Indeed \(\Delta(|x|^2 b\cdot x)=10b\cdot x\) in \(\mathbb R^3\) for any vector \(b\). The three Maxwell axes and \(\kappa\) are determined up to permuting axes and simultaneously changing signs of individual axis representatives and the overall coefficient. In particular \(\kappa^2\) is independent of representative signs.

## Proof
**1. Completeness of the cubic support space.** Threefold rotational symmetry of \(K\mid E\) after a translation means the restriction of \(h_K\) to the great circle \(S^2\cap E\) has only Fourier modes \(0,\pm1,\pm3,\pm6,\pm9,\ldots\). First modes represent the translation. Let \(W\) be the real subspace of continuous spherical functions with this property on every great circle. It is invariant under rotations and its closure in \(L^2(S^2)\) is rotation invariant. The harmonic-projection lemma and the equatorial-frequency separation lemma of Myroshnychenko–Ryabogin–Saroglou (their Lemmas 4.8 and 4.12, used for the same great-circle symmetry spaces) imply that every spherical-harmonic component of \(h_K\) independently belongs to \(W\); every nonzero harmonic of degree \(\ell\) exhibits each circle frequency of matching parity not exceeding \(\ell\) on some equator. Every nonzero **even** degree \(\ell\ge2\) exhibits forbidden frequency \(2\); every nonzero **odd** degree \(\ell\ge5\) exhibits forbidden frequency \(5\). Consequently only degrees \(0,1,3\) survive. Conversely degree-three polynomials restrict to only modes \(1\) and \(3\), so every convex support \(r+a\cdot u+P(u)\) has the desired threefold symmetry after planar translation. Degree-one terms are translations and have no effect on the projected area.

**2. Three axes and harmonic factorization.** Sylvester's/Maxwell's multipole theorem, established in the form needed here in Dennis (2004, §§1, 5–7), states that every nonzero real degree-three homogeneous harmonic polynomial has three unique unoriented real multipole axes, counted with multiplicity. Therefore \(P=\kappa\operatorname{Harm}[L]\), where \(L(x)=\prod_{j=1}^3(v_j\cdot x)\) and each \(v_j\) is a unit vector. There is no additional harmonic component because the harmonic projection of a degree-three polynomial differs from it only by \(|x|^2\) times a linear polynomial. This theorem includes multiple coincident axes; it is a classical algebraic ingredient, not a new uniqueness claim.

**3. Circle Fourier coefficient and exact area.** Fix any unit normal \(n\) and oriented orthonormal basis \(p,q\) of \(n^\perp\). Set \(m=p+iq\in\mathbb C^3\); it satisfies \(m\cdot m=0\) for the complex-bilinear Euclidean form. With \(u(\theta)=p\cos\theta+q\sin\theta=\frac12(m e^{-i\theta}+\bar m e^{i\theta})\), homogeneity of the cubic gives the coefficient of \(e^{-3i\theta}\) in \(P(u(\theta))\) as \(P(m)/8\). The other possible cubic frequencies are \(\pm1\) and are removable by translation. Thus the translated planar support function is
\[
\widetilde h(\theta)=r+\operatorname{Re}\!\left(\frac{P(m)}4e^{-3i\theta}\right).
\]
For any smooth planar convex support function \(s\), the standard identity
\[
\operatorname{area}_2=\frac12\int_0^{2\pi}\bigl(s(\theta)^2-s'(\theta)^2\bigr)\,d\theta
\]
gives, by Fourier orthogonality,
\[
\operatorname{area}_2(K\mid n^\perp)=\pi r^2-\frac\pi4|P(m)|^2.
\]
Because \(m\cdot m=0\), the trace-removal term in \(\operatorname{Harm}[L]\) vanishes at \(m\). Hence \(P(m)=\kappa\prod_{j=1}^3(v_j\cdot m)\), and the orthonormality of \(p,q,n\) yields
\[
|v_j\cdot m|^2=(v_j\cdot p)^2+(v_j\cdot q)^2
=1-(v_j\cdot n)^2.
\]
Multiplying these three identities proves the boxed factorization for **every** \(n\in S^2\), with no approximation or genericity assumption.

**4. Exact circles, multiplicities, and inverse realization.** The planar support \(\widetilde h\) is constant precisely when \(P(m)=0\). Its threefold term has zero mean and cannot be removed by a translation unless its amplitude vanishes, so this is equivalent to the projection being a circular disk of radius \(r\). In the factorized area identity, the nonnegative deficit vanishes exactly when \(n=\pm v_j\) for some \(j\). Multiplicity of a circular direction means its multiplicity among the three unique Maxwell axes. Three distinct axes occur, for example, for \(P(x)=x_1x_2x_3\); all three can coincide for the zonal harmonic \(P(x)=x_3^3-\tfrac35|x|^2x_3\). The distinct-axis property is generic because the nonzero discriminant of the associated binary sextic is a polynomial condition, and the \(x_1x_2x_3\) example has six simple projective roots.

Conversely, take any prescribed multiset of three unoriented planes. Choose unit normals \(v_1,v_2,v_3\), allowing repetitions, and set \(H=\operatorname{Harm}\bigl[\prod_j(v_j\cdot x)\bigr]\). The classical multipole theorem (or irreducibility of the complex null quadric) implies \(H\ne0\): the degree-three product of three nonzero linear forms cannot be divisible by the irreducible quadratic \(|x|^2\). Fix any \(r>0\). The spherical curvature matrix \(\nabla^2_{S^2}H+HI\) is bounded, so for sufficiently small nonzero \(\varepsilon\), the function \(r+\varepsilon H\) has strictly positive curvature matrix on the whole sphere and defines a smooth strictly convex nonball. Step 1 gives threefold symmetry of all planar projections; Steps 2–3 show that exactly the chosen three normal axes, with their multiplicities, are circular. This proves the inverse assertion.

## Verification
The standalone `verify.py` was run using Python 3.11 and SymPy 1.14. It reported `PASS 1558 exact and deterministic finite geometric diagnostics`. The tests independently form harmonic projections \(L-|x|^2\Delta L/10\), check their vanishing Laplacians, verify the complex-null-vector factorization across explicit and 1,500 deterministic randomly chosen normals, compare independently extracted third Fourier coefficients, and integrate the support area formula numerically by central differences for multiple cubic tensors. Exact polynomial checks also confirm the binary sextic \(P(s^2-t^2,i(s^2+t^2),2st)=2ist(s^4-t^4)\) for \(P=x_1x_2x_3\) and \(8s^3t^3\) for the zonal harmonic.

The finite diagnostics do **not** prove the universal classification, factorization, or inverse theorem. Those follow from the cited rotation-invariant harmonic separation and classical multipole representation plus the explicit all-direction area calculation above. For a stand-alone replay, run `python verify.py` in an environment with the stated SymPy version; the program has no data or network dependencies.

## Relationship to prior work
Myroshnychenko, Ryabogin, and Saroglou (2026) proved roundness for symmetry orders at least four and exhibited a cubic exception for threefold-symmetric projections. Their harmonic-projection and frequency lemmas also support the classification reduction used in Step 1, so that reduction is **not** claimed independently original. Dennis (2004) proves Sylvester's classical uniqueness of Maxwell multipole axes and their antipodal binary-polynomial roots in arbitrary degree. That paper already relates degree-two axes to the two circular projection planes of ellipsoids. The algebraic existence or uniqueness of the three cubic axes here is **not** claimed new.

Previously published geometric calculations treated two proper subfamilies: the tetrahedral cubic \(x_1x_2x_3\), with its explicit coordinate-axis brightness product, and the axial harmonic \((u\cdot e)^3-3(u\cdot e)/5\), with its third-power brightness factor. Their formulas are recovered as special cases of the boxed law. The contribution here is the **all-body** exact brightness factorization for the entire threefold-projection class, its equivalence to circular shadows, and the unrestricted inverse realization of any triple of circular projection planes. The checked sources did not state those three geometric conclusions together, although the classical multipole theorem makes the factorization natural once combined with the spherical support-function classification and planar area identity.

## Limitations
Only three-dimensional Euclidean convex bodies and ordinary two-dimensional *orthogonal projections* are covered, not sections or bodies in higher ambient dimension. For the ball, every projection is circular and the finite three-axis conclusion does not apply. In general the maximal allowed cubic amplitude depends on the specified multipole axes; the inverse theorem only asserts the existence of a sufficiently small positive-curvature realization, not a sharp amplitude interval. The factorization is quadratic in the amplitude and does not distinguish the sign of a cubic perturbation from brightness alone. Algebraic multiplicities are Maxwell-axis root multiplicities, not a count of physically different planes. A historically prior but unindexed general brightness formula cannot be excluded by search alone.

## References
1. S. Myroshnychenko, D. Ryabogin, and C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1, first public 2026-09-23, https://arxiv.org/abs/2609.27192. In particular, Sections 3–5 and Lemmas 4.8, 4.12.
2. M. R. Dennis, *Canonical representation of spherical functions: Sylvester's theorem, Maxwell's multipoles and Majorana's sphere*, Journal of Physics A 37 (2004), 9487–9500, arXiv:math-ph/0408046, https://arxiv.org/abs/math-ph/0408046. In particular, Sections 1 and 5–7 and the degree-two circular projection comparison.
3. N. Hitchin, *Spherical harmonics and the icosahedron*, arXiv:0706.0088 (2007), https://arxiv.org/abs/0706.0088, for an independent algebraic view of the seven-dimensional real space of harmonic cubics.
4. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed. (2014), for support-function curvature and planar area identities.
