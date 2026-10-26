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

# Reproducibility and analytical checks

**Theorem checks:** The lower Zak inequality uses \(\Re(1/(1-rz))\ge(1+r)^{-1}\) and \(r^\omega\ge r\); equality is approached simultaneously for every height at \((x,\omega)=(1/2,1^-)\). The upper inequality uses \(|1-rz|\ge1-r\) and \(r^\omega\le1\), with simultaneous sharpness at \((0,0^+)\). The exact rational identity for the normalized analysis condition deficit holds identically on \(0<r<1\); its integral is positive except for a point mass at the unique optimum height.

**Independent computational checks:** Execute `python verify.py` (Python 3 standard library); it ran 3,231 deterministic assertions and printed the output in `verification_output.txt`. Checks cover the two exact critical spectral bounds, the modulus of the Zak symbol for random mixtures and varying lattice scales, the analytic exact quadratic deficit, two boundary-corner sharpness limits, and an independently evaluated spatial-domain Zak sum. The computational checks test normalization and finite examples; they are neither a complete search over continuous positive measures nor a substitute for the proof.

**Limits:** Only the positive-measure, imaginary-axis-pole, rectangular-critical-density case is proved. No independent scientific audit, proof-assistant formalization, or exhaustive bibliographic priority certificate is claimed.
