---
audit_date_utc: 2026-10-01
status: passed
record_id: SCOPE-20260915-011
---

# Scientific audit

## Final claim

There is an explicit six-level tower of connected \(7\)-regular graphs \(G_0,\ldots,G_5\), with \(|V(G_i)|=8\cdot2^i\), in which every \(G_{i+1}\) is the displayed \(2\)-lift of \(G_i\) and every level is two-sided Ramanujan; the first signing has exact spectrum \(\{-3^3,-1,+1,+3^3\}\).

## Correctness — PASS

All six edge lists and five signing files were read from the assigned tree. Independent reconstruction verified every graph is connected and \(7\)-regular and that each next edge set equals the exact \(2\)-lift induced by its signing. For every signing, both shifted matrices \(2\sqrt6\,I\pm A_\sigma\) were independently Cholesky-positive with large positive pivots, giving the two-sided Ramanujan inequality; the smallest observed pivot across the five checks remained above \(2.22\). The first signing's exact symbolic verifier gives eigenvalues \(-3,-1,1,3\) with multiplicities \(3,1,1,3\).

Checked sources: artifacts/edges_G0.json through artifacts/edges_G5.json; artifacts/signing_G0_to_G1.json through artifacts/signing_G4_to_G5.json; artifacts/verify_g1_exact.py

Residual risk: Levels after the first were independently rechecked numerically rather than by symbolic characteristic polynomials; the margin to \(2\sqrt6\) is nevertheless much larger than floating-point error.

## Originality — PASS

Resultary found only this record for the exact tower. Bilu--Linial formulate the general two-sided signing problem, and current 2026 work still treats the general non-bipartite bound as open; Marcus--Spielman--Srivastava give infinite bipartite Ramanujan towers but do not cover this non-bipartite \(K_8\) chain. The published degree-7 graph census stops far below the later orders in this tower. No source inspected supplies these five signings or this six-level chain.

### Equivalent Formulations

Searches: explicit finite two-sided 7-regular Ramanujan 2-lift tower K8 16 32 64 128 256; K8 good signing Ramanujan 2-lift

Evidence: No exact chain or equivalent voltage/signing description was located.

Reasoning: The exact finite construction is not recovered from a named standard family in the inspected sources.

### Broader Coverage

Searches: Bilu Linial two-sided signing conjecture; Marcus Spielman Srivastava bipartite Ramanujan all degrees; 2026 improved Bilu Linial bound

Evidence: General two-sided non-bipartite Ramanujan signing remains stronger than what is known; MSS covers bipartite bases.

Reasoning: These broad results do not imply a Ramanujan signing at every level of this non-bipartite tower.

### Exact Database Or Table

Searches: Ramanujan graphs degree 7 database; Zenodo 6579837

Evidence: The cited census covers \(7\)-regular Ramanujan graphs only through 14 vertices, bipartite through 20, and vertex-transitive through 47.

Reasoning: It cannot tabulate the 32--256 vertex levels.

### Claim Vs Prior Implication

Searches: 2-lift spectrum union old signed adjacency

Evidence: Classical lift theory reduces verification of a proposed signing, but does not produce the five signings.

Reasoning: The construction data are the nontrivial content.


### Source inspections

- **NOT_COVERING** — s00493-006-0029-7 (https://doi.org/10.1007/s00493-006-0029-7): Primary theorem/abstract for the Bilu--Linial two-sided signing problem. Evidence: Provides a weaker general signing theorem and the conjectural Ramanujan target, not this explicit chain.
- **NOT_COVERING** — p07 (https://annals.math.princeton.edu/2015/182-1/p07): Primary abstract and theorem scope for interlacing families. Evidence: Infinite families are obtained in the bipartite setting; \(K_8\) is non-bipartite.
- **NOT_COVERING** — 6579837 (https://zenodo.org/records/6579837): Dataset scope and order cutoffs for degrees 3--7. Evidence: Order cutoffs are below most tower levels.
- **NOT_COVERING** — 2606.28797 (https://arxiv.org/abs/2606.28797): Current 2026 abstract on improved two-sided general bounds. Evidence: The full Ramanujan two-sided bound remains a conjecture for general regular graphs.
- **NOT_COVERING** — 2609.15715 (https://arxiv.org/abs/2609.15715): Current 2026 abstract, including its separate explicit \(K_8\) mixed-root example. Evidence: It gives no six-level Ramanujan tower and its \(K_8\) example serves a different lower-bound purpose.

Checked sources: https://doi.org/10.1007/s00493-006-0029-7; https://annals.math.princeton.edu/2015/182-1/p07; https://zenodo.org/records/6579837; https://arxiv.org/abs/2606.28797; https://arxiv.org/abs/2609.15715; artifacts/edges_G0.json; artifacts/edges_G1.json; artifacts/edges_G2.json; artifacts/edges_G3.json; artifacts/edges_G4.json; artifacts/edges_G5.json; artifacts/signing_G0_to_G1.json; artifacts/signing_G1_to_G2.json; artifacts/signing_G2_to_G3.json; artifacts/signing_G3_to_G4.json; artifacts/signing_G4_to_G5.json; artifacts/chain_certificate.json; artifacts/verify_g1_exact.py

Residual risks: A non-indexed computational graph repository could contain isomorphic levels under different labels; no such exact chain was located.

## Value — PASS

A concrete non-bipartite good-signing chain is a natural finite approximation to the unresolved two-sided \(2\)-lift program. Six consecutive certified levels, with explicit reusable signing data and a fully exact first step, constitute a meaningful finite construction rather than an arbitrary census cell.

Checked sources: Bilu--Linial 2006; Marcus--Spielman--Srivastava 2015; current 2026 Bilu--Linial-bound work

Residual risk: The result is finite and gives no mechanism proving continuation beyond 256 vertices.

## Disposition

**PASSED**. Acceptance requires PASS on correctness, originality, and value.
