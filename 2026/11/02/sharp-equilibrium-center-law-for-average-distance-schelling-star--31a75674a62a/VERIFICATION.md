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

# Reproducible calculations and their limits

Run `python3 verify.py` using Python 3 (standard library only) from the directory containing this file. The verifier directly compares hub--leaf before/after costs with the symbolic strict certificate for all sorted multisets drawn from six integer levels and with at most eight agents. It checks 20,586 such center/profile instances with exact rational costs, and checks every center of every equally spaced grid of sizes \(3\) through \(400\) against the independently evaluated radical interval rule (80,197 instances). It checks a five-type noninterval example and numeric convergence of the stable-center ratio at five increasing grid sizes.

Observed outcome: `ALL CHECKS PASSED (finite tests do not prove asymptotics)`. The tests are finite and do not constitute a proof of the limiting constant. The proof in `RESULT.md` establishes the strict boundary conditions, weak-convergence transfer, and count error, including integer endpoint handling. No independently commissioned audit, theorem-prover certificate or external validation is claimed.
