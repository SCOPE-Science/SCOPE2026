---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The exact terminal matrix is Σ_{j=0}^k binom(N,j)G^(N−j)(F−G)^j. Joint unitary diagonalization reduces operator norm to the scalar truncated binomial polynomial on |z|=1. Independently expanded its real-coefficient Chebyshev squared modulus using u=1−Re(z) and verified all four symbolic polynomial defects for free N and u. Their N-prefactors are positive for N>=k+1, giving the exact iff thresholds including Δ=0 and scalar boundary equality. Finite matrix trials and verified source recurrence are secondary; k>=N yields exact F^N but is excluded from four frontier domains.

## originality

PASS

Known general truncated-binomial Parareal amplification and qualitative wave/phase instability are credited. The exact signed low-correction universal unitary-circle inequalities, first nonzero k=3 stability window and sharp k=4 enlargement were not found as prior theorem. This is a best-of-knowledge claim, not novelty certification; known polynomial makes specialized prior derivations plausible.

## value

PASS

This is a motivated exact stability-design invariant for phase-inaccurate, nondissipative parallel time integration: the first two correction sweeps can never be terminally contractive under nonzero mismatch, but k=3/4 admit sharp, realizable O(1/N) phase windows. The exact order-by-order boundary distinguishes physically relevant stability regimes and not just a tabulated polynomial identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
