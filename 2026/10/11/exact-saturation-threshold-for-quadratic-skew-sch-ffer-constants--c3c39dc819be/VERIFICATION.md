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

## Mathematical checks
The finding is an analytic if-and-only-if theorem. Its quantitative normalization is the square of the quadratic power mean of the two output norms, not their unnormalized sum. The exact lower envelope is \((1+\tau^2)(1+\alpha^2)/2\), and the contact condition is \(\tau\ge\beta/m\), where \(m\) is the maximum of a strictly concave function on \([-\alpha^2,\alpha^2]\). The proof distinguishes the Euclidean cone of both transformed outputs from the condition that each input lie on the norm-unit sphere.

The golden-ratio branch crossing is the exact positive solution of \(\alpha^4+\alpha^2=1\). The lower and upper endpoints \(\tau=0,1\), equality at \(\tau=\tau_c\), and both sides of \(\tau=\beta\) are covered explicitly in the proof.

## Executable diagnostic
Run `python3 verify_threshold.py` from the directory containing the accompanying file. The program uses only Python's standard library. It checks the rational case \(\alpha=4/5\) and \(\tau_c=12/25\) with `fractions.Fraction` exactly, including the active-cone tie and equality of the two sides at \(31529/31250\). For the complementary branch \(\alpha=3/5\), it verifies the threshold contact with 65-digit `decimal.Decimal` precision. Successful execution prints `SKEW_SCHAEFFER_THRESHOLD_EXACT_CHECK_OK`.

These two instances provide useful arithmetic regression tests. They are not a proof of an infinite parameter family or strict positivity below its critical threshold; both follow from the analytical equality-case reduction.

## Scientific limits
The theorem classifies precisely when a known lower envelope is attained, and does not determine the optimal value in the strictly subcritical range. Its originality comparison relies on accessible published mathematical statements; unindexed or unpublished equivalents cannot be excluded by a search. No independent audit has been carried out.
