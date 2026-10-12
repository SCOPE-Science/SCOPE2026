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

# Mathematical verification record

**Certificate:** `python3 check_frank.py` runs on Python 3 without external dependencies; it was executed successfully against the bundled script. Its decisive comparison uses exact `Fraction` arithmetic rather than floating-point values. The script builds rigorous scaled-integer enclosures of each exponential and logarithm, checks all 361 copula terms, brackets the covariance, and upper bounds the latent Spearman correlation using the exact Debye identity and integral-test zeta tails. The certified lower gap exceeds \(0.00153839\).

**Separate numerical cross-check:** the nineteen rational thresholds were evaluated against the original (non-rearranged) Frank CDF with 65-digit arbitrary precision, and the latent Spearman correlation was independently integrated from the Debye formula. The resulting respective values were about \(0.930925698735820068\) and \(0.929365805485040129\). This floating computation is corroborating evidence only.

**Infinite-domain proof:** the large-dependence mechanism is proved analytically by rescaling the explicit positive covariance-deficit kernel and an exponentially dominated convergence argument. The constant \(\pi^2/6\) is the exact mass of the limiting kernel. The extension to ordinal scores uses uniform quantizer convergence for every fixed sufficiently large parameter. No interval checker asserts the asymptotic statement.

**Scope and limits:** only bivariate positive-parameter Frank dependence is considered. A particular twenty-category point and existence of some finite quantizer for every sufficiently large positive parameter are proved. No minimality, universal parameter threshold, arbitrary-marginal optimization, or external certification is asserted. The scientific review is not an independent audit.
