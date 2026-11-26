# Independent mathematical audit

## correctness

PASS

Over the algebraic closure the four E_i and six L_ij of the four-point blow-up sum to 6H−2ΣE_i=−2K. Label E_i by {i,5} and L_ij by the complement of {i,j} in {1,2,3,4}. Intersection number one corresponds precisely to disjoint pairs, so intersections are transverse; the Petersen graph is triangle-free, so no three curves meet. The graph gives 10 components, 15 distinct nodes, 30 branches, connectivity, genus 15−10+1=6 and stability (three branches on every rational component). Normalization gluing over the algebraic closure describes Pic^0 as the edge gluing torus modulo vertex rescalings. Dualizing the torus map sends an oriented edge to its endpoint difference, so the character lattice is the integral kernel H_1, with Frobenius reversing signs when it exchanges endpoints. The independent reproduction used a different reverse-Kruskal spanning tree, checked the signed action on full cycles and computed exact integer determinants of orbit-block bases for the seven representatives. In table order the determinants are −1,−1,−1,−1,−1,+1,+1. Conjugacy exhausts the classes; these certificates are integral, not just characteristic polynomials. Basis orbits of lengths d give R_d, negative return after one step gives N_2, and negative return after two steps gives the induced relative norm-one torus U_4. Each norm kernel over finite fields is cyclic, of order q+1 or q²+1 respectively; R_d(k) is cyclic of order q^d−1. Inversion of Frobenius does not change any of the seven classes. The independent orbit enumeration also reproduced the three spectra on components, nodes, and branches, including the unique nonsplit fixed node for (4,1). An orbit of d normalized genus-zero components contributes d(q^n+1) when d divides n and otherwise zero; genus zero over each finite constant field splits. Subtracting rational branch preimages and adding rational nodes gives the stated counts and the product zeta formula over every extension, with no sampling in q or exclusion of small characteristic. Replay: python3 /workspace/branches/independent_finite_checks.py 5.

## originality

PASS

The classical ten-line geometry, classification by S_5, normalization method, and rational-character background are prior coverage. Two distinct November 22 indexed findings exactly overlap the seven integral torus types and finite groups, and one also overlaps the boundary zeta calculation. The inspected versions are later than the November 2 frozen finding and explicitly cite a November 8 related lattice result. They show meaningful present-day equivalent coverage, not documented prior anticipation of the frozen finding. No earlier source inspected establishes the seven integral conjugacy types; historical priority beyond this evidence is not certified.

## value

PASS

The exact integral torus type of a naturally distinguished stable genus-six boundary determines finite abelian groups more sharply than rational characters or cardinalities. In particular the (3,2) type has a cyclic rational group because the full lattice is induced from degree six. The point-free (5) type with a split torus factor and the lone nonsplit node for (4,1) are meaningful arithmetic contrasts. The useful non-routine part is the integral all-type classification; the direct normalization zeta calculation is complementary, and no new geometry of the classical boundary is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
