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

# Reproduction of exact computations

Run `python3 verify.py` in the directory containing this file and the stand-alone checker. No network access, data files, or third-party packages are needed.

The checker calculates the scaled discrepancy \(d_i=Q(L_i-P_i)\) in exact integer arithmetic. It tests all transitions of the eight sorted three-machine states, for all four nonsingleton eligibility choices and all tied greedy recipients. This verifies closure of a stated finite *inductive invariant*, rather than claiming any finite test directly proves an infinite theorem.

For four machines it enumerates every possible eligibility choice of cardinality 2–4 and every tied minimum-discrepancy response through four arrivals. Its exhaustive state counts, from horizon zero through four, are `(1, 28, 187, 617, 1405)`, and every enumerated discrepancy is at most `12`. Singleton eligibilities leave discrepancies invariant, so this includes arbitrary four-item streams with singleton chores.

It next checks each branch in the printed five-item adaptive adversary and separately performs an exact recursive minimax check with all eligible subsets and all recipients, returning forced-failure results `[False, False, False, False, False, True]` at horizons 0–5. The explicit adversary is independently proved by its complete two-branch tree in the theorem. Finally the verifier sanity-checks the algebraic inequality \(2/n+1/2<1\) over representative \(n\ge5\); the complete all-integer assertion follows symbolically from \(n>4\), not from those finite samples.

The reviewed proof assumes deterministic irrevocable assignment under an adaptive adversary. The verifier does not assess other fairness notions, varied processing times, randomized algorithms, or historical priority. Independent audit is not performed.
