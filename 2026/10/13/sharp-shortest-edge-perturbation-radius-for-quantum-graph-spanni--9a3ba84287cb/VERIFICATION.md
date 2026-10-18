---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

From the known Friedlander determinant formula and weighted matrix-tree theorem, Q_G=mean(x_e) Σ_{spanning trees T} Π_{e not in T} x_e, with x_e=L_e/ℓ≥1 and β=m−n+1. It equals τ at x=1 and grows coordinatewise. Fix one actual shortest edge; maximizing a cap u occurs with that edge at 1 and all others at u. Contributions Q−τ cannot decrease when a missing edge of maximal length u is added: old complements gain a factor u, the mean increases, and new trees contribute nonnegative errors. Thus K_n is the universal maximizer. Cayley τ(K_n)=n^(n−2) and each edge appears in 2n^(n−3) trees give F_n(u); F_n(1)=τ, F_n strictly increasing, and the half-integer root is exact. Strict length cap avoids a tie. The tree n=2 exception, fixed-graph p_G refinement and ρ_n~n^(−n) follow as stated. Independent enumeration checked exact cotree extremality in 153 graph/shortest-edge cases with n=3,4; all-order proof is monotonicity plus edge addition.

## originality

PASS

Harrison–Weyand arXiv:2209.01284v2 Theorem 2 establishes a substantially smaller sufficient window and the determinant identity used here. Their arXiv:2406.17965v3 Sections 5.2–5.3 treats one-edge perturbations and explicitly only expects a window of order ℓ n^(−n) for complete graphs; it does not give the exact simultaneous-edge all-simple-graphs radius. The reviewed extremal add-edge comparison and precise tree-inclusion refinement close this stated gap. A differently indexed sharp bound remains possible.

## value

PASS

The source studies recovery of a global combinatorial invariant by integer rounding a metric-graph spectral statistic and explicitly calls the previous sufficient spread overly restrictive. The exact largest all-graph radius, extremizing topology and topology-dependent sharp cutoff are mathematically motivated new extremal information, not a mere normalization experiment. All original Kirchhoff/Friedlander identities remain attributed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
