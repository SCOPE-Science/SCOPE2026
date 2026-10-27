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

# Reproducibility of the five-site obstruction

The included standalone standard-library Python program runs polynomial additions and multiplications over the integers, checks the exact factorization of the sign numerator \(H\), and computes the transformed degree-28 polynomial coefficient-by-coefficient. The coefficient sequence has exactly one sign change. The program independently enumerates \(512\) Ising spin states for each of five inverse temperatures and reconstructs the Möbius sum directly from avoidance probabilities.

The root is isolated by 260 bisection steps with 70-digit decimal arithmetic, and its quoted decimal expansion is a numerical locator for the exact unique polynomial root. Re-execute the program in `verification/check_cross_intensity.py`; the recorded output is in `verification/check_output.txt`. No stochastic sampling, hidden files, external APIs or third-party packages are needed.

The enumerations are finite checks, not a proof of statements for all temperatures. Those statements follow instead from the exact factorization and Descartes sign certificate presented in RESULT.md. No claim of independent validation is made.
