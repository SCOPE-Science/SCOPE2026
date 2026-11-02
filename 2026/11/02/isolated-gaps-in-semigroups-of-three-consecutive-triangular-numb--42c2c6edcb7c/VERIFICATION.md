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
Run `python3 verify.py` (Python 3 standard library only). A successful run prints `VERIFY_OK n=3..150 inclusive; exact isolated sets and counts; 573796 Apéry residues; 14 direct-membership cases`.

For each parameter, the verifier independently constructs the residue shortest-path Apéry set with Dijkstra's algorithm, then derives all isolated gaps from adjacent Apéry thresholds. It checks the exact formula and, when applicable, every listed gap. At the fourteen smallest parameters it separately builds the semigroup's membership table through the Frobenius bound, using ordinary coin recurrences rather than Apéry arithmetic. All checks passed. These finite checks are reproducibility tests; they are not a substitute for the proof covering every index.
