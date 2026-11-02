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

The standalone `verify.py` was run using `python3 verify.py` after it was written to this package directory. It returned `PASS 8541 assertions; exact radical/Bernstein checks and numerical matrix/root checks` with no exception.

Checks include the exact specialization of the published stability function, the exact resolvent coefficient ratio, the rational Bernstein coefficients on \([0,1/2]\) and \([1/2,1]\), the exact five-state witness in \(\mathbb Q(\sqrt2)\), and a separate direct finite-matrix inversion calculation for 12 dimensions and nine positive timestep values per dimension. A further numerical grid brackets two roots for dimensions five through 64. No finite grid is used as a substitute for the analytical proof of root uniqueness or the assertions for arbitrarily large \(n\).

All computational inputs are included in the plain-text verifier. No remote service, private file, unbundled certificate, or external data are required for replay. Python 3's standard library suffices. Numerically reported roots are illustrative approximations only, while all theorem-defining boundaries use exact expressions or uniquely specified real roots.

The cited primary sources establish the numerical method and relevant historical comparison; they are not packaged or redistributed. Independent audit remains unperformed.
