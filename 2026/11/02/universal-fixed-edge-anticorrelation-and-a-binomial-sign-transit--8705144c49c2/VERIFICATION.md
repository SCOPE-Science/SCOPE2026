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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 and no third-party libraries. The code exhausts all 64, 1,024, and 32,768 graphs on four, five, and six labeled vertices, respectively, classifies the counts on every three-vertex subset, and computes conditional covariance at all exact edge levels. It asserts agreement with the orbit-sum formula and fully factored formula and verifies the zero/negative boundary classification. It independently forms binomial exact-rational expectations for probabilities 1/5, 1/2, and 3/4 and checks the stated closed form. It then checks all orders four through forty and every permitted fixed-edge count. Recorded outcome: `PASS graphs= 33856 identities= 21497`.

The exact finite checks do not prove the universal assertions. The proof uses the combinatorial orbit classification and a polynomial factorization valid for all graph orders. No human or independent audit was conducted. Historical novelty remains subject to broader literature comparison.
