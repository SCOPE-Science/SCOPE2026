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
# Reproducibility and verification

Run `python verify_negative_etm.py` with Python 3 and SymPy. The independent-audit channel has not been performed.

The script checks the exact degree-eight discriminant and its four real isolating intervals by rational Sturm root-counting; it checks the equilibrium scalar reduction, the transcritical factorization, a rational parameter where the quartic has exactly two real roots, and a parameter where it has none. It verifies the completed-square convexity identity, rigorous rational lower bounds for \(P_{xx}\) and \(P_r\) on the entire fold rectangle, the cancelling weighted energy, the critical resultant, and the local determinant/Routh bounds. All symbolic computations use exact arithmetic.

The universal assertions follow from the proof's continuous-parameter inequalities, Sturm-based topology changes, and standard Routh–Hurwitz criterion. The numeric approximations are labels for isolated algebraic values, not independently certified decimal expansions beyond the supplied isolating brackets. The script does not certify basin boundaries, global periodic-orbit absence in the coexistence window, or publication priority.
