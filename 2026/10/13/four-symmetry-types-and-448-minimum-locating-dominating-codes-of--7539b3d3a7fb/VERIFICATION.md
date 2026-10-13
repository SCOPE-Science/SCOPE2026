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

# Verification of the exact Heawood code census
The finite proof uses the point–line incidence model \(p_i\sim\ell_j\) exactly when the binary dot product of \(i+1\) and \(j+1\) is zero. `verify.py` requires only the Python standard library and is executable with `python3 verify.py` in the same directory as this file.

Two implementations independently enumerate the \(\binom{14}{6}=3{,}003\) six-subsets, using respectively Python sets and fourteen-bit integer masks. Both accept exactly \(448\); every subset of smaller cardinality is rejected. The checker separately validates the canonical local incidence lists of sizes \(4,4,9\), constructs all \(168\) elements of \(\mathrm{GL}(3,2)\), checks the \(336\) induced graph automorphisms entrywise, and certifies the four orbit sizes \(28,84,168,168\). The Fano axiom that distinct points or lines meet uniquely is also checked.

The argument is finite and exhaustive for the fourteen-vertex graph, not a heuristic, sampling experiment, or result about arbitrary cubic graphs. No independent external audit has been performed.
