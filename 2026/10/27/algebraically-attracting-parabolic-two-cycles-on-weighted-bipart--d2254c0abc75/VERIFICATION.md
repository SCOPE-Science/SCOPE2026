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

# Verification

Run `python verify_parabolic_cycle.py` in the directory containing this file. The script requires NumPy and SymPy and has no external inputs. `verification_output.txt` records the output from an execution of that exact source.

The script checks the two-color return and graph Laplacian spectral radius for a star, an unequal complete bipartite graph, a weighted even cycle, and an unweighted six-cycle; compares the cubic return with \(-\nabla W\) at four scales on each graph; checks a decreasing squared distance; and verifies the sharp spectral intervals at five amplitudes per graph. SymPy verifies the exact scalar coefficient \(-\pi^2/2\).

The all-connected-graph claim and the quantitative \(\Theta(k^{-1/2})\) rate rely on the proof in `RESULT.md`. Finite tests are diagnostics rather than exhaustive or infinite-dimensional certificates. Independent validation is not performed.
