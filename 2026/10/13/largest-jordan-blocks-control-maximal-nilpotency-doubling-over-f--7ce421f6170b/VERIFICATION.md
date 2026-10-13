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

The proof uses the exact identity
\[
(A+\varepsilon B)^m=A^m+\varepsilon\sum_{i=0}^{m-1}A^iBA^{m-1-i}
\]
in the square-zero extension. If \(A\) has index \(r\), this gives
\[
(A+\varepsilon B)^{2r}=0,
\qquad
(A+\varepsilon B)^{2r-1}=\varepsilon A^{r-1}BA^{r-1}.
\]
Thus the maximal-index test is exact and does not rely on computation.

For \(P=A^{r-1}\) of rank \(s\), vectorization identifies the linear map \(B\mapsto PBP\) with \(P^T\otimes P\), which has rank \(s^2\). Hence the nonmaximal set has dimension \(n^2-s^2\), proving the exact finite-field count.

`verify_dual_lift_max.py` independently checks finite cases over \(\mathbb F_2\). It exhausts every nilpotent \(3\times3\) real part and every dual part, and it exhausts every dual part for representatives of all nilpotent Jordan types in dimension four. The saved run terminates with `VERIFY_OK`.

The finite enumeration is a sanity check only. It does not prove the infinite family, and the theorem does not determine the full distribution of submaximal indices for a general multi-block nilpotent real part.
