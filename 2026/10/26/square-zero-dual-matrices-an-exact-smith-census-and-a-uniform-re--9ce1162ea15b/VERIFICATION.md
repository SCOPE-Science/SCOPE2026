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

The exact counting argument derives the anticommuting lift equation, its full block solution, a Smith elimination reduction to a uniform smaller matrix, and a Gaussian-binomial count of residue matrices. The limiting uniform law follows from summable bounds on the difference between exact residue weights and the common bulk value. Conditional random-matrix coranks supply the independent discrete limit.

Execute `python3 verify.py` from the extracted package directory. The independent enumeration checks the equations directly in the ambient matrix ring and derives Smith data from the rank of the underlying linear map, not from the block-normal-form proof. Prime-field test pairs are \((q,n)=(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2)\), all with exact matching rank strata and totals. Formula consistency is checked over field orders \(2,3,4,5,7,8\) in dimensions \(1\) through \(34\). Exhaustion and formula checks do not prove the infinite-dimensional limit; the supplied analytical argument does.

The source comparison excludes the explicitly square-free and irreducible-polynomial scope of Cheong--Liang--Strand's 2022 results, and distinguishes full square-zero and Smith-rank counting from published one-block nilpotency-index and strong nil-cleanness censuses. Historic finite-ring matrix enumerations remain a residual priority risk. No independent audit or external validation has been performed.
