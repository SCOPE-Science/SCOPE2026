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
# Verification record

A self-contained script `verify.py` constructs the clique windmill's graph adjacency directly. It computes all nonempty defensive alliances by vertex degree inequalities; for each candidate, a dynamic subset test detects whether **any** proper nonempty defensive subset exists. Exact set masks and cardinality distributions are independently compared with the classified family.

Across 136 ordered profiles of two to four blades, with blade sizes among \(2,3,4,5\) and at most 12 total peripheral vertices, the script examined exactly 537,880 nonempty vertex subsets and found 6,023 globally minimal defensive alliances, all matching the theorem. The script further checks 42 uniformly even/odd parity profiles, with \(2\le r\le7\) and \(1\le k\le7\). Run with `python verify.py` using Python 3.8+; no additional packages are required. The stdout from an actual execution appears in `verification_output.txt`.

These computations are finite corroboration. They establish no exhaustive result beyond the specified finite test profiles, and no bibliographic novelty or independent audit conclusion. The unrestricted classification is proved in `RESULT.md`.
