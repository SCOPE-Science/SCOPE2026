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

Save the accompanying `verify.py` and execute `python verify.py` in Python 3 with NumPy installed. The script uses graph adjacency generated directly from sampled geodesic distances, and tests that admissible circular gaps give exactly the cycle graph while inadmissible gaps give chordal interval graphs. It additionally checks Fourier coefficient inequalities and the coprime Chebyshev product formula by trigonometric quadrature and compares numerical conditional simplex integrals with the Hessian-covariance Taylor coefficient for two sample sizes.

An observed successful run reported `TOPOLOGY_OK 800`, `FOURIER_OK 24`, two `SECOND_ORDER_OK` lines, and final `VERIFY_OK`. These are finite consistency checks with numerical tolerances and do not prove the unrestricted claim. The mathematical proof, including all hypotheses and quantifiers, is in `RESULT.md`. The full 1982 and 1988 related circle-coverage papers were inaccessible for a complete originality comparison. No independent mathematical audit has been performed.
