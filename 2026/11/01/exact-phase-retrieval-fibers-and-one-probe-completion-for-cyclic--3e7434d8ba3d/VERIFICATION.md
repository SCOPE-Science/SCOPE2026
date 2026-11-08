---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Splitting geometric cyclic indices at k yields A_r(k,l)=r^-k(1-r^N)(r^N+(r²ω^-l)^k)/(1-r²ω^-l); the denominator is nonzero when r>0,r!=1. A zero requires k=N/2 and an odd l, hence even N only. Weyl double Fourier diagonalization then leaves precisely h=N/2 real degrees of freedom in purely imaginary antipodal Hermitian entries. For two equal-data rank-one matrices, equal diagonals fix magnitudes and all non-antipodal offdiagonals fix phase products; on >=3 occupied indices the graph deleting the antipodal matching is connected. Only an antipodal two-sparse signal has b versus conjugate-b ambiguity. Additional Q using phase i between the two halves determines the missing imaginary cross-term, while one extra scalar is needed because genuinely distinct 2-sparse fibers exist. Independently checked ambiguity formula and zero set for all N=2..16 with r=1.4; finite checks corroborate, not prove, all N/r.

## originality

PASS

The Weyl ambiguity diagonalization and sufficient nonzero-ambiguity criterion are known. Originality claimed only for complete nonlinear fibers of real cyclic geometric windows and one scalar completion; closest retrieved work uses different windows or gives only sufficient criteria.

## value

PASS

The specific geometric window is a simple canonical nonvanishing cyclic family; its even-dimensional linear Hermitian kernel is large yet the noninjective rank-one locus is only an explicit antipodal two-point stratum. The exact support-dependent fiber classification and a single deterministic extra phaseless intensity form a natural and useful measurement-design result that cannot be inferred merely from a zero-free criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
