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

The standalone Python 3 program `verify_spatial.py` uses only the standard library. Execute `python3 verify_spatial.py` to check the finite genealogy formula against a separate first-generation recursion, the exact random-walk convolution identity, and the Gaussian product identity. An actual execution produced `PASS: 669 finite rational and Gaussian product checks`.

The rational tests cover six generations and 49 ordered site pairs at each generation, and another 294 random-walk convolutions. The 81 Gaussian checks use a relative tolerance of \(10^{-12}\). These computations do not claim exhaustive infinite verification. The infinite-generation correlation and covariance asymptotics rely on the mathematical proof and standard two-dimensional lattice local central limit / Gaussian bounds in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
