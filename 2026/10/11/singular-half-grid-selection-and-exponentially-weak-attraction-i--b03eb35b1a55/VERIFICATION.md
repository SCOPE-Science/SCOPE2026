---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For every fixed coprime 1≤k<n, the discontinuous limiting rotation G maps half-grid p_j=(j+1/2)/n cyclically by τ. On t within √ε of h=1/(2n), ε=e^{-ah}, the n-return displacement has two dominant contributions ±ε e^{∓at}, with higher sites O(ε³) and propagated error O(aε²). Opposite endpoint signs and derivative 0<(F_a^n)'<1 on that itinerary give a unique local n-cycle. Summing the period equations and using logistic symmetry yields x_{-1}+x_0=O(ε²/a), improving phase t=O(ε). Then δ_{τ(j)}−δ_j=−ε for j=−1, +ε for j=0, O(aε²) otherwise, yielding s_j=±1/2 and x_{a,j}=p_j+s_j ε+O_{n,k}(aε²). Two nearest sites contribute derivative losses aε each and others O(aε³), giving Λ=1−2aε+O_{n,k}(a²ε²). Theorem 3.3 of Bielawski et al. identifies this attracting orbit uniquely via a.e. basin. Independent high-precision calculations for (n,k)=(2,1),(3,1),(5,2),(7,3) at a=24n agree with normalized profiles (error ≤0.00026) and multiplier ratio (≈1 within 1.3e−5). No claim of uniformity as n→∞.

## originality

PASS

PASS for quantified all-rational-rotation half-grid first correction and universal multiplier-gap constant, crediting 2024 theorem for attracting n-cycle existence and attraction. Prior qualitative piecewise rotation does not imply exact error, sign pattern, or exponentially small contraction coefficient. Full most relevant primary article was inspected; other smoothing asymptotic literature remains a risk.

## value

PASS

Near-neutral yet attracting cycles are a natural dynamical phenomenon whose precisely exponential contraction scale is useful for understanding extremely slow local relaxation; the denominator-only leading multiplier and numerator-sensitive half-grid sign pattern separate geometric orbit selection from stability. Valid all coprime k<n (fixed) rather than a numerical anecdote.

The dated certificate retains the supplied scientific assessment, sources and limitations.
