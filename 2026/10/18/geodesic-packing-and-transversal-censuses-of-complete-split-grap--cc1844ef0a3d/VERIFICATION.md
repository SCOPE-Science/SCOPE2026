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

Run `python3 verify_split_geodesics.py` with a Python 3 standard-library installation. The program reconstructs adjacency for each labelled complete split graph, enumerates shortest paths and removes non-maximal paths using contiguous-subpath testing. A disjoint-path dynamic program computes its entire packing-size distribution; an independent vertex-mask traversal counts every inclusion-minimal transversal. The executable compares both with the formula derived in `RESULT.md`, checks both scalar extremal parameters, and tests the packing–transversal gap.

Successful execution recorded:

`VERIFICATION_OK exhaustive_profiles=22 vertex_subsets=3592 packing_dp_states=15576 maximal_geodesics=414 arithmetic_profiles=5000`

Exhaustive cases have \(1\le r\le5\), \(2\le s\le6\) and \(r+s\le9\). Arithmetic cases have \(1\le r\le50\) and \(2\le s\le100\). These are finite checks, not an exhaustive verification of the infinite theorem. The symbolic proof is supplied in `RESULT.md`; independence and external certification are not asserted.
