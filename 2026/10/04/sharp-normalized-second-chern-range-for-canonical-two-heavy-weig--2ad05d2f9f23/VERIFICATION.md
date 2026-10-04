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

The proof is symbolic and valid for every integer \(r\ge2\). The packaged checker is a finite regression test, not a certificate replacing the proof.

`artifacts/verify_c2_ratio.py` performs the following exact checks:

1. For each \(2\le r\le25\), it scans a box containing and extending beyond the entire predicted canonical region. In each heavy-coordinate chart it computes every nonidentity Reid--Tai age as a rational number, and confirms agreement with
\[
0\le b-a\le r,\qquad 1\le a\le r+b-a.
\]
2. For every canonical pair in that scan it computes
\[
\rho=\frac{\binom r2+r(a+b)+ab}{(r+a+b)^2}
\]
with exact fractions and checks both bounds and their unique equality cases.
3. For every \(2\le r\le500\), it checks the closed formulas at \((a,b)=(1,1)\) and \((a,b)=(2r,3r)\).

A successful replay prints `VERIFY_OK`.

Limits: the finite scan does not prove the theorem for unbounded \(r\). The infinite argument is the Reid--Tai reduction, weighted Euler sequence, Cauchy--Schwarz equality analysis, and monotonicity calculation in `RESULT.md`.
