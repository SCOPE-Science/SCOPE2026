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
The universal proof uses three exact steps: the homogeneous-resultant criterion away from resultant primes, Chinese-remainder counting at the finitely many exceptional primes, and Möbius inversion for coordinate primitivity. The resulting floor and local-box errors are bounded absolutely by a harmonic sum, giving \(O(X\log X)\).

`verify.py` checks two independent examples. For \(X^2-Y^2\) and \(X^2-4Y^2\), it verifies the exceptional local count \(N_3=5\), the absence of non-origin common zeros at several primes away from \(3\), the pointwise gcd characterization on a \(150\times150\) grid, and exact Möbius reconstruction for three box sizes. It performs the analogous checks for \(X^2+Y^2\) and \(X^2-Y^2\), where \(N_2=2\).

These finite checks test the implementation and examples only. They do not certify the universal quantifier over all forms or all \(X\); that part is supplied by the symbolic proof in `RESULT.md`.
