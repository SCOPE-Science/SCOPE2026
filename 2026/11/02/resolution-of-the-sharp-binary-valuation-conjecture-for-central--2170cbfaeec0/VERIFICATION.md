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

# Verification instructions and scope

Execute `python3 VERIFIER.py` from the directory containing this document. The script requires only the Python standard library and prints `VERIFY_OK` on success. It checks, with exact integer and rational arithmetic, the formula for 4096 positive indices, the binomial definition through index 80, the exceptional polynomial coefficients, the complete finite inequality checks for \(2\le j\le31\), and convergence identities modulo powers of two.

The full proof is contained in `RESULT.md`, including the all-index valuation bounds and formal dilogarithm identity. Exhaustive checks of finite ranges do not certify an infinite theorem. This package makes no claim of an independent audit or external certification.
