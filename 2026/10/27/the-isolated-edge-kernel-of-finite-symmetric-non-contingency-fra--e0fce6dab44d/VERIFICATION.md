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

# Verification of the isolated-edge kernel theorem

Run `python3 checker.py` with Python 3.9 or later. The script uses only the standard library and systematically enumerates all labelled loop-free symmetric graph relations for \(1\le n\le6\), without heuristics or external data. It evaluates the primitive \(\Delta p\) at every vertex for every one-atom valuation; computes the canonical graph by deleting components isomorphic to \(K_2\); checks a unique one-step semantic signature per kernel; and compares every class with exact matching and coefficient counts.

Observed terminating output: `ALL_CHECKS_OK 66771`, with class totals \(1,1,5,55,959,31883\) at \(n=1,\ldots,6\). The six-vertex isolated-kernel distribution is \((s,C_{6,s})=(0,26864),(1,4368),(2,570),(3,80),(6,1)\).

The proof for arbitrary \(n\) does not depend on the checker. It requires: (i) exact characterization of one-step homogeneity functions by successor-set cardinality; (ii) recovery of all incident edges of vertices with at least two neighbours; (iii) the simple-graph fact that unrecovered edges form isolated \(K_2\) components; (iv) matching enumeration of the lifted graphs; and (v) the labelled exponential formula, already known for the univariate count. Those steps are supplied in `RESULT.md`.

No independent audit has been carried out. The known OEIS enumeration is credited as prior work, and prior general non-contingency bisimulation results are not claimed to be new. Exhaustive \(n\le6\) tests do not prove the all-size theorem.
