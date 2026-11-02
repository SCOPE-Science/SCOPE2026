---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Starting from the actual Q generator on +,−,0, direct determinant expansion yields λ(λ+a+b)(λ+a+2h)=(λ+b)v²q²; the simple principal eigenvalue controls fixed-order cumulant growth by finite-state Feynman–Kac analyticity and its uniform spectral gap. Matching powers of s=v²q² gives neutrality ac=b(a+b), A=1/L, C2=0, C3=−1/(bL^4), C4=1/(b²L^5). Hence κ6/T=−720v^6/(bL^4) and κ8/T=40320v^8/(b²L^5), while Brownian diffusion changes only κ2. Stationarity makes instantaneous velocity ±v with probability p/2 and zero otherwise; its sixth cumulant is v^6p(1−15p+30p²), yielding the exact threshold and positive short-time sign. Continuity plus negative long-time sign gives existence, not uniqueness, of T*>0. Independent symbolic cubic and threshold identities passed; finite-time numerical zero is not used as a proof.

## originality

PASS

The same three-phase intermittent propagation and fourth-order cumulant theory are already developed by Santra–Olsen–Gupta; neutral tuning follows from those antecedents. The narrower final result is the exact sixth/eighth order rates on this neutral locus and an analytical sufficient threshold for a strict sixth-cumulant time-sign change. A published all-cumulant characteristic transform makes the coefficients mechanically accessible and is the main originality risk, but the inspected source does not state this additional sign-classification result. Qualified best-of-knowledge PASS, not novelty certification.

## value

PASS

Eliminating long-time excess kurtosis is a physically motivated diagnostic of apparently Gaussian motion. A rigorous concealed sixth/eighth cumulant signature and forced finite-time sign reversal show why that fourth-order diagnostic can fail; the sharp parameter surface is a meaningful structural boundary, not an arbitrary finite-order substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
