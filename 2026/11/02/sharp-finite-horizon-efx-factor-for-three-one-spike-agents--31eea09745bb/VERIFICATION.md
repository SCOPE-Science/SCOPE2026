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

# Verification record

The proof establishes an infinite family of exact online minimax values analytically. The included `verify_one_spike.py` implements the policy and a second, separately structured minimax recursion. With Python 3 and no external dependencies, run `python verify_one_spike.py`.

Observed results from the extracted Python source: 14,175 high-occurrence triples for all horizons from 6 through 15, each tested at four heights, satisfy the claimed lower bound and the singleton-recipient and nonempty-bundle invariants. Independent exact recursive minimax matches the upper bound at horizons 6 through 10, for the first integer height above the sufficient threshold. The mathematical result for all horizons is not inferred from these finite tests. No Lean proof, expert certification or independent audit was undertaken.
