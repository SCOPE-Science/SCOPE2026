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

# Verification of the exact period-three eye strip

The proof reconstructs the full affine three-step return equation, factors the exact interval width, and checks the four remaining branch inequalities at the interval edges. The primitive period-three claim follows from the asymmetric itinerary, and the global period floor from an integer-lift inequality for two right-branch visits. The displayed rational orbit is checked against the original piecewise map with exact fractional parts.

Run `python3 verify_period_three_eye.py` after extracting the embedded files. The completed invocation reported `PASS: 231 exact rational assertions; primitive 3-cycle witness and strip samples` using the Python standard library only. Its sampled parameters establish reproducibility but not the universal theorem, which is proved symbolically in the main result. No independent audit has been performed.
