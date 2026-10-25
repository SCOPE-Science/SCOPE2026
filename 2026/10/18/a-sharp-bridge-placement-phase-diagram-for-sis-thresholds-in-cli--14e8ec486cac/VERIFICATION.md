---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The proof uses the exact graph G_k (K5 with distinguished vertex a, hub h, k leaves, and a single weighted bridge to K2); its symmetric (k+8)-square contact matrix and Perron radius define the stated threshold. For z>rho(A(G_k)), diagonal Green functions satisfy g_a=(z-3)(z²-k)/P_k and g_h=z(z-4)(z+1)/P_k, with g_a-g_h=((4-k)z+3k)/P_k. The verified signs of comparisons to other clique vertices and pendants exclude those placements. Strictly decreasing w²g_v(z)z/(z²-1) yields unique roots and the crossover z_k=3k/(k-4); P_k(4)=-4 and P_k(z_k) separate integer k=5..13 from k>=14. At k=7 the critical w²=40. The four rational Schur signs at (w,beta)=(6,149/2000),(7,263/4000), delta=1/2 certify strict mean-field stability reversals under admissible contact probabilities. The monotone SIS map and Perron sub/supersolutions justify subcritical global extinction and supercritical positive fixed-point persistence. Independently rebuilt matrices and checked 228 direct spectral placement instances (k through 30), crossover and all four exact rational signs; these finite tests do not prove the universal k,w statements.

## originality

PASS

Compared the exact one-bridge endpoint optimization with Dung–Phuc local/global threshold inequalities, Li–Eliassi-Rad–Zhang weighted-edge centrality intervention, and Ma–Valdez–Braunstein modular stochastic SIR bridge regimes. Different choices of attachment endpoint at fixed communities and variable single-edge weight, the three integer-k regimes, and the k=7 exact reversal are not directly stated in accessible prior statements. Full Dung–Phuc text could not be inspected: uncertainty remains about any implicit general attachment theorem. Resultary semantic search found related network/bridge and epidemic results but no strong exact implication; search failure alone does not establish priority.

## value

PASS

The endpoint of a single intercommunity bridge is a natural controlled design choice; its sharp optimal placement genuinely changes with weight and graph size while internal epidemic thresholds are fixed. An exact classification and exact opposite SIS outcomes at fixed biological parameters are useful as nontrivial benchmarks for network spectral intervention and distinguish risk from degree ranking.

The dated certificate retains the supplied scientific assessment, sources and limitations.
