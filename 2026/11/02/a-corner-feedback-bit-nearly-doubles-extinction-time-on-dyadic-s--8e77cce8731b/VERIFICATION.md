---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Over F2, the one-dimensional path adjacency on 2^a-1 vertices is cyclic nilpotent J_{L-1} by characteristic polynomial recursion. The grid is multiplication by z=x+y on F2[x,y]/(x^{L-1},y^{L-1}); quotienting the truncated free module over F2[z]/(z^L) yields N=J_L(0)^(L-2)+J1(0). Swapping two grid coordinates cancels all positive-length closed corner-return walk counts mod2, so mu_0=1 and mu_j=0 (j>=1). Sherman-Morrison resolvent in char2 gives B^k=N^k+sum_{i+j<=k-1}N^ie e^T N^j; the corner Krylov basis and its annihilator prove ranks (L-2)(L-k)+k through k=L and 2L-k afterwards. Rank-one idempotent B^{2L-1} proves one fixed eigencomponent and reconstructs Jordan blocks J1(1),J1(0),J_(2L-1)(0),J_L(0)^(L-4). Independent bitmatrix ranks at L=4,8 matched all predicted powers; counts follow from kernel dimensions, not trajectory simulation.

## originality

PASS

Best-of-knowledge PASS for the exact single-corner rank-one feedback block decomposition, sharp doubled transient and all labelled-state entry shells. Existing path/grid nilpotence/Jordan methods are credited. A plausible 2004 exceptional-rule paper was not accessible in full, so its exact overlap remains a residual priority risk rather than an automatic science failure.

## value

PASS

Single-vertex defect perturbations of binary cellular automata are natural structural questions. This theorem gives a complete nontrivial infinite dyadic grid family: one corner bit changes pure extinction into two absorbing fixed states, doubles the order of longest transient up to one, and exactly enumerates every initial-state entry shell. The result is not a routine reparametrization of homogeneous grid Jordan theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
