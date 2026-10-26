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

# Reproducibility and boundaries

Run `python3 path_check.py` with Python 3 and standard-library modules only. Compare its stdout with the included `path_check.out`.

The checker enumerates every length-\(n\) nearest-neighbor path map for each \(2\le n\le14\) without using the decomposition theorem to generate the candidates. It checks idempotence by direct composition, computes image ranks, conjugates each map by path reversal and constructs actual conjugacy orbits. All rank frequencies and fixed-orbit counts agree with the independent matrix-walk formulas. This comprises \(13\) dimensions and \(5515\) idempotents. Additional formula checks evaluate \(11\) near-full-rank deficiencies and their stable binomial counts for multiple path sizes.

No symbolic computer verification of the universal proof, external certification or independent audit has been performed. Finite enumeration only tests the stated cases.
