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

The exact stationary covariance was proved by spectral decomposition of the balanced bipartite migration matrix. Strict convexity proves uniqueness; derivative comparisons prove the exact four-vertex value, bounds, parameter monotonicity and large-size asymptotics. The formulas require \(N\ge4\) even, \(0<a<1\), independent temporal innovations with covariance \(\sigma^2I\), and \(0\le d\le1\).

The accompanying `verify.py` independently reconstructs the transport matrix over \(N=4,6,8\) and confirms the matrix Lyapunov identity and local/aggregate variances using rational arithmetic for 54 parameter triples. Its output is `certificate.json`, reproduced exactly by `python verify.py`. These finite computations do not certify the general theorem; that depends on the written proof. Neither exhaustive literature novelty nor independent scientific validation was performed. A general prior spectral method could cover this topology after specialization.
