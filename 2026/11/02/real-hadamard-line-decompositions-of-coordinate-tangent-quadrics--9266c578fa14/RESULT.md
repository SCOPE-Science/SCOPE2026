# Real Hadamard line decompositions of coordinate-tangent quadrics

## Finding

Let \(W\subset\mathbb P^3_{\mathbb R}\) be a smooth real quadric tangent to each of the four fixed coordinate planes. Write
\[
 W=\{[x]:x^{\mathsf T}Ax=0\},\qquad B=A^{-1}=(b_{ij})_{0\leq i,j\leq3},
\]
where \(A\) is real, symmetric, and invertible. Coordinate tangency is equivalent to \(b_{00}=b_{11}=b_{22}=b_{33}=0\). Put
\[
 r=b_{01}b_{23},\qquad s=b_{02}b_{13},\qquad t=b_{03}b_{12},
 \qquad \Delta=r^2+s^2+t^2-2rs-2rt-2st.
\]
Then \(\det B=\Delta\ne0\), and the following are equivalent:

1. \(W\) is the coordinatewise Hadamard product of two real projective lines in \(\mathbb P^3_{\mathbb R}\).
2. \(\Delta>0\) (equivalently, \(\det A>0\)).
3. The real quadratic form defining \(W\) has signature \((2,2)\).
4. At least one, and therefore every, tangent coordinate-plane section of \(W\) is a union of two distinct **real** lines.

When these conditions hold, every real point of \(W\) is a coordinatewise product of real points on one such pair of lines. The set of ordered real line pairs \((L,R)\) with \(L\star R=W\) is exactly two disjoint free orbits of the reciprocal coordinate-scaling torus \((\mathbb R^\times)^4/\mathbb R^\times\), interchanged by swapping the two factors. The real locus \(W(\mathbb R)\) is a two-torus.

If \(\Delta<0\), then \(W(\mathbb R)\) is a two-sphere, contains no real projective line, and **no** pair of real lines has Hadamard product \(W\). Nevertheless such a \(W\) has complex line decompositions, so this is an obstruction to *real* factorization rather than geometric factorization.

Thus the sign of an explicit degree-four polynomial in the six dual off-diagonal coefficients is a complete real-factorization and real-topology invariant on the smooth coordinate-tangent family.

## Assumptions and scope

The ground field is \(\mathbb R\). Lines, quadric equations, and Hadamard factors are all required to be defined over \(\mathbb R\). The Hadamard product of two subvarieties is the Zariski closure of their coordinatewise products where defined; in the split case below the map is in fact an everywhere-defined isomorphism. The four coordinate planes are fixed and labeled. \(W\) is assumed smooth, so \(\det A\ne0\). Scaling \(A\) by any nonzero real number does not change the criterion because its determinant has even degree four. The real torus acts by \((L,R)\mapsto(g\odot L,g^{-1}\odot R)\); its scalar diagonal acts trivially.

## Proof

**Dual equation and determinant.** The dual quadric is defined by \(u^{\mathsf T}Bu=0\). A coordinate plane \(x_i=0\), represented by the dual point \(e_i\), is tangent to \(W\) exactly when \(e_i^{\mathsf T}Be_i=b_{ii}=0\). Expanding the determinant of the symmetric zero-diagonal matrix gives
\[
\det B=(b_{01}b_{23})^2+(b_{02}b_{13})^2+(b_{03}b_{12})^2
-2b_{01}b_{23}b_{02}b_{13}-2b_{01}b_{23}b_{03}b_{12}-2b_{02}b_{13}b_{03}b_{12}=\Delta.
\]
The expression is nonzero by smoothness. As \(\operatorname{tr}B=0\), the real symmetric matrix \(B\) is indefinite. The number of its negative eigenvalues is therefore one, two, or three. The determinant is positive precisely when it is two. Inversion preserves the signs of all eigenvalues, so \(A\) and \(B\) have the same signature.

**Real rulings.** If the signature is \((2,2)\), the real quadratic form is isometric, up to an invertible real change of basis and a scalar, to the determinant form on \(2\times2\) matrices. Thus \(W\) admits a real Segre isomorphism
\[
\phi:\mathbb P^1_{\mathbb R}\times\mathbb P^1_{\mathbb R}\xrightarrow{\sim}W
\]
whose hyperplane bundle pulls back to \(\mathcal O(1,1)\). Since each coordinate plane is tangent, the pullback of its defining coordinate section is a nonzero rank-one bilinear form
\[
 x_i\circ\phi=\ell_i(s_0,s_1)m_i(t_0,t_1),\qquad i=0,1,2,3.
\]
This factorization is over \(\mathbb R\): a real rank-one matrix factors over \(\mathbb R\). The four sections span the four-dimensional real vector space \(H^0(\mathcal O(1,1))\), because \(W\) is nondegenerate in \(\mathbb P^3\). Consequently \([\ell_0:\cdots:\ell_3]\) and \([m_0:\cdots:m_3]\) are morphisms with line images \(L\) and \(R\) (each has two linearly independent coordinate forms and no common zero). Their coordinatewise product recovers \(\phi\). It is defined everywhere and induces equality of real points \(W(\mathbb R)=L(\mathbb R)\star R(\mathbb R)\).

