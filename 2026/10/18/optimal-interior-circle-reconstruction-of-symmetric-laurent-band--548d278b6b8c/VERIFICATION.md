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

# Verification of annular Laurent-band circle reconstruction

The complete theorem is proved analytically in `RESULT.md` from orthogonal Laurent modes, strict log-convexity of the area radial moments, balancing the two extreme modes, and a uniform hyperbolic-sine tail estimate. Normalizations are area probability on the annulus and angular probability on the measured circle.

Run `python3 verify_annulus.py` with Python's standard library. The script computes the exact displayed moments numerically, reconstructs all squared singular values and the endpoint-balanced radius for multiple annuli and finite bands, verifies the multiplicative-moment condition formula, compares stability against four perturbed radii, tests strict moment log-convexity and the large-cutoff condition-number asymptotic. Its successful finite checks are corroboration, not a proof for all bands or parameters. No interval-arithmetic or formal proof certificate is claimed.

For the proof-critical all-size spectral tail, the bound is obtained explicitly from the displayed hyperbolic-sine expression at a radius whose logarithmic deviation from the geometric mean tends to zero. This controls *all* indices as the band grows, rather than interpreting finite enumeration as exhaustive. The eventual maximizing index is \(j=-1\); for small cutoffs it need not be.

No independent audit has been performed.
