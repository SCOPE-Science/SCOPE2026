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

# Reproducibility of the finite checks

Run `python3 verify.py` with Python 3 and its standard library. The verifier uses exact rational numbers and symbolic pairs \(a+b\Lambda\) reduced by \(\Lambda^2=h\Lambda+Q\). It constructs arbitrary admissible leaf self-loop and leaf-to-leaf contact perturbations while maintaining the exact prescribed symmetric row sums. It verifies the Rayleigh defect formula identically in the resulting quadratic field, then calculates the leading eigenvalue by a separately implemented Jacobi diagonalization for a numerical cross-check.

The deterministic check covers five matrix orders, three through seven, with nine rational choices per order and eleven matrices per parameter choice: 495 exact row-sum, symmetry and quadratic-identity tests. It also checks the rational three-group threshold example, whose star Perron root is exactly one, and verifies the nonstar Rayleigh lower-gap \(3/55\). Expected final line:

`VERIFY_OK: 495 exact symmetric row-sum/Rayleigh identities and numerical eigenvalue checks; sharp three-type threshold and stability 3/55`

**Limits.** A finite number of cases cannot establish a theorem for arbitrary matrix size or real inputs. The proof in `RESULT.md` supplies the unrestricted sign argument, exact spectral minimization, and threshold equivalence; this script only checks concrete algebra and examples. Eigenvalue diagonalization uses floating point and a strict tolerance, while rational identities are exact. An independent scientific audit has not been performed.
