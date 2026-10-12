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

Run `python3 artifacts/verify.py` to reproduce the proof-critical exact certificate. It uses the Python standard library exclusively: integer sieve, modular inverses, residue dynamic programming, and upward/downward rational rounding.

The verifier enumerates every squarefree semiprime denominator at most \(2000\), computes each prime-local maximum for all modular residues, and verifies by exact integer comparison that the global dual bound is less than \(1\). The symbolic proof handles every larger denominator with no finite-search extrapolation.

The saved standard replay is `artifacts/replay.txt`. Coarser integer scales \(10^8\) and \(10^{10}\) independently preserve the strict inequality. The computed bound is an upper bound for a hypothetical *integer-valued* sum of at most \(40\) terms, not an upper bound for arbitrary unconstrained sums of \(40\) reciprocal semiprimes.
