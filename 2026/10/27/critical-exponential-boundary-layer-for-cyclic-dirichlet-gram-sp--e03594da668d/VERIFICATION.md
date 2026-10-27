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
# Verification record

The exact kernel-Gram Fourier decomposition and its uniform estimates are proved analytically in RESULT.md. The included `verify_dirichlet.py` was executed from the included package source before review. It reported 60 passing assertions, covering four finite sizes and three coefficient shifts by matrix/residue comparison, plus two critical exponential scales and two shifts over three larger sizes by high-precision closed-form Gram diagonalization. The program is an independently implemented finite cross-check, not an infinite proof or an independent scientific audit.

Exact assumptions: real \(c>0\), \(\tau>0\) fixed as \(N\to\infty\); normalized Gram of exactly \(N\) equispaced points with squared radius \(1-e^{-cN}\). Asymptotic error constants may depend on these fixed parameters. The proof does not cover changing \(c\), changing \(\tau\), noncircular point configurations or global uniqueness in the historical literature.
