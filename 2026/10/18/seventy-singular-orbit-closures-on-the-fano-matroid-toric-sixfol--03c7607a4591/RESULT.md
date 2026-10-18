# Seventy singular orbit closures on the Fano-matroid toric sixfold

## Finding
Let \(F_7\) be the rank-three Fano-plane matroid on seven elements. Let \(P=P(F_7)\) denote the convex hull of the incidence vectors of its \(28\) bases in the six-dimensional affine lattice \(\{(x_i)\in\mathbb Z^7:\sum_i x_i=3\}\). Let \(X_P\) be the normal projective toric variety over \(\mathbb C\) associated with the normal fan of \(P\). The reduced singular locus of \(X_P\) has **exactly \(70\) irreducible components**, all closures of torus orbits. They form three orbits under \(\mathrm{GL}(3,\mathbb F_2)\):

* \(21\) three-dimensional components indexed by tetrahedral three-faces of \(P\);
* \(21\) two-dimensional components indexed by quadrilateral two-faces of \(P\);
* \(28\) two-dimensional components indexed by triangular two-faces of \(P\).

The generic normal cone associated with each component has exactly one more primitive ray than its dimension, and its associated affine transverse toric singularity has divisor class group \(\mathbb Z\). **Every simplicial cone in the normal fan is unimodular**. Thus the singular locus equals the non-\(\mathbb Q\)-factorial locus, and the singularity is never a finite quotient at a generic point of one of these components. There are precisely \(308\) singular torus orbits in total (including their specialization orbits).

## Assumptions and scope
The ground field is \(\mathbb C\). Label the seven matroid elements by the seven nonzero binary vectors in \(\mathbb F_2^3\). The seven dependent triples are those \(\{i,j,k\}\) whose binary labels sum to zero; all other three-subsets are bases. Coordinates on the rank-six affine lattice are the first six coordinate entries; the seventh is three minus their sum. The singular locus and components are the **reduced geometric** ones, not claims about multiplicity in a Jacobian scheme. The polytope and its normal-fan toric variety, rather than a particular presentation of the projective defining ideal, are the objects classified.

## Proof
**Step 1: an exhaustive exact description of faces.** By the matroid base-polytope inequality theorem, \(P\) consists exactly of the real vectors satisfying \(\sum_i x_i=3\) and \(\sum_{i\in S}x_i\le r(S)\) for all proper, nonempty \(S\subsetneq\{1,\ldots,7\}\), where \(r\) is matroid rank. A subset of size at most two has rank equal to its size; a three-subset has rank two precisely when it is a Fano line; every larger proper subset has rank three. The included exact checker forms all \(126\) candidate inequalities and identifies a facet exactly when its equality bases have affine rank five. The resulting \(21\) facets are \(x_i\ge0\), \(x_i\le1\) and \(\sum_{i\in L}x_i\le2\) for each Fano line \(L\), seven facets of each type. Every nonempty face is an intersection of these facets. Enumerating the finite closure under intersection gives the complete face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(28,126,245,238,112,21).
\]
The computation includes the empty face and the full polytope, giving \(772\) faces altogether. It enumerates faces without numerical tolerance or a sampling assumption.

**Step 2: a complete toric smoothness test.** For a face \(F\) of dimension \(d\), let \(I(F)\) be the set of facets containing it. Its normal cone \(\sigma_F\) is of dimension \(6-d\), and its ray generators are exactly the primitive outward normals of the facets indexed by \(I(F)\). Writing a supporting subset as \(S\), this primitive integer normal has first-six-coordinate entries \(\mathbf1_{i\in S}-\mathbf1_{7\in S}\). A rational polyhedral cone of dimension \(k\) is regular in its saturated span if and only if it has exactly \(k\) rays and the gcd of the \(k\)-by-\(k\) minors of its integer ray matrix is one. This is equivalent to those primitive rays extending to a lattice basis of their ambient lattice. The checker tests all nonempty faces against both necessary-and-sufficient integer criteria. It finds \(308\) singular cones. Every cone with the expected \(k\) rays has gcd one: there are no simplicial non-unimodular cones.

