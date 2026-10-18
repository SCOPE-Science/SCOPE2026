# Scientific review: integral Petersen pentagon-torus presentation

## Correctness — PASS

The finite graph and Abrams complex are specified from the Kneser definition, with 45 vertices, 120 oriented one-cells, and 75 oriented two-cells. The attached checker verifies every integer boundary and the square-zero chain identity, enumerates exactly twelve five-cycles and six vertex-disjoint pairs, and constructs all six 25-square product-torus chains. All six are cycles and their oriented sum vanishes already in the integer chain group. Exact Gaussian elimination gives rank 70 modulo three for the second boundary; five linearly independent cycles give the matching rational upper bound, establishing an integral top-cycle lattice of rank five. A displayed five-row projection of the six cycles has all six maximal column-deletion determinants equal to a unit. This proves **integral** spanning and primitivity, not merely rational spanning. Enumeration of all 120 automorphisms verifies unsigned permutation of these oriented cycles. The Sylow-five correspondence and nonsplitting follow from explicit orbit calculation and transitivity. The proof covers exactly this finite complex and does not extrapolate from sample cases.

## Originality — PASS, subject to bibliographic risk

The closest known published Petersen-specific result, `2bac82e0590d`, establishes the ambient integral homology and the rational \(S_5\)-representation but does not identify its integral \(\mathbb Z[S_5]\)-lattice or six canonical embedded-torus generators. A historical integral Petersen two-point cohomology-ring calculation establishes cup-product information, not the embedding cycles, their primitive relation, or the unsigned integral automorphism action. The Petersen graph's known six pentagon partitions are combinatorial inputs, not a homology presentation. Barnett–Farber's integral face-torus statements apply especially to *ordered planar* graph configurations; Petersen is nonplanar and the current configuration is unordered. Maciążek–Sawicki's general product-cycle treatment does not state the exact integral six-torus relation. The exact statements and implications were compared, not merely titles. Relevant specialist literature or a partially inaccessible thesis could contain an equivalent description, so absolute priority is not certified.

## Mathematical value — PASS

The question asks for the **actual integral representation** carried by geometrically canonical smallest graph cycles in a symmetric nonplanar graph-braid space. The answer distinguishes the top homology lattice from its abstract rank and rational character, determines the precise integral relation among all six naturally occurring tori, proves that any five furnish a geometric integral basis, and identifies the nonsplit integral permutation-module extension. This is a structural, geometric and equivariant classification rather than an arbitrary numerical invariant, a restatement of Betti numbers, or a routine coefficient change.

## Scope and residual limitations

The conclusion concerns unordered two-point configurations on the Petersen graph only, with the displayed orientations and the specified canonical product tori. First-degree torsion, other particle counts, and a general classification of all geometric representatives are not addressed. A complete independent scientific audit has not been conducted, and searches cannot exclude equivalently formulated unindexed work. The accompanying executable uses exact finite enumeration and arithmetic and is available for reproducibility.

Self-review: passed. Independent audit: not yet performed.
