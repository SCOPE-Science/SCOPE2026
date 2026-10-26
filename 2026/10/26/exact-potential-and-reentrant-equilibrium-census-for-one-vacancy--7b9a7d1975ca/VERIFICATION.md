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

# Verification

The theorem follows from an algebraic cross-part move identity and direct necessary-and-sufficient equilibrium inequalities. The accompanying `verify_multipartite.py` enumerates all legal vacancy/color states for eleven binary cases and five ternary cases, independently recalculating the utility of each mover using graph neighborhoods, checking exact potential increments, and for the binary cases computing equilibrium coefficients independently of the criterion. It uses only the Python standard library and `fractions.Fraction`.

Observed totals: 16 cases; 35,349 configurations; 243,582 individual legal moves; no mismatches. Representative numbers of binary equilibrium assignments are 68 for \(K_{2,2,3}\), 96 for \(K_{2,2,4}\), and 252 for \(K_{2,2,5}\). Use `python verify_multipartite.py` to reproduce the finite checks. These tests verify finite instances only; no statement of full generality, bibliographic novelty or independent validation follows from them.
