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

# Verification of the exact finite claim

The enclosed `certify.py` and `independent_replay.py` are standalone Python 3.10+ programs. Neither requires nonstandard packages, downloaded data, or external network access.

`certify.py` regenerates the \(504\)-symbol word from its three-letter substitution, derives all distinct factor occurrence supports, computes the full antichain of twelve minimal supports, counts all triple hitting sets by exact coverage-signature multiplicities, checks the four Cartesian boxes, and checks ten explicit invalid-witness triples. The resulting ten-factor sufficiency and necessity statements are deduced by a finite covering argument explained in `RESULT.md`.

`independent_replay.py` independently generates the word, assigns identifiers to all distinct factors, constructs per-position coverage integers, and directly enumerates all increasing triples. It also confirms the \(224\)-attractor previous-stage comparison and exact equality with the four-box family. This is an independent implementation of the *finite* computation, not an external mathematical audit.

Recorded program outputs are `certify_output.txt` and `replay_output.txt`; rerunning the scripts must reproduce all asserted values and terminate with `PASS`. The proof of the finite theorem relies on exhaustive enumerators with explicit exact ranges and loop invariants, not on sampling or extrapolation. No infinite-stage claim is made.
