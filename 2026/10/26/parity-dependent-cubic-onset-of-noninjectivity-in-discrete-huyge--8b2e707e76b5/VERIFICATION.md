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

## Analytical obligations

The exhaustive first singular locus follows from simultaneous equality in a symmetric Rayleigh chain on the sum-zero tangent hyperplane and the Fourier top-eigenspace support properties. The two odd-frequency basis functions cannot share two distinct zeros on an odd ring. At every critical configuration, the one-dimensional nullspace and the orthogonal complement give an analytic Lyapunov–Schmidt reduction with strictly positive cubic coefficient. The nontrivial inverse branches are roots of an analytic equation in squared amplitude. These analytic arguments, not computation, cover all \(n\ge3\).

## Reproducible finite checks

Run `python checks/verify.py` after installing `checks/requirements.txt`. The script verifies the phase closure, Laplacian eigenpairs and critical nullity, fourth-power sums, transverse invertibility, and three solutions of the full lifted preimage equation. It covers lengths \(3\le n\le15\) and parameters \(\mu\in\{0.005,0.015\}\) with a least-squares root correction in the actual codimension-one transverse space. The program completed with `VERIFY_OK` in the stated run. Floating-point tolerances and the bounded length range prevent the tests from constituting universal certificates; the mathematical proof is independent of them.

## Limitations

The tested local roots do not establish the global number of preimages or behavior for large \(h\). Exact symbolic coefficients and the existence of the local branches are established analytically. This verification did not involve an independent scientific audit.
