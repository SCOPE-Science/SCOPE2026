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

For the exactly solvable repeated-minimum family
\[
\boldsymbol\gamma=(\delta,\delta),
\]
the uniform-GOS density is
\[
g(x)=\delta^2(1-x)^{\delta-1}[-\log(1-x)].
\]
Thus, with
\[
q=\frac1{1-p},
\]
the source's sharp bound evaluates exactly to
\[
B((\delta,\delta),p)
=
\delta^2\Gamma(q+1)^{1-p}
\left(\frac{1-p}{\delta-p}\right)^{2-p}.
\]
The standalone checker evaluates this identity in logarithmic form and verifies convergence to the predicted normalized constant when \(0<\delta<1\).

At \(\delta=1\), the same family gives
\[
B((1,1),p)=\Gamma(q+1)^{1-p},
\]
so the checker verifies
\[
(1-p)B((1,1),p)\to e^{-1}.
\]

It also checks the single-parameter exact source formula
\[
B((\delta),p)=\delta\left(\frac{1-p}{\delta-p}\right)^{1-p}
\]
against the general \(d=1\) limiting constant.

Expected successful output begins with:
`VERIFY_OK subunit_ratio=`.

The numerical tests validate special cases and constants only. The general theorem is established by the analytic endpoint sandwich in `RESULT.md`.
