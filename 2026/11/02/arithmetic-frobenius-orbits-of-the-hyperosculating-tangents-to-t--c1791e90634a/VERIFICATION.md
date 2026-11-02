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
# Verification of the characteristic-three hyperosculation orbits

Run `python3 verify_klein_frob.py` using Python 3.8 or newer. No third-party packages are required. The script checks irreducibility of the chosen degree-six polynomial by all possible divisors of degrees at most three, then verifies multiplication and exponentiation in \(\mathbb F_{729}\). It independently evaluates the original equation \(X^3Y+Y^3Z+Z^3X=0\) and the local cubic tangency condition for all nonzero candidate parameters, identifies exactly 28 hyperosculations, verifies their tangent lines are pairwise distinct, classifies element orders as \((1,6,3,18)\) at orders \((1,7,13,91)\), and computes all Frobenius orbit lengths. It also checks the rational-count formula for extension degrees 1 through 12.

Expected final marker: `KLEIN_CHAR3_HYPERFLEX_28_ORBITS_1_3_6_6_6_6_F729_PASS`.

**Limits.** The finite test proves the asserted identities within \(\mathbb F_{729}\), but the mathematical proof of *all* geometric hyperosculation points uses the tangent coefficient comparison, the degree-four factorization, and the order argument; the test is not a replacement for these steps. No separate independent proof review has been performed.
