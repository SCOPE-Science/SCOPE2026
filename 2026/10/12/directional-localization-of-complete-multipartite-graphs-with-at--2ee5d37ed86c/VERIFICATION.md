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

The analytic proof is the primary verification. The standalone script `verify.py` independently models the game as a finite-state reachability problem. A state is the current contaminated vertex set. For each probe set it enumerates every response vector compatible with at least one candidate robber position, forms the surviving candidate set, and applies exact closed-neighborhood recontamination. Winning states are computed by backward fixed-point iteration.

The checker exhaustively tests every integer multipartition with at least three parts and total order at most eight. It verifies both \(\zeta_d^*(G)=1\) and \(\zeta_d(G)=\min\{\min_i n_i,3\}\). It also checks that the theorem's direct one-round partial-feedback probe constructions separate all robber positions.

The finite range is not exhaustive over all graph orders and is not used as an infinite proof. No independent audit has been performed.
