---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For m>=2,k>=3, write L=L_{K_m}⊗I+I⊗L_star and G=(mI+L_star)^{-1}. A horizontal unit edge has potential (e_i−e_j)⊗G e_s, yielding its absolute clique and spoke voltage-drop column sums. A vertical unit spoke splits into a constant-in-clique tree mode plus (e_i−1/m 1)⊗G(e_0−e_ell). The derived inverse entries have fixed positive signs and 0<a<1, so all absolute values are resolved algebraically. P=I−Q gives each cycle column norm as 1+cut_column_norm−2Q_ee. Subtractions q_h−q_l>0 and p_h−p_l>0 exclude leaf maxima. Integer sign polynomials A_Q and A_P give the exact hub/spoke boundaries: Q tie m=4,k=11; P ties m=7,k=11 and m=8,k=37, and switch at m=6 k=5. An independent grounded-Laplacian numerical reconstruction on 64 (m,k) instances independently tested three edge columns per case, 192 in total; largest six-column formula error was 5.33e−15. The universal proof is symbolic matrix inversion and sign analysis, not the finite grid.

## originality

PASS

The cut/cycle orthogonal projector formalism and transfer-current matrix are classical, and Dilworth–Kutzarova–Ostrovskii compute endpoint norms on Hamming graphs, tori and hypercubes (their theorem 45 is specifically hypercube). The inhomogeneous K_m × star product, all six edge-type rational expressions and distinct hub/spoke switching thresholds are not asserted by the inspected prior source. A general graph Laplacian formula is a tool and does not by itself imply the optimized piecewise thresholds. Best-of-knowledge O PASS, with possible less-indexed transfer-current closed-form identities a residual risk.

## value

PASS

The canonical Hodge cut/cycle projectors are fundamental to transportation-cost and graph edge-space analyses, and the clique×star product is a natural inhomogeneous Cartesian family. Knowing exactly which geometric edge direction controls an endpoint norm and where it changes is a useful complete invariant, not an arbitrary tiny-graph computation; complementary projections exhibit different reentrant branching thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
