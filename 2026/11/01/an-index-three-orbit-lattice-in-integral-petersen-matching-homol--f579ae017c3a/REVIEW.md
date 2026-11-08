# Independent mathematical audit

## correctness

PASS

Petersen P=KG(5,2) has 15 edges; ordinary matching complex simplices are pairwise disjoint edges. Independently enumerated face vector (15,75,145,90,6), 331 nonempty simplices, and mod-two boundary ranks 14,61,79,6, giving Betti 5 in dimensions 2 and 3. Inspected complete deterministic verify_integral_petersen.py: its specified 160-pair Hasse matching has explicit acyclicity topological sorting and exact integer unit cancellations, leaving one critical vertex and five 2- and five 3-cells with all critical differentials zero, so integral homology is torsion-free Z^5 in both dimensions. Code builds integral cycle inclusions/projections, signed S5 action on all 120 permutations, and four generators. In generator_matrices.json, H2 signed orbit matrix has determinant −1. The H3 T-fixed primitive vector (0,0,−1,1,1) has ten pair orbit columns: independently calculated rank 5 and Smith diagonal (1,1,1,1,3) directly from the actual supplied 5×10 matrix, proving index three and quotient Z/3 of lattices, not homology torsion. Full script was inspected, but did not independently run its complete signed 120-element action construction.

## originality

PASS

Zaslavsky author manuscript classifies Petersen matching orbits and signed-graph automorphisms, not the integral S5 homology lattices. Earlier same-object rational characters and nonequivariant wedge are explicitly excluded. The integral determinant and Smith index cannot be inferred from rational characters and are meaningful new invariants; Resultary two-particle Petersen configuration and 3-cut complexes refer to different spaces.

## value

PASS

Primitive orbit bases, generator matrices and a genuine index-three failure of generation by a natural stabilizer-fixed orbit are specific exact integral-equivariant data that rational character tables cannot resolve for a canonical graph matching complex.

The dated certificate retains the supplied scientific assessment, sources and limitations.
