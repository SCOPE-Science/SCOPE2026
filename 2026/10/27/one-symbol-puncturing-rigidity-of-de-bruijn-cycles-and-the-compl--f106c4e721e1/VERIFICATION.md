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

Run `python3 verify.py` in the same directory. The checker uses only Python's standard library. It generates and rotation-canonicalizes every candidate full cycle and shortened cycle for \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1)\), testing all cyclic length-\(n\) windows directly.

It independently tests (i) the equivalence between successful indexed deletions and membership in a constant length-\(n\) window; (ii) exactly \(qn\) successful positions for every full cycle; (iii) the coincidence between the set of all near-universal cycles and the set of successful deletion outputs; and (iv) the classical full-cycle count and predicted near-universal count.

The check completed with these seven PASS lines: for binary orders \(1,2,3,4\), the numbers of full cycles are \(1,1,2,16\) and shortened cycles \(2,2,4,32\); for ternary orders \(1,2\), the corresponding pairs are \((2,3)\) and \((24,36)\); for alphabet size four, order one, they are \((6,8)\). These are exhaustive only for the listed finite cases. The proof of the infinite theorem uses the balanced-edge argument, insertion multiplicity, and the established de Bruijn enumeration formula. The public result neither assumes nor claims an independent mathematical audit.
