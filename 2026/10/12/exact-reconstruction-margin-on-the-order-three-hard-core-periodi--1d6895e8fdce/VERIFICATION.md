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

The exact proof uses the published order-three branch equations
\[
\lambda xy(x+y)=1,\qquad x^2+y^2+xy=x+y,
\]
together with the source formulas for the two-step Markov eigenvalue and \(\kappa\). Eliminating \(x,y\) through \(a=x+y\) gives
\[
xy=a(a-1),\qquad \lambda=\frac1{a^2(a-1)},\qquad 1<a<\frac43.
\]
Substitution gives
\[
s_2=\kappa=(a-1)^2.
\]
The independently checked hard-core estimate
\[
\gamma\le\frac\lambda{1+\lambda}
\]
then reduces the sufficient extremality criterion to
\[
F(t)=\frac{9t^2}{1+t(1+t)^2}<\frac{27}{43},\qquad 0<t<\frac13.
\]
The derivative satisfies
\[
F'(t)=\frac{9t(2+t-t^3)}{(1+t+2t^2+t^3)^2}>0,
\]
so the supremum follows analytically.

`verify.py` uses exact rational arithmetic to replay the branch identities and endpoint bound on a dense family of rational test points. These finite tests do not replace the analytic proof.

Replay output: `VERIFY_OK exact_points=10292 endpoint=27/43 max_sample=15500250/24828787`.

Scientific limits: the statement concerns only the nontranslation-invariant two-periodic branch of the two-state hard-core model on the order-three Cayley tree. The constant \(27/43\) is specific to this sufficient-certificate estimate. The Kesten--Stigum condition is not used contrapositively.
