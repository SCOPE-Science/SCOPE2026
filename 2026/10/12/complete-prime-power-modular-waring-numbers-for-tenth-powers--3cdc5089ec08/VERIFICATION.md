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
# Verification of the prime-power classification

Run `python3 verify.py` alongside `prime_exceptions.csv`; compare standard output to `verification_output.txt`. The required package consists solely of standard-library Python source, the prime CSV, and the scientific statement and proof. The exact test checks every odd prime below \(6000\), except \(5\), independently derives prime-field covering lengths and minimum nontrivial zero lengths, reconstructs the complete exceptional-prime certificate, and directly tests selected squares of odd primes. It also tests powers of \(2\) and \(5\) at the listed finite exponents. The output is a finite arithmetic replay, not independent validation of Hasse–Weil or of unrestricted prime coverage.

The large-prime proof uses the genus-\(36\) Hasse–Weil point lower bound \(p+1-72\sqrt p\), subtracts no more than \(30\) forbidden projective points, and verifies positivity uniformly from \(p\ge6000\). The reduction from field to higher prime powers depends on \(p\nmid10\) and uses a nonzero coordinate; the prime-\(5\) base starts at modulus \(25\). The prime-\(2\) infinite tail is governed by the odd tenth-power subgroup modulo powers of \(2\), while modulus \(16\) gives the matching lower bound.

The overall classification is mathematical and unrestricted only through these proofs and the exhaustive small-prime verification; testing finitely many moduli alone would not establish it. The result is specific to the tenth power. Independent audit has not been performed.
