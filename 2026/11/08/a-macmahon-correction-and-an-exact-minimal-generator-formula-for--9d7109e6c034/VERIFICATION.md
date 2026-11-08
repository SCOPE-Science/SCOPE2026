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

From the package directory run `python3 verify.py` using only the Python standard library. The verifier constructs finite transformation pairs directly from \(t^3=t\) and \(e^2=e=te=et\). It checks their relations explicitly, determines the set of rank-two outputs admitting rank-three square roots, and counts relabeling orbits by two independent methods: full canonicalization on up to five points and conjugacy-type Burnside averaging on six points. Separately it computes the Euler-product predictions via the exact logarithmic-derivative recurrence.

The checked values are \(r_3(5)=15\), \(r_2(5)=17\), \(r_3(6)=46\), and \(r_2(6)=37\), together with earlier degrees as consistency tests. Its successful terminal output contains `VERIFY_OK`. The finite checks do not certify the theorem for unbounded \(n\); that follows from the combinatorial decomposition and the published multiplication rule. No independent mathematical audit is represented.