**Step 3: maximal singular orbits.** A torus orbit corresponds to a face \(F\) and has dimension \(\dim F\); the orbit closure associated with \(G\) contains that associated with \(F\) exactly when \(F\subseteq G\). Hence irreducible components of the closed singular locus correspond exactly to inclusion-maximal faces carrying nonregular normal cones. An exact finite comparison of the \(308\) singular faces with the face-intersection partial order yields \(70\) maximal faces. Their tuples (face dimension, number of vertices, number of active facets) are
\[
(3,4,4)\quad\text{with multiplicity }21,\qquad
(2,4,5)\quad\text{with multiplicity }21,\qquad
(2,3,5)\quad\text{with multiplicity }28.
\]
The first type is a tetrahedron, the second a quadrilateral, and the last a triangle; these assertions follow from their vertex counts and affine dimensions. Enumerating all \(168\) invertible binary three-by-three linear transformations and applying the induced permutations to faces proves that each type consists of one symmetry orbit. Their sum is \(70\).

**Step 4: generic local class groups.** On each of the \(70\) component-defining cones, the number of primitive rays is \(k+1\), where \(k\) is its dimension (equal to three or four). Hence the class group of the transverse affine toric cone has free rank one. The gcd of all full-size minors of the ray matrix is one in each case; the cokernel of the ray map has no torsion. The toric class-group exact sequence thus makes the group precisely \(\mathbb Z\). In particular none of these cones is simplicial, so their toric strata are singular and non-\(\mathbb Q\)-factorial. Step 2 proves the converse on every torus orbit, completing the claimed equality of loci.

This is a finite but **exhaustive** proof: the matroid rank inequalities give a complete finite facet system, facet intersections give **all** polytope faces, and integer-minor regularity is an exact necessary-and-sufficient criterion for **all** normal cones.

## Verification
Run `python3 verify_fano_singular.py` using only Python 3's standard library. The script constructs every base directly from binary XOR, validates all \(21\) facets from the rank-inequality system, enumerates all \(772\) faces by exact set intersection and rational affine rank, verifies every cone through integer determinant minors, counts the \(308\) nonregular cones, extracts their \(70\) maximal faces, and checks all \(168\) Fano automorphisms and the class-group saturation condition. Expected final line: `generic_local_class_groups=Z`. This checker is included in full, not a detached transcript. Neither floating-point experiments nor untested external packages are needed.

## Relationship to prior work
Matroid base-polytope inequalities and toric normal-fan smoothness are standard general theorems. Kim's 2009 work treats face-flag enumeration of matroid base polytopes. García-Marco and Ramírez Alfonsín (2014) study matroid toric ideals and generators, rather than singular orbits of the Fano-base-polytope toric sixfold. Lasoń and Michałek (2020) investigate Gorenstein and other algebraic properties of matroid polytopes, including facet structure, but not this \(70\)-component singular-orbit classification. A 2026 Fano-specific paper by De Loera, Ferroni, Morales and Rambau treats Gröbner bases and regular unimodular flag triangulations; its full text was not accessible during the present comparison, and possible unforeseen overlap is recorded below. These works give context and general machinery but no identified theorem implying the above complete counts and three-stratum classification. A literature search alone is not proof of novelty.

## Limitations
All statements concern the toric variety of this one natural rank-three matroid. No analogous classification is claimed for arbitrary matroids or for scheme-theoretic singular multiplicities. The symbolic enumeration is a reproducible mathematical certificate tied to exact general polyhedral and toric equivalences, not an independent formal-verification certificate. Full-text comparison of the Fano-specific 2026 paper was unavailable, leaving a bounded originality risk. No external independent mathematical audit has been carried out.

## References
1. S. Kim, *Flag enumerations of matroid base polytopes*, arXiv:0901.3534 (initial public posting 2009-01-22), https://arxiv.org/abs/0901.3534.
2. I. García-Marco and J. L. Ramírez Alfonsín, *Matroid toric ideals: complete intersection, minors and minimal systems of generators*, arXiv:1408.0419 (2014), https://arxiv.org/abs/1408.0419.
3. M. Lasoń and M. Michałek, *On algebraic properties of matroid polytopes* / *Gorenstein matroids*, arXiv:2005.08359 (2020), https://arxiv.org/abs/2005.08359.
4. J. A. De Loera, L. Ferroni, S. Morales, and J. Rambau, *There are matroid toric ideals without quadratic Gröbner bases*, arXiv:2606.11014 (2026), https://arxiv.org/abs/2606.11014.
5. J. Edmonds, foundational matroid-polytope rank-inequality characterization (classical theorem).
6. W. Fulton, *Introduction to Toric Varieties* (1993), regular-cone and orbit-closure criteria.
