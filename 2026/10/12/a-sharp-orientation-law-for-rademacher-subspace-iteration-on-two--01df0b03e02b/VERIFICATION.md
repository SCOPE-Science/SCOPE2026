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

# Reproducible checks and boundaries

**Exact proof.** The identity is derived from an exhaustive symbolic event partition into both sign lines, all first line, and all second line. This is a complete partition for arbitrary \(\ell\), rather than finite-case enumeration. The pivotal exact formulas for a rank-one event are \(\rho=(b/a)^{4q+2}\) and the captured energy quotient in `RESULT.md`. Strict concavity of \(g(t)=t/(\rho+(1-\rho)t)\) proves equality locations and global sharpness.

**Executable diagnostics.** Execute `python3 verify.py` from this package directory. The program uses only Python standard-library rational fractions, forms symmetric and nonsymmetric exact matrices with rational orthonormal singular frames, exhaustively enumerates sign-line sequences up to five columns, and recomputes the projected rank-one error directly from matrix powers. It verifies **410 exact-rational identities and inequality cases** over two spectral pairs and multiple orientations, power counts, sketch widths, and Hadamard extrema. Observed output: `Verified 410 exact-rational identities and inequality cases.` No numerical tolerance is involved.

**Verification limits.** The finite program cannot certify the infinitely many parameter choices; those follow from the mathematical proof. For \(\ell>2\), the sketch is a redundant-column extension with rank-revealing orthonormalization, not a claim about a non-rank-revealing thin-QR implementation. All statements concern exact arithmetic, real full-rank \(2\times2\) matrices with separated singular values, and the expected **squared** Frobenius norm. This package has not undergone an independent audit.
