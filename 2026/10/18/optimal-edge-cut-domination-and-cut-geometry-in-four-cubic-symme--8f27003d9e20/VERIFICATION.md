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
# Finite verification

The two C++17 implementations perform distinct complete searches: one enumerates selected edge subsets, and the other enumerates separating vertex bipartitions and all legal extensions. Their edge orders are deliberately different for two generalized Petersen representations; the standard-library checker maps edges back to unordered vertex pairs.

Required files: `edgecut.cpp`, `edgecut_partition.cpp`, `bruteforce.out`, `partition.out`, `certificate.json`, `verify_certificate.py` and `verification.out`. Compile both programs as described in `RESULT.md` and replay. The published `verification.out` is a reproducible record, not a substitute for running the checker. This verifier checks every listed optimum's defining properties and deletion-component sizes and independently validates every claimed automorphism mapping, verifying exactly the six orbit families.

**Proved limits:** all qualifying sets at and below the optimum are covered for precisely the four indicated labeled graphs. The monotonicity argument makes absence at one below each optimum sufficient to exclude smaller sets. No claim is made for any unenumerated larger graph, alternative cut convention, or unreviewed publication. Scientific publication priority and independent assessment remain unperformed.
