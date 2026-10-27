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

# Verification of the two-monitor theorem

Run `python verify_two_monitor.py` in a Python environment with NumPy and SciPy installed. The file builds full Hamming adjacency matrices, spectral projectors from their distinct eigenvalues, and the exact Krawtchouk expression for site-level absorption. It checks nine graph families: (q,d)=(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(4,1),(4,2). There are 23 inequivalent monitor distances and 394 initial-state evaluations. It independently computes matrix ranks and diagonal bright-space projections and checks the binary antipodal and adjacent-site closed formulas. It also evaluates the full dissipative propagator with two different positive loss strengths at t=900 in H(2,3).

Observed result: PASS for all 23 detector-distance cases and 394 site comparisons; direct propagation survival 0.4444444444443397 compared with theoretical 4/9. Tolerances are explicit in the file. These are finite numerical consistency checks, not a proof for arbitrarily large parameters. The complete proof is in RESULT.md and uses exact finite Fourier character orthogonality and rank arguments. No independent audit has been performed.
