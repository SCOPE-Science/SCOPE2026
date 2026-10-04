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
The analytic proof was reconstructed from the definitions. Its critical step is that for distinct \(x,y\in V_i\), every shortest path is \(xzy\) with \(z\notin V_i\), so \(M\)-visibility holds exactly when an internal vertex exists outside both \(V_i\) and \(M\).

The standalone program `verify.py` does not assume this criterion. It constructs each graph, computes unrestricted shortest distances by breadth-first search, recomputes shortest distances while forbidding \(M\) as an internal-vertex set, tests every nonempty subset against the dual/outer/total definitions, and uses exact bitmask dynamic programming to find the least valid partition.

Its finalized output is `ALL CHECKS PASSED; multipartite_types=87; invariant_cases=261; max_order=9`.

The computation is exhaustive only through order \(9\). It is a finite stress test, not an infinite proof; the universal quantifiers are established by the analytic argument.
