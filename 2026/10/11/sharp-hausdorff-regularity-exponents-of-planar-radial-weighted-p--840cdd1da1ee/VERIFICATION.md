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

# Reproducibility checks and proof limits

The proof uses (i) the local measure growth bound \(\mu_K(B_r)\le2\pi r\) for every planar compact convex body with doubled lower-dimensional boundary multiplicity, (ii) the exact support-function first-variation identity for a radial weight, (iii) integration by parts for truncated singular powers, (iv) a bounded-radius gradient estimate for positive powers and (v) smooth-convex approximation and explicit disk witnesses.

Run the accompanying standalone `CHECKS.py` with Python 3. It uses only standard-library functions. The actual execution returned `RADIAL_WEIGHTED_PERIMETER_FINITE_CHECKS_OK`. It evaluates the bound for \(p=-0.9,-0.75,-0.5,-0.1,0,0.25,0.5,1,2,4\), compares exact disk and diameter-segment energies, checks the sharp exponent by scale invariance, independently checks the support-function derivative against the disk radius law, and checks repeated polygon quadratures away from the singularity.

The numerical loops are neither exhaustive nor independently certified; the infinite-dimensional assertion follows only from the analytic argument recorded in `RESULT.md`. The coefficient \(C_p\) for \(-1<p<0\) and the bounded-radius constants for \(p>0\) are not claimed sharp. The argument needs convexity and the integrable-weight threshold \(p>-1\). Independent audit has not been performed.
