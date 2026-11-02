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

The theorem is established for arbitrary positive \(a,b\) by an exact best-response analysis: all action profiles are partitioned by whether each of the two community magnetizations is zero, and no case is omitted or counted twice. The nonzero/nonzero case has exactly two complementary profiles when the role-imbalance signs agree; each single-tie case contributes all and only the nonbalanced profiles in the free part; the double-tie case contributes the product of the central binomial coefficients. Separate algebra gives the extremal role assignments and the fair-random-role probability.

The standalone script `verify_bipartite_equilibria.py`, requiring only Python 3.9+ standard libraries, independently evaluates the two available payoff options for each vertex and tests every binary action profile for sizes \(1\le a,b\le5\) and every coordinator-count pair. A successful run prints four `PASS` lines covering 400 composition counts, 102400 binary profiles, 25 extrema/existence checks, and 25 exact-rational probability checks. Finite enumeration verifies those cases only and does not establish the universal theorem; the mathematical proof is in `RESULT.md`.

No independent external audit or formal theorem prover verification has been carried out. The stated scientific priority is based on inspected sources rather than a certified exhaustive bibliography. The result assumes weak tie behavior, threshold \(1/2\), and unit-weight complete bipartite networks.
