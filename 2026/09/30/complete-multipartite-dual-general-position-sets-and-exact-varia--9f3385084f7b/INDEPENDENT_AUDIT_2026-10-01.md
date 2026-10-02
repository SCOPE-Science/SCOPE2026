---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For connected complete multipartite graphs, outer, total, and dual general-position sets admit the displayed exact counting polynomials; in particular, nonempty dual sets are exactly the two structural types in the record, giving the stated complete formula for \(\operatorname{gp}_d\).

## Correctness — PASS

The complete-multipartite distance structure gives ordinary general-position sets exactly as subsets of one part or sets meeting each part at most once. The published outer characterization reduces to mutual maximal distance: same-part pairs always qualify and cross-part pairs qualify exactly when both endpoint parts are singletons. The published total characterization reduces to simplicial vertices. For dual sets, the complement is convex exactly when two retained vertices in one part force every vertex outside that part into the complement. Combining this with ordinary general position yields precisely the two listed dual types and the piecewise enumerator. The inspected exhaustive script independently checks all 58 multipartite types through order eight and all coefficient vectors, but the general proof is combinatorial.

**Checked sources.** assigned RESULT.md and verify.py at tree 0e4a31e9124e17c7760f9f58f3ebc6fb8b3fa29d; Tian--Klavžar, arXiv:2402.17338, primary theorem statements

**Residual risks.** No correctness defect was found.

## Originality — PASS

Tian--Klavžar introduce the three variants and prove the general outer, total, and dual characterizations, but their public theorem description does not give the complete-multipartite dual classification or the counting polynomials. Resultary searches found the assigned theorem but no earlier equivalent complete-multipartite result.

### Equivalent formulations

Those general characterizations are ingredients; the audited claim classifies their simultaneous consequences for all multipartite part profiles.

### Broader coverage

No stronger inspected theorem determines the dual family or its polynomial.

### Exact database or table

Finite graph tables are inapplicable to an all-parameter symbolic classification.

### Claim versus prior implication

The prior characterization does not mechanically print the resulting polynomial or set classification.

**Checked sources.** https://arxiv.org/abs/2402.17338; doi:10.1007/s40840-024-01788-z; Resultary semantic search

**Residual risks.** Older strong-resolving literature may implicitly contain the outer companion formula, which is not the novelty-critical part.

## Value — PASS

Dual general position is non-hereditary and can vanish, so the exact set classification and generating polynomial expose a genuine phase transition on a canonical graph family. The result is a natural complete classification rather than a finite lookup.

**Checked sources.** Tian--Klavžar 2024/2025

**Residual risks.** The companion outer and total formulas are simpler consequences and carry less independent value.

## Limitations

- Finite simple connected complete multipartite graphs only.
- The outer and total structural characterizations used are prior work.
- The finite verifier through order eight is corroborative only.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
