# Independent scientific audit — Exact K_{2,4}-free Turán number for cographs

Audit date: 2026-10-01 (UTC) UTC.

Disposition: **PASSED**.

## Correctness

**PASS** — The cotree argument is sound. A connected cograph of order at least seven with no universal vertex has a root join factor of size at least two joined to at least four remaining vertices, forcing K_{2,4}. With a universal vertex, K_{2,4}-freeness is equivalent to Delta(H)<=3 and K_{2,3}-freeness in H; every connected cograph component of H then has at most four vertices. Convex clique packing gives the exact 6q+binom(r,2) remainder and uniqueness. The n=6 non-universal root join reduces to 3+3 with at most one internal edge per side, producing exactly the second 11-edge extremal. Strict superadditivity excludes disconnected equality. Boundary orders n<=5 are correctly handled by K_n.

## Originality

**PASS** — Zimmermann studies precisely K_{s,t}-free cographs, proves eventual pumping and the linear coefficient s-1+(t-1)/2, and gives an all-order K_{2,t} structural theorem only for t in {2,3}. The accessible full-text rendering explicitly remarks that larger t can have small extremals without a complete vertex. Resultary search found no separate all-n K_{2,4} closed formula/classification. Prior dynamic-programming data may cover individual small n values but do not imply the all-order theorem.

### Equivalent formulations

Aliases included induced-P4-free host graphs, K_{2,4} subgraph avoidance, cograph Zarankiewicz numbers, and universal-vertex formulations.

Searches: Resultary: exact K_{2,4}-free cograph Turan number all n; Zimmermann arXiv:2601.07406.

Evidence: No equivalent all-n formula/classification outside the audited record was located.

### Broader coverage

Those broader statements constrain the answer but do not imply the exact periodic correction or complete t=4 classification for every n.

Searches: Zimmermann Pumping Theorem; Zimmermann Theorem 3 for K_{2,t}.

Evidence: The Pumping Theorem gives eventual periodic linearity and coefficient 5/2 for (2,4); Theorem 3 is all-order only for t=2,3.

### Exact database or table

Exact database/table coverage is therefore partial and non-dominating.

Searches: Zimmermann accompanying dynamic-programming project; Resultary semantic search.

Evidence: The prior project contains small-instance data, which can cover individual finite values but not the proved closed all-n formula/classification.

### Claim versus prior implication

The audited t=4 proof is not a formal corollary of the source theorem; it adds a new structural argument and small-order classification.

Searches: Zimmermann arXiv:2601.07406.

Evidence: The source explicitly limits its simple K_{2,t} all-order theorem to t=2,3 and notes complications for larger t.

### Source inspections

- **Bipartite Turán problem on cographs** (https://arxiv.org/abs/2601.07406v2): Assessment: provides asymptotic/general framework and small-data algorithm but not the all-n K_{2,4} formula. Material read: abstract plus accessible full-text rendering of Theorem 3, its t in {2,3} scope, the larger-t remark, and Pumping Theorem context. Evidence: Theorem 3 is explicitly restricted to t=2,3; the paper remarks that larger t has exceptional small extremals.

Checked sources: https://arxiv.org/abs/2601.07406v2; Resultary semantic search for K_{2,4}-free cograph exact formula; Zimmermann project noted in the record.

Residual risks: The prior computational repository can contain finite K_{2,4} values not individually re-enumerated in this audit; that does not cover the all-n proof/classification.

## Scientific value

**PASS** — The result is the next natural K_{2,t} case beyond the prior t=2,3 all-order theorem and upgrades eventual/asymptotic information to a closed exact formula and complete extremal classification, including the exceptional n=6 type. That is a motivated structural extension.

## Final claim

Writing n-1=4q+r with 0<=r<=3, the maximum edge count in an n-vertex K_{2,4}-free cograph is (n-1)+6q+binom(r,2). For n>=7 the unique extremal graph is K_1 joined to q copies of K_4 and K_r; n=6 has exactly one additional extremal type.

This audit is a scientific assessment of the claim and supplied evidence. It is not peer review, formal verification, or a guarantee of first discovery.
