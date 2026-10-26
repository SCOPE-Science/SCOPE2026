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
# Reproducibility

The standalone `verify.py` uses only Python 3 standard-library modules. Execute `python3 verify.py`.

During verification, the program constructed the exact rational distribution of labeled-vertex degree vectors induced by the degree-proportional attachment rule, rather than Monte Carlo samples. It summed **6,917 degree-vector states** over tree sizes \(2\) through \(10\); for each size, it independently checked total mass, both means, the mixed moment, both variances, covariance, root-leaf survival, and covariance sign. It also checked **2,993 exact-rational recurrence identities** at sizes \(2\) through \(500\), and performed three large-size numerical asymptotic tests. All tests passed.

The finite enumeration is **not** a proof of an all-size statement. The analytic proof is the conditional one-step mixed-moment recurrence, the closed central-binomial survival probability, and the strict ratio inequality, followed by variance recurrences and Stirling asymptotics. The checked code is supplementary evidence for the algebra.

The result concerns a particular tagged initial vertex of a one-edge preferential-attachment tree; code and proof do not cover other seed graphs or weighted attachment models.
