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

The analytic proof diagonalizes the reduced three-vertex mass-weighted Laplacian, uses the positive zero-mode projection to force equal outer masses for near-unit endpoint transfer, and compares endpoint spectral measures to force equal bridge counts. In the symmetric case, elementary trigonometric extremality and Kronecker's density theorem yield the exact arithmetic classification. Pell identities give the explicit balanced-community convergence rate.

`verification_three_bridge.py` is a standalone Python 3 script requiring NumPy. Run `python verification_three_bridge.py` in the directory containing the embedded files. It independently assembles several three-community weighted Grover operators in their original directed-arc Hilbert spaces, tests unitarity, and compares finite-weak-weight transfer with the predicted reduced wave. It also diagonalizes reduced matrices independently, checks asymmetric mass projection bounds at finite times, and verifies Pell witnesses. The recorded run passed 307 finite checks.

The source theorem's weak-edge limit is invoked with each witness time held fixed before the weak-edge weight tends to zero. Neither finite numerical checks nor the source's fixed-time error bound establish a uniform-in-time theorem for the original walk at fixed nonzero weak-edge weight. No claim of exhaustive computational certification is made.
