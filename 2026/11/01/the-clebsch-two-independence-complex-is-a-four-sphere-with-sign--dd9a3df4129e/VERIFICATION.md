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
# Verification

The complete reproducible verifier is `verify_clebsch.py`, using only Python 3 standard-library facilities. Run from the same directory with `python3 verify_clebsch.py`. The supplied `verify_output.txt` records the exact execution and ends with `ALL_CHECKS_PASS`.

It constructs two separately defined face lists (induced maximum-degree at most one and avoidance of all 160 wedges), checks equality over all 65,536 vertex subsets, produces the 1,065 pairs of the sequential element matching, verifies the complete directed face-incidence DAG, and independently checks original simplicial mod-two ranks. An exact signed incidence recursion produces the integer Morse matrix; a determinant of minus one for its first five columns supplies the key integral topological premise. Every one of the 1,920 graph automorphisms is explicitly constructed, checked for edge preservation and tested by signed chain traces.

Computational verification is exhaustive only for the single 16-vertex graph and its explicitly described finite symmetry group. The homotopy and quotient statements additionally use the standard discrete-Morse, Hurewicz, Whitehead, and rational finite-group invariants arguments set out in `RESULT.md`. Independent mathematical audit has not been performed.
