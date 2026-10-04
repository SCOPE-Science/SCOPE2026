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

The proof is analytic and does not rely on finite enumeration. The critical checks are:

1. A leader exists exactly when the two marginal maximizing-index sets intersect.
2. Conditional on its size, each maximizing-index set is uniform by exchangeability; the two sets are independent because the coordinate samples are independent.
3. The disjointness probability for uniform subsets of sizes \(k\) and \(l\) is \(\binom{n-k}{l}/\binom nl\).
4. The upper bound uses \(\Pr(|I_X\cap I_Y|\ge1)\le\mathbb E|I_X\cap I_Y|=kl/n\).
5. The lower bound uses the exact product for disjointness and \(1-u\le e^{-u}\).
6. The implications involving \(n\to\infty\) are proved from those pointwise inequalities; finite checks are not extrapolated.

The bundled `verify.py` exhaustively checks the hypergeometric identity by direct subset enumeration for small sample sizes and checks the exact rational finite-size inequalities over a larger range. Its output is expected to be `VERIFY_OK`.

Limits: the checker is a stress test only. It does not certify the literature comparison or replace the all-\(n\) proof.
