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

Run the self-contained standard-library script with `python verify.py` (Python 3.9 or later). It enumerates all labeled quotient trees by their Prüfer words and counts each tree's physical realizations by assigning distinct physical vertices at each part, using exact integer falling factorials. For all admissible part profiles with \(k\in\{3,4,5\}\) and each part size in \(\{1,2,3\}\), it checks every matching of projected part-pair edges: 6,312 exact equality tests. It then enumerates physical graph edge subsets directly, filters physical matchings and quotient spanning trees, and checks six independent physical cases. Both methods report PASS, without external dependencies.

The analytic verification is the four-step proof in `RESULT.md`: (1) fixed-projection realizations; (2) a contracted-forest weighted Cayley polynomial; (3) factorial-moment/Vandermonde evaluation; (4) exact covariance subtraction. The computational sample is finite and does not establish the universal identity independently of that proof. There has been no independent external audit or formal proof certification.
