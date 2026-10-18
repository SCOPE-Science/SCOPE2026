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
# Reproducibility and evidence

The standalone `verify_baker.py` requires Python 3 and uses only `fractions.Fraction` from the Python standard library. Execute `python verify_baker.py`. On successful completion it prints:

`VERIFY_OK: all two-sensor, n=1..12 exact rational polygon integrals`

For each lag \(1\le n\le12\) the code exactly enumerates all \(2^n\) dyadic strips, independently builds the two active upper bounds for each sensor, partitions the unit interval at their intersections and zeros, and integrates the minimum positive height by rational primitives. The computed joint events agree exactly with \(1/4+1/(6N)\pm nN/[8(N^2-1)]\) where \(N=2^n\).

The proof valid for all lags is in RESULT.md: it derives the strip area identities and the binary-reversal mixed moment analytically, with explicit bounds ensuring crossings are admissible. Neither twelve-lag enumeration nor numerical experiments are represented as a proof for unbounded lag. Independent audit has not been performed.
