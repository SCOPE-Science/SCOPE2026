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

# Reproducibility and verification

The proof reduces the optimum over every real projection to a single rotation-equivariant Fourier multiplier. The edge derivative identifies the space with a zero-sum \(\ell_\infty\) hyperplane; finite-dimensional quotient duality gives an exact median formula. Geometric-series summation establishes the displayed residue-class formulas for arbitrary cycle lengths, and explicit elementary inequalities prove the contractivity boundary.

The standalone program `verify_cycle_harmonics.py` uses NumPy and SciPy. It evaluates the closed form against independently sorted median-deviation sums for all orders from \(3\) through \(2000\), then independently solves the constrained linear program for every \(3\le n\le64\) and \(1\le k<n/2\). The recorded execution printed `PASS 1998 exact-formula sample identities; 992 constrained linear programs`. All numerical comparisons were within the specified tolerances. The program additionally checks the classification through order \(2000\). Its numerical output is not an infinite proof or independent external audit.

No external proof assistant was used. This is a mathematical derivation with reproducible finite cross-checks; originality is subject to the literature limitations reported in the accompanying review.
