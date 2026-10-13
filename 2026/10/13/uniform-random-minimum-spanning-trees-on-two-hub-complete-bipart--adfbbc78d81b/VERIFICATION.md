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

# Verification of the two-hub random minimum-spanning-tree law

The general theorem is established by a combinatorial characterization of every spanning tree of \(K_{2,n}\), exact minimization of the sum of selected real edge weights, and independence of the orientation and maximum of each independent exchangeable weight pair. These steps are analytic for all integers \(n\ge2\), with no unproved limiting step and no dependence on computational exhaustion.

## Finite exact checker

Run `python3 checker.py` from the directory containing the embedded Python file. Standard Python 3 suffices; no third-party modules or external data files are used. The checker enumerates all weight orders (not just random samples) on \(K_{2,2}\), \(K_{2,3}\), and \(K_{2,4}\). Counts are respectively \(4\) trees, each with \(6\) of \(24\) orders; \(12\) trees, each with \(60\) of \(720\) orders; and \(32\) trees, each with \(1260\) of \(40320\) orders. It checks every edge and pair of edges using exact rational arithmetic.

As an independent boundary comparison, the checker exhausts \(9!\) edge orders of \(K_{3,3}\), yielding \(81\) trees with unequal multiplicities \(4200,4680,4800\). These numbers demonstrate nonuniformity on a nearby graph. This is not an impossibility proof for all larger bicliques, nor is finite enumeration used to establish the all-\(n\) theorem.

Expected terminal marker: `EXACT_CHECKS_PASS`. The reported checker run was compared with the theorem's symbolic probability formulas. No external or independent scientific audit has been performed.
