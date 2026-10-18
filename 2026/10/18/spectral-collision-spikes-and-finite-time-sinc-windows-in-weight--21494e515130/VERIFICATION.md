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

The analytical derivation uses the orthogonal transverse/uniform-sector decomposition and exact integration of Fourier-mode pairs. No numerical enumeration is used as an infinite-parameter proof.

Execute `python verify.py` from the same directory, with NumPy installed. The script checks weighted joins of complete graphs and cycles at generic and spectrally resonant couplings, verifies projected long-time occupation probabilities against full-matrix eigenvector calculations, and checks the finite-time sinc crossover and exact equal-clique finite-window formula. It contains 1,330 explicit assertions and a single final success report.

The largest infinite-time spectral comparison discrepancy observed in the delivered run was below \(2.3\times10^{-14}\). Exact elementary consistency checks additionally show a return mean of \(17/25\) at the \(K_3\)-to-\(K_2\) unit-weight join and a nonresonant limiting value of \(113/225\), with jump \(8/45\).

Tests cover finite sizes, not every graph and real coupling; those are handled by the self-contained invariant-subspace proof. No external mathematical certification or independent audit has been performed. Dependence on coherent, lossless evolution and uniform cross-edges is essential.
