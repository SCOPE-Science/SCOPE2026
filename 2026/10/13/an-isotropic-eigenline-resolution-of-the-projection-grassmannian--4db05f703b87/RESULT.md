# An isotropic-eigenline resolution of the projection-Grassmannian ED discriminant
## Finding
Write \(V=\mathbf C^n\) with the nondegenerate symmetric form \(\langle v,w\rangle=v^{\mathsf T}w\), let \(N=n(n+1)/2\), and let \(\mathsf{Sym}_n\cong\mathbf A^N\) denote the space of complex symmetric matrices. For every \(n\ge3\) and every \(1\le k<n\), the Euclidean-distance discriminant \(D_{k,n}\) of the projection Grassmannian \(\operatorname{pGr}(k,n)\) is an **irreducible rational reduced hypersurface of degree \(n(n-1)\)**.

More precisely, if
\[
\mathcal Q_{n-2}=\{[v]\in\mathbf P(V):\langle v,v\rangle=0\},\qquad
\widetilde D_n=\{(Q,[v])\in\mathsf{Sym}_n\times\mathcal Q_{n-2}:Qv\in\mathbf Cv\},
\]
then \(\widetilde D_n\to\mathcal Q_{n-2}\) is a vector bundle of rank \(N-n+1\). Its projection \(\pi:\widetilde D_n\to D_{k,n}\) is proper, surjective and birational, and its smooth rational source has dimension \(N-1\). Thus this incidence space supplies a uniform explicit resolution of the reduced discriminant, independent of \(k\). Its closed fibers consist set-theoretically of all isotropic eigenlines of the specified symmetric matrix.

The condition \(n\ge3\) is sharp for irreducibility. For \(n=2\), writing \(Q=\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)\), its characteristic discriminant is \((a-c)^2+4b^2=((a-c)+2ib)((a-c)-2ib)\); the reduced ED discriminant is the union of two distinct affine planes.

## Assumptions and scope
All varieties and incidence schemes are over \(\mathbf C\). The bilinear form is symmetric and complex bilinear, **not** Hermitian. The base quadric is smooth and irreducible for \(n\ge3\); the rank and rationality assertions refer to this range. We take \(D_{k,n}\) with its reduced hypersurface structure. The initiating theorem of Friedman--Hoşten--Rosana identifies its underlying set with the characteristic-polynomial repeated-root locus; the results here add irreducibility, degree, rationality, and an explicit proper birational smooth model.

## Proof
**1. Equivalence with isotropic eigenlines.** Let \(Q^{\mathsf T}=Q\) and fix an eigenvalue \(\lambda\). If \(\dim\ker(Q-\lambda I)\ge2\), its eigenspace contains a nonzero isotropic vector over \(\mathbf C\), since any homogeneous quadratic form on a projective line has a zero (possibly it vanishes identically). If its geometric multiplicity is one but algebraic multiplicity exceeds one, there is a nonzero eigenvector \(v\) and a Jordan-chain vector \(u\) with \((Q-\lambda I)u=v\). Symmetry gives
\[
\langle v,v\rangle=\langle v,(Q-\lambda I)u\rangle=\langle(Q-\lambda I)v,u\rangle=0.
\]
Thus repeated characteristic root implies isotropic eigenline. Conversely, suppose \(Qv=\lambda v\) and \(\langle v,v\rangle=0\). If \(\lambda\) were a simple characteristic root then \(\ker(Q-\lambda I)=\mathbf Cv\), and by symmetry the image of \(Q-\lambda I\) would be precisely \(v^\perp\) (both have dimension \(n-1\)). Since \(v\in v^\perp\), there would exist \(u\) with \((Q-\lambda I)u=v\), a forbidden Jordan chain for a simple characteristic root. Therefore the repeated-root locus equals \(\pi(\widetilde D_n)\).

**2. Smooth rational incidence.** Over the projective quadric \(\mathcal Q_{n-2}\), let \(\mathcal L\) be the tautological line. The fiberwise linear map
\[
\mathsf{Sym}_n\otimes\mathcal O_{\mathcal Q_{n-2}}\longrightarrow
\mathcal Hom(\mathcal L,V/\mathcal L),\qquad Q\longmapsto(v\mapsto Qv\bmod\mathcal L)
\]
is surjective: for every nonzero \(v\), the evaluation map from self-adjoint endomorphisms to \(V\), \(Q\mapsto Qv\), is surjective. Indeed, after choosing a basis beginning with \(v\), the associated symmetric bilinear form \((x,y)\mapsto\langle Qx,y\rangle\) can be assigned any first row and column, so \(Qv\) is arbitrary. The incidence is the kernel bundle, of rank \(N-(n-1)=N-n+1\). The quadric is smooth, irreducible and rational for \(n\ge3\) (projection from a rational point on this split quadric gives a dense affine parametrization). Its vector-bundle total space is therefore smooth, irreducible and rational, with dimension \((n-2)+(N-n+1)=N-1\). The projection to affine matrix space is proper because it is the restriction of projection from the product with the projective quadric. The repeated-root locus is therefore irreducible and closed.

