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

# Reproducibility and boundaries

The proof is given in `RESULT.md` and does not depend on experiments. Its critical algebraic steps are the cyclic-group decomposition of the index-\(d\) subgroup, the equality \(\operatorname{Tr}(h)^2=2\operatorname{N}(h)\) for a generator with fourth-order Frobenius ratio, and the resulting projected cubic-coset images.

Execute `python3 verify.py`. It uses only the Python 3 standard library, constructs seven quadratic extensions \(\mathbb F_{p^2}\) with \(p\in\{7,19,31,43,67,79,103\}\), verifies multiplicative generator orders by exact divisibility checks, enumerates every subgroup member and every additive subfield translate, and compares the resulting complete representation histograms with the theorem. It checks both cubic branches and the trace–norm identity.

Expected final output: `CERTIFICATE_OK 7 complete quadratic-prime-field enumerations`.

These exact finite enumerations demonstrate consistency for seven fields but are not exhaustive over prime powers; the infinite theorem follows from the written group and field argument. The completeness of prior-work searches and independent mathematical validation are not certified.
