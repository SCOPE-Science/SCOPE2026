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

The proof is self-contained after the cited definitions of the Mayer path complex. The complete formal parameters are \(n\ge3\), positive layer sizes, \(N\ge3\), a primitive \(N\)-th root \(\xi\), and \(q=N-1\) over \(\mathbb C\).

To reproduce the independent finite tests, run `python3 verify.py` using Python 3 without third-party packages. The script constructs the boundary matrices from all allowed directed paths of lengths one and two, then derives invariant degree-two chains by a separate missing-shortcut kernel calculation. It checks homology dimensions, the rank of the canonical vertex-to-edge averaging map modulo boundaries, all specified quotient character tests, and the scalar holonomy character of the degree-zero quotient.

The executed checker ended with:

`VERIFY_OK cases=261 character_cases=205 vertices=2267 arcs=4102 two_paths=7888 omega2_basis_vectors=3786`

Computations use finite fields containing primitive roots of the tested orders; they are consistency tests rather than a proof over \(\mathbb C\). The mathematical proof in `RESULT.md` uses characteristic-zero tensor decompositions and covers all permitted parameters. Inaccessible full texts of two directly related indexed notes prevent ruling out all possible implicit overlaps.
