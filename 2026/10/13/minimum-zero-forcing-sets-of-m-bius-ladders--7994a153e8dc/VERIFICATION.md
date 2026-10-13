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

The proof is symbolic and valid for all stated orders. The standalone checker `artifacts/verify.py` supplies an independent finite stress test of its critical combinatorial claims.

For \(n=3\), the checker enumerates every four-subset and verifies that exactly \(9\) are zero forcing. For each \(4\le n\le12\), it enumerates every four-subset of \(M_{2n}\), directly simulates zero forcing, independently evaluates the local criterion, constructs the five claimed dihedral orbits, verifies their pairwise disjointness and sizes \(2n,4n,4n,2n,n\), and checks equality of the three resulting set families.

A successful replay prints one `VERIFY_OK` line. This finite computation is not used as an infinite proof and does not assess novelty.
