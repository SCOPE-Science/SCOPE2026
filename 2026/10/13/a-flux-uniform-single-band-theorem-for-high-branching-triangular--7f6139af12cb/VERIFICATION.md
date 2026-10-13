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

`python3 verify.py` is executable using only the Python standard library, and was replayed from the decoded packaged artifact. It confirms exact rational specializations of the cubic discriminant identity over branching values 3 through 11 and several rational flux cosines and energies, factors the zero-flux-angle cubic into its indicated linear and quadratic factors, and compares return moments from the cavity Laurent expansion with the exact six-generator Cayley-group walk recurrence at branching three. These checks test algebraic consistency and the identification of the underlying triangle cactus. They do not prove the all-integer discriminant factorization, the physical-root selection, exclusion of singular measures, or universal spectral support: those steps are established in the written analytic proof using the resolvent sign, real-root derivatives, and the established free-convolution atom theorem. The conclusion remains subject to normal mathematical peer review; independent audit has not been performed.
