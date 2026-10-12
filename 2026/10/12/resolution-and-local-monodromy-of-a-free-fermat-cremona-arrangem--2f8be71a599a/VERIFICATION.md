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

# Verification steps and limits

The standalone `verification/verify.py` requires Python 3 with SymPy version 1.12 or later. It was executed from its actual saved path with the command `python verification/verify.py` (after placing it in the packaged relative location) and returned `VERIFY_OK` for two universal syzygies, the universal Saito determinant \(-4f\), direct checks in three sample degrees, and exact formulas for branch contacts, delta/Milnor/Tjurina numbers, the exceptional-divisor multiplicities and monodromy polynomial degrees.

The universal polynomial equalities are proved symbolically in independent variables \(X,Y,Z\), so they apply after the substitution \(X=x^m\), \(Y=y^m\), \(Z=z^m\) for **all** integer \(m\ge2\). The local branch splitting is verified mathematically by the implicit-function theorem, not by sampling roots. The blowup multiplicities follow recursively from a single exceptional component plus two smooth branches at each blowup center. The A'Campo formula converts those exact divisor multiplicities and the Euler characteristics of their punctured exceptional curves into the local zeta function.

The checker verifies algebraic identities and internal consistency, **not** the theorem by exhaustive numerical enumeration. No analytic Milnor-fiber computation, global Alexander polynomial, unpublished external certificate or independent mathematical audit is claimed. Source arXiv:2301.01117v1 is the first public version for the algebraic family; the Tjurina value itself is already attributable to its journal and preprint treatments.
