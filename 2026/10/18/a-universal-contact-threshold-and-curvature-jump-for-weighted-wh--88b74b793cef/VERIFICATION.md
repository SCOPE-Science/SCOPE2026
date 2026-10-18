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
# Verification of weighted-wheel Lipschitz ellipsoid formulas

The claimed domain is every integer \(m\ge3\) and real \(t\ge1/2\), with the hub anchored at zero and rim coordinates in ordinary \(\mathbb R^m\). The proof in `RESULT.md` is the mathematical basis of the universal statement.

Run `python3 verify.py` using the Python standard library. The recorded execution returned `VERIFY_OK 276 parameter configurations and 47 boundary-moment identities`, confirming contact equalities, positive-definiteness, the precision normalization, cyclic eigenvalues and the closed determinant formula. This includes parameters on both sides of \(t=1/\sqrt2\).

Run `python3 verify_unrestricted.py` in an environment with NumPy and SciPy. The recorded execution returned `UNRESTRICTED_OK 20 full symmetric-matrix optimizations`, testing \(m=3,4,5,6\) and five spoke lengths at each order. The implementation imposes no circulant symmetry on the competing covariance matrix. Numerical optimization starts from a strictly feasible scaling of the analytical covariance; it provides corroboration rather than an independent lower-bound proof.

The sharp curvature jump is derived symbolically from the cycle spectral moments in the proof. Additional finite-difference checks at rim counts \(3\), \(7\) and \(20\) approached the predicted one-sided second derivatives \(-2m\) and \(-10m\). All numerical tests are finite and subject to tolerance; neither the checks nor a literature search establish the theorem over infinitely many parameters or absolute originality by themselves. Independent scientific audit has not been performed.
