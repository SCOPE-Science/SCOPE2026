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

# Verification and limits

The analytical proof consists of five reconstructible steps: the three-matching quotient matrix \(Q\), the sign-twist formula, the exact Hadamard-basis restriction \(M\), the trace inequality and the star equality. No simulation is used to justify a universal quantifier.

The accompanying `verify.py` was run against the exact stage file. It passed **eight symbolic matrix/algebra identities**, **2053 deterministic seeded numerical rate-vector inequalities**, and an exact star-sharpness check. SymPy and NumPy are needed to reproduce it. The tests do not constitute an exhaustive search of all real weights or a second independent audit.

Checked source coverage comprises the relevant sections of Alon's 2026 full arXiv article, including Conjecture 1.5 and Theorems 4.4–4.5, and the primary Alon–Kozma 2013 PDF, including its definition of the Aldous order, Figure 1, and Corollary 3.2. Neither provides this weighted-four-vertex uniform lower bound as a theorem. Further undocumented priority is a residual risk.
