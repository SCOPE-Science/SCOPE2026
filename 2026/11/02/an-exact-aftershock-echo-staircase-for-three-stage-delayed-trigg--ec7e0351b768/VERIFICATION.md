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

Run `python verify_echoes.py` from the extracted package directory with Python 3, SymPy and mpmath installed. The program symbolically checks the exact three-stage derivative, numerically sums up to 139 generations in the renewal expansion at fifteen rate/time combinations, and independently brackets the first three echo thresholds. It reports the first thresholds and tests the example branching ratio \(99999/100000\).

The infinite enumeration of extrema is not established by finite computations; it follows from the analytic sign proof in RESULT.md. No empirical earthquake data or independent validation is included. The proof is specific to subcritical Erlang stages one, two and three, and the claimed infinite staircase is for stage three only.
