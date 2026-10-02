---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

For every real Banach space \(X\), the radius-extrusion map \(E(A)=A\times[-R(A),R(A)]\) is an origin-fixing Hausdorff isometric order embedding of the bounded closed convex hyperspace of \(X\) into that of \(X\oplus_\infty\mathbb R\), commuting with outer parallel bodies and sending every nonzero singleton to a segment; since \(c_0\cong c_0\oplus_\infty\mathbb R\), this yields a proper non-surjective Hausdorff self-isometry of the convex hyperspace of \(c_0\) with those properties.

## Correctness — PASS

The max-product Hausdorff identity gives \(d_H(A\times I,B\times J)=\max\{d_H(A,B),d_H(I,J)\}\). The radius functional is 1-Lipschitz for Hausdorff distance, so the extrusion preserves distance exactly. Projection recovers inclusion, and \(R(A\oplus tB_X)=R(A)+t\) gives exact outer-parallel-body preservation. Nonzero singletons become nondegenerate intervals in the added coordinate, and the standard coordinate shift identifies \(c_0\oplus_\infty\mathbb R\) isometrically with \(c_0\). These arguments also preserve compact convex sets.

**Evidence.** RESULT.md; Cheng–He–Liu–Zheng, arXiv:2609.18252

**Residual risk.** The construction is a counterexample mechanism, not a classification of non-surjective hyperspace isometries.

## Originality — PASS

The current arbitrary-Banach rigidity theorem is explicitly surjective. Its full introduction was inspected and distinguishes the finite-dimensional result of Gruber–Lettl, where surjectivity can be dropped, from the infinite-dimensional theory, where the main theorem remains surjective. The closest non-surjective source located is Zhou (2022); its accessible abstract gives support-space linearization and special smooth/additive representation results but does not state the radius-extrusion self-embedding or singleton-destroying \(c_0\) example. Its full text could not be obtained in this audit, which remains a localized risk rather than evidence of coverage.

**Equivalent formulations.** These properties distinguish the construction from generic isometric embeddings of support-function spaces.

**Broader coverage.** Finite-dimensional rigidity does not cover the infinite-dimensional \(c_0\) counterexample, and the surjective theorem cannot apply to a proper embedding.

**Exact database or table.** Coverage must come from a representation theorem or an equivalent explicit construction.

**Claim versus prior implication.** The audited example lies precisely outside the surjectivity hypothesis of the new rigidity theorem.

### Source inspections

- **Cheng, He, Liu and Zheng, arXiv:2609.18252** — full paper introduction and main theorem plus outer-parallel-body/order-rigidity sections. Arbitrary-Banach representation theorem is surjective; the paper records only finite-dimensional non-surjective rigidity.
- **Zhou, DOI 10.1016/j.jmaa.2022.126282** — abstract and bibliographic page; full text unavailable in this audit. Closest plausible non-surjective source; no explicit coverage visible in accessible material.

**Checked sources.** https://arxiv.org/abs/2609.18252; https://doi.org/10.1016/j.jmaa.2022.126282; https://doi.org/10.1112/blms/12.6.455; semantic search of the public findings corpus

**Residual risk.** The inaccessible full text of Zhou (2022) is a real but limited originality risk. If it contains an equivalent radius-dependent extrusion for nonsmooth spaces, originality would need revision.

## Value — PASS

The example pinpoints the necessity of surjectivity in a fresh arbitrary-Banach rigidity theorem and survives strong residual constraints—origin fixing, inclusion preservation, and exact outer-parallel-body compatibility. That is a motivated boundary counterexample with clear structural use.

**Residual risk.** It does not classify which additional hypotheses besides surjectivity restore rigidity.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
