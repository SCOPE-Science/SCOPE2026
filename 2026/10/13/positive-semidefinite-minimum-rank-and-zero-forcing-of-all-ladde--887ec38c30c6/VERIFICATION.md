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
# Reproducibility and limits

Run `python3 verify.py` using Python 3 without third-party packages. The verifier builds the ordinary ladder from its edge list and calculates graph powers by breadth-first search. Separately it constructs the proposed two-dimensional sliding-window Gram factor, verifies exact agreement of every off-diagonal zero/nonzero entry with the independently generated power graph, checks a maximum-size nonsingular minor using integer arithmetic modulo a prime, and verifies that the first \(k\) columns force all remaining vertices.

The complete run used 130 profiles with \(1\le k\le10\) and \(k+1\le\ell\le k+13\). Another 12 small profiles were independently checked by exhaustive enumeration of all starting sets of cardinality below \(2k\). Actual output is preserved in `verification_output.txt`, which reports `ALL CHECKS PASSED`. The combinatorial proof handles every \(k\ge1\) and \(\ell\ge k+1\) without dependence on the tested range.

The Gram factor proof uses signed dot products to force exactly the graph-power support, not only a graph superpattern; its full-row-rank minor is explicit. It proves a universal positive semidefinite nullity lower bound, complemented by the forcing upper bound. No finite test is represented as an infinite certificate. No claim of external independent verification is made.
