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

# Verification record

The analytic proof in `RESULT.md` gives a complete decomposition and all strict boundary inequalities for the entire infinite integer family. `checker.py` reconstructs independent distances and evaluates centered matrices at orders two through eleven. The observed mean-zero nullities are three at order two and one at each tested higher order; the analytically predicted sector signs agree. Run `OPENBLAS_NUM_THREADS=1 python checker.py` (requires NumPy). The numerical tolerance applies only to these test comparisons and not to the analytic theorem. The endpoint Euclidean realization dimension is deduced from exact centered Gram rank, not from a numerical rank threshold. Independent audit and external validation have not been performed.
