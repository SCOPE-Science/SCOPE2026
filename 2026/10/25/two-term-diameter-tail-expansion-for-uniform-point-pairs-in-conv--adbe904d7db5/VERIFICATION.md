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
# Verification of the diameter-tail expansion

The analytical checks reconstructed the location of all diameter pairs, strict positivity of axial slopes, the cone-coordinate Jacobian, the exact squared-distance identity, the uniform implicit-function expansion, and the Dirichlet moment formula. The proof applies in every dimension \(d\ge2\) to any fixed full-dimensional convex polytope. The orthotope calculation was checked separately by its exact two-point coordinate-difference law.

To reproduce independent finite numerical checks, run `python CHECKER.py` with Python 3 and the installed `mpmath` library. The script evaluates the rectangular pair-distance probability by one-dimensional high-precision quadrature, estimates the relative second coefficient at successively smaller deficits, and tests the sharp fixed-volume box inequality. The recorded output ends in `DIAMETER_TAIL_CHECK_OK`; four rectangles and several higher-dimensional sample boxes were checked.

This is not an interval-arithmetic or automated universal proof. Any local cone triangulation can be used: the coefficients are intrinsic sums of integrals over partitions. There is no claim of a uniform-in-shape remainder or of complete verification of historical priority. Independent audit: not performed.
