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

# Reproduction and mathematical scope

Run `python verify.py` with a standard Python 3 interpreter. In the completed package the checker reported `PASS: 716 checks; 24000 seeded iid-chord simulations; exact matching enumeration n=2..6`. It exhaustively enumerates all perfect matchings of up to 12 ordered endpoints, evaluates exact means and variances against the formulas, checks exact polynomial integrals and covariance identities, and checks the nontrivial optimum and geometric crossing condition.

The analytic core is the conditional crossing identity \(p(w)=w-w^2/2\), exact first-order and canonical second-order Hoeffding decomposition, and a Donsker empirical-process limit. Tests over finitely many cases cannot establish the Gaussian functional weak limit, universal quantifiers, or mathematical priority. The geometric observable requires iid uniform endpoint positions, not merely a uniform combinatorial matching. No independent audit has been performed.
