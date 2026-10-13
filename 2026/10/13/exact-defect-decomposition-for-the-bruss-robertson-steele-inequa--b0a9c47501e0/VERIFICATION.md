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

For a deterministic positive vector \((x_1,\ldots,x_n)\), budget \(s\), and threshold \(t\), define \(A\) to be a maximum-cardinality feasible set and \(B=\{i:x_i\le t\}\). The verifier checks exactly, using rational arithmetic,
\[
|B|+\frac{s-S_B}{t}-|A|
=
\frac{s-S_A+\sum_{i\in A\triangle B}|x_i-t|}{t}.
\]
It constructs \(A\) by sorting the positive item sizes, which is valid because the maximum number of items fitting under a positive budget is obtained by taking the smallest sizes.

The script exhausts deterministic grids of sizes, budgets, and thresholds, asserts nonnegativity of the defect, and separately checks configurations without threshold ties for the implication
\[
S_B=s\Longrightarrow A=B.
\]
All arithmetic in these finite checks is exact.

A successful replay ends with
`VERIFY_OK exact_cases=... equality_cases=...`.

These exhaustive finite checks are regression tests only. The theorem for arbitrary positive real observations and the expectation identity are proved algebraically in `RESULT.md`.
