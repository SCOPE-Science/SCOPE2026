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

# Verification and reproducibility

The theorem is analytic and unrestricted over odd moduli. The executable `verify.cpp` supplies **finite corroboration**, not an all-dimensional proof. Compile it with `g++ -std=c++17 -O3 verify.cpp -o verify` and execute `./verify`. The code constructs every entry of the integer \(n^3\times n^3\) left-regular matrix for \(n\in\{3,5,7,9\}\); performs modular exact Gaussian elimination over the verified prime \(1004221\); computes the conductor product separately in the prime field using a verified primitive root; compares determinants for unweighted and independently weighted coefficient triples; and checks the expected modular nullity of each unweighted operator.

Observed outputs were eight matching determinant comparisons, with unweighted ranks \(25,125,343,715\) and nullities \(2,0,0,14\), respectively. Nonzero determinants modulo the prime certify nonsingularity over the complex numbers; a modular zero determinant alone would not prove a complex determinant zero. The exact analytic factorization and cyclotomic root argument provide that proof. Modular ranks are not used as a substitute for the general nullity theorem.

Important limits: the code does not enumerate all odd moduli; large finite checks cannot establish the general formula. It is a direct, standalone matrix test of the first four selected moduli, not a proof assistant or an external certification.
