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
The critical finite construction is the separating one-parameter subgroup.

For each tested tensor format, choose
\[
B>\max_i a_i
\]
and assign the basis vector \(e_{i,j}\) weight
\[
jB^{i-1}.
\]
The tensor coordinate indexed by
\[
(j_1,\ldots,j_t)
\]
then has weight
\[
\sum_i j_iB^{i-1}.
\]
The checker enumerates all multi-indices and verifies that these weights are pairwise distinct and that their number is
\[
\prod_i a_i.
\]

The test range is
\[
3\le t\le6,
\qquad
2\le a_i\le5.
\]

The fixed-point count is only a regression check for the explicit weight construction. The infinite theorem follows from uniqueness of base-\(B\) expansion and the Euler-localization proof in the result.
