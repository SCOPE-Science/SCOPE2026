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

# Reproducibility and verification

The accompanying `check.py` runs with Python 3.9 or later and requires only the standard library. Execute `python check.py` in the same directory as this document. The script uses fixed random seeds, no network access, no external datasets, and no pre-generated log files.

The verification reconstructs the original temperature formula independently of the analytical derivative, compares 5,000 symmetric finite differences against that derivative, evaluates 3,000 randomly chosen finite spectral mixtures, and brackets any predicted minimum by bisection. It checks exact two-band values, finite saturation against the limiting root, the logarithmic law with no transparent band, and 1,000 exact weak-band crossover identities. The source code is provided completely, so results can be rerun or modified. Numerical values are approximate and are not interval enclosures.

Analytical checks independent of finite testing are explicitly provided in `RESULT.md`: ratio monotonicity for the global zero count, strict sign behavior of the positive part of \(P-Q\), transversality at the finite saturation depth, finite-sum exponential asymptotics, and monotone inversion of the two-band crossover. The verified mathematical statements apply only to the stated positive parameters and fixed Eddington closure. No formal proof assistant, externally commissioned verification or independent scientific audit has been performed.
