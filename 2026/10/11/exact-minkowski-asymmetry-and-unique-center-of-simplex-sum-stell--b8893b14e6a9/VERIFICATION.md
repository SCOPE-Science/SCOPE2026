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

# Reproducible checks and limits

The accompanying `verify.py` uses Python 3.9+ and only the standard library. Run it with `python verify.py`. It constructs all \(2^k-1\) summand simplices explicitly for each \(1\le k\le6\), computes exact subset minima and maxima, and uses rational arithmetic to check both Minkowski containment inequalities at the displayed center. It also generates all \((k+1)!\) coordinate-order greedy vertices and checks the image of each under the proposed reflection-contraction against every subset inequality. The executed check passed for every tested dimension: 5,912 greedy orders and 252 independent center subset tests, as well as all reflected-vertex subset tests.

As a separate additional check, numerical linear programs with independent variables \((s,(s+1)c_0,\ldots,(s+1)c_k)\) optimized the complete subset containment system for \(2\le k\le7\). These optima agreed with the displayed rational ratios to numerical tolerance. Those numerical LP comparisons are not part of the dependency-free verifier; they are supporting evidence only.

The exact proof in `RESULT.md`, rather than finite enumeration, establishes the formula and uniqueness for every integer \(k\ge1\). The proof does not extend to other graph-associahedron realizations. No independent scientific audit or priority certification has been conducted.
