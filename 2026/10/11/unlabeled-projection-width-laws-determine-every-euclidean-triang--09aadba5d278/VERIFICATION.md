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

# Reproducibility and boundaries

Run `python verify.py` with Python 3, NumPy and SciPy installed. The script compares three-vertex direct orthogonal projections in 140,000 evenly spaced orientations for each of 24 shapes against the exact sector-derived CDF at 75 thresholds per shape, then checks that the density integrates to one, that its mean is perimeter divided by \(\pi\), and that density singularity weights and finite jumps agree with all three formula cases.

The observed script results were `VERIFY_OK` with CDF maximum error about \(1.14\times10^{-5}\), quadrature mass error below \(2.3\times10^{-11}\), mean-width error below \(7.3\times10^{-11}\), and `SINGULARITY_CHECKS_OK` with acute/right/obtuse test counts 8/2/14. The finite numerical checks cover neither all possible triangles nor the uniqueness assertion at all parameter values: those claims are established by the written sector partition and limiting density analysis, not by numerical sampling. Equality and boundary cases are treated directly in the proof.
