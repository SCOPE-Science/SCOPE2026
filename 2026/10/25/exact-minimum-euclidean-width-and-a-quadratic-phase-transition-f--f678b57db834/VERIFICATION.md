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

# Verification and reproducibility

The proof in `RESULT.md` is exact for every integer \(n\ge5\), \(2\le k\le n-2\): it uses the support formula, centered ordered-chamber gap decomposition, Euclidean triangle inequality, and strict equality conditions. The parity arithmetic is displayed explicitly, avoiding extrapolation from finite experiments.

To reproduce the supplementary finite checks, run `python3 verify_width.py` in the same directory. The verifier uses Python's standard library, performs \(12{,}320\) rational phase/candidate checks, \(25{,}540\) explicit two-level checks and \(65{,}800\) random-direction inequality checks. The program was executed successfully. All numerical results are finite regression checks, not a proof of the quantified theorem and not a certification of novelty.

Only intrinsic Euclidean normals orthogonal to the all-ones vector are used. The known centrally symmetric subcase is acknowledged in the prior-work comparison. No independent audit has been performed.
