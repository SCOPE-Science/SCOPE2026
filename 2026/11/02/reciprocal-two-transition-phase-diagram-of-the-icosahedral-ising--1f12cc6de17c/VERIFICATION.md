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

# Reproduction and limits

`python3 checker.py` requires only Python 3 standard library. The source itself gives all 30 graph edges and contains every check necessary for the finite certificate: 12 vertices, 30 first-neighbor and 30 second-neighbor pairs, six antipodal pairs, each six-pair signed-extremum row, all 4096 spin configurations, the sharp supporting inequalities, the three energy lines, the ground-state degeneracies and the antipodal descriptions. Its assertions use integers and exact rational numbers, never floating-point tolerances. The fully general positive-coupling theorem follows from the explicit supporting-inequality proof in RESULT.md; the finitely many tested coupling values only check the corresponding equality cases.

Limits: this verification is specific to the exact twelve-spin Ising Hamiltonian and finite graph described in RESULT.md. It does not independently validate scientific priority or extend the claim to other spin models or infinite lattices.
