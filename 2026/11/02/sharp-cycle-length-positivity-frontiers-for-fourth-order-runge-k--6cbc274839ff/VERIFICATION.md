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

# Reproducibility and actual checks

The standalone `verify.py` requires Python 3.9+ and no third-party dependencies. Execute `python verify.py` in the directory containing the scientific files; a successful execution emits `ALL_CHECKS_PASSED 4070`.

The script independently constructs the finite-dimensional RK/Taylor polynomial \(\sum_{k=0}^p(hQ)^k/k!\) as a rational matrix, checks each entry against the binomial-residue formula, tests the table's sign criteria for \(2\le n\le12\), \(1\le p\le4\), and \(h=j/16\), \(0\le j\le40\), and checks column and row sums. A further exact test covers general two-state Markov generators with rational rates on a rational step grid, including absorbing states, and checks that positivity coincides with the nonstationary eigenvalue condition. The three-state negative-probability counterexample and its spectral modulus are checked exactly as fractions. Sharp root locations are bracketed by rational decimals.

The numerical grid is not exhaustive in step size or cycle dimension. The all-parameter proof is contained in `RESULT.md`; the verifier is an independent arithmetic consistency check and does not establish mathematical novelty or provide third-party review.
