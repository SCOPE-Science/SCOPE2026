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

The proof is fully analytic except for a finite, exhaustible 16-tree calculation, reproduced by the accompanying pure-Python `verify_square.py`. To run: `python3 verify_square.py`. It enumerates all spanning trees of the complete graph on the four square vertices; determines flow across each tree edge by exact rational cut sums; accounts for the \(\ell_1\) metric, including the two length-two diagonals; checks the seven sorted weighted-flow triples and multiplicities; checks that the smallest triple is \((1/4,1/4,1/2)\); tests both upper-bound cycle-elimination representations on 775 rational coefficient configurations with exact divergence checks; and verifies four exponent-specific numerical identities.

Successful execution returns:

`VERIFY_OK spanning_trees=16 distinct_profiles=7 exact_rational_cycle_tests=775 p_cases=4 global_continuum_proof_is_analytic=True`

The finite tree enumeration is exhaustive for four vertices, but the 775 grid configurations and four exponent checks are only additional diagnostics. They cannot establish the result for infinitely many coordinates and real exponents. The globally quantified upper bound follows instead from the exact two-representation combinatorial argument and concavity, and the equality for each \(p\) follows from the exhaustive, exponent-independent rational tree profile order. No independent audit or external certification has been performed.
