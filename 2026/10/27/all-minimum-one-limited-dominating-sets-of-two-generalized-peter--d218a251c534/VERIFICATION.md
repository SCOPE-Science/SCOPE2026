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

# Reproduction

Place `verify.py` in the same directory and run `python3 verify.py` on Python 3 without third-party libraries. The program rebuilds every candidate transition from the two local neighborhood equalities, independently computes strongly connected components, verifies that every cyclic component is a simple directed cycle of the asserted size, and checks exact directed-closed-walk counts for selected larger orders. Its separate brute-force traversal checks all two-class labellings of the original graph for several small orders. A successful complete run prints `VERIFY_OK`.

The global conclusion follows from the bijection between all cyclic length-\(n\) walks and all labelled minimum sets, together with exhaustive finite-state enumeration. The direct small-order enumeration alone is not used to justify the result for arbitrary \(n\). The finite enumeration has \(16\) or \(256\) states and tests \(4\) successors per state. There is no numerical floating-point tolerance or solver dependency.

# Boundaries

The proof and checker use \(n\ge3\) for \(k=1\), and \(n\ge5\) for \(k=2\), ensuring that inner predecessors/successors and outer predecessors/successors are distinct. Counts refer to labelled subsets, including both a set and its complement. An external independent audit has not been performed.
