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

# Direct verification and scope

Run `python3 verify.py` with Python 3 (standard library only). The script enumerates every element of the antichain monoids for ten small finite field/poset choices, builds ordinary block-matrix multiplication tables, and independently tests whether an Otto witness exists in each direction for **every ordered pair**. It compares these answers against the projective-line tag criterion and checks the full class-size spectrum, idempotent count, and special-field equality criterion. It prints `ALL_EXACT_CHECKS_PASSED` if every assertion holds.

Fields tested: \(\mathbf F_2\), \(\mathbf F_3\), and \(\mathbf F_4\), the last represented by \(\mathbf F_2[x]/(x^2+x+1)\). Graphs include a one-edge graph, stars with two minimal neighbors, a disjoint two-edge matching, a four-edge complete bipartite graph, and a non-complete mixed-neighborhood example. The 64-element \(K_{2,2}\) instance over \(\mathbf F_2\) has class-size profile \(9\) classes of size \(1\), \(6\) of size \(5\), and one of size \(25\). The \(K_{1,1}\) instance over \(\mathbf F_3\) has classes of size \(2\) and \(7\) but only \(4\) idempotents.

The general theorem for arbitrary fields and graph sizes is proved by explicit scalar and vector equations; finite exhaustive tests are not a proof of infinite quantifiers. No independent audit or formal verification is asserted.
