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
The proof is analytic. For \(G_{a,b,t}\), the four contributions are:

1. \(ab-t\) surviving cross edges, each with one geodesic.
2. \(t\) deleted cross pairs, each with \((a-1)(b-1)-t+1\) length-three geodesics.
3. Same-side pairs in the \(a\)-part, totaling \(b\binom{a}{2}-t(a-1)\).
4. Same-side pairs in the \(b\)-part, totaling \(a\binom{b}{2}-t(b-1)\).

Adding these terms and the \(a+b\) zero-length geodesics gives the claimed formula. The difference from the \(t=0\) case is exactly \(t(C-t)\), so the optimizer is the nearest allowed integer to \(C/2\).

The attached verifier independently constructs each graph, performs breadth-first search from every vertex, counts shortest paths dynamically, and sums over unordered pairs. It checks every \(3\le a,b\le8\) and every \(0\le t\le\min\{a,b\}\), plus the balanced transition through \(n=8\). A successful replay prints:

`ALL CHECKS PASSED; parameter_cases=199; a,b_range=3..8; balanced_n_range=3..8`

The finite replay is a stress test only; no finite enumeration is used to justify the universal quantifiers.
