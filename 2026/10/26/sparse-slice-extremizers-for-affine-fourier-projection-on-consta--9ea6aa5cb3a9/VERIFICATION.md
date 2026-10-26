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

The self-contained checker `johnson_projection_check.py` uses only Python standard-library exact fractions and combinatorial integers. Execute `python johnson_projection_check.py`. The observed result was `EXACT_VERIFY_OK assertions=44094` and exact layer maximizers \((n,k)=(20,4),(50,5),(100,7),(300,13)\). It constructs actual projection matrices and verifies symmetry, idempotence, trace, and row norms for small dimensions. It checks the binomial hypergeometric formulas through \(n=120\), including special cases. The mathematical proof of the universal asymptotic, the strictly decreasing Poisson peaks, and uniqueness of the sparse optimizer is in `RESULT.md`; finite runs do not establish these infinite claims. Independent audit has not been performed.
