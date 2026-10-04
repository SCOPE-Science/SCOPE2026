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
The analytic verification has four layers. First, direct substitution verifies the affine identity \(\widehat\mu_i-\mu=\sigma(S-Z_i)/(\sqrt m(B-1))\). Second, the covariance calculation gives diagonal \(B-1\), off-diagonal \(B-2\), and therefore equicorrelation \((B-2)/(B-1)\), yielding the one-factor integral. Third, Gaussian orthogonal projection makes \(S/\sqrt B\) independent of the centered residual vector and produces the exact conditional coverage representation in terms of residual extrema; a Taylor bound and standard Gaussian extreme-value estimates give the asymptotic constant. Fourth, the range of \(S-Z_i\) is exactly the range of \(Z_i\), which proves the samplewise width factor and expected-width formula.

The supplied `verify.py` uses only the Python standard library. It numerically checks the exact coverage integral at \(B=2,3,6,10,20,100\), the samplewise range identity, the independent-hull coverage at \(B=6\), and consistency with the large-\(B\) scale. Numerical quadrature is a reproducibility check, not the proof of the asymptotic statement.

Scientific limits: the exact law is for iid Gaussian location observations, equal folds, and the stated leave-one-fold-out reuse rule. It does not validate dependent HulC variants generally and does not claim that the published independent-subsample HulC fails.
