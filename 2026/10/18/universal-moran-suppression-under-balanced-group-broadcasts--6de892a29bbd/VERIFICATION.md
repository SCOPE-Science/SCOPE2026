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

# Verification and limits

The standalone script `verify.py` requires Python 3 and SymPy. Execute `python verify.py` in a directory containing the file. It builds exact rational transition matrices for the specified parent-choice and whole-group copying process, solves the absorbing-chain fixation equations, and compares the resulting fixation probabilities with the complete-population Moran benchmark. It checks the equality case at neutral fitness and on pair-only networks, and verifies strict inequalities for advantageous and deleterious mutants whenever larger groups exist.

Successful executed checks comprise 330 nonabsorbing state/fitness combinations across a single whole-population hyperedge, a complete triple hypergraph, a cyclic triple hypergraph, a mixed-rank cycle with a four-person hyperedge, a pairwise-only cycle, and a positive-weight balanced mixed-rank example. The script also checks the local exact conditional-drift formula state by state and 294 rational instances of the signed hyperedge-defect lemma. The program was executed in the same environment as the record was prepared and returned PASS.

This verification is bounded finite testing. It is not a formal proof for arbitrarily large weighted hypergraphs, nor a replacement for the geometric-series and optional-stopping proof in `RESULT.md`. It does not establish results for irregular hypergraphs, majority replacement or arbitrary game payoffs. Independent scientific audit has not been performed.
