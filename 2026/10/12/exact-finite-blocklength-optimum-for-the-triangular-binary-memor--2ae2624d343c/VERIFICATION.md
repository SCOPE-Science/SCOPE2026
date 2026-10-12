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

# Computational verification

Execute `python3 verify_pairs.py` and `python3 verify_transfer.py` in the directory containing those files. Both programs use only the Python standard library. The pair checker compares every pair of `111`-avoiding binary words at lengths 3–11 against the canonical-image equivalence criterion, and verifies the local replacement implication at lengths 3–8; it also checks the length-two boundary. The transfer checker computes the four-state count for lengths 2–100, compares it to the three-term recurrence and enumerates all allowed words directly through length 17.

Observed terminal markers: `PAIR_VERIFICATION_OK` and `TRANSFER_VERIFICATION_OK`. The independently obtained length-2-through-length-16 sequence is `3 5 9 17 31 57 105 193 355 653 1201 2209 4063 7473 13745`.

The all-length guarantee follows from the proof's replacement and canonical-equivalence lemmas and Cayley–Hamilton calculation. Finite exhaustive programs alone would not prove the infinite theorem. No formal proof-assistant validation or independent external scientific audit is claimed.
