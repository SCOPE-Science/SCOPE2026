# Independent mathematical audit

## correctness

PASS

With all edges nonzero the three-term recurrence injects the kernel into each adjacent coordinate pair, so corank >=2 means exactly two and gives a point of U_n. The indicated determinant relation annihilates both kernel columns; all b_i p_{i,i+1} must equal the same scalar. Clearing denominators in the homogeneous Pluecker formulas gives the regular projective inverse, and the constant-rank kernel map is regular. U_n is nonempty (use rows (1,t_i) for distinct t_i) and has dimension 2n-4. A single zero edge gives a path with nullity at most one; multiple zero edges give path blocks, and two cuts separating two singular blocks put every boundary point in some Z_ij. The two connected-path determinant equations have disjoint variables, so each Z_ij is irreducible; the two negative path Laplacians witness its open part with every uncut edge nonzero and both kernels one-dimensional. At such a point the rank condition is given locally by the three entries of the symmetric 2-by-2 Schur complement of an invertible principal (n-2)-block. Its differential is restriction to the kernel. Two diagonal variations make the two independent diagonal coordinates, and each cut produces a nonzero mixed coefficient because path endpoint values cannot vanish. In the smooth local ring neither cut function is identically zero (one tangent vector changes both), so the product is nonzero and the generic cut locus is in the dense-edge closure. This proves irreducibility of the full zero set; verified prior radicality gives primality. A rank-(n-1) symmetric matrix has adjugate czz^T with a nonzero diagonal, so the reduced projective singular support is exactly Y_n. On U_n the adjacent-coordinate isomorphism makes the two diagonals and intervening edge span the three Schur differentials; the determinant is a unit times xy-z^2 in these transverse coordinates (formal over the stated field, analytic over C). The dense-edge formulas were also tested over Q at n=4,5. The two-cut Laplacian cases C4 with opposite cuts and C6 with cuts three steps apart have ranks 2 and 4 respectively, both with kernel dimension two; their block-constant kernel vectors exhibit the three independent restrictions directly. The in-package verify_cycle.py was inspected, not executed; its finite cases are not used as the all-n proof.

## originality

PASS

The supported distinction is the all-cycle primality and explicit open Grassmannian geometry plus the generic transverse node. General radicality, dimension, degree, and connected-support determinant irreducibility are prior. Earlier results also imply primality for the individual cycles C4 and C5; this does not give the uniform theorem for longer cycles. The comparison does not assert an answer for all two-connected supports.

## value

PASS

Cycles are the basic minimally 2-connected family, so their submaximal locus is a natural test of the published sufficiency question. The proof turns abstract reducedness into primality by showing how the cut strata deform to nonzero-edge matrices, and the kernel parameterization identifies what the generic rank-defect matrices and singularities look like. This is a substantive infinite-family result independent of the pre-existing small computations and does not rely on speculative generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
