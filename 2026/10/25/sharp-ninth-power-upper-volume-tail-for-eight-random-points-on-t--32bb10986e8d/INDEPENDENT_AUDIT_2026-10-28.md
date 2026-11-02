# Independent mathematical audit

## correctness

PASS

Medgyes Corollary 5.2 supplies the global maximum V=2/3 and uniqueness up to O(4) of the regular cross-polytope for eight spherical vertices. There are exactly 8!/(2^4*4!)=105 disjoint label-pair orbits, each free O(4) of dimension six in ambient (S^3)^8 dimension 24. Fixed local crosspolytope facet chamber gives exact V=(2/3)det((p_i^+-p_i^-)/2), without requiring perturbed antipodal symmetry. In tangent coordinates x=(u-v)/2,y=(u+v)/2 the quadratic determinant deficit is (1/2)sum ||y||^2+(1/2)sum_{i<j}(x_ij+x_ji)^2: six antisymmetric x modes are rotational tangents, leaving 12 y modes and 6 symmetric modes. Under product-sphere orthonormal coordinates, Delta=(1/6)||z_y||^2+(1/3)||z_s||^2+O(||z||^3), positive on the 18-dimensional normal. The ellipsoid measure is pi^9 6^6 3^3/9! epsilon^9. Each maximizing orbit has induced volume 2^6*32pi^4, while ambient volume is (2pi^2)^8; multiplication by 105 gives 2916/pi^3. Compactness and uniform tubular dominated convergence justify the limit. Independently checked the exact prefactor as rational 2916, 16 determinant-vs-SciPy hull comparisons (max error 2.3e-16), and second variation (error <5.1e-6 at tested scales). Neither these numerics nor logs replace the Morse–Bott proof or Medgyes input.

## originality

PASS

Best-of-knowledge original exact upper-endpoint probability tail for eight iid sphere-surface points in R^4. The new global deterministic maximizer theorem of Medgyes (2026-10-12) is an essential input; Horváth–Lángi established crosspolytope maximality within that combinatorial type. Neither supplies a random labelled-orbit tube volume, normal Hessian, ninth power or coefficient. Other random-polytope works address different N/dimensions or expected global statistics.

## value

PASS

The fixed-N near-extreme distribution of a canonical random inscribed polytope is a natural probability-geometry invariant. The exponent nine records a nontrivial normal codimension and the coefficient captures all labeled extremizer orbits and local curvature. It is not a purely deterministic volume maximum or an arbitrary finite numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
