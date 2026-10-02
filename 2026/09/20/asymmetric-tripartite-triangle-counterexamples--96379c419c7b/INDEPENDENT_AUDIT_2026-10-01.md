# Independent mathematical audit — SCOPE-20260920-96379c419c7b

Audited at: 2026-10-01T18:05:11.787582Z

Disposition: **passed**

## Correctness — PASS

The three-part construction is internally consistent. Every vertex class meets degree at least \(n+t\) under \(n\ge3t+p+q\), and the only possible triangles are exactly the two gadget-supported types, giving \(F_t(p)+F_t(q)\). On the relevant branch, \(F_t(u)/t^3-2=(u/t-1)(2-(u/t)^2)\), so \(p_t=\lfloor\sqrt2\,tfloor+1\) is the first integer parameter that can make one contribution strictly below \(2t^3\); pairing it with \(t\) yields the stated order threshold. The inspected verifier exhaustively confirms the construction for small parameters and the threshold arithmetic through \(t=5000\), but the symbolic argument is the proof.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify.py
- Fang-Xu arXiv:2609.20590

### Correctness risks

- The claim is an upper-bound construction only; it does not determine the true minimum \(f(n,t)\).

## Originality — PASS

The September 2026 Fang-Xu paper gives the symmetric one-parameter construction and its \((3+2\varphi)t+O(1)\) threshold. Resultary returned no earlier published SCOPE theorem with the asymmetric \(p,q\) construction or the \(4+\sqrt2\) threshold. The audited two-parameter split changes the order-versus-triangle optimization and is not implied by the symmetric specialization.

### Equivalent formulations

No equivalent asymmetric two-parameter theorem was located.

### Broader coverage

The broader problem setting does not imply the new order threshold because the asymmetric construction is not a specialization of the published symmetric family.

### Exact database or table

This is a construction theorem rather than a table lookup; the database check is supportive only.

### Claim versus prior implication

The assigned result strictly extends the construction family and yields a lower order threshold not mechanically implied by the symmetric statement.

### Sources inspected

- On the minimum number of triangles in balanced tripartite graphs with large minimum degree — https://arxiv.org/abs/2609.20590. NOT_COVERING_IN_MATERIAL_READ: The primary statement uses the symmetric threshold \(3t+2\lceil\varphi tceil\), not the asymmetric \(4t+\lfloor\sqrt2 tfloor+1\) construction.

### Checked sources

- https://arxiv.org/abs/2609.20590
- Resultary semantic search
- Bollobas-Erdos-Szemeredi 1975 reference in the package

### Residual risks

- The primary preprint is very recent, and its complete full text was not independently retrieved in this run during this audit.

## Value — PASS

The result gives a structurally new asymmetric counterexample family and substantially lowers the first known order coefficient for violating the proposed \(4t^3\) bound, from about \(6.236\) to \(5.414\). That directly narrows a live extremal-combinatorics gap.

### Value sources

- Fang-Xu arXiv:2609.20590
- assigned RESULT.md

### Value risks

- It is not an optimality theorem for arbitrary tripartite graphs.

## Limitations

- Upper-bound construction only; \(f(n,t)\) is not determined.
- Optimality is only within the displayed two-parameter family.
- Full text of the very recent Fang-Xu preprint was not independently retrieved in this run during this audit.
