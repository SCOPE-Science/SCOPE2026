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

The proof is structural and applies to every integer \(n\ge3\). Its critical step is the exact private-neighbor criterion: for selected \(a_i\), self-privacy holds exactly when \(Y\subseteq\{b_i\}\); otherwise an external witness is precisely an unselected \(b_j\) with \(j\ne i\) and \(I\setminus\{i\}\subseteq\{j\}\). The symmetric statement holds on the other side. This forces the complete case split and the maximality arguments.

`verify_irredundance.py` independently constructs the graph and directly evaluates the definition from closed neighborhoods. It exhaustively checks every subset for \(3\le n\le8\), compares the direct predicate with the structural classification, tests maximality by all one-vertex extensions, and compares both coefficient tables with the formulas.

The finite exhaustive check is a boundary and arithmetic verification only. It is not used to infer the theorem for untested values of \(n\). No independent audit has been performed.
