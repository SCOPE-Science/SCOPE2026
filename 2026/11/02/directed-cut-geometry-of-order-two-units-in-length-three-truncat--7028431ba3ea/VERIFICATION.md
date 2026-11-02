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

# Verification record

The general theorem is proved in RESULT.md by the path-basis coefficient equations, squarefree monomial prime decomposition, the directed-cut equivalence, and a counting argument; no experimental extrapolation is used.

Run `python3 verify.py` from this package. It constructs the path basis of \(kQ/J^3\), builds its multiplication table, and exhaustively tests the original square equation on all elements \(1+u\) in \(27\) finite-field configurations across \(\mathbb F_2\), \(\mathbb F_4\) and \(\mathbb F_8\). Its second computation independently enumerates independent arrow supports and verifies both the finite-field formula and the equality between maximum independent-set cardinality and maximum directed cut for twelve labelled quivers. Checks include a loop, two loops, directed cycles, paths, parallel arrows, forks and disconnected quivers.

Terminal success: `CUBIC_QUIVER_INVOLUTION_OK 27 complete finite-field multiplications 12 geometry comparisons`.

Scope limits: Only tested finite sizes are exhaustively enumerated. The symbolic proof covers arbitrary finite quivers over all fields of characteristic two. The theorem describes reduced geometry inside the normalized subgroup \(1+J\); the full scheme of all units satisfying \(g^2=1\) can have additional infinitesimal directions in diagonal coordinates. Independent mathematical audit: not performed.
