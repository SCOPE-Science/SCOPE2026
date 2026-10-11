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

The exact checker `verify.py` was run from this package and returned `VERIFY_OK`. It verifies the polynomial identity \(\dot R=2ay^2\) for \(R=x^2+y^2\) from the displayed four-dimensional vector field using exact rational polynomial arithmetic.

The recurrence conclusion is analytic: a recurrent orbit cannot carry a nonconstant monotone continuous observable. Once \(y=0\), the equations reduce to \(\dot z=-bz\) and \(\dot w=-cw\), so positive \(b,c\) force recurrent points to satisfy \(z=w=0\).

For an invariant probability measure with compact support, integrating the generator identity for \(R\) gives \(\int y^2\,d\mu=0\). The support is therefore contained in \(y=0\); integrating the induced identities for \(z^2\) and \(w^2\) gives \(\int z^2\,d\mu=\int w^2\,d\mu=0\).

The result does not certify the behavior of unbounded trajectories, finite-time numerical traces, or the degenerate case \(a=0\).
