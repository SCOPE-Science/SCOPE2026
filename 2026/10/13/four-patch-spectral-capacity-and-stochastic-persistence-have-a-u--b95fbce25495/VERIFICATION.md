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
The claim concerns the continuous-time finite patch-occupancy chain with unit independent local extinction rates and per-neighbor colonization rate \(\lambda>0\), starting from all patches occupied.

`verify_metapop_spectral_discordance.py` reconstructs the full Markov generator from the four specified graph edge sets and computes exact automorphism quotients of dimensions \(11\), \(5\), \(7\), and \(9\). Every orbit member is checked to have identical rates to the quotient classes.

Each closed rational extinction-time formula is tested by exact Cramer polynomial determinant identities, not merely by interpolation or sampling. The two key difference factorizations are verified as exact polynomial equalities, as are adjacency characteristic polynomials. The unique-root proof checks positivity of all denominator coefficients, precisely one sign change of the crossing polynomial, and strict integer signs at the rational isolating endpoints.

As an independent numerical implementation check, the complete \(15\)-state (unlumped) chain is solved by exact rational Gaussian elimination for each graph at three positive rates. Connected unlabeled simple graph types are exhaustively generated under vertex permutations for every fixed order/link-count stratum through four vertices, establishing the claimed finite minimality.

Run from the folder containing the script:

`python3 verify_metapop_spectral_discordance.py`

The first output line must be `VERIFY_OK`. This is an exact finite algebraic certificate; it does not assert broader ecological persistence rankings outside the defined model.
