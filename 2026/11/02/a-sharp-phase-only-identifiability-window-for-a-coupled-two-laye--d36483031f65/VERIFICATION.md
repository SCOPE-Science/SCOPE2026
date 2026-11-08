---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Derive the exact harmonic inverse response Z=lambda+i omega C+i omega D*kappa/(kappa+i omega D). Rationalizing gives the open right semicircle X>lambda and Y increasing. Differentiating arg Z leaves positive denominator and the bracket (C+D)kappa^2+2 lambda D kappa-omega^2 C D^2, strictly increasing from negative at kappa=0 to positive as kappa grows: exactly one fold. Restricting to [a,b] puts the fold strictly within iff Omega(a)<omega<Omega(b). The monotonic branches prove phase multiplicities with correct open endpoints, and fractional-linear injectivity proves different gains for two phase aliases. Independently checked rational exact semicircle/derivative and the two gains for kappa=1/2 and 3/2. No inference about unknown other physical parameters.

## originality

PASS

Geoffroy et al. (2013) Appendix D explicitly derive harmonic frequency response, gain and phase of exactly the two-reservoir model. Those formulas cover the transfer itself; the assessed additional result fixes frequency, varies exchange kappa, proves the global unique phase fold and exact alias-count and interval-design classification. A classical two-node thermal or electrical circuit phase-ambiguity theorem could cover it and remains a residual risk.

## value

PASS

The phase-only inverse-identifiability obstruction is a natural uncertainty in harmonic calibration: a single phase observation gives exactly two physically different couplings within a sharp experimentally checkable region, and adding amplitude removes this ambiguity. This is more than a raw derivative evaluation because it supplies a global inverse classification and boundary-frequency prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
