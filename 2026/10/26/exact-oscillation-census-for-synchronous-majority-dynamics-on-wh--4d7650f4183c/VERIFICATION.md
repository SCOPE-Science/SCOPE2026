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

# Reproducible checks

Run `python3 verify_wheel.py` using Python 3 standard library in the same directory. The code independently checks cyclic no-isolated-one word counts against the closed binomial-run polynomial for lengths 2 through 14, and compares direct wheel majority updates over all \(262112\) labeled states for rim lengths 4 through 16 against the exact periodic-point census.

Proof-critical identities are \(A(A(x))_i=x_{i-2}x_ix_{i+2}\), \(C(A(x))_i=x_i(x_{i-2}\lor x_{i+2})\), and the integer marked-run count \(\ell\binom{a-r-1}{r-1}\binom{\ell-a-1}{r-1}/r\). These are derived in RESULT.md, not inferred from code. The proof of period at most two uses a finite symmetric matrix with odd row sums. The growth bound uses an injective block construction. No checker establishes originality, validates all infinite cases by exhaustion, or provides independent audit.
