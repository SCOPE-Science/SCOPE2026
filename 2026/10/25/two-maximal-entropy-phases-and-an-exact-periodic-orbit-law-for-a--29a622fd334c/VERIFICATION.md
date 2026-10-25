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

The standalone `verify.py` runs using Python 3 with no third-party packages. It constructs the finite forbidden-pattern graph rather than reading a cached adjacency matrix, checks its exact component/edge list, and proves its integer characteristic-polynomial identities by arithmetic. The weighted identity is determined by 11 exact integer evaluations because each relevant polynomial coefficient has degree at most ten in the weight.

For periods 1–14 the checker independently enumerates the cyclic binary sequences. To test whether a periodic sequence contains an antisquare of any forbidden order, the tester considers orders 2 through \(2n-1\) for period \(n\). Indeed, an antisquare of order \(m\ge n\) forces symbolwise complementation by shift \(m\) at all residue classes modulo \(n\); the order can then be replaced by a congruent value in \([n,2n-1]\). Direct periodic tests agree with the forbidden-pattern graph and its trace counts.

Run: `python3 verify.py`. Expected final line begins `ANTISQUARE_GOOD_ZETA_PASS`.

This computational certificate proves the finite graph and determinant reductions used in the theorem. The reduction from unrestricted antisquare avoidance to the graph additionally uses the published minimal-antisquare and bi-infinite exceptional-word theorems, which are explicitly cited and inspected but are not independently reproved by code. The result has not received independent mathematical audit.
