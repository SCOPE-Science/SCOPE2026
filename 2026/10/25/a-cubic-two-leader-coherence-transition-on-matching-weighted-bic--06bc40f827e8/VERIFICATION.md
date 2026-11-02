---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The weighted Laplacian decomposes into restricted symmetric, restricted antisymmetric and bipartition-sign eigenspaces of eigenvalues n, p=n−2+2t and q=2(n−1+t), positive for n≥3,t≥0. Exact orbit projection weights give R_{same/matched/cross} and B_{same/matched/cross} with denominators p,n,q and squares. A grounded Green matrix followed by Schur complement proves C=2tr L^+−B/R−(N/4)R with N=2n, so maximizing Φ=B/R+nR/2 orders all pairs. The matched-minus-same difference is −P_n(t) divided by a positive denominator; same-minus-unmatched-cross is strictly positive. Positive cubic derivative coefficients, P_n(0)<0 and P_n(1/2)=n−1>0 give unique c_n and all tie counts. Resistance quadratic root r_n is smaller because P_n(r_n)=−n(n−2)/2<0. Mean-value control on P_n′ and the explicit radical prove n(c_n−r_n)→1/4. Direct exact rational n=3,t=2/5 example yields resistance 1/108 and coherence 5/342 of opposing signs. Independent SymPy simplification confirmed cubic orbit score identity; 27 exact direct inverses of follower matrices for n=3..5/t=0,2/5,1 and three pair-orbits confirmed formula. Finite matrices corroborate, not replace, the all-n polynomial proof.

## originality

PASS

Best-of-knowledge, not absolute priority: On K_{n,n}, n≥3, with cross-part conductances t on a perfect matching and 1 elsewhere, the optimum two noise-free leaders for tr(L_FF^−1) switch at unique c_n∈(0,1/2), root of explicit cubic P_n(t), from matched cross-part pairs to same-part pairs (both at equality), and never unmatched cross pairs. Effective-resistance pair ranking switches earlier at r_n<c_n and n(c_n−r_n)→1/4, with rational n=3,t=2/5 disagreement. The inspected primary sources contribute prerequisite constructions or related weaker/different statements, without identifying a prior theorem that logically entails the distinctive final statement. Inaccessible/unindexed historical overlap remains an explicit risk.

## value

PASS

Exactly two pinned leaders are a natural noisy-consensus/control placement problem. Varying the matching conductance t continuously deforms crown graphs to the full biclique and beyond, yielding a complete all-n optimal-pair classification. The sharp mismatch interval shows a mathematically consequential limitation of resistance-only heuristics despite transitive equal-information-centrality vertices; no claim about general weighted graphs or three leaders is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
