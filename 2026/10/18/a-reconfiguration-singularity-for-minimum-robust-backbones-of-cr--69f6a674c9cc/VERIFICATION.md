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

The graph is reconstructed directly from its missing perfect-matching edges. Two supplied scripts were executed; the second imports graph routines from the first (these are reproducible finite checks, not an independent scientific audit): one computes actual connectivity and domination for each of 5,440 subsets of graphs with three to six matched pairs, while the other enumerates minimum feasible sets and all one-token replacements, separately calculating connected components and degree profiles for ten parameter pairs. The recorded `checks/output.txt` is from execution of the included code.

Commands after extraction at package root:

```
python checks/crown_conn_check.py
python checks/crown_reconfig_check.py
```

The scripts use only the Python standard library. They verify the finite instances shown in the log, not the theorem's infinite quantifiers; those are addressed by the constructive proof in RESULT.md. No independent scientific audit has been performed.
