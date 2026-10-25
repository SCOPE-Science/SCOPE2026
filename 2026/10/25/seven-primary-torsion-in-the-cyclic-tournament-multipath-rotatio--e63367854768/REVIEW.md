# Scientific review

## Correctness — PASS
The face criterion is equivalent to being a union of vertex-disjoint directed paths. Exhaustive enumeration checks every subset of 21 arcs. An acyclic augmented face matching leaves 24, 54 and 17 reduced Morse cells in dimensions 3, 4 and 5; the integer Morse differential has eleven unit factors and no others. The free rotation action follows because a face contains at most six arcs while every nontrivial translation has seven-element edge orbits. The orbit cellular chains are formed with orientation signs, checked to square to zero, and their exact Smith forms yield the stated integral groups. Independent direct finite-field ranks check the rational computation but are not used as a substitute for the integer Smith normal forms. The included `check.py` executes these steps.

## Originality — PASS against inspected evidence
The primary 2022 multipath-complex paper computes transitive-tournament topology, not the rotation quotient of this seven-vertex cyclic tournament. The 2024 quiver-minor article proves general finiteness and a blow-up comparison requiring absence of oriented cycles; neither implies the claimed finite homology or the two order-seven summands. Searches for cyclic-tournament multipath quotient homology and comparisons against indexed related calculations revealed no covering statement. The nearest related computations use either different homology constructions on cyclic tournaments or different directed graphs. Search incompleteness, including possible unindexed calculations, remains a risk.

## Value — PASS
The natural orientation is the smallest odd-prime regular cyclic tournament beyond the five-vertex example. Its integral equivariant quotient contains two seven-primary degree-three classes despite torsion-free homology upstairs, a distinction not recoverable from nonequivariant Betti numbers. Determining every integral quotient group together with the full rational cyclic representation provides a concrete nontransitive benchmark for the directed-complex literature. The exact torsion classes and multiplicities, rather than only an Euler characteristic or one extra Betti number, constitute the mathematical contribution.

## Closest literature and limitations
Caputi–Collari–Di Trani–Smith, arXiv:2208.04656, especially Definition 2.2 and Theorem 5.1; Caputi–Collari–Ramos, arXiv:2401.01248, especially §4.1 and Theorem 4.20. The result is restricted to the specified tournament and rotation action, and no independent audit or integral representation-lattice determination is claimed.

Self-review: passed. Independent audit: not yet performed.
