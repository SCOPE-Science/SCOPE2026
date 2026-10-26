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

The standard-library Python file `check.py` reconstructs finite weighted Bergman kernel Gram matrices by complex Gaussian elimination, separately computes the discrete-Fourier residue formula, checks local and global maximizing-radius comparisons at sampled points, and compares selected large-degree cases with the two sharp asymptotic predictions. Run `python3 check.py` from this directory; the associated checked output is included as `check_output.txt`.

The checker uses log-gamma evaluations, finite sums with explicitly programmed exponential-tail truncation, and numerical tolerance tests. These finite checks cannot certify the asymptotic theorem; the proof in `RESULT.md` establishes the infinite claims analytically. The highest-degree tests and limited number of parameter values are illustrative, not exhaustive.
