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

# Reproducible checks and scope

Use Python 3.9+ (standard library only). Execute `python verify_direct.py` and `python verify_templates.py` with both scripts in the same working directory; there are no downloads, random seeds, external dependencies, or input files.

`verify_direct.py` builds the circular ladder as an explicit 2-row adjacency-bitset graph. For each integer \(6\le n\le11\) it checks *every* subset of size \(n-1\) for infeasibility, checks *every* subset of size \(n\) for connected domination, and forms every one-for-one exchange from the resulting minimum sets. It checks the exact \(2n^2+2\) vertex count, connectedness, degree distribution and \(4n(n+2)\) edges; success ends with `DIRECT_ALL_SUBSETS_AND_EXCHANGES_PASS`.

`verify_templates.py` constructs all A/B/C families directly from the definition for each \(6\le n\le38\). It enumerates all selected/omitted single-vertex swaps, confirms that the full neighbor set of every configuration equals the seven-case symbolic exchange table, checks edge reciprocity, connectedness, cardinality, exact degree polynomial, and edge count. Success ends with `ALL_ADJACENCY_RULES_AND_CONNECTIVITY_PASS`.

These are two finite exact cross-checks on independently represented objects. For the unbounded range \(n\ge6\), the mathematical proof's connectivity, empty-column restriction, family classification and exhaustive exchange-case analysis establish the result. The checks do not prove every unbounded case by enumeration, and independent validation is not represented.
