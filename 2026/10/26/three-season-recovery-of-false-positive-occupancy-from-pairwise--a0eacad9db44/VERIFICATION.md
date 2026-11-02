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

For stationary irreducible binary Markov occupancy, E[X]=π and Cov(X_i,X_j)=π(1-π)λ^{j-i}. Conditional independent emissions with common f and discriminations δ_t=d_t-f>0 yield m_t=f+πδ_t, c_ij=π(1-π)δ_iδ_j λ^{j-i}. Because λ≠0 and δ0≠δ2, c01-c12≠0, so normalized adjacent covariances uniquely solve f=(c01*m2-c12*m0)/(c01-c12). Then r01=r12=((1-π)/π)λ and r02=((1-π)/π)λ² imply λ=r02/r01 and π=r02/(r01²+r02); recover d_t,γ,ε algebraically. Direct substitution establishes strict feasibility iff including interior γ,ε and m_t-f>0. With two seasons varying f,π keeps the full bivariate law fixed; with d0=d2 varying f fixes all six moments; λ=0 makes full Y0,Y1,Y2 independent. Independently enumerated all eight hidden paths and eight observed patterns with exact fractions for interior example, reconstructing m=(3/10,19/50,17/50), c=(21/500,63/1250,9/500) and full parameters.

## originality

PASS

Claim-specific Resultary and relevant primary literature were compared by statements and implications. The assessed specialized mathematical statement was not identified as covered in the material actually inspected. This is a best-of-knowledge judgment, not absolute novelty proof; stronger plausible inaccessible works are explicitly retained as priority risks.

## value

PASS

An explicit globally identifiable inverse from only one detection per season and six natural low-order statistics is directly motivated by false-positive ecological occupancy observations. The sharp minimal observation design and outer-detection heterogeneity boundary are independently useful exact methodological facts, not just a known generic HMM parameter-count restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
