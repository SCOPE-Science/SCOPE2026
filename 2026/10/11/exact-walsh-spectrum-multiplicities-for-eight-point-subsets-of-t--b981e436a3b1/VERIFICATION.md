---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For 8-point E in F2^4, t absent from E+E iff E+t=E^c. If E is nonhyperplane, |T(E)|<=2, so its difference set has at least 13 nonzero elements. Balanced sign s=2 1_A-1 is a Walsh polynomial with at least four nonzero Fourier modes unless A is affine hyperplane; hence A has at most 11 nonzero Fourier zeros. Orthogonality forces every nonhyperplane spectrum B to be an affine hyperplane, precisely when its annihilator t complements A. Hyperplane supports yield 2^8 transversals. Exact incidence counts 15*2^8=3840 and 15*14*2^4=3360 imply profile 10080,1920,840,30 and total 14880. Independently enumerated all 12,870 eight-sets and all t using Python integer bit masks; T histogram {0:10080,1:1920,2:840,8:30}. This separate finite check corroborates but does not replace the structural proof.

## originality

PASS

Best-of-knowledge complete finite incidence census and structural all-spectra theorem for the fixed Sylvester-16 character matrix. Spectral implies tile theorems do not count all frequency bases; the primary Huckle--Kravvaritis paper is a plausible same-matrix comparator but its accessible abstract targets eigenvalues and leading principal submatrices, not unordered arbitrary 8x8 Hadamard incidences. Its full text was unavailable and this is explicitly retained as a bibliographic risk, not automatically scored as failure.

## value

PASS

The entire natural half-size class of the smallest nontrivial 16-point Boolean Sylvester character matrix is classified, not a selected example. The spectral-partner counts distinguish an extremal 256-valued affine stratum from nonaffine 0/2/4 strata and explain the sharp incidence count by translation/Fourier structure. Such per-support exact Walsh bases could be reused in finite harmonic analysis and Hadamard submatrix classification; an exact self-contained finite census qualifies without a general-dimensional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
