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
# Verification and replay

The proof is self-contained apart from the standard uniform distribution of Lebesgue-typical orbits of the integer expanding map and the finite-generator entropy identity. The exact algebraic partition inequalities and the entropy lower bound are laid out in `RESULT.md`.

Execute `python verify.py` using Python 3 and the standard library. Its exact-rational checks cover \(q=2,\ldots,9\), \(m=2,\ldots,8\), and 2,520 finite orbit prefixes. It tests special-cell disjointness, label witnesses, the full alphabet, recovery of the underlying expanding digits, and finite-length digit-cylinder bounds. A further diagnostic estimates the three fixed coordinates \((1/5,1/2,4/5)\) from special-symbol frequencies over a 120,000-step approximate base-two orbit. This finite experiment is deliberately not treated as proof of the almost-everywhere assertion.

The infinite statement requires a common full-measure equidistribution set valid for all interval endpoints; using only finitely many tested thresholds would leave a logical gap. The entropy argument excludes an \(m\)-cell generator only after deriving uniform distributions at **every** finite block length. The publication comparison leaves a residual possibility of older equivalent polyhedral codings.
