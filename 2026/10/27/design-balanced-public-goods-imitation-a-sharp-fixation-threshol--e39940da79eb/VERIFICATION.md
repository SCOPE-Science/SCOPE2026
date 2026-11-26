---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Averaging edge payoffs gives (r−1)s_i+(r/d)∑_{j≠i}m_ij s_j. In a singleton-cooperator state, equality among defectors determines the off-diagonal row of the pair-count matrix up to a constant; doing this for each row and using symmetry makes the constant global, positive since d>0 and g≥2. Conversely pair balance with d(g−1)=λ(v−1) gives the stated payoff gap, independent of the mixed state. In either strict regime only the disfavored action can change, and one chosen opposite-action pair is jointly incident to an edge, giving at least |γ|/(vdΔ) probability of progress in every mixed state. Hence fixation is almost sure with finite mean, and at zero gap every update is null. The normalization rg−1 at r>1 bounds the payoff range: cooperators earn between r−1 and rg−1, defectors between 0 and r(g−1). On the complete hypergraph the no-opposite-type edge fraction is the binomial ratio, so exchangeability gives the count chain and geometric holding times. For an independent check of the coefficient, set m=v−1, p=g−1, and C equal to the hit probability among p draws. Bonferroni gives 0≤pk/m−C≤binom(p,2)k(k−1)/(m(m−1)) and C≥k/m; thus 1/C=m/(pk)+O_g(1). Splitting v/((v−k)C) into v/(v−k) and v(1−C)/((v−k)C), the second term equals m/(pk)+O_g(1) uniformly for k≤v/2, and also for k>v/2 because 1−C≤(m−k)/m there. The sum is [v+m/p]H_m+O_g(v), which yields the declared leading constant after multiplying by Δ/γ. In the Fano example the line triple leaves six mixed lines with two defectors each; the nonline triple has three mixed lines with one defector each and three with two, and one all-defector line. The incidence totals 12 and 9 give the asserted rates and disprove strong lumpability. The uploaded finite checker was inspected, not executed.

## originality

PASS

The payoff and best-earner mechanism are prior work. The supported distinct contribution is the exact incidence necessity and sufficiency with its fixation consequences for this update, plus the finite complete-hypergraph timing and the witness that this balance alone does not close the count dynamics. The closest same-model primary passages and adjacent indexed records do not provide that analysis.

## value

PASS

The result identifies precisely when two payoff levels suffice for a structural explanation of selection and fixation, yet supplies a small symmetric design showing that payoff sufficiency is not stochastic count sufficiency. The finite-population threshold and the leading exact-update absorption time on complete hypergraphs are useful analytic baselines for the existing imitation model. These comparisons go beyond recalculating a single finite example or importing a well-mixed replicator threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
