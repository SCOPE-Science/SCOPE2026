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

The analytically proved theorem concerns all nonnegative harmonic degrees and all real continuation parameters. The accompanying checker is a finite corroboration and does not assert an independent or exhaustive computational proof.

Run `python verify.py` in the same directory with SymPy and mpmath installed. The checker uses exact rational beta integrals at 144 physical integer parameter/degree pairs, directly evaluates the 2026 terminating even-dimensional hypergeometric formula at 144 nonintegral parameter/degree pairs, tests 7 positive and 7 negative parameter samples across degrees up to 100, and verifies 40 degree identities at the Hardy duplication point \(s=-2\).

Expected successful output: `VERIFY_OK independent_exact_beta_cases=144 terminating_4F3_checks=144 positive_parameter_samples=7 negative_parameter_samples=7 s_minus_two_cases=40`.

The universal sign classification is established in the Proof section of `RESULT.md`: use the exact gamma quotient, partition the real line, rule out all non-allowed open bands by coefficients of sufficiently large degree or degree one, and rule out integer poles by a degree depending on the pole index. The reproducing-kernel assertion uses spherical addition-kernel polynomial bounds and geometric radial convergence. This is self-review mathematics only; no independent audit was performed.
