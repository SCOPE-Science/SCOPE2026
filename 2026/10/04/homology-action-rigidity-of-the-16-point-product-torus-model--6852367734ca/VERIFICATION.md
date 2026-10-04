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
The deterministic verifier `verify.py` reconstructs the 16-point product poset and checks the complete finite claim.

Checks performed:
- the displayed factor chains are 1-cycles;
- the two coordinate cochains are 1-cocycles on every strict 3-chain;
- their pairings with the cycles form the identity matrix;
- every order-preserving self-map is enumerated by exhaustive constraint backtracking;
- the total self-map count is 8,042,896;
- exactly 25 induced integral first-homology matrices occur;
- exactly 32 maps have nonzero determinant on first homology;
- exactly 32 maps are bijective;
- every rank-two matrix is a signed permutation matrix;
- the shear matrix with rows \((1,1)\) and \((0,1)\) is absent.

The homology rank-two identification uses the established fact that this finite model has the weak homotopy type of the torus. The exact enumeration itself is self-contained in the verifier. No claim is made for the other 16-point minimal torus model or for refinements/enlargements.
