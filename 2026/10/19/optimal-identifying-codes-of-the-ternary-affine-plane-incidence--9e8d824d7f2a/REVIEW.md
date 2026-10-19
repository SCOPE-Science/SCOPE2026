# Self-review

## Correctness — PASS

The proof defines the graph and identification condition without ambiguity. The general maximum-degree bound from Gravier et al. (2015), Proposition 2, gives the optimal cardinality as at least nine; the full point set attains it. Two independently formulated exact tests examine every one of the 293,930 nine-subsets and agree on exactly 109 codes, equal *setwise* to the 1+36+72 geometric constructions. Both tests also reject all 203,490 eight-subsets. Geometric adjacency proofs identify the cone over the incidence line graph and four bi-Cayley/Pappus components; full exchange-edge enumeration, 432 affine permutations, and all-source BFS confirm 234 edges and the claimed radii/diameters. `verify.py` and `verification_output.txt` are included and were replayed from the final package paths.

## Originality — PASS, with residual risk

This finding explicitly does not claim the minimum identifying-code size nine, as Gravier et al.'s quoted degree bound plus the all-point construction imply it. The statement-level contribution is the complete classification of all 109 optimal codes and their exchange graph decomposition. Gravier et al. study strongly regular adjacency graphs and generalized quadrangles; Bousquet et al. study hereditary-class complexity and approximation; Foucaud et al. study line graphs as the objects on which codes live. None of their inspected results entails the optimizer census, geometry, or Pappus components for this irregular Levi graph. Relevant published mathematical-record searches and accessible historical claims showed no equivalent or stronger coverage. Residual risk: computations in unindexed reports or unpublished work may coincide, and no formal universal prior-art exclusion is possible.

## Value — PASS

The smallest nontrivial odd-order affine plane supplies a natural point-line sensor-selection problem. Knowing the cardinality alone gives no information on whether sensors can be exchanged without losing identification. The optimal code space unexpectedly splits into a universal-apex incidence cone and four highly symmetric Pappus components, pinpointing a natural obstruction to minimum-budget reconfiguration. The result distinguishes optimizer geometry and mobility, not an arbitrary unmotivated count.

Self-review: passed. Independent audit: not yet performed.
