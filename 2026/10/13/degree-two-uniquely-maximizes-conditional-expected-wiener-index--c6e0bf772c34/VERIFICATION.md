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

# Reproducibility
The attached \(\texttt{verify.py}\) runs using only Python's standard library:

```sh
python3 verify.py
```

The code independently enumerates all Prüfer sequences for tree sizes \(2\le n\le8\), totals \(280392\) labelled trees, groups by the distinguished degree, checks all condition probabilities and the root/nonroot Wiener contributions, and verifies every finite mode. It additionally tests the analytic strict-inequality formula at thousands of integer parameter pairs beyond enumeration, using exact fractions. The all-integer theorem does **not** follow from the finite checks: its proof is the weighted path-counting identity, rational difference induction, and degree-one-to-two contraction argument in the accompanying result.

No external audit or mathematical certification is represented by this document.
