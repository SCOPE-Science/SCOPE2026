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
# Finite verification and reproducibility

Run `python3 VERIFY.py` with Python 3 (standard library only). It constructs the exact large Schröder sequence using the integral recurrence, checks all stated valuation identities for positive indices through 2030, tests the cited shift congruences for exponents \(1\) through \(8\), tests the derived difference-shift congruence and valuation-level residue sets for levels \(4\) through \(10\), and checks four two-adic precisions for the zeros of the interpolated difference. Successful execution prints `VERIFY_OK`.

The central proof is analytical and uses the fully credited Theorem 2 of Cao–Pan. Finite cases cannot independently certify that theorem, nor prove this conclusion for infinitely many indices. The theorem intentionally excludes index zero, where the positive-index interpolation differs from the standard combinatorial initial term. Independent audit has not been performed.
