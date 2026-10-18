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

Execute `python3 verify.py` with Python 3. No third-party packages, data files, network connections, or external proof systems are required.

The checker independently computes the three moments defining the covariance by enumerating every binary word for \(2\le n\le12\), every \(2\le k\le n\), and rational success probabilities \(1/7\), \(2/5\), \(3/4\). It checks 198 exact moment identities. It additionally tests 3,002 numerical polynomial-root placements and 37 large-size limiting-root predictions. Finite computations do not establish the theorem for arbitrary parameters; the proof is the indicator-localization identity and the ensuing quadratic sign analysis in RESULT.md.

The only primary-source date asserted is the online-publication date explicitly printed in the precursor manuscript: July 18, 2009. General older bivariate run-distribution formulas could implicitly cover some covariance identities, so priority is not independently established.

Independent scientific audit has not been performed.
