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

# Reproducible verification

Use Python 3 (standard library only) and execute `python verify.py` in this directory. The program reconstructs, for each odd \(r=3,5,\ldots,15\), the \(k=2^r-1\) differential indices and checks their branch valuations. It independently determines the characteristic-two Cartier targets, computes the stable set by iterating the partial-permutation graph, enumerates complete doubling orbits modulo \(k\), and compares them with a separate cyclic-bit adjacency predicate and with \(L_r-1\). A final consistency check compares each resulting cover rank with the genus bound.

The program printed `VERIFY_OK` after exact integer calculations. The computed quotient \(2\)-ranks for \(r=3,5,7,9,11,13,15\) are respectively \(3,10,28,75,198,520,1363\). These are finite cross-checks. The mathematical proof establishes the assertion for all odd \(r\ge3\) by a general Cartier formula and the transfer-matrix identity.

No independent audit or external verification is claimed. The historical completeness of the literature comparison, particularly broad treatments of three-point cyclic-cover ranks, is not formally certified.
