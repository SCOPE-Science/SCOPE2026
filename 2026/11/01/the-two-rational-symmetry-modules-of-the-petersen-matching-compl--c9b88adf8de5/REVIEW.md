# Scientific review

## Correctness — PASS
The full matching-face census, exact chain ranks and all \(120\) signed symmetry actions are reconstructed in `verify.py`; `verify_output.txt` records the successful execution. The rational chain complex has face counts \((15,75,145,90,6)\), differential ranks \((14,61,79,6)\), and reduced homology of dimension five in each of degrees two and three. The degree-three character comes from the actual rational quotient \(\ker D_3/\operatorname{im}D_4\); the degree-two character follows from the signed Lefschetz chain calculation and known vanishing of other rational groups. Character equalities identify the modules uniquely over characteristic zero.

## Originality — PASS, with residual risk
Zaslavsky, *Six signed Petersen graphs, and their automorphisms*, §3.2, treats the same finite matchings but only classifies their orbit types, not the two graded homology representations. The classical five-point matching complex \(\mathsf M(K_5)\), whose graph is Petersen, is not \(\mathsf M(P)\). Indexed results about Petersen two-matching, Morse-matching, three-cut and particle-configuration complexes study different objects. Exact formulation and numerical searches did not identify either graded character table. Equivalently stated or unindexed prior results remain a nonzero risk. A failed search is not novelty proof.

## Value — PASS
The two nonzero rational homology groups have *equal ranks* but fundamentally different symmetric-group structure: one is a sign-twisted five-point permutation module and the other an irreducible Specht module. This character-level distinction supplies useful new structure for natural graph-matching topology, beyond orbit counts and Betti numbers.

## Scope and limitations
No integral homology, torsion, or global homotopy equivalence is claimed. The finding has been reviewed against directly inspected sources and exhaustive exact calculations; external independent validation is not established.

Self-review: passed. Independent audit: not yet performed.
