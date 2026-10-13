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

# Finite arithmetic replay

Run `python3 verify.py` from the directory containing this set of files. The test uses Python's standard library only, with independently generated greedy-permutation values and a separate least-prime-nondivisor record generator. It compares 2,949 turning-point records and checks translated primorial blocks for indices 3 through 6. For indices 3 through 7, it independently enumerates all record values up to the corresponding primorials to verify the residue-specific counting recurrence. From index 8 through 14, it uses only the short prime gaps to obtain an exact integer certificate for the large-index density difference.

The checker tests the displayed strict rational inequality using exact fractions, and verifies that the symbolic \(2p_{n+1}\) discrepancy bound holds against all integer counting points through \(P_7=510510\) (these are regression checks). The actual run output is embedded as `verification_output.txt`.

The infinite-density statements, tail estimate, and logarithmic error are established by the proof in `RESULT.md`, not by the finite tests. There is no independent audit.
