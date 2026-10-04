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
`verify.py` uses exact rational arithmetic. For each \(1\le m\le40\), it constructs the standard centered first-derivative weights from
\[
\alpha_{m,j}
=
(-1)^{j+1}
\frac{(m!)^2}{j(m-j)!(m+j)!}.
\]
It verifies polynomial exactness through degree \(2m\), antisymmetry, strict decay of positive-side weight magnitudes, the sign of every positive-side tail, and that the second tail is the most negative whenever \(m\ge2\).

It also verifies exactly that
\[
\sum_{j=1}^{m}\alpha_{m,j}=H_{2m}-H_m,
\]
that the sharp defect equals
\[
V_m=\frac{m}{m+1}-(H_{2m}-H_m),
\]
and that the two stated step vectors attain \(-V_m/h\) after setting \(M=1\). Strict growth of \(V_m\) is checked over the replay range.

The all-order proof is analytic and appears in RESULT.md; the finite replay corroborates the algebra rather than replacing it.
