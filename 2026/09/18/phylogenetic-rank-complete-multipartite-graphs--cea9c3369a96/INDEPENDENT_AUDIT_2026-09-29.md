# Independent audit — Exact phylogenetic rank of complete multipartite graphs

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/phylogenetic-rank-complete-multipartite-graphs--cea9c3369a96`
**Audited tree:** `6e74a6f7bab086491387971298b4fcb3abf2d242`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

**PASS.** The explicit star metrics give the claimed upper bound. For the lower bound, the tree four-point condition forces one coordinate per non-singleton part, and uniqueness of the midpoint in a tree forces an additional coordinate when at least two singleton parts are present. The max{1,...} term correctly handles the all-singleton complete-graph case.

### Independent checks

- Reconstructed the star-coordinate embedding for each non-singleton part and the half-unit singleton star.
- Verified the four-point contradiction 4 versus at most 2 for two distance-two pairs from different multipartite parts.
- Checked the singleton midpoint collapse argument in every forced coordinate.
- Checked edge cases K_n, K_{m,1}, K_{m,n}, K_4-e, and complete graphs minus a matching.
- Verified this record was committed at 2026-09-18T05:48:28Z and therefore predates the later same-repository duplicate.

## Originality

**PASS.** PASS to the best of current searchable knowledge. At this record's repository commit time it precedes the later duplicate 9f7547419b5e. The September 2026 Ashworth--Clarke--Giansiracusa--Jones--Quijas-Aceves--Ren preprint studies graph phylogenetic rank, rank one, complete bipartite graphs, and several extremal families but no indexed source located the full complete-multipartite formula. Cartwright--Chan use a distinct tropical tree-rank notion.

### Literature and chronology checked

- https://arxiv.org/abs/2609.19372 — Ashworth et al., The phylogenetic rank of a graph, submitted 2026-09-16. The abstract and current indexed descriptions establish the surrounding parameter and known families but do not state the audited complete-multipartite formula.
- https://doi.org/10.46298/dmtcs.2865 — Cartwright--Chan, Three notions of tropical rank for symmetric matrices; an adjacent but explicitly different tree-rank convention.
- https://github.com/SCOPE-Science/SCOPE2026/commit/e8bec6bf82f5defcf526703435d8aaf715180c47 — Repository commit establishing the chronology of this record as the first of the two equivalent SCOPE entries.

## Scientific value

**PASS.** The theorem gives a closed formula on an entire classical graph family, unifies the known complete-bipartite and matching-complement examples, and yields an immediate bounded-rank classification inside complete multipartite graphs.

## Limitations

- Originality is to the best of current searchable knowledge, not a guarantee of priority against poorly indexed older metric-decomposition terminology.
- The result is restricted to connected complete multipartite graph metrics and does not solve the general bounded-rank classification problem.

## Publication guard

The current source tree on `main` matched the assignment tree `6e74a6f7bab086491387971298b4fcb3abf2d242` exactly during this audit. The guarded change-set records the independent-audit evidence and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
