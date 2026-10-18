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

# Reproducibility checks

Run `python3 verify.py` in a directory containing the complete embedded file; the checker has no nonstandard Python dependencies. It enumerates 16 rational linear inequalities, solves all nonparallel pairs exactly, obtains six vertices, and checks both analytic witness formulas, the flux identity, and 39 rational parameter values from \(1/40\) to \(39/40\). The unit ball computation and the independent proof in `RESULT.md` cover all real \(0<t<1\); finite parameter tests are not treated as a proof of that quantifier. In an additional separate numerical cross-check, a six-variable linear program for four test-function values and two norm auxiliaries agreed with the formula at 98 distinct parameters; numerical optimization cannot establish an exact symbolic theorem.

The minimal-cardinality statement is supported analytically by endpoint flattening on paths of at most three sites; the checker is not presented as a census of every smaller metric. The comparison to earlier finite LP algorithms is a statement about the additional explicit monotonicity transition, not a claim that those algorithms cannot compute these norms. Independent audit is not performed.
