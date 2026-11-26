---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The grand coalition gives positive utilities n+3, so an optimizer cannot have a zero utility. Splitting any disconnected coalition into components strictly improves every utility there (all removed co-members are enemies), hence only the grand coalition and tilings by proper arcs of lengths >=2 need be compared. The arc formula follows from two endpoint utilities n+2-s and s-2 interior utilities 2n+3-s; all legal length compositions can tile the cycle. Multiplication over arcs proves the recurrence and backtracking, with zero for impossible states. The finite table was independently reproduced by direct-utility subset DP (and arc DP): for n=11, proper 3269493248000 < grand 4049565169664; for n=12, proper and unrestricted optimum 154922431942656 > grand 129746337890625. The direct replay finds one optimizer at each n=4–11. For larger n, the even and odd near-halves comparisons each have an increasing first log term and a decreasing subtracted log term after k=6; their exact base comparisons are strict. This proves the threshold for all n, not by extrapolation. For each arc, endpoint utilities <=n give the term 2 log(2)/s in the logarithmic deficit, and the interior loss is at least (s-2)(s-3)/(2ns) for s>=3, with s=2 checked directly. The resulting lower bound is 2 log(2)/s+s/(2n)-5/(2n). Choose a nearest-integer number of nearly equal arcs to obtain all lengths 2 sqrt(n log 2)+O(1), where the endpoint and interior Taylor remainders combined are O(1/n). This gives the matching upper bound on optimal deficit. Completing the square gives a nonnegative arc excess (s-2 sqrt(n log 2))^2/(2ns). Its agent-weighted mean is O(1/n), while outside the prescribed relative window it is at least a positive epsilon-dependent constant times n^(-1/2). This establishes the uniform concentration assertion over optimizers.

## originality

PASS

The distinct finding is the exact breakup threshold and arc-product optimization, including asymptotic leading welfare deficit and concentration for the +n/-1 additive Nash objective on friendship cycles. Related sources match the game and objective, or the cycle and a different objective, or a Nash objective with different cardinal utilities. The closest inspected catalogue formulas give different transitions or different coalition structures under those changed rules.

## value

PASS

The cycle is a natural degree-two graph in the existing additive game model. Exact optimization shows a sharp switch from keeping all agents together to splitting, contrary to the adjacent egalitarian behavior, and explains at scale why optimal groups are neither bounded-size nor a macroscopic fraction of the cycle. The deficit and concentration identify the balance between losing a friend at arc endpoints and accumulating enemies in the interior; the transition is not merely a computed table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
