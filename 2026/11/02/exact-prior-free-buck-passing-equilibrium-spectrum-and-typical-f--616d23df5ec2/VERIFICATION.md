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

For every pure strategy profile on bidirected loopless K_(a,b), the functional digraph has disjoint cycle components. With multiple cycles, a cycle vertex can redirect to a vertex of the opposite part on another cycle and eliminate its own recurrence, strictly reducing its full-support-prior cost. With one cycle but an off-cycle vertex at depth d≥2, a parity-correct cycle vertex can redirect to that tail to extend the cycle by d (even d) or d−1 (odd d), reducing its cost. Conversely with one cycle of length 2k and only depth-one noncycle vertices, every legal cycle-vertex deviation yields a cycle no longer than the original, and offcycle players have zero cost. Thus the precise prior-free equilibria are one alternating cycle and depth-one attachments. Choose k vertices per side, k!(k−1)! cyclic orders, and k^(a+b−2k) depth-one links to derive the exact labeled N_k. Balanced m,m log count has uniform Stirling exponent F(x) strictly concave and maximized at α=1/(1+ω), ωe^ω=1; concentration of K_m/m and fairness m/K_m follow. Independent exhaustive direct uniform-prior best-response comparisons for K_(1,1), K_(1,4), K_(2,3), K_(3,3), K_(3,4) matched structure and complete coefficients.

## originality

PASS

Cominetti–Quattropani–Scarsini introduce the prior-free game and supply general profitable-cycle extensions, component merging, and equilibrium existence, all acknowledged. The inspected arXiv treatment does not provide the exact labeled complete-bipartite equilibrium cycle-length polynomial or the balanced uniformly-sampled-equilibrium Lambert-W limit. These quantitative results are additional; an unindexed specialized cycle-arborescence enumeration remains a historical risk.

## value

PASS

A complete natural infinite-family equilibrium spectrum answers how many pure prior-free equilibria of each cycle size exist, not just existence. The typical recurrent fraction ≈0.638 and fairness ratio ≈1.567 provide motivated quantitative welfare/fairness information distinct from worst-case or algorithmic dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
