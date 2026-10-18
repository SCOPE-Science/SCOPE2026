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

# Exact computational checks

Run `python3 verify.py` with Python 3 and `sympy==1.14.0` as pinned in `requirements.txt`. The script reconstructs every graph vertex, graph edge, matching simplex and induced six-vertex octahedron without external data files. It constructs oriented simplicial boundaries and checks 110 zero boundary equations directly.

It enumerates every automorphism induced by permutations of the five Kneser symbols, confirms carrier orbit cardinalities 10/60/40 and omitted-center adjacency types 3/1/0 with uniform counts per omitted graph vertex, and checks ranks over three finite fields. Integer Smith reductions independently compute: 79 unit factors for the degree-three simplicial boundary; 80 unit factors after adding one sphere from each representative orbit; rank84 with invariant factors 83 units and 2 for orbit10; rank84 with all units for orbit60 and orbit40; and rank84 with all units for all 110 cycles together.

The finite-field calculations alone do not certify integral saturation. Exact integer Smith invariants and the presented free-quotient exact sequence do. This checks the finite graph only. There is no independent scientific audit or claim that searching proves absolute novelty.
