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

The symbolic verification is contained in `artifacts/verify_type12_quotient.py`. It checks the invariance of \(u=t^2+t^{-2}\) under the residual Klein four action, factors the fibers over \(u=\pm2\), computes the discriminant locus \(\beta=\pm2\) of the quartic Kummer branch polynomial, verifies that the four finite Kummer branch points map to \(u=-\beta\), and checks the tame Riemann--Hurwitz equality for inertia orders \(12,6,2,2\).

Fresh replay produced:

`VERIFY_OK degree=24 quotient=P1 signature=[0;12,6,2,2] branch_values=infinity,-beta,2,-2 orbit_sizes=2,4,12,12 discriminant_beta=+-2`

The script does not attempt to re-prove the Badr--Bars classification of the full automorphism group; that theorem is a cited premise. It verifies the new fixed-field and ramification consequences of the published generators.
