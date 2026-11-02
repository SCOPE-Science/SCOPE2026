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
# Reproducible checks

Run `python3 verification/verify_simplex_absorption.py` with Python 3 standard library. Successful replay prints a `VERIFY_OK` line. The script needs no external files, downloads or numerical packages.

The replay establishes: 24 direct Fourier-matrix rank comparisons for the simplex construction at dimensions \(N=7,15\); 24 independent exact Gram eigenvalue/rank checks for those cases; a complete full-rank multiset enumeration of 2696 generator-column configurations when \(m=3\), confirming the upper bound and 176 unlabeled optimizer multisets; 400 deterministic full-rank random-generator trials for \(m=4\); and an independent physical 128-site Krylov span rank of 46 for the simplex trap arrangement at \(m=3\).

The direct Walsh entries are integers \(\pm1\). All relevant minors involve at most 16 rows and have absolute determinant at most \(16^8=2^{32}\) by the Hadamard bound. Therefore computations modulo \(2^{61}-1\) preserve the rational ranks. The Krylov check supplies an independent lower bound that matches the analytical upper bound, and does not claim a general modular-rank equivalence for arbitrarily large Krylov minors.

**Limits of verification:** finite examples and random tests are not proofs of infinite-family optimality. The proof's general combinatorial bound, simplex Gram positivity, and positive-loss spectral decomposition are essential. No separate independent scientific audit has been performed.
