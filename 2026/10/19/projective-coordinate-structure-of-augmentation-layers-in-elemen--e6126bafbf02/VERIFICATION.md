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

`verify.py` runs with Python 3 and SymPy. It computes exact integer Hermite bases of positive powers of the augmentation ideal of \(\mathbb Z[(\mathbb F_p)^d]\) and Smith forms for successive quotients, verifies the normal-monomial evaluation matrix has full column rank over \(\mathbb F_p\), and checks the core-quandle operation against its group-ring transport in finite groups.

Checked triples \((p,d,r_{\max})\): \((3,2,6)\), \((5,2,5)\), \((3,3,5)\), and \((2,3,4)\). The last is a boundary test of the ordinary group ring only: the core-quandle theorem requires odd \(p\). Replay of the included script returned `VERIFY_OK: exact Smith forms, projective evaluations and core transport`.

The proof in `RESULT.md`, not the computations, establishes all primes and unbounded degrees. Previous results on additive augmentation powers remain relevant literature; several older full texts were not accessible for a complete comparison. Independent mathematical review has not been performed.
