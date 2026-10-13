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
# Finite verification and reproducibility

Run `python3 verify.py` from a directory containing `verify.py`; Python's standard library suffices. The script rebuilds the disjointness adjacency matrix for each graph, independently constructs the six labeled supports from three perfect matchings, and checks the full rainbow-neighborhood union and total weight for every \(4\le n\le15\), \(3\le k<n\). It then enumerates **all** subsets of fewer than \(2k=6\) vertex-color incidences for \(KG(4,2)\) and \(KG(5,2)\), both with \(k=3\), rejecting 12,616 and 174,437 assignments respectively. Multiple colors per graph vertex are naturally included in incidence-subset enumeration. The tests assert the complete count of incidence subsets at each weight, rather than relying on sampled assignments.

The observed output, stored in `verify_output.txt`, is:

```
exhaustive n=4 k=3 minimum=6 rejected_below=12616
exhaustive n=5 k=3 minimum=6 rejected_below=174437
construction_checks=78 exhaustive_rejected=187053
VERIFY_OK
```

The infinite lower bound rests on the counting and two-spoke obstruction in `RESULT.md`, not on these finite cases. These checks are not a formal machine proof, independent audit, or certification of historical originality.
