# Self-review

## Correctness — PASS

The proof reconstructs the unrestricted \(n\ge1\) quantifier and the head-excluding-premise normalization, exhibits an explicit witness to every asymmetric premise dependency, and checks that mutual dependencies cannot create a new enabled head. It then proves the one-pass fixed-set criterion. Exchange is tested with the exact witness \(X=N_G(u)\setminus\{v\}\), forcing adjacent true twins, and the converse uses direct sums of uniform matroids. The Boolean submodularity equivalence uses intersection-closure of fixed sets and a three-vertex fork to obstruct union closure; the matching converse is componentwise. The labelled counts are graph, partition and partial-pairing enumerations. Executable exhaustive checks corroborate all claims through five vertices (and all rule pairs through four), without being substituted for the arbitrary-size proof.

## Originality — PASS, with residual risk

The Horn closure and exchange framework in Bérczi--Boros--Makino 2023 and the general Boolean-submodular Horn characterization in Lozin--Zamaraev 2023 are explicitly credited. Their full texts do not state this single-clause-per-head commutation graph classification and joint cluster/matching thresholds. The 1999 bidual Horn framework treats a different dual condition. Searches for implication-rule commutation, graph neighborhoods, set closure, and the exact trichotomy did not identify an equivalent statement in published records. This absence does not prove global uniqueness; the matroid and submodularity boundaries may be implicit corollaries of broader known results, and rewrite-system or dependency-theory terminology remains a material indexing risk.

## Mathematical value — PASS

The one-head rule assumption defines a concrete, motivated order-independence problem for Horn forward chaining. Its simultaneous solution provides a canonical graph normal form, exact labelled counts, a one-pass algorithm, a visible fixed-set invariant, and sharp boundaries for two independently important semantic classes (matroids and Boolean-submodular functions). This is a structural classification across every finite size rather than isolated numerical data. The Bell and matching sequences themselves are known and are not claimed as new.

## Limits

No claim is made for arbitrary multi-clause Horn bases or unlabeled isomorphism counts. Computations are finite corroborations of a complete symbolic proof; earlier source terminology may hide an equivalent theorem. No external independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
