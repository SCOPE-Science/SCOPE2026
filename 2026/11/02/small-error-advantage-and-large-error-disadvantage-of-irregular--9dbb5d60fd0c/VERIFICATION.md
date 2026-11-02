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

# Verification and limits

The comparison theorem is proved symbolically in `RESULT.md` using the published independent Poisson-wedge limit law and two new endpoint analyses. The lower-tail coefficient follows from a two-strip exponential-density limit. The large-tail exponent is certified by explicit gamma/exponential upper and lower bounds, not inferred from simulations. Jensen's inequality with strict equality analysis gives universal small-error ordering; the least-angle exponential rate gives opposite large-error ordering.

`checks/wedge_crossing_check.py` directly integrates the exponential two-endpoint distance without using the pre-existing published integral expression. It was executed and checked the small-threshold coefficients and both sides of the square/rhombus crossing. Numerical quadrature checks do not establish inequalities for all polygons, or the exact endpoint limits; those follow from the proof.

The published Poisson-process weak convergence is an explicitly cited premise. No claim of independent or external validation is made. Historic novelty remains subject to literature beyond the material inspected.
