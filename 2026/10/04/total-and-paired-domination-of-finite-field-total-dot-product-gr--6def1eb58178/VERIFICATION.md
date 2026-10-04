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

The verification separates finite replay from the general proof.

1. **Lower bound.** A total dominating set \(D\) gives a cover of \(\mathbb F_q^n\) by the hyperplanes \(d^\perp\), \(d\in D\). The proof uses the explicit bound
\[
|H_1\cup\cdots\cup H_k|\le q^{n-1}+(k-1)(q^{n-1}-1),
\]
which is strictly below \(q^n\) when \(k\le q\).

2. **Odd-characteristic witness.** An anisotropic two-plane has \(q+1\) projective lines, and orthogonal complement is a fixed-point-free involution on them. Representatives give a paired total dominating set.

3. **Even-characteristic witnesses.** A two-plane with one-dimensional radical yields a total dominating set of size \(q+1\). A nondegenerate two-plane has exactly one isotropic projective line; adding one nonzero vector from its ambient orthogonal complement matches that line and gives a paired dominating set of size \(q+2\).

4. **Finite replay.** `verify.py` builds the graph from the dot-product definition and exhaustively finds the two minima for \(TD(\mathbb F_2,3)\), \(TD(\mathbb F_2,4)\), and \(TD(\mathbb F_3,3)\). It also checks an explicit size-six paired witness for \(TD(\mathbb F_5,3)\).

Exact output:

```text
q=2,n=3: vertices=7, gamma_t=3, gamma_pr=4 exhaustive
q=2,n=4: vertices=15, gamma_t=3, gamma_pr=4 exhaustive
q=3,n=3: vertices=26, gamma_t=4, gamma_pr=4 exhaustive
q=5,n=3: explicit paired-total witness size=6 verified
hyperplane-union lower-bound arithmetic checked
VERIFY_OK
```

The finite replay is corroborative only. The arbitrary-prime-power theorem follows from the algebraic hyperplane-cover and projective-line constructions.
