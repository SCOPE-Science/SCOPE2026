---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Tree edge gradients are independent coordinates modulo constants. On every gradient-box face, the largest signed outward derivative is exactly r^(p−1)(A_e−D_e), obtained by independently assigning signs/magnitudes to adjacent gradients. Invariance of all gradient boxes proves iff condition and instantaneous derivative. x_e=c_eℓ_e^(p−1) converts the inequalities to Bx≤x; irreducible Perron–Frobenius establishes ρ(B)≤1, with critical positive gauge unique up to scale. For p≠2 and adjacent edges, the Jacobian off-diagonal response |g_f|^(p−2) can overwhelm fixed diagonal loss by varying g_f; an explicit 3-vertex path witness makes two-input distance increase. Independent p=1.2,1.5,2.5,3,4 path Jacobians and a 3-leaf star PF threshold corroborate, not prove, the theorem.

## originality

PASS

Mugnolo arXiv:1207.1996 develops nonlinear p-heat contraction in vertex ℓ^q norms; Münch–Wojciechowski arXiv:1712.00875 characterizes linear p=2 graph Lipschitz contraction via Ricci curvature. Neither inspected theorem implies nonlinear p≠2 edge-box criterion, PF length design and universal two-input obstruction. Related edge total variation star mass threshold is different norm and is acknowledged.

## value

PASS

Sharp local invariant-box conditions, a computable PF design boundary and a structural separation between one-input decay and two-input stability are useful results for nonlinear graph diffusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
