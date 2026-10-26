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

# Verification

Run `python3 artifacts/verify.py` with the Python standard library. It computes all reachable subset images using zero-one BFS, with a-cost zero and b-cost one, and separately enumerates all permutations of candidate deletion sites. For all 3048 automaton/target instances with 2 <= n <= 8, it compares the exact schedule count with the multinomial theorem and checks the optimal number of b letters. It also scans every cardinality in the coprime regime for the sharp envelope and replays the resource-minimal reset witness. Expected final line: `VERIFY_OK 3048 subset/automaton cases`. No search beyond n=8 is claimed; the proof in RESULT.md establishes the universal statements. Independent audit: not performed.
