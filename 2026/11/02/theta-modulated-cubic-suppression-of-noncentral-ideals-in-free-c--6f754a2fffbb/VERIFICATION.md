---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

An ideal I of free class-two L_d=V_d⊕Λ²V_d is equivalent to A=π(I)≤V, W=I∩Λ²V≥A∧V and a graph of a lift A→(Λ²V)/W. For a=dim A and m_a=binom(d−a,2), this gives T_{a,d}=[d:a]_q Σ_{c=0}^{m_a}[m_a:c]_q q^{ac}. The central count is Σ_c[N:c]_q; a=1 has M=binom(d−1,2), q^{d−1}/(1−q^{-1}) multiplier asymptotically. Gaussian coefficients are q^{c(n−c)}/P∞ (1+o(1)) at their peaks, yielding theta_(n+h parity) q^{(n+h)^2/4}/P∞. The exponent difference is exactly −d³/4+d²−d/2. Convex endpoint bounds on m_a+a and a(d−a) control every a≥2 by an exponent Δ_d~d³/4, so rank-one ideals dominate all noncentral ideals and the stated probability with four-class theta modulation follows. q fixed; finite diagnostics alone do not certify d→∞.

## originality

PASS

Qualified PASS: 2023/2024 Carnevale–Schein–Voll's complete primary ideal-zeta machinery for free class-two nilpotent Lie rings is credited as strongly covering fixed-rank ideal counts and methods. Inspection of its introduction and Section 5.2 Example 5.4 did not find a fixed-q, growing-generator-rank uniform-random-ideal theta asymptotic or conditional rank-one law. Published fixed-rank zeta formulae may allow derivation after new asymptotic analysis and an unobserved implicit version is a significant residual risk.

## value

PASS

Uniform sampling from the full ideal lattice of a canonical family is a natural probability problem in nilpotent algebra. The cubic exponent and genuinely d mod4 theta prefactor quantify the rarity of noncentral ideals, while conditional rank-one concentration identifies their mechanism; this is substantially more than recomputing a fixed-rank ideal zeta count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
