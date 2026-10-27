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

# Reproducibility and verification

The package contains `verify.py`, a standalone Python 3 script requiring only the standard library. It builds two perfect matchings explicitly on disjoint unions of even alternating cycles (including doubled-edge two-cycles), runs synchronous infection directly through each snapshot, and compares the resulting success counts by initial-cardinality with the independently calculated cyclic-gap polynomial. It also compares the success predicate with the theorem's gap criterion for every tested initial subset.

Run in the directory containing the extracted package files:

```sh
python3 verify.py
```

Expected output:

```text
VERIFY_OK schedule_graph_cases 648 initial_sets_checked 257976
```

A completed check tests 648 combinations of component structures and binary snapshot schedules of lengths from one to five, covering 257,976 initial subsets. The script does not assume that repeated consecutive snapshots change nothing; that consequence is tested by explicit simulation. It does not exhaust infinite families or verify the asymptotic random-seed limit. General correctness relies on the written interval and cyclic-composition proof; the stochastic result is proved by independent-block and union bounds.

Sources compared: Baste et al., arXiv:2609.29054v1 (full PDF inspected); Boyer et al., arXiv:1801.08910 (abstract and indexing inspected); indexed archive summary on temporal matching dynamics by K. Harish (full manuscript inaccessible). Priority is not independently certified.
