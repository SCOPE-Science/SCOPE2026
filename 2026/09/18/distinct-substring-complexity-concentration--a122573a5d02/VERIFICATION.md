---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

For two starting positions, even when the length-r blocks overlap, sequentially revealing fresh constrained symbols bounds the match probability by p_*^r. A union bound gives the stated longest-repeat tail. On the good event L_n<=ell, all longer windows are unique, while changing h coordinates affects the set of length-k substrings by at most hk; summing k<=ell gives Hamming Lipschitz constant ell(ell+1)/2. McShane extension followed by clamping preserves that constant. The expectation shift is at most M_n delta, McDiarmid yields the stated tail, and Efron–Stein plus the bad-event square bound gives Var(D_n)<=n c_ell^2+2M_n^2 delta. With ell proportional to log n, delta is O(n^-6) and the advertised variance/fluctuation orders follow. No finite enumeration is needed for the proof.

## originality

PASS

The 2004 primary material treats expectation and explicitly leaves variance characterization aside; the September 2026 Godbole paper studies E(D) and explicitly asks for variance/concentration. Exact and semantic searches found no earlier tail or O(n log^4 n) variance theorem for total distinct-substring count. Older suffix-tree literature remains a residual risk but the closest inspected primary material points away from coverage.

## value

PASS

The theorem answers a directly motivated and explicitly posed concentration question for a natural string statistic. It gives a nontrivial near-root-n fluctuation scale using a transparent structural reduction to the longest repeat, and is not a mere numerical cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
