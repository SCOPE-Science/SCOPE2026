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

# Verification of the signed-area phase diagram

The standalone `CHECK.py` requires the packages in `requirements.txt` and can be run as `python CHECK.py`. The program prints `PASS` only after exact symbolic stationary-generator checks, the exact factored sample with two roots, symbolic verification of the unique shape maximum, eight high-precision independent renewal-reward quadratures, and three random-time stationary Gaussian-law sampling checks. These checks were executed successfully.

The main infinite-domain zero count does not rely on scanning or sampling: it follows from the explicit derivative \(h'(r)=(1-u^2-r^2)/[(r+1)^2-u^2]^2\) and its unique sign change. The existence and moment identities follow from regenerative exponential-age stationarity of the stable linear process. The long-time area law follows from finite-mean cycle rewards and the renewal-reward theorem.

Numerical sampling is finite and is *not* a proof of uniform validity. The result does not establish the full stochastic-area distribution, entropy production, or performance at finite measurement times; the source-comparison conclusions are subject to independent scientific validation.
