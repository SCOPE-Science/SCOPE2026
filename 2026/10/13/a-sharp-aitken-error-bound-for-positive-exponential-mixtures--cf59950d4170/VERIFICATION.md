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
The universal proof is analytic. At any fixed index, normalize the positive modal contributions and set \(a=1-\lambda\). Then
\[
\Delta e=-e\,\mathbb E[a],
\qquad
\Delta^2 e=e\,\mathbb E[a^2],
\]
so the Aitken residual ratio is
\[
\operatorname{Var}(a)/\mathbb E[a^2].
\]
Bounding \(a\) between \(m=1-\lambda_+\) and \(M=1-\lambda_-\), applying \((a-m)(M-a)\ge0\), and optimizing over \(\mathbb E[a]\) proves the exact factor.

The embedded `verify.py` uses exact rational arithmetic. It checks the moment identity on several rational mixtures and verifies the equality witness with rates \(1/4\) and \(3/4\) and coefficients \(1\) and \(3\).

Finite checks are witness replays only. They do not prove the all-mixture theorem. Signed coefficients, negative rates, iterated Aitken transforms, higher-order epsilon algorithms, and floating-point stability are not covered.
