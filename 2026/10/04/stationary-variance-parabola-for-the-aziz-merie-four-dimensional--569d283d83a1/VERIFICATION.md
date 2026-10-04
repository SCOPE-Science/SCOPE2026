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

The symbolic replay in `verify.py` reconstructs the Lie derivatives of \(x^2/2\), \(z\), \(w^2/2\), \(xw\), \(y^2/2\), and \(z^2/2\) directly from the displayed vector field. It checks the elimination chain leading to \(\int z^2\,d\mu=B\bar z\), and it evaluates \(B=2973/400\) and \(B/\phi=2973/4000\) exactly at the source parameters. The replay returns `VERIFY_OK`.

The compact-support endpoint arguments are mathematical deductions rather than computational certificates. No numerical time integration, finite enumeration, or timeout is used as evidence for the universal claim. The verification does not establish existence or uniqueness of a nontrivial invariant measure.
