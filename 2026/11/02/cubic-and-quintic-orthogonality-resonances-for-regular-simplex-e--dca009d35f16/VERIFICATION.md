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
# Verification

Run `python3 check_simplex_resonances.py` using the included standalone script. It requires only the Python standard library. The checker compares direct normalized Gegenbauer Gram entries with the incidence-projector spectrum, verifies exact rational interpolation for dimensions 4 through 15, checks quintic resonances including dimension 27, and replays the dimension-five Chebyshev periodicity through degree 120.

Analytic verification: \(BB^\top=nI-J\) makes \(B^\top B/n\) a rank-\(n-1\) projector; the normalized zonal recurrence gives the two stated rational values at \(1/2\); their substitution yields strictly positive eigenvalues and zeros only in the enumerated degree-three/five cases. For dimension-five parameter \(n=5\), the Chebyshev identity establishes the infinite congruence class without relying on the finite test.

Limitations: finite checks do not certify universal theorems and no independent audit has been performed. The historical literature overlap check is bounded, with older full-text access gaps.
