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

Run `python verify_bridge_transfer.py` with NumPy and SciPy. The checker builds independent full-graph and four-dimensional Hamiltonians, verifies the orthogonal low/high block decomposition, checks complex propagator agreement, and probes the sharp asymptotic infidelity across balanced and unbalanced clique-size families at several fixed bridge weights. The executed program reported **108 passing numerical checks**. Its largest listed asymptotic ratios at clique orders above two hundred were close to one; these are finite diagnostics, not a proof or exhaustive certification.

The proof of the infinite-size limit uses the explicit spectral-gap and resolvent arguments in `RESULT.md`, not the checker. Different finite dimensions, large variable bridge weights, time growing with graph size, and higher-excitation dynamics are not covered. Independent audit has not been performed.
