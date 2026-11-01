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

The standalone `checker.py` constructs the two hop adjacency matrices for prime cycle sizes \(5,7,11,13,17,19,23,29\), scans every derived positive resonance and multiple nonresonant coupling ratios, and checks all two-sink separations. It independently computes the exceptional four-dimensional eigenspace by Hermitian diagonalization, identifies the two-dimensional dark kernel with a singular-value decomposition, and compares each diagonal projector value with the exact cosine expression. It checks the generic two-sink observation rank and compares selected long-time lossy matrix exponentials to the limiting survival fraction.

Actual checker output, retained as `verification_output.txt`, reports 3,408 coupling/separation comparisons and 68,328 site-resolved comparisons; maximum absolute projector discrepancy \(2.649\times10^{-14}\), and largest tested long-time loss discrepancy \(2.835\times10^{-10}\). The checker ends with `PASS`. The minimum observed separation of resonance ratios in the tested prime set is positive; this is a numerical sanity check only. The symbolic cyclotomic argument in `RESULT.md`, not that separation, proves exact distinctness for every prime.

**Reproduction.** Run `python checker.py` in an environment with NumPy and SciPy. Its output can be compared verbatim to `verification_output.txt`. Computations are finite and cannot certify all primes or historical originality. Independent external audit has not been performed.
