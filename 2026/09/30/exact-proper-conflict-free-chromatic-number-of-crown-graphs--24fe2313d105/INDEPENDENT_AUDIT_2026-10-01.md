# Independent mathematical audit — Exact proper conflict-free chromatic number of crown graphs

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The cross-side color lemma follows directly from crown adjacency: a color used on both bipartition classes is confined to one deleted matched pair and is a singleton on each side. The displayed four-color construction therefore supplies a unique-colored neighbor to every vertex from order four onward. The cases of zero, one, two, or three shared colors exclude every coloring with at most three colors in that range, while orders two and three are direct.

Checked sources: Assigned RESULT.md; Inspected verify.py finite checker; Fabrici--Luzar--Rindosova--Sotak 2023; Caro--Petrusevski--Skrekovski 2023.

Residual correctness risks: The finite checker is only corroborative; the uniform argument proves the infinite family..

## Originality

**PASS.** Best-of-knowledge originality survives. Foundational and later proper conflict-free papers treat planar/basic classes, complexity, and general maximum-degree bounds, but the inspected primary descriptions and published-record searches did not state the exact crown-graph transition or an equivalent deleted-perfect-matching formula.

### Equivalent formulations

Searches/sources: Published-record semantic search for proper conflict-free crown graphs and complete bipartite graphs minus a perfect matching; arXiv:2202.02570; arXiv:2203.01088.

Evidence: The exact archive match was the audited theorem. Fabrici et al. introduce the proper open-neighborhood parameter with a planar focus. Caro et al. list trees, cycles, hypercubes and subdivisions of complete graphs among their exact/basic classes.

No inspected alias or equivalent class description subsumed the crown result.

### Broader coverage

Searches/sources: Cranston--Liu 2024 large-maximum-degree bounds; Liu--Reed 2025 asymptotically optimal proper conflict-free coloring.

Evidence: These sources give general bounds or asymptotics, not the exact crown value. A general upper bound does not imply the sharp lower bound or the two small exceptional values.

No inspected broader theorem determines the exact crown formula.

### Exact database or table

Searches/sources: Published archive exact search under crown, deleted matching, and proper conflict-free synonyms.

Evidence: No earlier exact crown entry was located.

This is an infinite theorem rather than a known-value table; theorem-record search is the applicable database check.

### Claim versus prior implication

Searches/sources: Compare general proper conflict-free bounds with the crown shared-color structure; Check whether complete-bipartite class results mechanically imply crowns.

Evidence: Deleting a perfect matching changes both legal cross-side color classes and neighborhoods. The lower bound needs the crown-specific shared-color lemma.

The exact formula is not a mechanical corollary of the inspected general results.

### Source inspections

- **Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods** — BACKGROUND_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2202.02570
  Trigger: Foundational source for the parameter.
  Material read: Complete abstract and theorem-level public description.
  Method: lawful open-access source page
  Evidence: The accessible description focuses on planar and outerplanar bounds, not crowns.
- **Remarks on proper conflict-free colorings of graphs** — RELATED_ACCESS_RISK.
  Identifier: https://arxiv.org/abs/2203.01088
  Trigger: Basic-class source with plausible exact-value overlap.
  Material read: Complete abstract and public theorem description.
  Method: lawful open-access source page
  Evidence: The abstract lists several basic classes but not crowns; whole-document noncoverage is not asserted from the abstract alone.

Residual originality risks:
- The complete Caro--Petrusevski--Skrekovski text was not inspected in this run.
- An older equivalent result may use deleted-matching terminology without the phrase crown graph.

## Scientific value

**PASS.** Crown graphs are a classical dense bipartite family of unbounded degree. An exact infinite-family value together with the cross-side color lemma is a reusable structural result rather than a tiny-instance computation.

Residual value risks: The theorem does not classify all optimal colorings..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
