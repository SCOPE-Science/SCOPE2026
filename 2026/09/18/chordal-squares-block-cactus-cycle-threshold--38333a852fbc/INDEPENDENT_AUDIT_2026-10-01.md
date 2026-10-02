---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For a finite cactus-block graph, its square is chordal exactly when every non-complete cycle block has length at most five; the criterion is sharp at the six-cycle and admits a constructive perfect-elimination ordering by leaf-block peeling.

## Correctness — PASS

Distances between vertices of a block are preserved in the ambient graph, so a cycle block of length at least six contributes the same induced hole already present in its square. Conversely, if every non-complete cycle block is a 4- or 5-cycle, removing a leaf block preserves the square induced on the remainder, and the displayed deletion orders make every private vertex simplicial for clique, 4-cycle, and 5-cycle leaf blocks. Induction gives a perfect-elimination ordering. The threshold checks are exact: the square of a 5-cycle is complete and the square of a 6-cycle contains an induced 4-cycle.

**Checked sources.** Assigned RESULT.md at tree 9b9e474915f74f4ad06b6302ffc45efea246b70a; Golovach–Kratsch–Paulusma–Stewart 2018; Ducoffe 2019; Le–Tuy 2010

**Residual risks.** No computational certificate is needed; correctness rests on the block metric lemma and leaf-block induction, both reconstructed directly.

## Originality — PASS

Targeted searches and the most relevant square-root literature did not locate the five-cycle chordality threshold. The inspected cactus/cactus-block papers focus on recognizing square roots and recovering cut/block structure, while the block-graph endpoint concerns roots whose blocks are all cliques.

### Equivalent formulations

The closest synonymous formulation is chordality of graph powers of cactus or block-cactus roots; searched sources do not state the audited iff criterion.

### Broader coverage

Those broader algorithmic results do not imply when a known cactus-block root has a chordal square.

### Exact database or table

Tabular comparison is inapplicable beyond the elementary boundary examples because the theorem is an infinite structural characterization.

### Claim versus prior implication

The block-graph endpoint does not mechanically imply the sharp extension to cactus-block graphs.

**Checked sources.** https://doi.org/10.1007/s00224-017-9825-2; https://doi.org/10.1016/j.dam.2018.10.028; https://doi.org/10.1016/j.disc.2009.09.004; semantic published-results search

**Residual risks.** Older graph-power literature under different terminology could contain the same criterion, but targeted searches and the directly relevant cactus-block source did not reveal it.

## Value — PASS

This is a natural sharp structural boundary extending the tree/block-graph square setting to cactus-block roots, with the first obstruction at a six-cycle and a constructive perfect-elimination ordering. It is a reusable characterization rather than a small isolated computation.

**Residual risks.** The theorem does not solve arbitrary square-root recognition or strong chordality.

## Limitations

- The cactus-block root is assumed given; this is not a square-root recognition algorithm.
- The theorem characterizes chordality, not strong chordality.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
