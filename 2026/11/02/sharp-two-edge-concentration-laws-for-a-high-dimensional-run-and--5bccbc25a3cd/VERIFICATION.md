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

The source `verify.py` is a self-contained standard-library program with a fixed random seed. Invoke `python3 verify.py`. It checks four exact stationary first-moment identities and corresponding independent conditional on/off Monte Carlo means, conditional uniform-sphere inner-product variance, and approximate upper/lower edge behavior in the symmetric-rate example. The numerical diagnostics are finite stochastic tests, not a substitution for the exact probability arguments in `RESULT.md`; they do not establish uniqueness of a published result or independent scientific validation. All bounds and constants claimed analytically are derived in the paper text.
