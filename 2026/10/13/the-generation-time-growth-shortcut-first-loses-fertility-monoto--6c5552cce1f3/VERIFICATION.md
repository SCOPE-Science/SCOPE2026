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
For a two-age schedule with reproductive contributions \(a,b>0\), exact Euler–Lotka growth satisfies
\[
\lambda^2=a\lambda+b,
\qquad
r=\log\lambda.
\]
Thus exact growth increases strictly when \(b\) increases.

The generation-time shortcut is
\[
\widetilde r(a,b)=\frac{(a+b)\log(a+b)}{a+2b}.
\]

For
\[
S=a+b,
\]
the one-unit comparison
\[
\widetilde r(a,b+1)<\widetilde r(a,b)
\]
is equivalent to the exact integer inequality
\[
S^{S(2S+2-a)}>(S+1)^{(S+1)(2S-a)}.
\]

The embedded `verify_generation_time_shortcut_monotonicity.py` exhausts all positive integer schedules with initial
\[
R_0=S\le6
\]
and verifies that no failure occurs for \(S\le5\), while the unique first failure is
\[
(5,1)\to(5,2).
\]

For that witness it checks
\[
6^{54}>7^{49}
\]
and independently verifies that the exact quadratic growth factor increases.

Run:

`python3 verify_generation_time_shortcut_monotonicity.py`

The first output line must be:

`VERIFY_OK`