**3. The map is birational.** Consider
\[
B=\begin{pmatrix}i&1\\1&-i\end{pmatrix},\qquad
Q_0=B\oplus\operatorname{diag}(3,4,\ldots,n).
\]
The matrix \(B\) is a nonzero square-zero symmetric matrix with unique eigenline \(\mathbf C(1,-i)\), which is isotropic. The remaining eigenvalues are simple and different from zero. Consequently \(Q_0\) has exactly one isotropic eigenline. The locus in the repeated-root hypersurface with a single Jordan block of length two, all other roots simple, is nonempty and Zariski open: the complementary root-collision and further Jordan-degeneration conditions are closed, as is clear by polynomial factor and rank conditions locally near this type. Because the hypersurface is irreducible, this locus is dense. Every matrix in it has exactly one isotropic eigenline (a simple eigenvalue has no isotropic eigenvector, by step 1). Hence the proper dominant map of irreducible varieties of equal dimension is generically of degree one. In characteristic zero this proves birationality.

**4. Reduced equation and exact degree.** Let \(\delta_n(Q)=\operatorname{Disc}_z\det(zI-Q)\). The degree under scaling \(Q\mapsto tQ\) is \(n(n-1)\), because \(\delta_n\) is the product of the squares of all pairwise eigenvalue differences. The zero locus is the irreducible hypersurface above. We show \(\delta_n\) is not a nontrivial power. Perturb only the upper-left entry of \(B\) by \(\varepsilon\). Its quadratic characteristic polynomial becomes \(z^2-\varepsilon z-i\varepsilon\), with discriminant \(\varepsilon^2+4i\varepsilon\). All resultants against the factors \(z-j\) for \(3\le j\le n\), and all pairwise differences among those simple roots, are nonzero at \(\varepsilon=0\). Therefore \(\delta_n\) has first-order vanishing along this perturbation. Since its support is an irreducible hypersurface and it has a simple zero, \(\delta_n\) is irreducible up to a scalar. It defines the reduced ED discriminant and has the claimed degree. In size two, the displayed factorization gives exactly the exceptional reducible case.

## Verification
An accompanying exact checker in `verification/check_discriminant.py`, run using Python 3 and SymPy 1.14, checks the isotropic square-zero block, the two linear factors for size two, surjectivity of the fiberwise linear map for sizes \(3\) through \(8\), and explicit nonzero first-order discriminant coefficients for the same sizes. It prints `VERIFY_OK` on success. These finite checks are consistency tests; steps 1--4 above, not an enumeration, establish the general result.

## Relationship to prior work
Friedman--Hoşten--Rosana, arXiv:2610.02018v1 (2026-10-01), Theorem 3.3, identifies the ED discriminant of \(\operatorname{pGr}(k,n)\) set-theoretically with the repeated-root locus in complex symmetric matrix space. Its Section 3 analyzes critical point counts and Jordan chains, but does not construct the isotropic-eigenline bundle, a resolution, or a rational parametrization of the discriminant. Breiding--Kozhasov--Lerario study the **real symmetric repeated-eigenvalue locus** and its real codimension-two geometry, Euclidean distance degree and volume; that real locus is not the complex codimension-one characteristic discriminant considered here. Searches also considered matrix-invariant/subdiscriminant formulations and indexed mathematical findings; no checked source states an implication covering the explicit proper birational vector bundle construction for all \(n\ge3\).

## Limitations
This is a resolution of the **reduced affine discriminant**, not a claim that its singularities are rational singularities, that the map is small or crepant, or that the singular locus or exceptional fibers are classified scheme-theoretically. The resolution need not be an isomorphism above every diagonalizable matrix with repeated eigenvalues. No assertion is made over \(\mathbf R\) or for arbitrary bilinear forms in characteristic two. An older equivalent incidence construction under different terminology remains an originality risk; no independent audit has been performed.

## References
- H. Friedman, S. Hoşten and A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1, posted 2026-10-01, especially Theorems 1.1 and 3.3 and Section 3. https://arxiv.org/abs/2610.02018
- P. Breiding, K. Kozhasov and A. Lerario, *On the Geometry of the Set of Symmetric Matrices with Repeated Eigenvalues*, Arnold Mathematical Journal 4 (2018), 423--443, https://doi.org/10.1007/s40598-018-0095-0.
- M. Domokos, *Invariant theoretic characterization of subdiscriminants of matrices*, Linear and Multilinear Algebra 62 (2014), 63--73, https://arxiv.org/abs/1206.2358 (different invariant-theoretic focus).
