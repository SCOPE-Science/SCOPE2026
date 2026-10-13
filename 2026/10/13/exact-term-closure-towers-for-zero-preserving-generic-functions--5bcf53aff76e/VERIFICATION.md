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

The proof was checked in two independent forms: the direct stage count
\[
d_{n+1}=d_n+\sum_j\left(q^{r_jd_n}-q^{r_jd_{n-1}}\right)
\]
and the collapsed recurrence
\[
d_{n+1}=m-s+\sum_j q^{r_jd_n}.
\]
The accompanying `verify.py` evaluates both formulas on several parameter choices and checks the invariant
\[
d_{n+1}-\sum_j q^{r_jd_n}=m-s.
\]
It also checks the one-generator unary \(\mathbb F_2\) sequence \(1,2,4,16,65536\). The script returns `VERIFY_OK`.

The computation is a consistency check, not the proof of the infinite statement. The infinite statement is established by the recursive free-algebra universal-property argument in `RESULT.md`.
