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

# Verification notes

The exact proof needs no machine computation. The accompanying `check_cascades.py` program independently implements synchronous activation, counts final adopters from every single seed, and checks the independently derived component formula and equality types over all unlabeled trees of order 4 through 12. Executed with Python 3 and `networkx`, it passed 984 topologies and 11,000 seeded simulations; minima by order 4–12 were 7, 9, 10, 12, 13, 15, 16, 18, and 19 as total cascade sums. The proof for unbounded order is the connected-active-set argument, tree decomposition, degree-sum inequality, and explicit construction. The finite census makes no claim to exhaust trees of orders greater than 12.

The literature comparison assessed full public text of the primary 2002 model and the 2007 random-network analysis, available sections of the 2009 finite-network study and the 2017 algorithmic intervention study. None of those inspected passages states or implies the exact fixed-order tree minimization; this is not a claim of exhaustive bibliographic coverage. No external independent validation or certification has taken place.
