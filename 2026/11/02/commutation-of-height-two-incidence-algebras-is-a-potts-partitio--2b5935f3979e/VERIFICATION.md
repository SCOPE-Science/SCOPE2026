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

# Reproduction and limits

The self-contained `verify.py` has no third-party dependencies. From a directory containing this file and `verify.py`, run `python3 verify.py`.

The direct multiplication check constructs all elements of several small incidence algebras over the prime fields of orders two and three, evaluates both products entrywise, and counts commuting ordered pairs. A second independent check compares explicit \(q^2\)-colorings with all graph-edge subsets. A third checks Edmonds' two-forest rank numerically by enumerating possible red and blue forests rather than reusing the minimization expression. The saved verifier returned `VERIFY_OK 9 direct algebra cases, 16 independent color sums, 10 two-forest rank checks`.

These computations are finite checks; they are not exhaustive for arbitrary posets, arbitrary field sizes, or arbitrary vertex counts. The proof of the general statement is algebraic, and the forest-union interpretation cites the classical matroid-union theorem. Publication priority is not independently established.
