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

The mathematical proof in RESULT.md uses edge-balance classification, the directed matrix-tree theorem, the BEST theorem, and an explicit finite-rank determinant calculation. The standalone `verify.py` does not reuse the reduced determinant expressions: it constructs full directed de Bruijn Laplacians and uses integer Bareiss elimination to evaluate their exact cofactors.

Execution: `python3 verify.py` (Python 3 standard library; no external dependencies). Successful output terminates with:

`VERIFY_OK parameter_cases=6 balanced_missing_sets=212 exact_cofactors=212 independent_direct_necklaces_q3n2=True`

Validated parameter pairs: \((q,n)=(3,2),(4,2),(5,2),(3,3),(4,3),(3,4)\). Each pair includes exhaustive balanced three-edge deletion sets, direct cofactor comparisons, and exact BEST counts. The \((3,2)\) case additionally enumerates all source necklaces directly and counts 20. Finite enumeration does not prove the identities for unbounded alphabet size or order; those cases rely on the symbolic proof. No external or independent audit is claimed.
