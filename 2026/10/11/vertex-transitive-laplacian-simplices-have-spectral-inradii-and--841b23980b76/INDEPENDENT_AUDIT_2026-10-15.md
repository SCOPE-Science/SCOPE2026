# Independent mathematical audit

## correctness

PASS

Connected L has kernel span(1), so its n columns are affinely independent in 1^⊥, centroid 0. Vertex transitivity implies degree k and equal squared column norms k(k+1). Averaged squared distances give unique circumcenter and R. Barycentric coordinates α_i(x)=1/n+⟨L⁺e_i,x⟩, so facet clearance at origin is 1/(n||L⁺e_i||). Automorphism transitivity equalizes norms and Frobenius trace gives q=||L⁺e_i||²=(1/n)Σ_{j≥2}λ_j⁻². Summing constraints α_i(x)≥ρ√q gives sharp unique inradius 1/(n√q), all facets tangent. Independent exact rational SymPy tested K2,K5,C6,Q3, including barycentric normals and spectral traces; cycle fourth-cosecant identity numerically tested n=3..14. Euclidean full-Laplacian metric is essential.

## originality

PASS

Comparison of actual geometric objects, metrics and formulas found no checked pre-existing spectral inradius/circumradius identity for the canonical Euclidean Laplacian simplex of a connected vertex-transitive graph. Braun–Meyer and Meyer–Pllaha study the associated integral/lattice and Ehrhart invariants; Manjunath–Sturmfels use a non-Euclidean simplicial metric on a lattice. Neither a spanning-tree product of eigenvalues nor lattice unimodular equivalence fixes the Euclidean inball formula involving the sum of inverse squares. General simplex barycentric identities are known, but the vertex-transitive spectral specialization is not found as an exact result. Best-of-knowledge PASS with explicit priority risk.

## value

PASS

The canonical Euclidean metric of a natural graph-associated simplex has two independent computable geometric invariants: a universal degree-based outer radius and a pseudoinverse/spectral-moment inner radius, with exact centers and supporting facets. This is a broad structural relation across connected vertex-transitive graphs, not a numerical one-off or routine known-table substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
