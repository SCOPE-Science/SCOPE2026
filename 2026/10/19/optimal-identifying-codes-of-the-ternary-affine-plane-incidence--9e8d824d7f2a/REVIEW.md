# Self-review

The scientific summary below corrects the maximum-degree-bound argument in the frozen self-review; the independent assessment is separate.

## Correctness — PASS

The proof defines the graph and identification condition without ambiguity. The full point set gives a size-nine code. Two independently formulated exact tests reject all 203,490 eight-subsets; since identification is upward closed, this rules out every smaller code as well. The two tests examine every one of the 293,930 nine-subsets and agree on exactly 109 codes, equal *setwise* to the 1+36+72 geometric constructions. Geometric adjacency proofs identify the cone over the incidence line graph and four bi-Cayley/Pappus components; full exchange-edge enumeration, 432 affine permutations, and all-source BFS confirm 234 edges and the claimed radii/diameters. The original package includes `verify.py` and `verification_output.txt`.

## Originality — PASS, with residual risk

This finding does not claim the minimum identifying-code size nine in isolation. The general maximum-degree bound gives only seven on this graph; the complete finite test certifies nine. The statement-level contribution is the complete classification of all 109 optimal codes and their exchange graph decomposition. Gravier et al. study strongly regular adjacency graphs and generalized quadrangles; Bousquet et al. study hereditary-class complexity and approximation; Foucaud et al. study line graphs as the objects on which codes live. None of their inspected results entails the optimizer census, geometry, or Pappus components for this irregular Levi graph. Relevant published mathematical-record searches and accessible historical claims showed no equivalent or stronger coverage. Residual risk: computations in unindexed reports or unpublished work may coincide, and no formal universal prior-art exclusion is possible.

## Value — PASS

The smallest nontrivial odd-order affine plane supplies a natural point-line sensor-selection problem. Knowing the cardinality alone gives no information on whether sensors can be exchanged without losing identification. The optimal code space unexpectedly splits into a universal-apex incidence cone and four highly symmetric Pappus components, pinpointing a natural obstruction to minimum-budget reconfiguration. The result distinguishes optimizer geometry and mobility, not an arbitrary unmotivated count.

Self-review: passed. Independent audit: not yet performed.
