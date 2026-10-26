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

# Verification of the marked-cycle descent law

Run `python3 verify.py` using Python 3 and its standard library. The program enumerates every one-line permutation through nine symbols, reconstructs the cycle containing symbol \(1\), and checks all conditional sitewise descent probabilities, the uniform law for cycle length, the conditional mean, and the covariance using exact rational arithmetic. The expected terminal output is `VERIFICATION_OK 336`.

The finite checks supplement the analytical proof; they do not establish the statement for unbounded sample size. The involution and complementary-cycle arguments in `RESULT.md` provide the unrestricted proof. The exceptional sample size \(n=2\) is excluded from the theorem. No independent audit has been conducted.
