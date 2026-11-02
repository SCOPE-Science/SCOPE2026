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

Factor δ(ζ)+s=(3/2+s)(1−λ+(s)ζ)(1−λ−(s)ζ) with λ±=1/[2(1∓sqrt(1−2s)/2)] and differentiate the analytic logarithmic generating ratio. Then w0=log[(3/2+hb)/(3/2+ha)]>0, w_n=(p_n(ha)−p_n(hb))/n (n>=1), p_n=λ+^n+λ−^n. For s<=1/2, p_n(s) decreases strictly and p_n>=2^(1−n). For s>1/2, complex-conjugate eigenvalues have modulus (3+2s)^(−1/2)<1/2. Thus all weights positive iff ha<=1/2. For ha>1/2, the slower endpoint dominates exponentially and cos(nθ_ha) attains positive and negative values bounded from zero along infinite integer subsequences; both signs recur. Independent rational logarithmic-derivative series confirmed 50 exact coefficients for four parameter cases on both sides and at the boundary. Infinite sign recurrence follows analytically, not from finite tests.

## originality

PASS

Best-of-knowledge exact statement and implication comparison: closest accessible primary papers and ranked published findings do not establish this precise claim under the stated parameters. This is not a historical-priority certificate; see source inspections and risks.

## value

PASS

Exact coefficientwise positivity is the precise condition for positivity preservation of arbitrary nonnegative discrete causal inputs and is stronger than positive-definiteness of quadratic forms. The sharp slow-endpoint threshold explains why broad high-frequency relaxation mixtures can remain positive and why all finite-horizon sign checks can miss eventual oscillation. This natural all-order design criterion has independent mathematical and numerical-analysis value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
