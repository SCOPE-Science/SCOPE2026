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

# Reproduction of the finite certificate

From this directory run `python3 verify.py` (Python 3.9 or later, standard library only). It constructs every binary unbordered word beginning in `0` and ending in `1` through length 10, tests all pairwise compatibility conditions, and performs the cardinality and minimum-total-length clique searches with provably safe upper and lower bounds. Every returned word set is explicitly checked. Its final line is `VERIFY_OK binary lengths 2..10, exact maximum sizes and minimum total codeword lengths`. All exact optimum values and witnesses are serialized in `WITNESSES.json`.

For order ten the source enumerates 295 candidate words. A separate mixed-integer 0–1 optimization using the same exact forbidden pair constraints produced optimum total length 227 (solver reported zero optimality gap), corroborating the standalone branch-and-bound implementation, but that external package is not needed to verify the claim. Finite verification makes no assertion about unbounded word lengths or absolute novelty. Independent scientific audit has not been performed.
