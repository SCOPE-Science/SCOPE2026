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

For \(\operatorname{Cr}_n\), the direct proof uses the exact formulas
\[
\delta_S(a_i)=|J|-\mathbf 1_{i\in J},\qquad
\delta_S(b_j)=|I|-\mathbf 1_{j\in I}.
\]
Because every vertex has degree \(n-1\), the strong defensive inequality is equivalent to internal degree at least \(\lceil(n-1)/2\rceil\). This establishes the two overlap regimes. Connectivity is checked separately: the zero-overlap regime induces a complete bipartite graph, while the positive-overlap regime induces a complete bipartite graph with independent matching edges deleted and both sides large enough to remain connected.

The standalone checker `artifacts/verify_strong_alliance_crown.py` independently constructs the graph, evaluates connectivity and every vertex inequality from the adjacency relation, and compares each subset with the structural criterion. It then compares the brute-force cardinality vector with the two closed parity formulas and checks the resulting minimum coefficient. Exhaustive replay covers \(4\le n\le8\), i.e. graphs through sixteen vertices. It also verifies that \(\operatorname{Cr}_3\cong C_6\) is the exceptional connectivity boundary and has the known cycle coefficient vector.

Finite exhaustive replay is not used to infer the infinite theorem; it only stress-tests the proved classification and its boundary.

Executed package replay:

`VERIFY_OK n_range=4..8 subset_checks=87296 classification_checks=87296 coefficient_checks=65 minimum_checks=5 max_order=16 boundary_n3=C6`
