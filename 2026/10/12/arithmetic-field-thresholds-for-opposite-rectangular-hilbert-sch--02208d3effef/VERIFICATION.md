---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For characteristic-zero K and d≥3, equality of weighted Hilbert functions of (x²,y^d) and (x^d,y²) forces weight u=v; opposite lex degree-two terms force f=Ax²+Bxy+Cy² with A,C≠0. Pure last-degree initial generators and colength give I=(f,x^d), y^d∈I. Degree-d quotient identifies with K[t]/(A+Bt+Ct²), and t^d scalar implies distinct nonzero roots α,β in characteristic zero with (α/β)^d=1 and trace ζ+ζ⁻¹∈K. Conversely g=t²−(ζ+ζ⁻¹)t+1 (ζ≠−1), or t²−1, constructs the edge. Rational traces yield orders 2,3,4,6, so rational iff 2|d or 3|d; real traces exist for all d. For odd d the smallest prime p|d minimizes φ(m)/2 to (p−1)/2 and Q(ζ_p+ζ_p⁻¹) attains it. Traces are exact, not numerical. The standard-library checker was read: finite cases do not establish universal statement.

## originality

PASS

Best-of-knowledge PASS. Hering–Maclagan Example 2.11 already gives the d=5 real-versus-rational phenomenon. Maclagan–Silversmith Example 2.3 gives a sufficient degree-two-factor condition, and Silversmith Theorem 5.11 describes complex edge components. The assessed unrestricted necessity for K-rational edges and sharp number-field degree for every d go beyond these inspected geometric/sufficient statements.

## value

PASS

PASS: the arithmetic obstruction and optimal field degree solve a natural rationality problem of coordinate-torus 1-orbits between two fixed Hilbert-scheme monomial points, explaining and classifying the previously known d=5 discrepancy for every d, rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
