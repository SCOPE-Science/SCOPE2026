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

## Reproduction

Run `python3 verify.py` in the directory containing the standalone source. It uses only the Python standard library and independently builds the finite-field matrix tuples and tests all exact joint rank strata. Observed final marker: `VERIFY_OK`.

Eight exhaustive configurations were checked: `(q,n,ell)=(2,2,2),(3,2,2),(2,3,2),(3,3,2),(2,4,2),(2,2,3),(2,3,3),(2,3,4)`. Total valid tuples respectively: `10,33,148,1665,8296,22,736,3256`. The checker independently calculates `rank([A_1 ... A_ell])` and `n-rank([A_1; ...; A_ell])`.

The unrestricted correctness argument is the fixed-subspace bijection, double Möbius inversion, transpose involution, and maximum-degree proof with line/hyperplane bounds; the finite experiment alone proves none of these universally. Prime-power extension relies on the field-uniform algebraic proof; no nonprime finite field was exhaustively enumerated by the supplied checker.
