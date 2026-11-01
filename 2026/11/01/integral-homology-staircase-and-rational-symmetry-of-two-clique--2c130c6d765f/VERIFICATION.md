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
# Reproducibility and limits

Run `python verify.py` for independent enumeration of graph cliques and forbidden-clique faces, binary simplicial boundary ranks, and signed Lefschetz character comparisons. Run `python verify_integral.py` with SymPy installed for exact integer signed-boundary Smith normal forms.

Checks actually executed: 11 mod-two Betti computations, 492 finite signed Lefschetz comparisons, and four exact integral Smith-form homology computations. They all passed. The two files are standalone; neither imports or depends on the other. Their bounded test cases do not prove the infinite-family formula. The proof of the formula is the integral filtration and degree-support argument in RESULT.md. No independent audit or external proof certification has been performed.
