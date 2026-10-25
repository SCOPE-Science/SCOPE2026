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

# Verification instructions

Install Python 3 and SymPy; execute scripts in their shared directory in order: `python bideg23.py`, `python prank.py`, `python prank_branch.py`, `python independent_all_forms.py`. The first uses exact projective orbits and four-chart Gröbner smoothness. The second computes exact F4 point counts and Jacobian 2-ranks from Weil coefficients. The third computes 2-ranks from distinct Artin–Schreier branch points. The last is an independent four-chart full enumeration of every nonzero form. Compare results with supplied deterministic reference outputs; stopwatch timings, if any, are not part of a mathematical certificate. None of these finite verifications establishes publication originality or supplies an independent mathematical audit.
