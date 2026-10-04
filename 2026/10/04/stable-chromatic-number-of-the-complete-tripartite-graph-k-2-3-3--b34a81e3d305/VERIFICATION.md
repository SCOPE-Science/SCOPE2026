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
# Verification

The claim is \(\chi_{\mathrm{stable}}(K_{2,3,3})=6\).

For the upper bound, the proof uses the published reachability theorem and the explicit acyclic orientation \(C\to B\to A\).  Direct traversal gives reachable-set sizes \(1\) on \(A\), \(3\) on \(B\), and \(6\) on \(C\).

For the lower bound, `artifacts/certificate.json` contains the five-color preference profile and one blocking cycle for every proper coloring.  `artifacts/verify.py` does not trust a precomputed list of proper colorings: it enumerates all \(5^8=390625\) vertex-color maps, tests the graph edges directly, reconstructs the envy relation from the rankings, and checks acyclicity.  It finds exactly \(2940\) proper maps and zero stable maps.  It separately checks that the certificate has exactly \(2940\) unique entries and that every listed directed cycle consists of actual envy arcs for its coloring.

Run:

`python3 artifacts/verify.py`

Expected output:

`ALL CHECKS PASSED; proper_5_colorings=2940; stable_5_colorings=0; blocking_cycles=2940; orientation_max_reach=6`

The finite verification proves only the displayed five-color obstruction for this graph.  No extrapolation to other multipartite graphs is made.
