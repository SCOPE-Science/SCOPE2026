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
The analytic checks are independent of finite sampling: zero-energy inertia gives the state count once strict positive eigenvalue flow is established from the resolvent Gram derivative, and the determinant Taylor coefficients give the threshold exponents.

The accompanying checker evaluates the exact principal-matrix entries numerically. It confirms that the source parameter set \(R=\mu=1\), \(a=2\) has one positive determinant zero at \(\lambda_2=10\) and two at \(\lambda_2=20\). It also approaches the predicted generic ratio \(E_2/D^2\to-16\) and exceptional ratio \(E_2/D\to-4/3\).

These numerical checks do not certify the infinite-domain statements by themselves; the proof in RESULT.md supplies the global argument. Independent audit has not been performed.
