---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For two deleted interior nodes with fixed separation h≥2 and *reindexed* alternating barycentric signs, the signed denominator in either length-two gap is the limit F_h(t)=πcsc(πt)−1/t−(−1)^h/(t−h)−2Σ_{j=1}^{h−1}(−1)^j/(t−j). Its magnitude reduces by reciprocal-tail pairing to D_h(t)=B(t)+(−1)^h I(h−t), positive and strictly convex, attaining unique d_h at t_h∈(−1,1). Each exceptional gap contributes numerator 2logN+O(1); ordinary cells satisfy L≤2+H_N and have log coefficient at most one, while the two gaps have coefficient C_h=2/d_h>1. Endpoint boundary layers vanish as competitors. The integral I(p) is strictly positive decreasing, yielding even C_h rising toward 1/log2 from below and odd decreasing from above. I(h)=1/(2h²)+O(h^−3), I'(h)=−h^−3+O(h^−4), B''(0)=3ζ(3), giving C_h=1/log2−(−1)^h/[4(log2)^2h²]+O(h^−3), t_h=(−1)^{h+1}/[3ζ(3)h³]+O(h^−4). Independent high precision numerical minimization agrees with displayed C2≈1.334642697, C3≈1.500180056, C4≈1.411794833, C5≈1.463423475, and sign/ordering. Numerical values do not prove the limiting/convexity claims; proof uses alternating rational tails and inequalities.

## originality

PASS

Classical intact-grid and general well-spaced-grid papers supply O(log N) scale but not two separated erasures' sharp coefficient or distinct two-gap localization. Consecutive deletions form one longer gap and are not equivalent to h≥2; its exact constants do not imply even/odd separation law. Intact exact coefficient literature is distinct. Priority uncertainty persists because the full 2016 sharp-bound article and all obscure scattered-data variants have not been read.

## value

PASS

Two missing samples in stable rational interpolation are a natural defect configuration. Exact leading operator-norm growth and location of worst amplification improve qualitative logarithmic bounds; parity-modulated pair interaction, sharp inverse-square tail and inverse-cube extremizer displacement are a meaningful structural defect law, not a routine rescale of intact grid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
