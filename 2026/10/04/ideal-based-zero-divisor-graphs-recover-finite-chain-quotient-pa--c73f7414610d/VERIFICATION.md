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

The proof was replayed from the actual package artifact `verify.py`.

The symbolic check constructs
\[
n_i=s(q-1)q^{\ell-i-1}
\]
and
\[
d_i=\sum_{j=\ell-i}^{\ell-1}n_j-\mathbf 1_{\{2i\ge\ell\}},
\]
verifies strict increase of the degree sequence, and reconstructs \((q,\ell,s)\) from the unlabeled degree classes.

The profile grid uses ten prime-power residue orders, every nilpotency length from \(3\) through \(8\), and ideal sizes from \(1\) through \(6\). The checker also constructs ideal-based graphs directly for several rings \(\mathbb Z/p^N\mathbb Z\) and reconstructs the parameters from actual adjacency lists.

Finally, it directly checks the sharp length-two collision between
\[
\Gamma_0(\mathbb Z/9\mathbb Z)
\quad\text{and}\quad
\Gamma_{(4)}(\mathbb Z/8\mathbb Z).
\]

Exact output:

```text
VERIFY_OK
symbolic_profiles_checked=360
actual_Zmod_case=(2, 3, 3, 3, 1, (2, 3, 1))
actual_Zmod_case=(2, 4, 3, 6, 2, (2, 3, 2))
actual_Zmod_case=(2, 5, 4, 14, 2, (2, 4, 2))
actual_Zmod_case=(3, 3, 3, 8, 1, (3, 3, 1))
actual_Zmod_case=(3, 4, 3, 24, 3, (3, 3, 3))
actual_Zmod_case=(3, 4, 4, 26, 1, (3, 4, 1))
length_two_collision=Gamma_0(Z9)=Gamma_(4)(Z8)=K2
```

The finite calculations are corroborative only. The arbitrary finite chain-quotient theorem is established by the symbolic valuation and degree-class proof.
