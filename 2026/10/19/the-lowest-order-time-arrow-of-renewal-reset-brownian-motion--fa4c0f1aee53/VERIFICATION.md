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

# Reproduction and limits

Execute the included `verify.py` with a standard Python 3 interpreter. It imports only Python standard-library modules and carries out exact rational checks of two independently evaluated Gaussian-renewal expressions for the same mixed-moment difference. The checked families are one-, two-, and three-atom renewal distributions, rational observation lags and diffusivities, and integer orders through \(m=4\). Additional independent calculations verify the squared-stop-loss fourth-order specialization, piecewise-exact right second derivatives away from inter-reset atoms, and the periodic/Poisson examples. The run performed on the delivered code reported **899 passing checks**.

The program does not sample every positive renewal law or certify a limiting process; the universal assertions follow from the direct stationary renewal and Gaussian-moment proof in `RESULT.md`. Right derivatives at atoms are established analytically rather than by the finite-difference checker. A complete novel-priority assessment has not been performed; the complete text of an older response-theory article relevant to the covariance equivalence was not accessible. No independent audit has been performed.
