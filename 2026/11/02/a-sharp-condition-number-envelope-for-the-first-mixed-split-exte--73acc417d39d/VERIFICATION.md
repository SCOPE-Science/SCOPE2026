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

# Reproducibility and verification

The proof in RESULT.md gives a continuous-domain spectral variational argument: a first-variation derivative is strictly concave, hence minimizers are endpoint-supported, and a one-sign-change cubic has a unique positive root. The sharpness construction uses three distinct active eigenvalues for every positive small mixing weight. These steps, rather than a numerical search, establish the universal statement.

Execute `python3 verify.py` with Python 3 and the standard library. The checker computes all candidate projection ratios using weighted Gram projection formulas independent of the closed-form moment ratio, and checks an algebraically independent quotient-rule derivative identity on rational grids. The completed execution reports 779 exact candidate comparisons, 779 rational interval checks, 1,639 exact derivative checks, and 1,495 exact cubic transformations, for 4,692 supplementary checks.

Separate floating-point envelope stress tests compared 7,000 randomly generated spectral measures against numerically optimized two-point envelopes. This sweep is independent supporting evidence, not exhaustive certification. No simulation or finite test establishes originality, infinite-domain correctness, floating-point stability, or independent validation. Only the first nonbreaking third step is covered. The sharp infimum is not attained at a nonbreaking step.
