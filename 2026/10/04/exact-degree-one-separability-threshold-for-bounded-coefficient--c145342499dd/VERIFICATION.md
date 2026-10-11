---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Maximum overlap degree one makes every connected term component a singleton or one edge, and different components act on disjoint qubit sets. The Pauli-mixture lemma is an explicit convex decomposition. For commuting pairs the nonidentity coefficient l1 norm is at most 2t+t^2<=1 exactly through t=sqrt2-1. For anticommuting pairs tanh(beta r)(|a|+|b|)/r<=2 beta J<1 at the same boundary, so they are safely separable. For H=-J(XX+ZZ), the partial-transpose Bell eigenvalue (1-2t-t^2)/4 changes sign exactly above t=sqrt2-1, proving sharpness. The packaged checker corroborates the scalar inequalities and witness sign transition.

## originality

PASS

Fresh inspection of the primary 2026 paper confirms that its exact universal theorem, notation, tree recursion, and sharpness construction assume maximum overlap degree Delta>=2. Its weighted all-degree corollary yields only the weaker sufficient degree-one bound beta J<=1/(4e). Fresh Resultary and keyword searches found no universal Delta=1 theorem at atanh(sqrt2-1). The submitted result is therefore a genuine missing boundary case rather than a substitution into the published Delta>=2 formula.

## value

PASS

The result closes a natural low-degree boundary deliberately excluded from a new exact Delta>=2 theorem, identifies the qualitative jump from infinite threshold at degree zero to a finite sharp degree-one constant, and supplies a matching extremal single-edge witness. This is a motivated endpoint classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
