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

# Verification record

The complete analytic proof is in `RESULT.md`. The branchwise integrals used there were evaluated symbolically and yield
\[
\Pr(\mathrm{acute}\mid2\mathrm{\ sides})=4\log(4/3)-5/6,
\qquad
\Pr(\mathrm{acute}\mid3\mathrm{\ sides})=27\log(4/3)/2-7/2.
\]
The mixture weights \(2/3\) and \(2/9\) then produce the stated full-boundary law, with an additional \(1/9\) degenerate mass.

The included `verify_boundary.py` script ran successfully. Composite Simpson quadrature with 100000 subintervals per branch agreed with each exact constant to better than \(2\times10^{-9}\). A seed-fixed experiment with 300000 sampled triples gave acute fraction \(0.2961267\), close to the exact \(0.2968651\). The finite sample is not used to prove any exact or general statement. This record does not assert independent mathematical audit or external certification.
