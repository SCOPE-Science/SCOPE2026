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

Run `python3 verify.py` with Python 3 and no third-party packages. This checks multiplication-table associativity for both five-element examples, exhaustive homomorphism cases for all loopless bipartite digraph targets on two and three labelled vertices and all loop-allowed input digraphs on at most three vertices, and oriented odd cycles through nine vertices. It also checks the three-level transitive-tournament criterion in the indicated finite range.

Observed output:

`VERIFY_OK bipartite finite targets: [14, 25] odd obstructions tested through size 9`

These tests are finite corroboration. The infinite family of critical odd-cycle obstructions, the finite-basis dichotomy, and the four-variable bound require the mathematical argument in `RESULT.md` and the cited general finite-basis theorem. No independent audit has been performed.
