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

# Verification evidence and limits

Run `python3 verify.py` from this directory. The script has no third-party dependencies and constructs the edges of the five-vertex obstruction directly. It enumerates all \(12\) proper three-colour assignments and checks that an explicit preference profile produces a mutually envying adjacent pair in every assignment. It enumerates all \(7776\) named strict three-colour profiles, compares two separate directed-cycle detectors (three-state DFS and Boolean transitive closure), and verifies the exact counts \(624\) (no stable colouring), \(576\) (all proper assignments have mutual envy), and \(48\) (no stable assignment but some proper assignment with no mutual pair). It also checks the orientation reachability bound on a bounded set of graph parameters.

The general theorem for every \(m,r\) is justified by the structural orientation and induced-subgraph proof in `RESULT.md`, not by extrapolating finite orientation tests. The finite profile counts are exhaustive because every one of the \(6^5\) preference profiles and every one of the \(12\) proper colour assignments is enumerated. Neither code reuse nor the two local cycle tests establishes independent mathematical auditing; independent audit has not been performed.
