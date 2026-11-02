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

# Reproducibility and proof checks

Run `python verify_hankel.py` using the Python standard library. The actual executable enumerates every defining tuple over \(\mathbb F_q\), for \(q=2,3,4,5,7,8,9,11\) and specified orders \(n\), computes determinants by field Gaussian elimination, and calculates the theoretical fibers independently from finite-field generator logs, divisor sums, and the arithmetic Möbius function. Binary fields use irreducible polynomials \(u^2+u+1\) and \(u^3+u+1\); \(\mathbb F_9\) uses \(u^2+1\) over \(\mathbb F_3\). All field arithmetic is explicit and integer-exact.

Successful verification in this package:

`VERIFY_OK fields=8 cases=27 enumerated_matrices=127102 predicted_fibers=136`

Additionally checked by proof reconstruction: the Hermite-pair map has exactly \(q\) lifts per nonsingular Hankel matrix (one free next Laurent coefficient); the Bezoutian sign is \(arepsilon_n\); the prime-power norm character sum vanishes exactly when the order does not divide the exponent; the Euler factors reduce to a rational series; Fourier inversion gives all fibers and the nontrivial-character criterion excludes false uniformity claims. Formula also includes \(n=1\) and characteristic two.

Limits: these finite experiments are not an exhaustive verification over all \(q\), \(n\), or fields, and do not prove the infinite theorem independently of the mathematical proof. No external independent audit was performed.
