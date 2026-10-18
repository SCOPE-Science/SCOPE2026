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

# Reproducible checks and their limits

A proof using the irrational-rotation cylinder partition is given in `RESULT.md`. For every integer \(n\ge1\), the \(n\) discontinuities \(t_j=\lceil j\alpha\rceil-j\alpha\) are all distinct. The image at a boundary merges with its neighbor exactly when the preceding prefix has zero ones; this is equivalent to \(j\alpha<1\) for \(1\le j<n\). The proof is symbolic and does not rely on numerical output.

Run `python3 sturmian_tortoise_check.py` and compare the five status lines with `CHECK_OUTPUT.txt`. The script uses two separately constructed finite factor sources: the complete \(n+1\) mechanical-cylinder collection through length 100 and a 25,000-symbol irrational-rotation orbit through length 60. For each of five algebraic irrational slopes it tests the exact number of tortoise images and the set of merging thresholds. The finite orbit is not exhaustive for all real slopes or all lengths; the 90-digit Decimal approximations support regression tests only.

The external independent audit remains unperformed. No computational log by itself is presented as infinite proof.
