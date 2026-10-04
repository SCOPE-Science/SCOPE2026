---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof has three independently replayable algebraic checkpoints.

1. **Valuation model.** In each chain factor, an annihilator class is determined by the valuation \\(a_i\\). In a product, classes are valuation vectors; the unit and zero vectors are omitted. Distinct vectors are adjacent exactly when every coordinate sum reaches the corresponding chain length.

2. **Degree and leaf reconstruction.** For a vertex \\(a\\), the degree formula
\[
d(a)=\\prod_i(a_i+1)-1-\\delta(a)
\]
is obtained by direct counting, where \\(\\delta(a)\\) records whether the vertex squares to zero. With at least two factors, the leaves are exactly the single-coordinate valuation-one vectors. The degree of each leaf’s unique neighbor gives the associated chain length, with the \\(T=6\\) overlap resolved by the factorization \\(6=2\\cdot3\\).

3. **Boundary cases.** Graph orders corresponding to \\(T=2,3,5\\) force one factor. At \\(T=4\\), the two possible length multisets \\(\\{3\\}\\) and \\(\\{1,1\\}\\) both give \\(K_2\\), producing the unique ambiguity.

The standalone `verify.py` checks the valuation graph, degree formula, and reconstruction procedure over a bounded but broad parameter grid. Its exact output is:

```text
VERIFY_OK
length_multisets_checked=225
maximum_graph_order_checked=498
exception=(3)<->(1,1)=K2
```

The computation is corroborative only. The general theorem rests on the symbolic reconstruction in `RESULT.md`.
