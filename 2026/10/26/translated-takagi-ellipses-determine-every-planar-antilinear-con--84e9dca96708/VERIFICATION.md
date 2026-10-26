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

# Reproducibility and limits

The proof is entirely algebraic and geometric. The key identities to check are the two-parameter orthonormal decomposition, \(x^TBy\) under a Takagi basis, inequalities \(|h_2|\le h\), \(v_2\le v\), and exact exhaustion of the filled ellipse by segments between the nested ellipse boundaries. The extremal formulas are ordinary Euclidean distances and, in the real-skew case, a concave quadratic maximization.

The attached `checker.py` executes with Python 3.9+ and no third-party packages: `python3 checker.py`. It includes deterministic randomized finite checks, edge degeneracies and matching specialized formulas. Such tests corroborate algebraic computations; they cannot establish the theorem for infinitely many possible matrices or exhaust historical publication priority.

Earlier two-dimensional antiunitary and quaternionic-root cases are recognized as covered restricted families, not new independent claims. Only self-review was performed; independent audit and external validation were not performed.
