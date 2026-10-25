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
# Finite verification of the quiver Jordan defect formula

The standalone `verify_quiver_jordan_defect.py` constructs each finite radical-square-zero algebra directly from the listed vertices and arrows (including parallel arrows and loops), sets up coefficient equations for the quadratic Jordan identity and the ordinary Leibniz identity, and computes the two solution-space dimensions over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). The rank difference is checked against the combinatorial formula in the theorem for sixteen different finite quivers.

Replay: `python verify_quiver_jordan_defect.py` using Python 3 (no external modules). The script was executed successfully, ending with `QUIVER_JORDAN_DEFECT_OK 16 examples`. The script includes one-loop and two-loop single-vertex algebras, multiple disconnected loop components, opposing arrow pairs with parallel arrows, directed three-cycles, connected edges carrying loops, and mixed examples.

These finite tests do not prove the universal theorem for all quivers/fields. The general proof explicitly normalizes vertex idempotents, classifies arrow and loop components, proves the characteristic-two central-component constraint, and computes the quotient of two linear operator spaces. No third-party or independent mathematical validation has been performed.
