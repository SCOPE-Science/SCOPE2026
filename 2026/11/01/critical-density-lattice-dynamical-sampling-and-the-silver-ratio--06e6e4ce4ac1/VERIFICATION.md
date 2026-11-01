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

# Verification scope

The analytic proof establishes the infinite-lattice block decomposition, exact determinant for all positive integers \(K\), explicit Chebyshev inverse, and two-sided exponential estimates. It does not rely on a finite experiment or on numerical singular-value extrapolation.

Run the supplied `checker.py` with Python 3 using only the standard library. Exact fractions verify the determinant and inverse identities on all columns for \(1\le K\le7\); coefficient signs are checked as an independent finite normalization control. Expected output: `CHECK_OK: exact block determinants, Chebyshev inversion, coefficient alternation (k=1..7)`.

The script does not verify mathematical originality, numerical values for untested dimensions, or the infinite asymptotic independently. No external certification or independent audit has been performed.
