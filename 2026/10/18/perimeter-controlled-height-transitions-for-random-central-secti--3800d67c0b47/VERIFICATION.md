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
# Reproducibility and limitations

Run `python3 checker.py` using only the Python 3.10+ standard library. The checked program compares two independent formula parametrizations at 45 regular-prism settings, tests 45 derivative approximations, verifies the 3/4/5-sided stationary points and the 6–11-sided monotone regimes, compares two additional cyclic pentagon configurations, and performs independent random-direction vertex counts for seven prismatic solids (770,000 Gaussian normals in total). It reported **135 passed comparisons**.

The proof is the exact angular crossing probability plus strictly decreasing derivative bracket and angular-gap perimeter inequalities. Numerical tests do not certify the all-height or all-polygon claims. The full text of the related 2023 random-section-angle source was inaccessible; a possible older equivalent expectation identity is a residual historical risk. Independent mathematical validation has not been performed.
