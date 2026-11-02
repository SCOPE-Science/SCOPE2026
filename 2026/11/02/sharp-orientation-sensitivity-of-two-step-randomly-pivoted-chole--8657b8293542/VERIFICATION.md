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

# Reproducibility and evidence

Run `python3 verify.py` using Python 3 standard-library rational arithmetic. The program computes two sequential residual-dependent pivot updates for every ordered pair, without using the compact two-pivot expectation formula to generate the enumeration. The second computation evaluates the determinant identity, the predicted sharp bounds, exact equality examples, the one-step trace invariant, and the determinantally sampled benchmark. The finite cases include \(L\in\{1,3/2,2,4,11,100\}\) and exact rational unit vectors.

All automated assertions must pass and print `ALL_EXACT_ENUMERATIONS_PASS`. The global extrema, all equality cases, and the \(L\to\infty\) limit follow from the symbolic strict-concavity and Schur-complement proof in RESULT.md, not from finite enumeration. No external verification, priority certification, or finite-precision stability guarantee is claimed.
