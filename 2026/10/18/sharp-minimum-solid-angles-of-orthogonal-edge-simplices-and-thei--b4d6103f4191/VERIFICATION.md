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

# Verification and reproducibility

The included `right_simplex_checker.py` was run against its own source bytes with Python 3, NumPy, SciPy, and SymPy. It prints `PASS` and verifies the following.

1. Numerical quadrature for the exact Dirichlet expressions at dimensions two and three matches independent analytic angle formulas to \(5\cdot10^{-13}\) or better.
2. The first and second moments of \(d\sum_{j<d}R_j^2\) agree with the stated exact rational formulas by symbolic simplification.
3. With fixed pseudorandom seeds and 40,000 draws per dimension, normalized Dirichlet expectation factors were approximately \(0.4417854\), \(0.3872053\), \(0.3728229\), \(0.3690013\) at dimensions 16, 64, 256 and 1024, consistent with convergence to \(e^{-1}\approx0.3678794\). These finite data do not establish an asymptotic theorem.

The proof is self-contained apart from standard Gaussian spherical invariance, the Dirichlet law of normalized independent exponentials, the strong law, dominated convergence, Stirling's approximation and the three-dimensional trihedral-angle formula. Its all-dimension conclusions follow from cone inclusion and exact integration, not from numerical experiments.

The originality comparison is based on the available full text of historical primary literature and the public abstract of the recent motivating manuscript; the latter's complete propositions were not available. This is not external or independent validation.
