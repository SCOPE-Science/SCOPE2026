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

The verifier works over characteristic \(2\) and checks the following exact identities. Substituting \(s=t^3\), \(u=tx\), and \(v=x^3\) reproduces both quotient relations and the source equation. The Jacobian minor in the \((u,v)\) columns reduces modulo \(u^3+sv\) to \(s^3\); hence singularity forces \(s=0\), then \(u=0\), then \(v=0\), then \(y=0\). At the origin the Jacobian rank is one, so that point is singular. Formal elimination of the equation with linear term \(s\) gives cubic initial form \(u^3+uv^2+vy^2\), proving local multiplicity \(3\).

The executable check prints:

`VERIFY_OK invariant_ring_relations=2 singular_locus=origin local_multiplicity=3`

The verification does not classify the analytic singularity type and does not address a global compactification or resolution.
