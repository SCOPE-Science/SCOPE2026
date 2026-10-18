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

# Reproducibility and exact checks

Run `python artifacts/verify_rook_pade.py` using Python 3 and SymPy. The included checker was executed from its actual file path and printed `VERIFY_OK exact checks: 255`.

The program independently forms the rational function and verifies both edge-orbit numerator identities over the symbolic parameters; checks the opposite-coordinate entry expression; verifies the strict negative witness identity; derives the exact Sturm endpoint sign patterns for every integer from seven through seventeen; and checks the root counts, witness inequalities and recovery inequalities for additional sample sizes.

It independently constructs the complete exact-rational diffusion update matrices for sizes two through six at four rational timesteps per size, comparing the matrix entries with the symbolic orbit formulas and checking exact row sums and positive diagonals. For the 36-vertex onset it evaluates rational sign witnesses at the steps \(1/3,2/5,4/5,6/5\).

The analytical proof in `RESULT.md` is necessary for the unbounded integer domain. Numeric root approximations and finite matrix tests are not presented as proof of statements beyond their checked ranges. This package includes no independent audit.
