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

# Verification

Run `python verify.py` with Python 3 standard library only. It enumerates all subsets of the vertex set of each squared cycle for orders 7 through 23 at all cardinalities up to the asserted optimum, independently verifies open-neighborhood total domination and the cyclic-gap characterization, and reconstructs all minimum-configuration exchange edges. At orders 7, 14 and 21 it checks cycle/frozen predictions; at 9, 16, 23 it checks the exact plus/minus seven translation rule and connected cycle structure. The final line should read `ALL_VERIFY_OK`.

This computational check is finite and cannot prove the asserted infinite-family formulas. Those conclusions follow from the symbolic gap and exchange proofs in RESULT.md. External independent auditing has not been performed.
