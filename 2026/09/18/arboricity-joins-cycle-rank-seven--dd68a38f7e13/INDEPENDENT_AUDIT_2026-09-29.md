# Independent audit — A cycle-rank criterion for exact arboricity of graph joins

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/arboricity-joins-cycle-rank-seven--dd68a38f7e13`
**Audited tree:** `ceeb7f3ea9dff09be7a90f6e007d4cf2237ec69a`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The Nash–Williams argument is correct. For a two-sided induced set of sizes s,t the excess c over two trees satisfies c<=beta, and the desired K-forest density inequality is exactly c<=R_q(s,t)=q^2-q+1-(q-s)(q-t), q=K-1. The proof correctly handles large-large, mixed, and small-small regimes, treats one-sided subsets separately, and gives a valid exceptional q=2 bound beta<=7. An independent exhaustive check of all 961 ordered pairs of connected graph-atlas graphs of orders at most five found no counterexample whenever the theorem's hypotheses held. The beta=8 sharpness construction independently gives full-set ceiling 3 but exact arboricity 4.

### Independent checks

- Re-derived the identity e((G*H)[A union B])=st+s+t-2+c and the equivalent Nash–Williams condition c<=R_q(s,t).
- Verified the factorization R_q=q^2-q+1-(q-s)(q-t), the small-small simple-graph inequality, and the separate one-sided bound e(U)<=min(C(r,2),r-1+beta).
- Exhaustively enumerated all 961 ordered pairs of connected graph-atlas graphs of orders at most five satisfying the theorem hypothesis and computed arboricity exactly from all vertex subsets; zero counterexamples were found.
- Independently reconstructed the beta=8 witness: G has 7 vertices and 14 edges, H=K1, the join has 21 edges on 8 vertices (full-set ceiling 3), while a 7-vertex induced subgraph has 19 edges, forcing arboricity 4.
- Independently inspected all ten pages of arXiv:2609.20606 via authorized full-text retrieval after ordinary arXiv/OA full-text access was unavailable; its join section contains bounds and examples only.

## Originality

PASS to the best of current searchable knowledge. The directly relevant Kuanyshov–Yeginbay arXiv:2609.20606 was independently inspected in full: Theorem 23 gives only max/lower and additive upper bounds for joins, followed by examples, and contains no cycle-rank exactness criterion. Fresh searches through 2026-09-29 found no theorem giving the submitted quadratic criterion or the sharp universal beta<=7 threshold.

### Literature checked

- https://arxiv.org/abs/2609.20606 — Kuanyshov–Yeginbay, Arboricity and Simplicial Geometric Category of Wedges and Joins of Graphs; full text inspected, Theorem 23 supplies general join bounds but no cycle-rank exactness theorem.
- https://doi.org/10.1112/jlms/s1-39.1.12 — Nash-Williams, Decomposition of Finite Graphs Into Forests; classical arboricity characterization used in the proof.

## Scientific value

The result turns broad join bounds into an exact formula on a natural structural regime, with a best-possible uniform cycle-rank threshold and an explicit obstruction at eight. It is elementary graph theory, but the theorem is clean, sharp in its universal corollary, and directly advances the newly studied join-arboricity problem.

## Limitations

- The main criterion is sufficient, not necessary, and the quadratic beta threshold is not claimed optimal for each fixed K>=4.
- The sharpness claim concerns the universal constant seven, not every parameterized threshold.
- The motivating join-arboricity paper is very recent, so unindexed parallel work remains a residual originality risk.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
