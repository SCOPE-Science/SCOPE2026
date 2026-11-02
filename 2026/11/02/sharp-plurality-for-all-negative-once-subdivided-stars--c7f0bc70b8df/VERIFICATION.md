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

# Verification of the all-negative subdivided-star plurality

The finite verifier uses the original negative-edge influence sum and a strict-majority spread followed by a single legal ignition. It enumerates all labelled reachable states of the original graph for arm counts \(1\) through \(6\), then independently enumerates every arm-permutation orbit for arm counts \(3\) through \(60\). It also replays the four-round achieving schedule, checking each ignition remains legal. Run `python3 verify.py` from the directory containing the file.

The inspected output was:

```text
DIRECT_ALL_LABELLED_PROCESSES_OK 1 13 6 2
DIRECT_ALL_LABELLED_PROCESSES_OK 2 69 14 3
DIRECT_ALL_LABELLED_PROCESSES_OK 3 317 38 5
DIRECT_ALL_LABELLED_PROCESSES_OK 4 1345 114 6
DIRECT_ALL_LABELLED_PROCESSES_OK 5 4855 242 7
DIRECT_ALL_LABELLED_PROCESSES_OK 6 17221 726 8
ARM_ORBITS_AND_EXPLICIT_WITNESS_OK 3 71 12 5
ARM_ORBITS_AND_EXPLICIT_WITNESS_OK 4 115 16 6
ARM_ORBITS_AND_EXPLICIT_WITNESS_OK 5 153 18 7
ARM_ORBITS_AND_EXPLICIT_WITNESS_OK 10 361 34 12
ARM_ORBITS_AND_EXPLICIT_WITNESS_OK 20 771 64 22
ARM_ORBITS_AND_EXPLICIT_WITNESS_OK 40 1591 124 42
ARM_ORBITS_AND_EXPLICIT_WITNESS_OK 60 2411 184 62
VERIFY_OK
```

The computation is not an infinite proof. The all-parameter upper bound follows from the round-indexed classification of doubly yellow arms in `RESULT.md`; the lower bound follows from the exact four-round construction. This verification does not assess historical priority or independent mathematical certification.
