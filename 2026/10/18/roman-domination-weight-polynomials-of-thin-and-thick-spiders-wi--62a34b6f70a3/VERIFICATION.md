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

# Independent reproducibility from included data

Run `python verification.py` with Python 3 (standard library only). The script has a deterministic random seed for constructing mixed finite cases. It constructs spider adjacency from the definition, independently generates every vertex labeling, checks each zero for a neighboring two, tallies weights in exact integers, and compares the vector against algebraic polynomial recurrences. The saved exact terminal output is `verification_output.txt`.

264 checked graph instances contained 8,244,702 possible labelled functions. Additional polynomial-degree and minimum-multiplicity tests covered the empty-head thin and thick families for \(2\le n\le9\). In each case the number of possible labellings, not the number of valid Roman labelings, is counted in the total. Every checked coefficient was exact; no stochastic mathematical inference is used.

The exhaustive experiments are finite and do not prove the all-head, arbitrary-order identities. The unrestricted proof is the case partition in `RESULT.md`; the published graph-decomposition theorem supplies the recursive structural class. The material was checked in the present review only. Independent validation has not been performed.
