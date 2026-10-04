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

The analytic proof has four independently checkable components: character-kernel reduction to an \(L\)-point root-of-unity average; two exact quartic factorizations proving \(q(x)\ge\lvert x\rvert\) on \([-1,3]\); the exact discrete moments \(3\) and \(19\) for every \(L\ge5\); and the concavity chord bound for \(\sqrt{1+4u}\) together with the exact average \(\frac12\) of \(\sin^2\theta\) for \(L\ge3\).

The bundled `artifacts/verify.py` rechecks the algebra with integer arithmetic and performs a numerical stress test for every \(3\le L\le1000\). The numerical sweep is corroborative only and is not used to extend a finite calculation to the all-\(L\) theorem.

Limit: no claim is made that the certificate bounds are sharp for \(L\ge5\), and no claim is made for non-arithmetic three-frequency supports or exponents other than one.
