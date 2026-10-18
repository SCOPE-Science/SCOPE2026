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

For 0<p≤1 and positive weights, fiber disjointness gives ||Tx||_p^p=Σ_n λ_n^p|w_nx_n|^p, proving boundedness exactly when sup λ_n<∞. For t>σ_j, at most j−1 columns exceed t; coordinate truncation yields a_j,c_j,d_j≤t and dimension-intersection gives b_j≤t. For s<σ_j choose j columns λ_n>s; their span gives b_j,a_j,c_j≥s. The nonstandard Kolmogorov lower bound is justified: for normalized pairwise disjoint z_i, approximants f_i in a lower-dimensional F with ||z_i−f_i||_p^p<1 imply strict column p-mass diagonal dominance D_ii>Σ_{r≠i}D_ri. Any dependence Σα_i f_i=0 contradicts p-subadditivity after summing each block, since Σ|α_i|^pD_ii≤Σ|α_i|^pΣ_{r≠i}D_ri. Thus some z_i has distance at least 1 from F; d_j≥s. Supremum/nonattainment, λ=0 and j arbitrary are handled. Compactness follows from finite-coordinate truncation, whereas nonvanishing infinite λ selects an infinite-dimensional coordinate subspace where T is bounded below, so compact/strictly singular/finitely strictly singular are equivalent. The source examples and finite verifier are corroborative only.

## originality

PASS

Best-of-knowledge comparison of statements/implications from genuinely inspected primary material and the audited claim. Resultary returned temporarily_unavailable/search_completed:false; this failed search supplies NO negative novelty evidence. Compactness and essential-norm characterization provide asymptotic information; they do not identify each finite-index approximation, Bernstein, Gelfand and Kolmogorov width or prove their exact equality. A Hilbert-space four-minimax identity does not transfer through uncomplemented quasi-Banach images.

## value

PASS

The equality of four natural finite-index widths for all bounded weighted composition operators on the nonlocally convex ℓp(w) scale answers a complete spectral question, not merely restating compactness. The Kolmogorov component demands a substantive disjoint-support quasi-Banach distance lemma in precisely a setting where norm-one range projections fail. Nonattained singular profiles, arbitrary repeated fibers and all positive weights are covered; the compact/strict-singularity threshold is a natural additional consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
