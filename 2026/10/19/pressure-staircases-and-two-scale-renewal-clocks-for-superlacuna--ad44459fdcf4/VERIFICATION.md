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

# Reproducibility and limits

Execute `python3 verify.py` in the directory containing this file and `RESULT.md`. The script requires only the Python standard library and evaluates the normalized pressure equation using bisection, not any precomputed result or externally stored data. It also computes the exact weighted renewal-size-bias identities, exact Laplace transforms of the inter-clock correction, and finite return-composition checks.

The proof for unbounded superlacunary sequences rests on the elementary tail estimates, the entropy/relative-entropy inequality for induced gap processes, Kac and Abramov return formulas, and Palm size bias, all spelled out in `RESULT.md`. The Python checks are limited to factorial sequences at finitely many indices and do not certify the general class or infinite-dimensional vague convergence. No external audit or independent validation has occurred.
