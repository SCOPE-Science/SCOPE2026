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

# Exact verification

Run `python3 verify_binary80.py` without external dependencies. The companion `verify_binary80.out` records a successful full run. The code constructs all 252 source inputs, tests distinctness, replays all 251 greedy merges while independently calculating the global live maximum and checking noncontainment after each merge, and independently constructs a 259-character common superstring by an Euler tour. Its cross-bifix-free code test covers all 17-squared codeword pairs and all nine proper overlap lengths. It then checks all 63,252 ordered pairs of distinct binary inputs, each selected encoded merge, all 252 contained binary inputs, both exact output lengths, and the ratio. A direct spacing argument in RESULT.md proves the 2,590 lower bound for every common superstring; the finite checker confirms all premises of that argument.

Independent mathematical review and exhaustive historical priority verification have not been performed. SHA-256 values are reproducibility checks only.