Conversely, suppose \(W=L\star R\) for real lines. Neither line is contained in a coordinate plane because \(W\) is nondegenerate. Choose a real point \(p\in L(\mathbb R)\) with all four coordinates nonzero. The coordinatewise product \(p\star R\) is the image of \(R\) under an invertible real diagonal transformation, so it is a real projective line contained in \(W\). A real quadric of signatures \((1,3)\) or \((3,1)\) has Witt index one and contains no real projective line (a line would correspond to a two-dimensional totally isotropic real vector subspace). Therefore \(W\) must have signature \((2,2)\). In that signature its tangent hyperplane sections are unions of one real line from each ruling; in Witt-index-one signatures they have no real line components. This proves all four equivalences.

**Counting real factorizations.** An ordered real Segre isomorphism chooses an ordering of the two real rulings. For one fixed ordering, the four bilinear coordinate sections have unique factorizations into real one-variable linear forms, up to four independent nonzero real reciprocal scalars. Changing parameter coordinates by an element of \(\operatorname{PGL}_2(\mathbb R)\) on either factor does not change the resulting embedded lines. Hence the decompositions for one ruling order form one orbit of \((\mathbb R^\times)^4/\mathbb R^\times\). The orbit is free. Indeed, if a reciprocal diagonal scaling preserves both embedded lines, it induces projective automorphisms of their parameter lines. Their product automorphism fixes the Segre embedding pointwise because the coordinatewise products are unchanged. Since the Segre map is an isomorphism, both automorphisms are the identity. A diagonal map acting pointwise on either embedded line scales every nonzero coordinate form by the same scalar, so the reciprocal scaling is scalar in the projective torus. Reversing the rulings gives the second orbit, not the first, because a factor-preserving reciprocal rescaling cannot interchange the two ruling classes of curves in \(W\).

**Topology.** The real locus of the split Segre surface is \(\mathbb RP^1\times\mathbb RP^1\cong S^1\times S^1\). If \(\Delta<0\), the form has signature \((1,3)\) or \((3,1)\). Its projectivized real isotropic cone is homeomorphic to \(S^2\), by normalizing the coordinate of the unique eigenvalue of one sign. Complexifying either type makes a split smooth complex quadric, proving that the negative-sign case has complex but no real line decompositions.

## Verification

Run `python verify.py` with Python 3, SymPy, and optionally NumPy. It derives the six-variable determinant identity symbolically, checks exact positive- and negative-sign examples, verifies the split Segre product equation identically, and performs 128 deterministic numerical inertia comparisons away from the discriminant. The actual run returned `VERIFY_OK: symbolic determinant identity, 2 exact examples, 128 sampled signature checks`. These finite checks do not substitute for the signature and Segre proof.

Concrete witnesses: for \(B\) having all off-diagonal entries equal to one, \(\det B=-3\) and its eigenvalues are \(3,-1,-1,-1\); its corresponding smooth quadric is coordinate-tangent but admits no real line-product factorization. For the zero-diagonal \(B\) with \(b_{03}=1\), \(b_{12}=-1\), and other off-diagonal entries zero, \(\det B=1\), and the resulting equation is \(x_0x_3-x_1x_2=0\), up to nonzero scalar. It equals the product of the real lines \([s:s:t:t]\) and \([u:v:u:v]\).

## Relationship to prior work

Antolini, Ballico, and Oneto, *Algebraic surfaces as Hadamard products of curves* (arXiv:2502.18813, first publicly submitted 2025-02-26), Theorem 1.1 and Lemma 3.2, characterize complex smooth quadrics tangent to the coordinate planes as complex Hadamard products of lines; their proof is over \(\mathbb C\). The present statement does not claim that complex characterization. It classifies which **real forms** of those complex surfaces have real line factors and distinguishes their real topological types by a single explicit discriminant sign, including the completely obstructed but real-point-bearing case.

Ballico, *Real Ghosts of Complex Hadamard Products* (2024), studies real images and real ghosts for Hadamard products in general. The present calculation is a special inverse problem about factorization of a coordinate-tangent quadric, not a generic-point real-ghost assertion. Brysiewicz, Fevola, and Sturmfels, *Tangent quadrics in real 3-space* (2020/2021), study enumerative real tangencies of quadrics, not their Hadamard line factorization. Standard classification of real quadratic forms and real Segre surfaces is used throughout.

## Limitations

The theorem assumes a smooth real quadric and tangency to all four fixed coordinate planes. It does not classify degenerations at \(\Delta=0\), other coordinate systems, higher-degree surfaces, or products of nonlinearly embedded curves. The reciprocal-torus orbit claim concerns geometric line pairs, not the scheme structure of a parameter fiber. The sign test is not a claim of a new quadratic-form classification. The relevant 2024 real-Hadamard paper was available only partially through accessible online excerpts; priority against all prior work requires independent literature review.

## References

1. D. Antolini, E. Ballico, A. Oneto, *Algebraic surfaces as Hadamard products of curves*, arXiv:2502.18813 (v1 dated 2025-02-26), Sections 2–3, Theorem 1.1, Lemma 3.2. https://arxiv.org/abs/2502.18813
2. E. Ballico, *Real Ghosts of Complex Hadamard Products*, *Symmetry* 16 (2024), 1300, DOI:10.3390/sym16101300. https://www.mdpi.com/2073-8994/16/10/1300
3. T. Brysiewicz, C. Fevola, B. Sturmfels, *Tangent Quadrics in Real 3-Space*, arXiv:2010.10879, *Le Matematiche* 76 (2021), 355–367. https://arxiv.org/abs/2010.10879
