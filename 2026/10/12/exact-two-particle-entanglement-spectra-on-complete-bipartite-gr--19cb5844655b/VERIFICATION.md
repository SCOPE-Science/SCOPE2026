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

# Verification of the exact spectrum

The theorem is proved by symbolic finite-rank algebra for **all** integers \(m,n\ge1\). It does not rely on the finite checker to extrapolate to arbitrary size.

Run `python3 -m pip install -r requirements.txt` in an isolated environment, followed by `python3 verify.py`. The checker separately constructs the two-particle Grover transition directly from incoming directed arcs on \(K_{m,n}\), with no invocation of the analytic amplitude formulas for propagation. It compares propagation against those formulas and verifies singular spectra, repeated multiplicities, normalization, exchange symmetry and four-periodicity.

The eleven tested pairs are \((1,1)\), \((1,2)\), \((2,1)\), \((2,2)\), \((2,3)\), \((3,2)\), \((2,4)\), \((3,3)\), \((3,4)\), \((4,3)\) and \((4,4)\). Both exchange signs and times zero through four are tested, including vanishing Schmidt values and unbalanced dimensions. Recorded result: `VERIFY_OK 572 matrix identities 11 graph sizes`.

The analytic proof independently checks the coefficient-matrix Frobenius norm and exterior-product determinant, the exact identity between the time-two matrix and a partially transposed rank-one projector, and the extremal elementary inequality. The verifier uses floating-point arithmetic, so it provides numerical corroboration, not exact certification for its finite cases nor any infinite-family certificate. Source-priority uncertainty remains; no independent audit has been performed.
