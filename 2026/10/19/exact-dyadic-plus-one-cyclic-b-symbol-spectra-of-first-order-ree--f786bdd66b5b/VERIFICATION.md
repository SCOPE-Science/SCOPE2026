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

# Reproduction and scope

Run `python3 verify_spectrum.py` with Python 3.10 or newer, without third-party dependencies. The checker enumerates every affine evaluation vector over the two-element field in both increasing-integer and reflected-Gray coordinate order for m=2 through m=9. For each m it directly counts all cyclic windows for each b=2^s+1, 0<=s<m, then compares the entire integer multiplicity map to the exact displayed formula.

The checker prints `RM_OK` for each dimension followed by `VERIFY_OK`. These finite exact enumerations corroborate the proof but are not an infinite certification. The proof's nonstandard input is the binary-carry transition count and its exact zero-run multiplicities; it is supplied in the `Proof` section of `RESULT.md`. The proof applies to all m>=2 and does not require a computational assumption. There has been no independent scientific audit.
