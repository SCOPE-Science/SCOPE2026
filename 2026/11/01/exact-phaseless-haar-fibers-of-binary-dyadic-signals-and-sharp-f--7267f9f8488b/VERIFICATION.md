---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

On each subtree I, restricted Haar Parseval and binary x_j²=x_j imply s_I-s_I²/|I| equals a sum determined by internal detail magnitudes. Thus a competing subtree total can only be observed s_I or its complement |I|-s_I. At fixed parent total, swapping child sums is possible for nonzero contrast exactly when s_I=|I|/2; complementation within the children bijects the two solutions, yielding a product recurrence and |F(x)|=2^{b(x)} by induction. A second induction gives b_I<=min(s_I,|I|-s_I), saturated by ones in distinct lowest adjacent pairs, and equality at N/2 forces all higher details zero. Independently enumerated every binary vector at N=2,4,8,16, grouping by complete signed-total/labelled-absolute-detail data; for N=16, all 65,536 signals, 3,256 fibers with exact histogram 2,85,453,862,921,650,238,44,1 at sizes 1..256 powers of two, all fixed-weight maxima confirmed. The all-N conclusion rests on induction.

## originality

PASS

Known wavelet phase retrieval theorems use redundant continuous wavelet frames and establish injectivity in a different regime. The candidate classifies exact multiplicities of the nonredundant finite Haar basis on binary signals, and sharp fixed-weight extremal ambiguity.

## value

PASS

A full labelled nonredundant Haar transform is a canonical multiscale measurement; binary/quantized inversion is a natural reconstruction problem. The computable balanced-split exponent exactly predicts all ambiguity multiplicities in a practical linear-size tree statistic, and sharp weight-conditioned maximum and unique maximum measurement fiber provide a complete quantitative extremal law, not a renaming of generic nonuniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
