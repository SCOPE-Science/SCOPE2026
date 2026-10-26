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
# Verification and limits

The proof establishes the stated claim analytically in two exhaustive cases: distinct and repeated joint eigenvalues. Each input tuple is compressed in a common unitary triangularizing basis; the simultaneous commutation constraints, amplified Cartan automorphism defect identity, strict block norms, scalar Schwarz–Pick inequalities, and final \(2\times2\) positivity test are all explicit in `RESULT.md`. The cited published Hartz–Richter–Shalit Proposition 3.5 is the source of the previously known three-dimensional counterexample, which is transferred to rectangular block factors by coordinate embedding and adjunction.

Run the included script `python checks/cartans_two_level.py` with NumPy and SciPy to reproduce finite numerical diagnostics for the automorphism defect identity and triangular contraction calculations. The algorithm is deterministic and does not attempt exhaustive or symbolic certification of the infinite-dimensional function class. The theorem's universal quantifiers and all product ranks are handled by proof, not experiment. Earlier equivalent literature formulations remain a source-priority risk; no independent audit is represented.
