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

# Verification of minimum zero-forcing starters in graph powers

Execute `python3 verify.py` in the folder containing the verification script. The `verification_output.txt` artifact is the resulting output from the script in this package, not a conjectural or simulated transcript.

The code directly constructs the adjacency graph of each path or cycle power. It computes the closure and parallel propagation time independently for each size-minimum vertex subset, compares the entire set family and time multiplicities, then checks the first-force minimum-degree lower bound. The tested profiles number 97; 115832 starting sets are tested, 2466 of them minimum zero-forcing sets, with 180 additional cyclic representation profiles. The output ends in `ALL CHECKS PASSED`.

A finite test cannot establish an infinite theorem, so the analytic first-force and interval arguments in `RESULT.md` are essential. The calculations do not address larger initial sets, other color-change rules, or independent review by a separate party.
