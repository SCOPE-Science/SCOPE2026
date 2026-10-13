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

# Verification instructions and limits

Run `python3 verify.py` with Python 3.10 or later; no third-party packages are required. The script constructs all 81 transfer states, checks all 89 allowed arcs, computes the cyclic strongly connected components, enumerates every directed simple cycle and vertex-disjoint cycle family, and checks the exact determinant coefficients over the integers. It then computes transfer traces through order 30, checks the closed generating function independently, performs complete direct vertex-subset enumeration for graph orders 5 through 10 (1,397,760 vertex subsets in total), verifies the formula for minimum cardinalities through order 100, and verifies three concrete shared-state witness cycles.

Successful completion prints:

`VERIFY_OK states=81 arcs=89 cyclic_SCCs=17+3+3 simple_cycles=6+1+1 exact_det=passed trace_n=5..30 brute_n=5..10 brute_subsets=1397760 minimum_n=5..100 exceptional_n=8`

The exhaustive vertex-subset checks are finite corroboration, not a substitute for the general transfer construction or the formal determinant identity. The determinant is certified using exhaustive finite cycle enumeration and is an exact identity for the 81-state matrix. Independent mathematical audit has not been performed.
