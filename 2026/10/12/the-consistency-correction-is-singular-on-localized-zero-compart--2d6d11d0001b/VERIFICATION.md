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

The verification checks the printed correction and the finite-stencil support argument.

For nonzero current state, Eq. (25) implies \(1+k\nu=U^{n-1}/U^n\). At the simultaneous zero, this ratio has no unique continuous extension: along \(U^{n-1}=U^n\) its value tends to \(1\), while along \(U^{n-1}=2U^n\) it tends to \(2\).

The bundled checker initializes a finite two-dimensional grid with positive susceptible population, a localized exposed/infected source, and zero quarantined/recovered populations. It executes the first corrected-form update with the article's initial convention \(\nu(U^0)=0\). Remote nodes remain exactly zero in \(E^1,I^1,Q^1,R^1\), so evaluating Eq. (25) there for the next step raises the expected zero-denominator condition. The checker prints `VERIFY_OK` only if all these assertions hold.

The numerical values in the checker are illustrative positive parameters; the zero-support conclusion is algebraic and does not depend on their particular magnitudes. No claim is made about an unpublished implementation.
