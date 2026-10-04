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

The analytic proof is self-contained once the published critical formula is accepted. The key global step is the strict bound
\[
\psi_1\!\left(p-\frac12\right)-\psi_1(p)<\frac{2}{(2p-3/2)^2},\qquad p>1,
\]
obtained from the trigamma integral and \(1+e^{-s}>2e^{-s/2}\). Combined with
\[
(2p-3/2)^2-2p(p-1)=2(p-1)^2+\frac14>0,
\]
it proves \(H'(p)<0\) on the entire domain. Endpoint signs then give one zero and hence strict unimodality.

`verifier.py` numerically re-evaluates only the supplementary decimals. It is not used to infer uniqueness or any infinite-domain property. Expected output includes a root near \(1.317094285913839\), a normalized maximum near \(3.821987752657050\), and opposite signs for \(H(1.31)\) and \(H(1.32)\).

Scientific limits: no higher-dimensional analogue is checked here, and the numerical decimals are not independently certified interval bounds.
