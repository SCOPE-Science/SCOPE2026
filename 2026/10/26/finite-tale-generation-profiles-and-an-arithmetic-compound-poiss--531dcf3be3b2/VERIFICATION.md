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

# Mathematical verification

Run `python3 checker.py` using Python 3 with only the standard library. The checker exhaustively enumerates all \(16,403\) generator arrays in eight configurations of prime finite fields \(\mathbb F_2,\mathbb F_3\), extension degrees \(1,2,3\), sample counts \(1,2\), and algebra powers of sizes \(2,3\). It builds finite fields, computes generated algebra dimensions through iterative unital algebra closure, verifies primitive field-factor counts via the number of idempotents, independently computes Frobenius orbit profiles, and compares the full joint frequencies with the exact occupancy formula. The last output line is `ALL_FINITE_ETALE_SUBALGEBRA_CHECKS_PASSED 8 16403`.

The analytic compound-Poisson law is proved in `RESULT.md` by rare-subfield counting, disjoint-pair factorial moments and asymptotic independence; no finite computation verifies its universal limit. The checker does not represent independent mathematical auditing. All conclusions are restricted to the hypotheses stated in `RESULT.md`.
