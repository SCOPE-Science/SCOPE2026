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

# Reproduction and limits

Execute `python verify_hazard.py` after installing `sympy>=1.10` and `mpmath>=1.2`. The script checks exact rational-polynomial identities, the series-inversion coefficients, and numerical root/derivative/endpoint examples. Expected console output is embedded in `verification_output.txt`. The tests do not cover an infinite interval by enumeration; the exact derivative factorization and strict positive-coefficient inequality in `RESULT.md` provide the full proof. Literature comparison is not formalized by the checker.

The computation is reproducible from the standalone script and does not require any unbundled input data or inaccessible prior-run artifact. Independent audit has not been performed.
