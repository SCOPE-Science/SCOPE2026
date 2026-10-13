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

Execute `python verify.py` using Python 3.10 or newer. No external libraries, data files, or network access are needed. A successful exact-arithmetic check prints `VERIFY_OK`.

The checker independently substitutes the rational parameter point into the published rumor ODEs and reproduction number; verifies the rational equilibrium; reconstructs the elimination equation as a rational polynomial identity; and checks the two exact characteristic polynomials. The proof in `RESULT.md` supplies the analytic arguments not certifiable by a finite test: Descartes' sign rule, the intermediate-value theorem, the cubic Routh–Hurwitz criterion, and the implicit-function theorem.

A precise limitation: the checker does not prove all mathematical assertions by formal methods and does not survey the entire literature. The claim makes no assertion of independent validation.
