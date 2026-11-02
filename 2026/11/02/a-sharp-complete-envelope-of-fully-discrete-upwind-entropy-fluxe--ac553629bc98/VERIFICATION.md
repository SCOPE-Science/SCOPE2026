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

# Reproducibility

Extract `verify.py` from the same package and execute `python3 verify.py` with a standard Python 3 installation. The script uses `fractions.Fraction` to check the all-state dissipation identity on finite rational grids, the sharp coefficient boundaries, the specialized half-cell interval formula, state-dependent flux selections inside the exact envelope, and explicit violations outside the envelope.

The executed verifier reported `PASS: 12072 total exact-rational algebraic and universality checks` after a preliminary `PASS: 10620 exact-rational identities and interval tests`. The proof in `RESULT.md`, rather than these finite checks, establishes the universal statement for all real data and functions.

Scientific limits: scalar quadratic entropy, exactly upwind flux, one forward Euler step, physical consistency of the entropy flux, periodic meshes with at least three cells. Historical priority and independent audit are not established.
