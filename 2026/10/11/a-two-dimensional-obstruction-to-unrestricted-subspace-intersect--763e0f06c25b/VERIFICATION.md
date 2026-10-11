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
The claimed Parseval property follows from the orthogonal decomposition of \(\mathbb{R}^2\) into the two coordinate lines. Because both woven families are identical, every possible weaving has exactly the same two components and therefore the same unit lower and upper bounds.

For \(W=\operatorname{span}\{e_1+e_2\}\), direct linear independence shows that each coordinate line intersects \(W\) only at zero. Thus the restricted energy is exactly zero for every nonzero vector in \(W\).

The proof diagnosis was checked against the primary theorem: it uses \(P_{M\cap W}=P_M P_W\) with no commutation assumption. For orthogonal projections, equality with an orthogonal projection makes the product self-adjoint and hence forces \(P_M P_W=P_W P_M\); the converse follows because a commuting product of orthogonal projections is the orthogonal projection onto the common range.

The displayed \(2\times2\) matrices independently verify the failure in the counterexample. No numerical approximation, exhaustive search, or unproved computational certificate is used.

Scope limit: the verified correction establishes failure of the unrestricted theorem and a commutation-based repair in the ordinary specialization. It does not establish a complete set of hypotheses for the fully controlled setting.
