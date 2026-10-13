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

# Verification of the sharp finite-horizon product norm

Execute `python verify.py` with standard-library Python 3.9+ in the same directory as this document. The program runs exact rational tests of fifteen square diagonal ratios across eighteen consecutive alternating products, including matrix idempotence, key annihilation, zero determinants, and exact matching of squared operator norms through rank-one trace identities. It also checks a distinct admissible example with \(\kappa=2\) and gate \(3/4\), and performs 48,000 deterministic pseudo-random comparisons of arbitrary products against the claimed bound.

Observed output:

`VERIFY_OK exact_fraction_identities= 630 random_product_norm_checks= 48000 two_step_growth_kappa2= 1.125`

The checker uses the known closed-form two-by-two spectral norm for finite tests and exact fractions for its symbolic examples. It does not enumerate all dimensions or every real diagonal and key, and its numerical checks do not establish an infinite/universal theorem. The proof in `RESULT.md` establishes the general bound and simultaneous equality for every product length.

Key limitations: exact arithmetic; positive bounded diagonal metrics; unit keys; at least two key coordinates; arbitrary switching; zero targets for the exhibited growing homogeneous state. No external audit or implementation-level empirical validation was performed.
