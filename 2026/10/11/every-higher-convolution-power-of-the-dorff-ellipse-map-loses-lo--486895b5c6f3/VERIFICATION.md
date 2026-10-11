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
# Verification of all higher harmonic convolution powers

The normalized map and coefficient tails are the exact rational formulas of Wang and Zhong, arXiv:2609.11556v1, Sections 5–6. The proof in RESULT.md contains the complete universal argument for every integer \(m\ge3\): sign of the rational generating derivative \(S_t\), binomial expansion for \(p_m'\) and \(q_m'\), exact lower bound at \(m=3\), monotonicity in \(m\), the intermediate value theorem, and Lewy's local-univalence necessary criterion.

Run `python3 artifacts/verify.py`. The checker uses Python standard-library fractions, performs exact rational operations, confirms the six source constants and elementary inequalities, and checks the analytic/coanalytic derivative bounds for every integer \(3\le m\le12\). The expected output starts `EXACT_RATIONAL_CHECKS_PASS`. These checks corroborate the algebra but do not replace the proof for all \(m\), and do not count nonreal critical points or claim any independent certification.
