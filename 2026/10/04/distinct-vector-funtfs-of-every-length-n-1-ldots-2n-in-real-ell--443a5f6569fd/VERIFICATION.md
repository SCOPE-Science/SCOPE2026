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
The proof is symbolic. The key checks are: every added row is strictly positive and sums to \(1\); every column sum is \(k/n\); the first \(n\) functionals have \(\ell_\infty\)-norm one because \(k\le n\); each extra all-ones functional norms its positive unit \(\ell_1\)-vector; and the two frame-operator contributions cancel their \(J\)-terms exactly, leaving \(((n+k)/n)I\).

The bundled checker uses exact rational arithmetic. It verifies the general formula for all \(2\le n\le12\) and \(1\le k\le n\), and separately checks the displayed \((n,k)=(5,2)\) seven-vector example. Those finite checks are consistency tests only; the all-\(n\) statement follows from the algebraic proof.

No independent audit has been performed.
