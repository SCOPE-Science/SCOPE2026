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

# Reproducibility and scope of checks

The derivation and exact quantifiers are in `RESULT.md`. Run `python check.py` with the small dependency in `requirements.txt`. The recorded `check_output.txt` is the actual output from that checker. The checker directly compares the probability-normalized Fourier transform to quadrature, evaluates the numerator and its first three derivatives near explicitly predicted resonances, excludes higher multiplicities in tested cases, checks nonresonance at sampled odd/odd rational ratios, and follows the three complex roots near a radius perturbation of the resonance at ratio \(1/2\).

Twelve transform-integral comparisons, twenty-five resonance evaluations, twelve nonresonant shared-root evaluations, and four signed-perturbation triple-branch tests passed. These are numerical samples, not an exhaustive enumeration and not certificates of global uniqueness or of all-parameter correctness. The latter follow from the analytic derivative factorization and the holomorphic local-root argument in the proof. Independent audit is not performed.
