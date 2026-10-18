---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For signed K_(m,n) with m,n>=2, the signed-burning rule propagates one synchronous round then ignites one remaining vertex. With first ignition at a_i of colour +, the entire opposite shore is forced to s_ij in the next spread; the second ignition can preempt at most one same-shore vertex before the correlation wave. Unignited a_k receives sign rho_ik=sum_j s_ij s_kj; negative/positive correlations can be preempted once while zero correlations remain later independently ignitable. Hence the exact maximum is R_i=r_i^0+max(1+p_i+r_i^++1_[r_i^->0],q_i+r_i^-+1_[r_i^+>0]); swap shores for C_j and maximize. Reversing both colours accounts for either chosen target. Independently implemented signed-round recursion versus formula, exhaustively for all 16 K2,2, 64 K2,3, 64 K3,2, 256 K2,4 and 512 K3,3 signings (912 signing tests); all matched. The structural proof covers arbitrary m,n and is not inferred from finite cases.

## originality

PASS

The initiating 2026 Fallat–Gupta–Khodamoradi–Zilles full arXiv rendered article defines precisely this two-colour burning process, proves switching/coding reductions and signed-path results and hardness, but in inspected complete text contains no K_mn, complete-bipartite, or biclique all-signature correlation formula. A generic Hamming-code characterization alone does not evaluate each signing in O(m²n+mn²). The exact row/column-correlation formula is a family-specific structural consequence, not a claim of a new burning process.

## value

PASS

A complete polynomial-time plurality formula for arbitrary signed complete bipartite graphs is a natural full-family tractable island inside a general hard signed-burning problem. It converts an adaptive process to low-degree sign correlations and can be used directly on signed bicliques.

The dated certificate retains the supplied scientific assessment, sources and limitations.
