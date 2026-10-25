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

# Reproduction of the arithmetic certificates

Execute `python3 verify.py` with the Python 3 standard library. No online resources or third-party packages are required. For both Stirling indices, the program checks normalized prime-power differences for \(p=2,3,5\), their complete bounded coprime-exponent periods, and every exponent up to the proven stability threshold. It reconstructs the five lower-bound denominators by a recurrence and Möbius inversion.

Expected final output: `ALL CERTIFICATES PASS`. The proof in `RESULT.md` establishes why these finitely many arithmetic checks control all positive indices. The program does not mechanically check that proof, does not constitute an independent mathematical audit, and makes no claim about other Stirling indices.
