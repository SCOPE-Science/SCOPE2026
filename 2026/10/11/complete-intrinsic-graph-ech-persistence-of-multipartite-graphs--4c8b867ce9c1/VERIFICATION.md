---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For every k≥2, n_i≥2, the graph is connected with v=sum n_i vertices, e=sum n_i n_j edges. Lemma 2.2 gives r0 v isolated vertices and r1 graph wedge^{e−v+1} S1. For x in P_i, radius-one neighborhood is V\(P_i\{x}), so r2 simplex condition is |σ∩P_i|≤1 for SOME i. This proves exact cover T_k=union_i (Δ_1*…*D_i*…*Δ_k). With T_1=D_1, the induction T_j=(T_(j−1)*Δ_j) ∪ ((Δ_1*…*Δ_(j−1))*D_j) has contractible pieces, intersection T_(j−1)*D_j, yielding via cofibration homotopy pushout T_j≃Σ(T_(j−1)*D_j), hence T_k≃Σ^{k−1}(D_1*…*D_k)≃wedge^{prod(n_i−1)}S^{2k−2}. The join reduced-chain Künneth and natural Mayer–Vietoris boundaries under part-preserving permutations identify integral top homology with tensor_i ker(Z^{n_i}→Z), with no interpart permutation signs. Any edge between parts has N1[u]∪N1[v]=V, so r3 full simplex, and only integer thresholds matter. Integral free barcodes follow. All-scale small tuples independently exhaustively reconstructed and mod2 boundary-reduced (checks do not replace unbounded pushout induction).

## originality

PASS

PASS best-of-knowledge for the complete multipartite family homotopy persistence and integral part-preserving symmetry module. Earlier Previte thesis explicitly poses this D-neighborhood multipartite homology direction; Adams–Shukla–Singh supplies the general generating-simplex construction but not the cover/suspension classification. Uniform derivation and module are mathematically distinct from indexed prior statements read.

## value

PASS

This is an all-parameter structural classification of a standard graph family, not a one-off example. It gives complete closed-graph Čech barcode and an integral symmetry representation for every multipartition, addressing a specific multipartite D-neighborhood homology direction explicitly suggested in Previte’s original open-problems chapter. Future workers can use both closed formulas and group module type, which are not routine direct consequences of the parity facet lemma alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
