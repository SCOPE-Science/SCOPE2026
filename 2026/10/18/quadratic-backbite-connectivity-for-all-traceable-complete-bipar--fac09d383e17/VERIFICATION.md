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

The proof reduces each class of Hamiltonian path to a pair of permutations and identifies individual backbite generators explicitly. A standalone independent local-move checker enumerates the actual endpoint reversals and verifies them against generator formulas for selected orders; it then verifies the pure adjacent-transposition macros and constructs sorting sequences with bounded length for sampled paths. Invoke `python3 verify.py` in a local directory containing the extracted script.

Proof-dependent identities are written in RESULT.md and are valid for all specified integer parameters; exhaustive computation across a finite parameter range is corroborative rather than an infinite proof. No external oracle or independent certification is claimed.
