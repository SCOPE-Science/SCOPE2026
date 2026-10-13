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

Install the NumPy dependency from `requirements.txt`, then run `python verify.py` alongside this file. On the reviewed package the program printed `PASS: 948 checks.` and the diagnostic outputs below.

- At \(k=1,m=3,L=2\), the batch-median estimator of \(\mathbb E\|q\|_2^2\) was about 4.0594 versus the proven value \(6\log2\approx4.1589\); measured angular mean about 0.2507 versus 0.25.
- At \(k=2,m=4,L=2\), the batch-median estimate was about 8.0825 versus \(12\log2\approx8.3178\); measured angular mean about 0.4006 versus 0.4.
- Independent numerical integration of \(\int_0^\infty(e^{-t/2}-e^{-t})\,dt/t\) gave approximately 0.6931471827, consistent with \(\log2\approx0.6931471806\).

Monte Carlo means of heavy-tailed variables can be unstable even if their first moment is finite, hence the diagnostic batch-median comparison. Finite simulation and truncation of an improper integral cannot verify global moment finiteness, divergence or the exact Beta law. Those conclusions instead use the analytic Gaussian decomposition, Schur complement, endpoint-density asymptotics, and Frullani identity given in `RESULT.md`. Independent audit has not been performed.
