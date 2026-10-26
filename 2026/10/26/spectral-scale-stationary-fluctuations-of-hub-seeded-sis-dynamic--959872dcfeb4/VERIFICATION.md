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

# Reproducibility and scope of verification

The standalone `verify.py` runs with Python 3 and the packages listed in `requirements.txt`. Execute it using `python verify.py`. Its completed output ended in `PASS 171 checks`.

The executable checks the stationary forward equations and zero-flux relation symbolically, 20 numerical integral normalizers against confluent hypergeometric expressions, 100 stationary moment recurrences, and exact finite generator relations at the twelve combinations of graph size and two model parameters. For each finite generator it checks normalization/nonnegativity of the stationary solution, generator residuals and the exact stationary leaf-count balance. It additionally prints finite-size scaled correlation quantities beside their analytic limits, permitting direct numerical comparison.

The tests use ordinary finite precision for the matrix solves and quadratures, and symbolic algebra for the stated forward-equation identities. They do not establish the limiting theorem, exhaustive historical originality, or independent audit: the analytical proof of the infinite-size limit appears in `RESULT.md`. No external reference corpus or institutional access is needed to rerun the checker.
