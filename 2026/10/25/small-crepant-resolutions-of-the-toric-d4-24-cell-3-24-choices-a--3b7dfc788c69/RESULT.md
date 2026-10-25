# Small crepant resolutions of the toric \(D_4\) 24-cell: \(3^{24}\) choices and their cohomology

## Finding
Let \(N=D_4=\{(a_1,a_2,a_3,a_4)\in\mathbb Z^4:\sum a_i\equiv0\pmod2\}\), let \(P\subset N_{\mathbb R}\) be the convex hull of the 24 vectors \(\pm e_i\pm e_j\) with \(1\leq i<j\leq4\), and let \(X\) be the projective toric fourfold defined by the fan of cones over proper faces of \(P\). Over any algebraically closed field, the torus-equivariant smooth small resolutions **over this fixed \(X\)** are in natural bijection with the \(3^{24}\) independent selections of a long diagonal in each of the 24 octahedral facets. Every resulting resolution is crepant. Each has 24 disjoint exceptional surfaces isomorphic to \(\mathbb P^1\times\mathbb P^1\), one over each singular torus-fixed point. At least one such resolution is projective. For each resolution the Betti numbers in even cohomological degrees \(0,2,4,6,8\) are, respectively,
\[
(1,20,54,20,1),
\]
all odd Betti numbers vanish, and the Euler characteristic is \(96\). Over \(\mathbb C\) these are singular cohomology Betti numbers; in positive characteristic they are dimensions of \(\ell\)-adic cohomology for every \(\ell\) prime to the characteristic. The count refers to toric morphisms over \(X\), not to isomorphism types of abstract varieties, and not exclusively to projective resolutions.

## Assumptions and scope
The ground field is algebraically closed, of arbitrary characteristic. Toric varieties are normal, with the lattice and fan specified above. A torus-equivariant resolution means a proper birational toric morphism inducing the identity on the dense torus. 'Small' means no exceptional prime divisors. All triangulations discussed use only the original 24 rays. Projectivity is asserted for at least one, not all, of the \(3^{24}\) resolutions.

## Proof
**1. Facets and singularities.** In the ambient real coordinates the facets of \(P\) are exactly the eight sections \(\pm x_i=1\) and the sixteen sections \((\pm x_1\pm x_2\pm x_3\pm x_4)/2=1\), where the signs vary independently. Their primitive supporting normals lie in \(N^*\) and their constant is one. Each section contains six vertices forming an octahedron. There are 24 facets, 96 edges and 96 triangular two-faces; every proper cone of dimension at most three is unimodular in its saturation. A maximal four-cone is not simplicial and supplies a singular fixed point, so \(X\) has precisely 24 isolated singularities (also described by Braun [1]). The primitive-normal condition makes the fourfold Gorenstein; the face fan is complete and projective.

**2. Classification of small toric resolutions.** A toric resolution that is small introduces no new one-dimensional rays: an additional ray would determine an exceptional invariant divisor. Each maximal cone must therefore be subdivided into unimodular cones using its six original generators. A triangulation of an octahedron on precisely its six vertices has exactly three possibilities: choose one of the three segments joining opposite vertices, then take the four tetrahedra incident to that segment. These tetrahedra are unimodular in \(N\). This last assertion can be verified without classification assumptions: express all 24 roots in the lattice basis
\[
(1,-1,0,0),\ (0,1,-1,0),\ (0,0,1,-1),\ (0,0,1,1),
\]
whose ambient determinant has absolute value two, and compute the determinants for all \(24\cdot3\cdot4=288\) candidate tetrahedra. Every lattice determinant has absolute value one, as exhaustively reproduced by `verify.py`. Alternatively the symmetry of the octahedra reduces the assertion to finitely many representatives. As two facets meet only in triangular, already simplicial faces, subdivisions chosen on different facets agree automatically. Thus all \(3^{24}\) selections give distinct smooth complete fans refining the original fan; conversely any toric smooth small resolution corresponds to such a choice. All morphisms are proper, birational and small. Their canonical divisors agree under toric pullback since no divisorial ray was inserted and the original canonical divisor is Cartier: hence each resolution is crepant.

