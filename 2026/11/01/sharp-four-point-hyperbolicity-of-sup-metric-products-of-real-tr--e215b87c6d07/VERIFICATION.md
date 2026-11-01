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

# Verification record

The analytic upper bound was checked at both critical branches \(A>D\) and \(A\le D\), including the equality convention for second-largest pairing sum and the triangle-inequality estimate \(S_{(1)}\le S_{(2)}+S_{(3)}\). The lower bound was independently reconstructed from four compass points in a sup-metric square: pairing sums \(2L,L,L\) imply exact defect \(L/2\). The nonattainment and infinite-diameter limits were checked symbolically.

The standalone `verify.py` uses only the Python standard library and `fractions.Fraction`. Run `python verify.py` to enumerate all unordered distinct four-point subsets of six finite interval-grid sup products and three sup products of metric stars. The saved program was executed directly and returned `PASS: 14680587 exact four-point checks across 9 finite spaces`. Repeated-point quadruples have zero defect, so their omission in finite enumeration is harmless.

The finite tests are not exhaustive for continuous real trees, arbitrary dimensions, or unbounded diameters; those claims rely on the proof in RESULT.md. Independent audit has not been performed.
