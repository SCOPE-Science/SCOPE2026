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
The survival function is
\[
R(x)=\exp\{1-\exp[(\tau x)^\eta]-(\kappa x)^\varphi\}.
\]

Boundary substitution gives, exactly,
\[
R(x;0,\eta,\kappa,\varphi)=e^{-(\kappa x)^\varphi},
\]
which is independent of \(\eta\), and
\[
R(x;\tau,\eta,0,\varphi)=\exp\{1-e^{(\tau x)^\eta}\},
\]
which is independent of \(\varphi\). At \(\tau=\kappa=0\), \(R(x)=1\) for every finite \(x\).

For positive scales, write
\[
K(x)=-\log R(x)+1=e^{a x^\eta}+b x^\varphi.
\]
Then
\[
\frac{\log\log K(x)}{\log x}\to\eta,
\qquad
\frac{\log K(x)}{x^\eta}\to a.
\]
After \(a,\eta\) are recovered, exact subtraction leaves \(b x^\varphi\), which determines \(b,\varphi\).

The bundled checker directly replays the boundary equalities and numerically verifies the two interior asymptotic recoveries at increasing arguments. The computation is only a consistency check; the identifiability classification is analytic. No rate of weak identification near a zero scale is claimed.
