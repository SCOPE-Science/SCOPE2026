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

Run `python verify_product_rank.py` using a standard Python 3 interpreter. No external package, downloaded dataset, or external executable is needed. The program independently enumerates all partial order-preserving isometries of \(\{1,\ldots,n\}\) through \(n=7\), evaluates all ordered products as partial maps, and compares rank profiles to two separately constructed enumerators. It also checks the one-sum and two-displacement polynomials through \(n=40\), total pair counts, top rank multiplicities, limiting geometric moments, and selected mean-bias inequalities.

An expected successful final line is `VERIFY_OK_PARTIAL_TRANSLATION_PRODUCT_RANK`. The independent direct enumeration covers finite sizes only. The arbitrary-size polynomial and probabilistic limit rely on the counting and coupling proofs in `RESULT.md`. The computations do not constitute an independent mathematical audit; no such audit has been performed.
