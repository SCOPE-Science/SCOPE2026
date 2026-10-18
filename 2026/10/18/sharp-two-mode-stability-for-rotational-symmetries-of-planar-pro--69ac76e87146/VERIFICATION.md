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

# Verification details

Run `python3 check_frame.py` in the directory containing this file and the standalone script. The script uses only Python's standard library. On the saved candidate it returned `PASS: 2006 exact/large-degree checks`, with upper constant approximately `0.08703785950338026` and lower constant approximately `0.05066059182116889`.

The critical infinite checks are analytic: normalized associated Legendre evaluation, Schur orthogonality over rotation matrices, exact recurrence of central-binomial ratios, a strict numerator/denominator inequality equal to \(\(4j^2-1\)\), and Stirling's asymptotic formula. The script tests exact rational instances of the recurrence and low-degree moments and a numerical large-degree limit; it does not certify all infinite degrees by enumeration.

With area-measure-normalized spherical harmonics, the independently integrated zonal tests give energies \(3/(32\pi)\) for degree two and \(5/(64\pi)\) for degree three. The upper sharp ratio occurs at degree three and the lower sharp ratio is an unattained high-degree limit. For a smooth convex support function \(r+\varepsilon Y\), the required positive support Hessian follows by choosing \(\varepsilon\) sufficiently small for the finite maximum of \(\|\nabla_S^2Y+Y\,\mathrm{Id}\|\).

No independent audit or external mathematical certification was carried out. Known limitations include the exact normalization dependence and the absence of a Hausdorff-stability claim.
