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

The proof of the rank law is mathematical and finite-dimensional. Its critical steps are: (1) invariant bright/dark decomposition for positive local loss; (2) exact radial eigenvalues and Fourier eigenvalues; (3) arithmetic count of Fourier pair-probe rank drops; (4) two-by-three merged evaluation matrix at resonance; (5) the coprimality argument excluding a perfect two-rim pair at interior resonances.

Independent numerical arithmetic checks run `python checker.py` with Python 3 standard library only. The checker constructs full two-source Krylov matrices from a diagonal similarity of the symmetric weighted adjacency matrix. Two prime fields are used for 5,194 finite comparisons across all spacings for \(5\le n\le37\) and seven rational squared spoke weights, with 16 additional exact rational ranks at three special parameter points and nine exact ranks in \(\mathbb Q(\sqrt5)\) for irrational resonances at \(n=5,10\). The printed deterministic results are in `checker_output.txt`.

The similarity replaces hub-spoke entries by \(1\) and \(a^2\) in opposite directions. It preserves rank because it is an invertible diagonal change of basis. A modular rank may be strictly smaller than the characteristic-zero rank, so successful modular tests alone would not prove the formula; the analytical spectral proof is required. Float calculations select tested resonance candidates only and are not used to establish the theorem's exact parameter boundary.

No independent audit or external formal certification has been performed. Historical uniqueness is not certified. Long-time capture statements do not imply a uniform finite-time convergence rate as the spoke coupling approaches a resonance.
