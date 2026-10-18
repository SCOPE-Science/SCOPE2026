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

# Reproducibility of the two-root Hamming graph classification

The mathematical derivation in `RESULT.md` is an all-parameter proof. Three separate executable standard-library Python tests checked its statements over finite regimes. Running commands from a directory containing the scripts:

```
python3 verify_direct.py
python3 verify_quotient.py
python3 verify_metric_boundary.py
```

`verify_direct.py` independently constructs labelled vertices and all Hamming graph edges for \(q=2\), \(1\le d\le8\); \(q=3\), \(1\le d\le6\); \(q=4\), \(1\le d\le5\); and \(q=5\), \(1\le d\le4\), for every allowed marked distance. The 82 cases total 18,903 vertices, and every stable colour class matches exactly one asserted orbit type. It independently checks the neighbour statistic and distance-pair collision condition. Observed output is recorded in `direct_run.txt`.

`verify_quotient.py` builds a weighted adjacency transition system directly from the coordinate type calculus, rather than enumerating graph vertices. It checks 1,026 cases for \(2\le q\le7\), \(1\le d\le18\), and each \(1\le t\le d\), comprising 174,420 orbit profiles cumulatively. It compares stabilized colour classes and type counts. Observed output is recorded in `quotient_run.txt`.

`verify_metric_boundary.py` independently enumerates possible integer coordinate profiles over 2,646 cases for \(2\le q\le8\), \(1\le d\le27\), and all \(1\le t\le d\). Exactly the 1,950 cases predicted by \(q\ge3\), \(2\le t<d\) contain a distance-pair collision; the explicit witness profiles were also checked. Observed output is recorded in `metric_run.txt`.

No exhaustive computation over unbounded \(d\) or \(q\) is claimed. The infinite assertion follows from the elementary coordinate and equitable-partition proof in `RESULT.md`; no independent expert or external audit has been performed.
