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

# Reproducibility and scope

Run `python verify_cycle_two_sink.py` with `numpy` available. The script constructs a Hermitian Peierls-phase adjacency matrix, finds each distinct energy eigenspace, then computes the simultaneous nullspace of the two contact-evaluation functionals by SVD. It checks all predicted site-by-site survival values, projection ranks, Hermitian orthogonality, and the real-spectrum count of dissipative generators with two different positive-rate pairs.

The run completed successfully for 195 combinations of ring size, sensor position and flux class: \(N=3\) through \(12\), every \(s=1\) through \(N-1\), and total flux \(0\), \(\pi\), and \(0.461\). Two independent rate pairs were checked in each of those cases. These numerical tests are not exhaustive for unbounded \(N\) or continuous rates. The infinite statement is supplied by the contraction, spectral-pair counting, and roots-of-unity arguments in RESULT.md.

No independent audit or external certification has been performed.
