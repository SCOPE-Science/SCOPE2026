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

The checker implements Chen's five preconditional axioms literally.

For
\[
n=1,2,3,
\]
it exhaustively enumerates every binary operation on \(C_n\). The preconditional counts are
\[
1,2,8,
\]
while the \(\mathsf T\)- and \(\mathsf F\)-counts are
\[
1,1,1.
\]

A separate normal-form enumerator generates every compatible family \((S_a,r_a)\) through
\[
n=8.
\]
It counts
\[
1,2,8,47,359,3344,36530,455907
\]
unrestricted preconditionals. Through \(n=6\), every generated operation is replayed against the original five axioms directly.

For every
\[
2\le n\le8,
\]
the normal-form specializations satisfying conditional identity and semicomplementation are counted exactly; each is also replayed against the original \(\mathsf T\)- and \(\mathsf F\)-conditions. Their common count is
\[
(n-2)!.
\]

The script prints `VERIFY_OK`.

## Limits

The finite enumeration corroborates the proof. The arbitrary-\(n\) normal form and factorial formula are proved symbolically and are not inferred from the first eight values. For the unrestricted class at \(n=7,8\), the checker counts the proven normal-form objects rather than re-evaluating all five axioms on every resulting operation.
