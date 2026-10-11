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

# Verification scope

The proof of the exact root uses the finite generator suspension and the entropy variational principle. The asymptotic proof uses the Catalan generating function, Stirling's asymptotic with a uniform error, and a monotone squeeze around an explicitly computed Laplace threshold. These steps, including the constant \(\tfrac12\log\pi\), were reconstructed analytically.

The included `check_entropy.py` is runnable with Python 3 and the standard library from this directory. Executing `python3 check_entropy.py` reported `PASS: 18 finite diagnostics (not a proof).` Checks comprise seven exhaustive primitive-word counts through semilength 7, eleven approximate roots through cutoff 100000, a residual bound below \(5\cdot10^{-13}\) at each tested cutoff, and a loose asymptotic threshold check for cutoffs at least 1000. The checker is an optional finite sanity check, not a verification of infinitely many parameters, a machine proof, or an independent audit.

The theorem concerns finite generator sets of semilength at most \(N\), not generic enumerations. The \(o(1)\) remainder is not assigned an effective global rate. A related older pressure article was available only at abstract level for literature comparison, so originality has residual priority risk.
