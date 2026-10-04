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

Run `python verify.py` in an environment with Python 3 and SymPy. The script rebuilds the lower-unitriangular chart, the six Hessenberg equations, and the restricted Jacobian from the definitions rather than hard-coding only the claimed factor. It then enumerates all potentially nonzero maximal minors.

Expected terminal line: `VERIFY_OK`.

The exact checks are: the cell makes all six equations vanish; there are exactly seven nonzero maximal minors; each is divisible by \(\Delta=z_{12}-z_{23}-z_{45}+z_{56}\); one is exactly \(\pm\Delta\); a specified \(5\times5\) minor is identically \(1\); a non-permutation point on \(\Delta=0\) has Jacobian rank \(5\); and a point with \(\Delta=1\) has rank \(6\).

The verifier establishes the cell-level Jacobian statement only. It does not compute the global singular locus or analytic transverse type.