**3. Exceptional fibers.** For each subdivided octahedral four-cone, the chosen long diagonal spans a new two-cone whose orbit closure has dimension two. This is the only exceptional orbit closure of maximal dimension for that original cone. In the quotient lattice by the saturated span of the diagonal, the other four rays form two pairs of opposite primitive vectors, with a unimodular basis given by one vector in each pair. The complete two-dimensional star fan is therefore the product fan of \(\mathbb P^1\times\mathbb P^1\). The exceptional surface lies above the original isolated torus-fixed point. Distinct original maximal cones give disjoint exceptional fibers, hence 24 disjoint surfaces and no additional exceptional components.

**4. Cohomology and projectivity.** Choose one global linear order on the 24 vertices and use the induced pulling triangulation on every octahedral facet (the long diagonal through its first vertex). This is a coherent boundary triangulation, hence its normal-equivalent support function gives a projective refinement; because \(X\) is projective, the corresponding smooth toric variety is projective. Every other choice yields a smooth complete toric variety, whether or not it is projective. For each chosen triangulation, the simplicial face numbers of the boundary of the four-dimensional fan are
\[
(f_0,f_1,f_2,f_3)=(24,120,192,96).
\]
Indeed each octahedron contributes one new diagonal, four internal triangles and four maximal tetrahedra, while its boundary faces were already globally shared. The associated simplicial-sphere \(h\)-vector is \((1,20,54,20,1)\). The cohomology theorem for smooth complete toric varieties identifies this \(h\)-vector with even Betti numbers, and gives zero odd Betti numbers (over \(\mathbb C\), or for \(\ell\)-adic cohomology in arbitrary characteristic). Summing gives \(96\), equal to the number of maximal cones.

## Verification
The standalone standard-library Python script `verify.py` enumerates the 24 rays and facet vertex sets from explicit integral inequalities, finds the three opposite-vertex diagonals in each octahedron, tests all 288 resulting determinants in an integral \(D_4\) basis, and independently computes the old boundary incidences and refined fan face numbers and \(h\)-vector. Running `python3 verify.py` yields the success marker `VERIFY_OK` together with the values above. The exhaustive computation checks this finite fan, not arbitrary toric fourfolds, and the geometric statements about exceptional stars and projectivity use the mathematical argument rather than the success marker alone.

## Relationship to prior work
Braun [1] identifies this \(D_4\) root 24-cell face-fan fourfold and its 24 octahedral singularity cones, giving their affine equations. Haase–Paffenholz–Piechnik–Santos [2] investigate unimodular triangulations of the 24-cell boundary and construct specific such subdivisions in another context. Thus **the singular cones and existence of certain unimodular triangulations are prior knowledge**. The claim here is the exhaustive over-\(X\) count of toric smooth small resolutions together with explicit exceptional fibers, smooth-fan cohomology and a projective existence construction. General toric facts about subdivisions, exceptional orbit closures and cohomology are standard, and are not presented as new.

## Limitations
The count does not classify abstract isomorphism classes, flop equivalence, all projective/coherent choices, non-toric small resolutions or derived categories. Although full texts of [1] and [2] were examined in the portions governing the 24-cell and its triangulations, equivalent coverage in another historical toric-resolution reference remains a residual originality risk. The finite checker certifies integral polytope computations, not the global toric theorems; proofs of the latter are supplied above.

## References
[1] Volker Braun, *The 24-Cell and Calabi–Yau Threefolds with Hodge Numbers (1,1)*, arXiv:1102.4880 (first public version 2011-02-23), particularly Sections 2 and 3.5.

[2] Christian Haase, Andreas Paffenholz, Lindsay C. Piechnik and Francisco Santos, *Existence of unimodular triangulations—positive results*, arXiv:1405.1687 (first public version 2014-05-08), passages on the 24-cell and boundary triangulations.

[3] William Fulton, *Introduction to Toric Varieties*, Princeton University Press, 1993 (standard toric subdivision and cohomology background).
