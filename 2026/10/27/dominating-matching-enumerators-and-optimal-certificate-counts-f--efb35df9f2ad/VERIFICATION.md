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

# Verification procedure and limits

Use Python 3.10+ and SymPy 1.12+ and execute `python verify.py`. The checker constructs all 49 matching-compatible three-column states, all 147 domination-approved transitions, computes an integer potential by finite Bellman–Ford relaxation, verifies nonnegative reduced transition costs, and proves the four stated rational-matrix identities by exact symbolic arithmetic.

The independent brute-force portion selects edge subsets of each labelled prism with 3 through 9 columns, rejects pairs of edges sharing an endpoint, directly tests whether the selected endpoints dominate every graph vertex, and compares the entire polynomial with the independently built transfer matrix. It checks 35,425 valid dominating matchings in aggregate. A separate transfer recurrence checks the minimum-size coefficient through 30 columns.

The symbolic finite matrix computations establish infinitely many coefficients when used with the proof's exact state bijection and trace-log identity. Finite graph checks alone establish nothing for larger orders. The checks do not establish independent review, nor historical priority.
