---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For each orbit a_k=||T^kx||^p and tail sum S_k, absolute Cesàro boundedness applied to T^kx with remaining horizon n-k+1 yields S_k <=K(n-k+1)a_k. Therefore S_{k+1}/S_k <=1-1/[K(n-k+1)] for k<n, without dividing by vanishing orbit norms; combine k=0 and iterate through n-1. The weighted backward shift on ℓp with w1^p=2K-1 and w_j^p=1+(K-1)/(Kj) for j>=2 has nonincreasing positive weights. For e_j the cumulative orbit norm A_j obeys A_1=2K and A_j=1+w_j^pA_{j-1}=K(j+1). Every partial average is <=K because the nonzero orbit norms increase with k and later terms vanish; coordinate additivity extends this to arbitrary ℓp vectors. e1 gives optimal K and e_n attains the power product for all n. Gamma identity and K=1 endpoint checked. The result is a complete infinite proof; finite recurrences are supplementary.

## originality

PASS

Abbar–Arnold–Coine characterizes weighted shifts and power growth ranges, Arnold gives self-improvement exponents, and Cohen et al. establish nonsharp growth estimates. Those accessible statements do not give the same universal exact n-and-K envelope or one simultaneously extremizing positive shift. Full recent primary texts could not be retrieved, so this is a bounded best-of-knowledge comparison, not proof of absence.

## value

PASS

The universal best finite-time power amplification under a natural orbit-average constraint is an exact operator-theoretic extremal problem. The single explicit shift realizing all horizons and the exact asymptotic coefficient are useful independently of already known growth exponents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
