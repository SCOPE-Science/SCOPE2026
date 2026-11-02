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

# Reproduction

Run `python verify.py` in the directory containing the extracted files. The standalone script uses only Python's standard library. During the scientific review it completed without exceptions and printed the lines in `verify_output.txt`; it counted 894 exact-rational and deterministic assertions. It checks greedy mass conservation and prefix saturation in two finite examples, subset-rank submodularity, an exhaustive integer-allocation census for a three-atom example, dyadic partitions for the sharp two-variable uniform probability, and numerical integration of the general uniform-profile formula.

# Proven limits

Finite arithmetic and quadrature cannot establish the theorem for arbitrary Borel measures, arbitrary dimensionality, or all feasible label vectors. Those assertions rest on the separate measure-allocation, convex support-function, and quantile-coupling proof in RESULT.md. In the atomless strict-separation case, the proof uses continuous conditional CDFs to ensure no ties. This evidence is self-review only; independent mathematical auditing has not been carried out.
