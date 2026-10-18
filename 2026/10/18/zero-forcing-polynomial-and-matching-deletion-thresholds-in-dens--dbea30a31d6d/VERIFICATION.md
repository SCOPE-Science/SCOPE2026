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

# Reproducibility

Run `python3 verify.py` with Python 3.9 or later. The program implements the color-change rule directly from an adjacency bitmask for each graph, without relying on a precomputed coefficient table. It also implements the mathematical occupancy prediction and asserts exact agreement for each initial white subset on all boards with \(3\le a,b\le7\) and all matching sizes \(0\le t\le\min(a,b)\).

The check covers 130 parameter profiles and 407040 total vertex subsets. The additional large-board loop checks all configurations with at most two whites on each side on three larger boards and four matching sizes each, totaling 60824 checks. It reports `VERIFICATION_OK` and the counts in `verification_output.txt`.

The finite checks exclude larger white-side configurations in the large-board loop deliberately; those are ruled out in general by the proof's first-decrease lemma, and the full small-board enumeration tests them directly. These checks do not constitute independent validation or certify the claim for infinitely many graphs.
