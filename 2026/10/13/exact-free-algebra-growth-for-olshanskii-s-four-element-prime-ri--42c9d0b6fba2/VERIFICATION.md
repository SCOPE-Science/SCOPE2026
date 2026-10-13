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
The proof is symbolic for every \(n\ge1\). Its critical steps are: (1) every product has zero \(e\)-coordinate; (2) the product-generated \(f\)-coordinates form an ideal of the full Boolean function algebra; (3) \(q_{ii}=a_i+a_ib_i+b_i\) is the indicator of a nonzero coordinate, so these elements generate exactly the functions vanishing at the unique all-zero point; and (4) the variable span meets that \(f\)-only ideal trivially.

`CHECKER.py` independently constructs the finite term-function algebra for \(n=1,2,3\) and reports dimensions \(4,17,66\), matching \(4^n+n-1\). It also checks the zero set of the diagonal generator. `CHECKER_OUTPUT.txt` records the run and ends with `CHECK_OK`.

The computation is deliberately limited: it is a regression check, not an exhaustive proof for arbitrary \(n\). No external or independent audit has been performed.
