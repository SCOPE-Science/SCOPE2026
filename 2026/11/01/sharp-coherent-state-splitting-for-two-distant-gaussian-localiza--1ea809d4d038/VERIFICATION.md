---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Single-disk monomial diagonalization gives λ0=1−e^(−s), λ1=1−(1+s)e^(−s), gap δ=se^(−s). For the disjoint restriction B=(Ba,Bb), nonzero spectrum of B*B agrees with BB*. The normalized disk-top vectors compress BB* to 2×2 with off-diagonal λ0<ka,kb> of modulus λ0 exp(−d²/2). A cross-disk kernel Hilbert–Schmidt integral bounds ||C||≤s exp(−(d−2√s)²/2)=η. For η<δ/4, min–max and Schur-complement spectral inertia bound the positive errors to both λ0(1±ε) by η²/(δ−2η). Since η²/e^(−d²/2)→0 for fixed s, sharp coefficient λ0 and the gap asymptotic follow. Independent checks recover gap/overlap/error order; source CHECKER.py is finite Galerkin only and was not used as proof.

## originality

PASS

The independently read Faber–Krahn theorem optimizes the largest concentration eigenvalue for fixed area, not the exponentially small splitting in a two-disk family. Spectral-deviation literature controls bulk eigenvalue counts rather than this pair with exact coefficient. Recent related eigenfunction work remains a priority risk without strong evidence of an identical theorem.

## value

PASS

Near-degenerate fixed-index spectral tunneling between two well-separated concentration regions is a motivated quantitative spectral problem. An exact leading exponential coupling coefficient and rigorous two-eigenvalue positive remainder refine known concentration bounds and may aid Gaussian localization spectral analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
