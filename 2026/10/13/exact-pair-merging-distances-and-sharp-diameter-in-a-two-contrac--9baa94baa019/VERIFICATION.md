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

# Reproduction

Run `python3 verify.py` in the directory containing this file and the accompanying standalone script. The script uses the Python standard library and no downloaded data. It constructs the *entire* graph of unordered state pairs for every integer \(n\) from \(5\) through \(120\). Reverse BFS from one-letter mergeable pairs gives exact shortest word lengths, independently of the proposed closed formula. It checks every such pair, both endpoint recurrences, monotonicity of each oriented cost, four critical starting phases per gap, and the displayed band and diameter formulas.

Expected successful output:

`VERIFY_OK n=5..120 pair_distances=287970 all_oriented_masks=checked monotonicity=checked four_phase_maxima=checked diameter=checked`

This finite experiment is not an exhaustive proof for arbitrarily large \(n\). The infinite proof uses the gap recurrence, symbolic parity solution, monotone Bellman potential and the finite symbolic four-phase maximum argument in the main result. No independent audit or external verification is claimed.
