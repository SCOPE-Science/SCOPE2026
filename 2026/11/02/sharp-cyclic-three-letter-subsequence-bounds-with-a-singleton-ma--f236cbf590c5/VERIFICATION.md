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

# Reproducibility

Run `python verify.py` using Python 3 and its standard library only. The checker counts literal increasing-position \(\mathtt{abc}\) triples separately for every distinct rotation of each necklace with \(1\le a,b\le7\), then checks the algebraic rotation identity, exact upper and lower extrema, optimizing necklaces, and spectral gap. Executed output:

`VERIFY_OK profiles=49 circular_classes=12854 literal_rotations=170100 maxima_and_all_extremizers=True positive_gap=True`

The finite run does not establish the theorem for unbounded \(a,b\): the proof in RESULT.md does. In particular, the code does not prove that the remaining positive integer spectrum is contiguous, and neither does the theorem.
