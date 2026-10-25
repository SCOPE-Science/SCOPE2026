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

Execute `python3 verify.py` with a standard Python 3 interpreter and no external dependencies. The program computes partition numbers by Euler's pentagonal recurrence; enumerates every partition of each \(0\le n\le26\); and checks the exact marked count, multivariate survivor, and coincidence count against their combinatorial definitions. It also computes the marked distributions at \(n=1000,4000,16000\). Successful execution prints `VERIFY_OK` and three numerical comparison rows.

The numerical convergence is slow: for \(n=16000\), the computed \(\Pr(M_1=M_3)\) is approximately \(0.357980\), compared with the infinite limit \(1/3\). These computations verify finite identities and orientation of asymptotic behavior; they cannot prove infinite distributional statements. Those are proved by the uniform partition-ratio estimate, a Riemann-sum limit, uniform marked local estimates and tightness.

Full-text scientific comparisons include Wagner's 2011 author PDF, Ballantine–Merca's 2017 arXiv paper, and Bhowmick–Meher's 2026 arXiv article. The 2025 Baruah–Talukdar paper was available only as a publisher preview; its full text was not inspected. Independent audit has not been performed.
