# Scientific review: Euclidean inballs of hypercube symmetric edge polytopes

## Correctness — PASS
The Euclidean structure is fixed to the zero-sum hyperplane, so the graph Laplacian's first positive eigenvalue is exactly \(2\). Its spectral inequality and the \(d2^{d-1}\) unit-bounded edge differences give the sharp squared polar norm \(d2^{d-2}\). Equality forces the degree-one Walsh eigenspace and unit-magnitude gradients, yielding exactly the stated \(2^d\) facet normals. Paired contact-facet inequalities bound every inscribed-ball radius, irrespective of its center. Exact squared-norm integrality for polar vertices provides a positive margin at every noncontact facet and a genuine relative neighborhood of admissible centers. The proof applies for every \(d\ge2\), and the standard-library verifier corroborates the first three dimensions with exact arithmetic.

## Originality — PASS, with residual risk
D'Alì–Delucchi–Michałek give facet-potential structure for connected bipartite graphs; Çelik–Jamneshan–Montúfar–Sturmfels–Venturello give the hypercube polar-vertex description and enumeration; Chen–Davis–Korchevskaia give general facet-subgraph criteria. These prior statements do not specify the polar Euclidean norm maximizers or the affine dimension of all maximal inscribed-ball centers. Explicit searches were also made for equivalent Lipschitz-polytope, Hamming metric, Wasserstein-ball and orthotope formulations. Absence of an exact match is not an originality certificate, and terminology-dependent equivalent literature remains a genuine residual risk.

## Value — PASS
The exact Euclidean insphere and its complete contact-facet classification provide a geometric invariant for an established nontrivial high-dimensional polytope family. More importantly, the all-dimensional formula \(\dim\mathcal C_d=2^d-d-1\) is a structural extremizer classification: almost every intrinsic coordinate direction admits a small optimal-center displacement, but exactly the degree-one Walsh modes are forbidden. The sharp dimension and explicit nonzero neighborhood are mathematically motivated by the natural symmetry of the Hamming cube, not by an arbitrary parameter slice. The first three known counts of polar facets are \(6,38,990\), while the new contact counts are \(4,8,16\), emphasizing that general facet enumeration does not determine the inball structure.

## Closest literature and limitations
Relevant full texts are arXiv:1910.05193 (general symmetric edge facets, particularly Lemma 4.5), arXiv:2003.06725 (Section 4, Proposition 10 and Hamming-cube polar vertex counts), and arXiv:2107.12315 (general facet subgraphs). A complete description of the center polytope beyond its affine hull and a general enumeration of noncontact facets are not asserted. An equivalent result under finite-metric or Walsh-analysis terminology cannot be entirely excluded.

Same-model review: passed. Independent audit: not yet performed.
