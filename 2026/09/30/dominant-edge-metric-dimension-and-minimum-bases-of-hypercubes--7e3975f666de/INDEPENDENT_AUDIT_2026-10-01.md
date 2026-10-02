---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

The dominant edge metric dimension of \(Q_n\) is \(1\) for \(n=1\), \(3\) for \(n=2\), and \(2^{n-1}\) for \(n\ge3\); for \(n\ge3\) the only minimum bases are the two parity classes.

## Correctness — PASS

For \(n\ge3\), either parity class is a vertex cover of size \(2^{n-1}\). Orient each edge by its even endpoint. Distinct even endpoints are separated by the landmark at one endpoint; two edges sharing the even endpoint but changing coordinates \(i\ne j\) are separated by an even landmark obtained by toggling \(i\) and a third coordinate. A perfect matching gives the matching lower bound for every vertex cover. If a minimum vertex cover has size half the vertices, its complement is an independent half-set; regularity forces every edge across the cut, so connected-bipartite uniqueness makes the cover one of the two parity classes. The \(Q_1,Q_2\) cases are direct. The inspected verifier confirms the exact basis counts through \(Q_4\) and both parity bases through \(Q_{10}\), without serving as the infinite proof.

**Checked sources.** assigned RESULT.md and verify.py at tree f205db034d68401084b4c1c840b83b15bf976781; Tavakoli et al. 2023 full primary PDF; Kelenc et al. 2023 hypercube metric-dimensions paper

**Residual risks.** No correctness defect was found.

## Originality — PASS

The defining 2023 dominant-edge paper treats complete graphs, complete bipartite graphs, cycles, paths, wheels, and graph operations; its inspected full text does not contain the higher-dimensional hypercube result. Existing hypercube metric-dimension work concerns ordinary metric, edge metric, and mixed metric dimensions, not the vertex-cover-constrained dominant edge parameter. Resultary found no earlier equivalent formula or basis classification.

### Equivalent formulations

The audited parameter combines vertex cover and edge resolution and is not equivalent to the ordinary hypercube edge metric dimension.

### Broader coverage

No stronger inspected theorem supplies the exact value or uniqueness of bases.

### Exact database or table

Finite tables are inapplicable to the all-dimensional theorem.

### Claim versus prior implication

Prior generic bounds alone do not mechanically imply the theorem.

**Checked sources.** https://doi.org/10.5614/ejgta.2023.11.1.16; https://doi.org/10.26493/1855-3974.2568.55c; Resultary semantic search

**Residual risks.** Because the parity construction is short, an unindexed equivalent observation remains possible, but no direct prior implication was located.

## Value — PASS

This determines a natural infinite family for a recently introduced invariant and classifies every minimum basis, revealing an exact coincidence between the hypercube bipartition, minimum vertex covers, and edge-resolution structure. That is a motivated structural result rather than a finite computation.

**Checked sources.** Tavakoli et al. 2023; hypercube metric-dimension literature

**Residual risks.** The result does not extend to general Hamming graphs or Cartesian products.

## Limitations

- Binary hypercubes only.
- The theorem concerns dominant edge metric dimension, not ordinary edge or mixed metric dimension.
- Finite computation through the stated range is corroborative only.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
