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
# Verification

Run `python octahedral_two_point_verify.py` with SymPy. The program exhaustively builds all 15 vertices, 48 edges, and 30 squares of the unordered two-point cubical model of the octahedral graph. It checks both signed boundary maps, rank and Smith invariants, four signed opposite-face torus cycles, a determinant-one integral minor, all 48 graph automorphisms as chain maps, and the full ten-class character and rational irreducible decompositions.

Exact computations executed successfully from the included verifier; no floating-point arithmetic or random sampling is used. This certificate proves only the finite algebraic and combinatorial steps. The identification with the continuous graph configuration space relies on the Prue–Scrimshaw theorem and its verified subdivision hypotheses. The originality comparison does not guarantee completeness of unindexed mathematical literature. No independent scientific audit has been performed.
