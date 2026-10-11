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

# Verification of the finite-shift asymptotic

The proof (see `RESULT.md`) is analytic. For \(1<p<\infty\), Young's inequality makes every edge deficit nonnegative. The substitution \(u=x^{p/2}\) yields a positive homogeneous ratio whose diagonal limit is \(2(p-1)/p^2\). The sine construction is an upper-bound recovery sequence; compact \(H_0^1\) interpolation and localization away from its zero set supply the lower bound using sharp Poincaré. The exact boundary contributions vanish for the sine sequence after scaling by \((n+1)^2\).

Run the included `verify.py` using a standard Python 3 interpreter. It reproduces the nontrivial quartic polynomial identity at \(p=4\) using exact rational arithmetic; verifies the Hilbert cosine relation for multiple sizes; and computes finite sine-recovery tests at several non-Hilbert exponents. Successful execution ends with `CHECK_OK`. Only the rational identity is an exact machine-checked algebraic equality; the sine diagnostics are finite evidence and neither certify the full limit nor replace the Sobolev proof.

No finite-dimensional exact numerical radius for \(p\ne2\), numerical error bound, uniform-in-\(p\) convergence, or independent mathematical verification is claimed.
