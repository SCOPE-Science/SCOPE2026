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

# Reproducibility and limits

The standalone `verify.py` script runs with Python 3 and no third-party dependencies. Run `python verify.py` from the directory containing it. An executed run returned exactly `PASS 2945 exact assertions; all matchings through six chords, finite factorial checks through n=200`.

The program enumerates all labeled linear perfect matchings with one through six chords, counts crossing pairs and linearly adjacent short chords directly, and checks the two-variable generating identity coefficient by coefficient against a separate deletion-polynomial reconstruction. It checks every available factorial order and crossing value in the finite range, exact mean/variance/covariance formulas, and the sign of each threshold-indicator covariance. It also checks the factorial coefficient bound for sample sizes through 200 and factorial orders up to 12.

The exhaustive checks are finite; they do not establish the identities at arbitrarily large size. The unrestricted proof is elementary counting plus a stochastic deletion coupling. The Gaussian component of the joint asymptotic result relies on the independently published crossing central limit theorem of Flajolet and Noy. The joint factorization is proved by the bounded factorial transform in the research text; it is not certified by finite computation. Independent audit has not been performed.
