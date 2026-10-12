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
The packaged checker `artifacts/verify.py` encodes the seven multiplication tables from the published complete two-dimensional classification.

For each algebra it introduces a general linear map
\[
\phi(e_1)=a e_1+b e_2,\qquad
\phi(e_2)=c e_1+d e_2,
\]
forms all eight scalar equations arising from
\[
\phi(e_i)e_j=e_i\phi(e_j)
\]
for \(i,j\in\{1,2\}\), and computes the exact nullspace over \(\mathbb Q\).

The resulting dimensions are
\[
4,\ 3,\ 3,\ 1,\ 1,\ 2,\ 2.
\]

The checker also compares the nullspaces with the seven claimed matrix families and returns `VERIFY_OK`.

The computation verifies the quasi-centroid calculations. Exhaustiveness of the seven underlying complex associative isomorphism classes is supplied by the published classification theorem cited in the result.
