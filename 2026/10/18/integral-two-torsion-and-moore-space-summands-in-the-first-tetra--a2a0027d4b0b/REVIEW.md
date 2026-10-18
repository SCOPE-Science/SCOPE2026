# Scientific review

## Correctness — PASS

A simplex belongs to the open-neighborhood complex exactly when contained in the explicitly generated neighborhood of a graph vertex, so generating and deduplicating all subsets is exhaustive. For \(n=6\) and \(n=7\), the complete directed Hasse graphs have respectively 8,620/41,940 and 136,220/839,580 vertices/covers; topological sorting consumes all vertices, certifying acyclicity of the prescribed pairings. The resulting critical-cell profiles are \((1,0,1,142)\) and \((1,0,1,772)\). All 798 and 3,848 dimension-two-to-three pivots are exact units. The resultant single integer Morse attaching rows have gcd two, so the resulting simply connected three-complexes are the asserted Moore-space wedges. The \(n=5\) comparison has a separately verified acyclic matching, and \(n=4\) is immediate. The included stand-alone Python reproduces these exact facts; integer computations, not sampled field ranks, control torsion. Risk: the finite proof is computer-assisted and requires independent reproduction, not an external proof assistant.

## Originality — PASS, with residual risk

The compared literature includes Kahle's common-neighborhood construction and random-graph results, Matsushita's general neighborhood fundamental groups, the directly read all-parameter scale-one Johnson clique-complex statement, and the directly read triangular-graph neighborhood homology calculation. These other Johnson/triangular results use respectively a different complex (clique rather than open-neighborhood) or a different Johnson rank (two-subset rather than three-subset) and cannot imply this exact integral Moore summand. Queries under tetrahedral Johnson, hypersimplex, graph-Hom, open neighborhood, and two-torsion gave no directly covering indexed result. Risk remains of another representation of this finite calculation under association-scheme or Hom-complex terminology; failed searches alone do not establish absolute novelty.

## Mathematical value — PASS

Johnson graphs on fixed-sized subsets are canonical combinatorial families. The natural first nontrivial three-subset cases produce **genuine integral torsion**, invisible in rational homology, at the sharp threshold \(n=6\) after two torsion-free cases, and retain it at \(n=7\). A complete Moore-space wedge decomposition is strictly stronger than a known-or-computable Betti vector and resolves the attaching-degree obstruction. The result does not purport to be a general-family theorem, and its exact finite threshold is mathematically motivated rather than an arbitrary labeled subcomplex.

Self-review: passed. Independent audit: not yet performed.
