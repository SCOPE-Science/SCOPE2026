# Self-review

## Correctness
PASS. The proof uses the exact universal-cover interpretation of color refinement. For a connected unicyclic graph, the universal cover is a bi-infinite path decorated periodically by finite rooted trees. The bi-infinite path is intrinsically characterized as the set of vertices whose deletion leaves two infinite components, so every universal-cover automorphism preserves it and acts there by a translation or reflection. This action descends modulo the cycle length to a dihedral symmetry of the unique cycle, and the induced rooted-tree isomorphisms on the finite decorations glue to an automorphism of the original graph. Thus equal stable colors imply equal automorphism orbits; the reverse inclusion is automatic. The tree case is the same argument with the universal cover equal to the tree itself. The cyclomatic-number-two counterexample is checked directly by its equitable degree partition.

The standalone checker independently verifies the conclusion on all 79 connected Graph Atlas representatives with at most seven vertices and cycle rank at most one, and verifies the explicit bicyclic obstruction.

## Originality
PASS with residual priority risk. Targeted published-finding corpus searches for “color refinement automorphism orbits unicyclic graphs”, “coarsest equitable partition orbit partition unicyclic graph”, “unicyclic graphs stable coloring automorphism orbits”, “1-WL unicyclic graph orbit partition”, and “unicyclic graph color refinement Tinhofer Godsil” returned no matching result. Web searches using “refinable”, “fractional automorphism”, “coarsest equitable partition”, “unicyclic”, and “pseudoforest” likewise did not locate the theorem.

Arvind--Köbler--Rattan--Verbitsky define refinability and explicitly cite the tree case, but their full text has no occurrence of “unicyclic” or “pseudoforest”. Kiefer--Schweitzer--Selman show orbit recovery for graphs identified by \(C^2\), which does not cover all unicyclic graphs because cycles of length at least six are not \(C^2\)-identified. Krebs--Verbitsky supplies the universal-cover lemma but does not state the unicyclic descent theorem.

The residual risk is that an older result in equitable-partition, fractional-automorphism, or chemical-graph literature states the same fact under different terminology.

## Value
PASS. Refinability is a named structural level in the standard color-refinement hierarchy. The theorem gives a natural complete class guarantee at the first cyclic level beyond trees and identifies a sharp cyclomatic boundary: every connected graph with at most one independent cycle has exact orbit recovery, while a connected graph with two independent cycles can already fail. It also separates refinability from amenability in a concrete way, since long cycles are refinable but not identified by \(C^2\). This is a structural class theorem rather than a family-specific iteration count.

## Closest literature and limitations
The closest source is Arvind--Köbler--Rattan--Verbitsky, arXiv:1502.01255, which introduces the refinable class, records the tree case, and studies the hierarchy containing refinable graphs. Krebs--Verbitsky, arXiv:1407.3175, supplies the exact round/universal-cover equivalence used in the proof. Kiefer--Schweitzer--Selman, arXiv:1503.08792, provides the strongest nearby orbit-recovery implication for \(C^2\)-identified graphs but does not cover all unicyclic graphs. No independent literature audit has been performed.

Self-review: passed. Independent audit: not yet performed.
