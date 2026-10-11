---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

After normalizing one coefficient, the Fourier polynomial is \(1+Z+W+\eta ZW\) with \(Z,W,\eta\) unimodular. For \(\eta=1\) it factors as \((1+Z)(1+W)\), so the zero set is at most one complete row and one complete column, giving counts \(0,n,m,m+n-1\). For \(\eta
e1\), the zero equation and unit-modulus condition imply \(Z^2=\eta^{-1}\), hence exactly two unit-torus solutions \((s,-s)\) and \((-s,s)\). A rotated root grid contains both simultaneously exactly when both moduli are even; otherwise at most one is present. The explicit coefficient quadruples in RESULT.md realize every listed count. This proves the complete all-\(m,n\ge2\) spectrum; the finite verifier is only corroborative.

## originality

PASS

Originality passes. Finite-Abelian equality-case work and Kronecker-Fourier rank-deficiency work allow unrestricted coefficient vectors and address support minima or linear nullspaces. The audited theorem instead fixes one Cartesian four-point support and classifies the complete Fourier-zero spectrum under the nonlinear equal-magnitude constraint through the cross phase. Fresh Resultary comparison returned the audited theorem as the exact hit and no earlier result with the same all-(m,n) phase-only spectrum.

## value

PASS

A Cartesian four-point rectangle is the smallest nontrivial product support where one can see both entire Fourier rows/columns and isolated zeros. The exact phase-only spectrum cleanly separates factorable and nonfactorable cross phase and shows a sharp parity transition, furnishing a reusable model for unimodular sparse Fourier cancellation rather than a raw enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
