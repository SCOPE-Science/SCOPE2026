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

# Verification of the double-cone rank recurrence

Run `python3 verify_double_independent_cone.py` using Python's standard library only. It constructs all labelled skew edge matrices for the specified graphs, performs independent Gaussian elimination modulo the indicated primes, and compares the resulting rank-half histograms against the three-branch recurrence. In the complete-bipartite cases, it also checks the rectangular rank formula by direct enumeration.

Actual complete enumerations: \(K_2\) bases at \(q=2,3,5\); \(K_{1,2}\) bases at \(q=2,3\); \(K_{2,2}\) base at \(q=2\); edgeless three-vertex base at \(q=3\); edgeless one-vertex base at \(q=5\). Each test checks the total number of edge assignments and the character degree-squared identity as an algebraic check on the odd-field multiplicity formula.

Recorded terminal success: `VERIFY_OK_DOUBLE_CONE 8 full edge assignment configurations`. In particular, the new \(K_{2,2}\)-edge extension over \(\mathbb F_2\) has rank-half histogram \((1,135,2376,1584)\) on all \(4096\) assignments, while the new \(K_{1,2}\)-edge extension over \(\mathbb F_3\) has \((1,368,6192)\) on all \(6561\) assignments.

**Scope of verification.** All tests are finite and run in prime fields; they are not exhaustive for arbitrary graph sizes or extension fields. The all-field recurrence is supported by the independently stated symplectic-block proof, not by extrapolating from this program. The complex-character formula is proved only in odd characteristic; characteristic-two rank checks test the linear algebra, not character theory.
