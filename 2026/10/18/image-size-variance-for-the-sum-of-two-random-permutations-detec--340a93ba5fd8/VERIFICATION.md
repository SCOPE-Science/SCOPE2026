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

# Checks and boundaries

Run `python verify.py` using Python 3.9 or newer, with no external dependencies. The check script independently constructs addition tables and element orders, enumerates every permutation in eleven finite abelian test groups of cardinality two through eight, computes image-size histograms and their exact rational moments, and directly checks joint absent-output probabilities against the theorem's coefficient extraction. It also enumerates forbidden rook positions in smaller cycle boards and checks the cycle-matching coefficient formula independently.

The completed run printed `PASS: 200 grouped exact identities; zero Monte Carlo estimation.` In particular, the order-four histograms are \((4,4,16)\) at image cardinalities \((1,2,3)\) for \(\mathbb Z/4\mathbb Z\), and \((4,12,8)\) at \((1,2,4)\) for \((\mathbb Z/2\mathbb Z)^2\), each over 24 equiprobable permutations.

Finite exact enumeration corroborates but is not an infinite-order proof. The general validity follows from the separately stated bijection, alternating-cycle decomposition and inclusion-exclusion. Full historical priority verification and any independent audit have not been performed.
