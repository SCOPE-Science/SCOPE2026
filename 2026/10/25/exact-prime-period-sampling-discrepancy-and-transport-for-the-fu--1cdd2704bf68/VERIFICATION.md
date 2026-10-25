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

# Verification of the finite prime-period tent-map formulas

Run `python3 verify_prime_tent.py` beside this file with Python 3 and its standard library. No third-party dependencies are required. The program creates each dyadic fixed grid in exact `Fraction` arithmetic and checks independently that each point returns after the claimed least period. For primes \(p\in\{2,3,5,7,11,13\}\), it directly checks the complete point count, first point, sorted grid membership, star discrepancy, covering radius, largest internal gap, and every individual signed discrepancy inequality. Composite controls \(n\in\{4,6,8\}\) check that the least-period count differs from the prime formula; at \(n=6\) it also reports distinct discrepancy and radius.

Observed completed run: **41,669 exact-integer/rational assertions passed**, no failures. Exemplars: for \(p=2\), the common metric is \(2/5\); for \(p=3\), \(2/9\); for \(p=13\), \(2/8193\). For composite \(n=6\), star discrepancy is \(2/63\), while covering radius is \(2/65\).

These computations test finitely many periods and do not certify the theorem for all primes. The universal claim rests on the explicit dyadic affine formula, exhaustive symbolic rank inequalities and optimal-coupling argument in the proof. The historical priority assessment is neither an independent audit nor a guarantee of novelty.
