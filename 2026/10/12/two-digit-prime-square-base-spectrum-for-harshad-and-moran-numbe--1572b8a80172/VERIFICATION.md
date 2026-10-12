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

For each prime \(p\le500\), the checker enumerates every base
\[
p<B\le p^2.
\]
It computes the two base-\(B\) digits of \(p^2\), checks Harshad and Moran membership directly, and compares the observed base sets with the theorem.

The predicted Moran set is
\[
\{pd+1:d\mid p-1\},
\]
and the predicted Harshad set is that set together with
\[
\{p^2\}.
\]
The checker also verifies the explicit digit formula
\[
\left(\frac{p-1}{d},\,p-\frac{p-1}{d}\right)
\]
for every predicted Moran base.

This finite computation is corroborative only. The infinite result follows from the proof in `RESULT.md`.
