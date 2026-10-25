# Scientific Review

## Correctness — PASS

All four graphs are defined by explicit vertex and switch sets. `CHANG_CHECK.py` independently constructs their adjacency matrices, tests the complete strongly regular parameters, enumerates all independent faces, verifies the unique-extension property for triangles, and computes the exact mod-two second-boundary rank. The algebraic proof then lifts the maximum mod-two rank to the exact rational rank and uses a unit-pivot integral splitting of the third boundary to show that the second integral homology is free. The derived ranks are \(132,164,172,172\). The theorem does not claim the absence of first-homology torsion.

## Originality — PASS

The classical matching-complex literature already treats the unswitched triangular graph. The three nonisomorphic Chang graphs are distinct objects, and a published comparison for the smaller Shrikhande/rook parameter class does not imply the present values. Targeted searches for the exact ranks, graph aliases, complement flag complexes, and switching constructions found no direct covering result. This is not a claim that all literature has been exhaustively searched. An inaccessible related repository full text and unindexed older calculations remain residual risks.

## Value — PASS

A complete comparison for all four strongly regular graph types sharing \((28,12,6,4)\) connects a natural spectral-degeneracy question to integral simplicial homology. The calculation determines three distinct second-homology ranks, identifies an exact unit-pivot structural reason for torsion-freeness, and records the two Chang cases that this particular invariant fails to separate.

## Scope and limitations

The result concerns integral homology in degree two and vanishing in degree three, not a complete integral homology calculation or homotopy classification. The unswitched comparator is known; the Chang cases are the targeted contribution. No independent audit or validation is claimed.

Self-review: passed. Independent audit: not yet performed.
