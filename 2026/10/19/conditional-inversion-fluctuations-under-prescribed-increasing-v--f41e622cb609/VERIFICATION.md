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

# Verification evidence
The included `verify.py` requires only the Python standard library. Run `python verify.py` in a directory containing the extracted file. It enumerates all order-2 through order-7 permutations and all possible prescribed succession subsets, independently computes the weighted-block permutation distribution, and checks exact rational mean and variance identities. It also checks single-run positional extremizers and several larger block examples. The actual execution reported `PASS: 505 exact assertions`.

The unrestricted theorem is established analytically by the bijection and an exact orthogonal decomposition. The script is corroborating evidence, not an infinite certificate. Independent audit has not been performed.
