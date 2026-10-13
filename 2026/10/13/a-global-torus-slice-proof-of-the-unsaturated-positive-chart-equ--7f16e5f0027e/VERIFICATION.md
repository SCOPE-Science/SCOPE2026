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

The algebraic proof establishes a scheme-level inverse on the principal open \(D(\prod_i F_i)\), which is smooth and irreducible. The inverse contains negative powers only of nonvanishing \(F_i\), so no pole remains on that open. Weighted Euler operators have the identity matrix as their action on \((F_i)\) along the level-one fiber; this supplies Jacobian rank \(r\) at every point. The associated divisor degrees in the toric application are an integral basis by the initiating paper's unimodularity hypothesis, and the parametrized dense-torus locus is nonempty.

Run `python checker.py` using Python 3 standard library. Expected single line: `VERIFY_OK: unimodularity, weight basis, multihomogeneity, exact torus slice`. This arithmetic covers the published five-coordinate pentagon example only. The global statement requires and receives the symbolic ring-map proof, not finite enumeration. Nonunimodular weights are excluded: for example \(F=u^2\) of degree \(2\) in the usual \(\mathbb Z\)-grading has a disconnected level-one fiber.

Public primary-text inspections covered the initiating paper's Assumption 1, Lemma 3.3, Proposition 3.8, Corollaries 3.9–3.10, Conjecture 3.11, and its computationally unresolved example; comparison sources covered the Cox torus action and the related localized graded-factorization theorem for finite-representation-type varieties. No independent audit or exhaustive historical novelty certification has been performed.
