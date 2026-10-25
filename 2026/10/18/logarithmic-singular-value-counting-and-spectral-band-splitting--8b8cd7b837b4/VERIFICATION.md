---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

At fixed ω≠0, piecewise constant embedding of A_N=[C_N,diag(j^{iω})] into [H,M_{x^{iω}}] on [1,N+1] has uniformly bounded S2 error by summing cell derivative bounds O_w(1/(jk)+1/j²). Logarithmic unitary conjugation gives finite Wiener-Hopf convolution with h(s)=1_{s≥0}e^{-s/2}(e^{-iωs}−1), symbol σ_w(ξ)=w/√((ξ²+1/4)((ξ+w)²+1/4)). Boundary compression correction E_L≥0 has uniformly bounded S1 trace ∫s|h|²; cyclic kernel integration proves 1/log N trace(A*A)^m→(2π)^−1∫σ_w^{2m}. Uniform S2 discrepancy transfers moments with O(sqrt(log N)) error. Weighted positive spectral measures, compact supports and no atoms at fixed t>0 imply normalized threshold counts. Completing square in ξ+w/2 yields q± roots and two-component superlevel set iff w>1 and 4w/(1+w²)<t<2; HS coefficient =2w²/(1+w²). Independent finite double-checks across w/t bands and N=128,512,2048 show expected convergence but do not prove the limit.

## originality

PASS

Best-of-knowledge originality after direct comparison of normalized mathematical statements, source theorem scope and implications; not absolute historical-priority certification. Normalized modulated finite-section log spectral count and two-band algebra exceed cited generic Wiener–Hopf/Mellin frameworks as explicitly stated results.

## value

PASS

A sharp logarithmic density law for singular values of a naturally modulated discrete averaging operator, with complete even moments and explicit frequency-dependent topological splitting of its spectral superlevel bands at w=1. This gives nontrivial quantitative spectral geometry beyond general convolution calculus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
