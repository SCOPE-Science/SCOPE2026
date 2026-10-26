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

# Verification record

The proof uses the coefficient identity \(H(z)=e^{-\theta z}(1-z)^{-\theta}\), a three-term coefficient asymptotic at \(z=1\), and the signed Taylor remainder of \(e^{-1}\). The analytic steps cover every fixed \(\theta>0\), all distinct integer \(a,b\ge2\), and all finite \(n\ge a+b\) for the critical sign statement.

Running `python3 checker.py` from the package directory performs the complete independent small-size permutation census, exact coefficient comparisons, exact covariance formula checks, and numerous exact parity assertions. The successful execution reports `PASS: 4883 exact checks (including complete derangement census for n=5..8).`

Finite computation is not a proof of eventual signs or factorial asymptotics. Those follow from the explicit expansions and inequalities in `RESULT.md`. No independent external validation has been performed.
