# Scientific review

## Correctness — PASS

The proof reconstructs strong domination from the actual vertex-degree comparison, classifies the unique/repeated minimum-part cases, and checks all one-vertex or two-vertex deletion possibilities. It explicitly handles complete graphs by the empty-graph convention and one-part residuals. The standalone checker independently evaluates the defining neighborhood predicate, not the theorem's reduced formulas, for every complete multipartite profile through eleven vertices; all 183 agree, including minimum witness multiplicities. It separately checks the key twelve-vertex example.

## Originality — PASS

The closest primary literature is the initial and revised versions of *Stability of the Strong Domination Number of Graphs*, arXiv:2601.03891. Both relevant multipartite sections and the revised join discussion were materially inspected. There is genuine overlap at balanced profiles, but the inspected prior statements do not imply the all-profile exact theorem; selected printed numerical predictions conflict with independently proved and directly checked post-deletion examples. Related Roman, paired, and super domination concern different conditions. Alternate terminology or later corrections remain possible; an unsuccessful search alone cannot prove uniqueness.

## Value — PASS

The theorem gives a closed three-regime stability rule for all complete multipartite profiles and a full optimal-deletion-witness classification, including the unique repeated-minimum-size-three obstruction. It offers an exact robustness answer and explains why degrees in the post-deletion graph, not just ordinary domination, determine stability. The result is a mathematical classification, not a routine parameter-only recalculation.

## Scope and risks

This is specific to finite simple complete multipartite graphs. The complete-graph endpoint adopts strong domination number zero for the empty graph. The motivating source has conflicting printed subclass statements; no independent confirmation of its state or of global priority is claimed. Finite tests are corroboration, not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
