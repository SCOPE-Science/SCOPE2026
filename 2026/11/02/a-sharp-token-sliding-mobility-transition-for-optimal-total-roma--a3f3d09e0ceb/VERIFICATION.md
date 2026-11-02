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

# Reproduction and verification

Execute `python3 verify.py` using Python 3 without third-party packages. The program uses the literal adjacency definition of \(K(n,k)\) and constructs configuration graphs separately from the factorial formulas.

It enumerates all three-matchings and all permitted disjoint-replacement transitions for \(k=2\), \(6\le n\le10\). It checks every component and degree and compares total labeled state counts. It checks the **original total Roman predicate** against every three-defender assignment for \(k=2\), \(6\le n\le9\), including assignments that are not matchings. It independently verifies that the auxiliary Kneser graphs \(K(5,2)\), \(K(7,3)\), and \(K(9,4)\) are connected; it also checks the boundary factorial identity for \(2\le k\le14\).

Observed execution ended with `VERIFY_OK`. For \(k=2\), the component profiles for \(n=6,7,8,9,10\) were respectively \(15K_1\), \(105K_1\), \(105K_4\), one connected graph of order \(1260\), and one connected graph of order \(3150\). The respective degrees were \(0,0,3,9,18\). The auxiliary connectivity and boundary factorial checks all succeeded.

The analytic proof in `RESULT.md` is required for every integer parameter; these computations have only finite coverage. Independent audit has not been performed.
