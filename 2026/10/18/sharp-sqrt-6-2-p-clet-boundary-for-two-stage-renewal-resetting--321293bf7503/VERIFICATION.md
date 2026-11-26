---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For dimensionless H, the positive-drift hitting-time Laplace transform follows from the bounded solution of the one-dimensional backward equation and equals exp(−u). Conditioning on H gives the Erlang-two within-attempt success probability φ−qφ′; integrating its survival kernel against P(H>s) gives the mean attempt duration 2(1−φ)/q+φ′. Renewal yields the stated quotient A/B, with B>0, zero-rate limit 1/d, and q strictly increasing in u. Its derivative sign is the sign of N=A′B−AB′. Independent symbolic expansion as P(u)exp(u)+R(u) checks the low coefficients and, by the falling-factorial identity, the entire tail formula for n>=7, not merely a finite enumeration. The exact rational root brackets and Descartes' rule order the sign switches of c_6,c_5,c_4,c_3. When c_3<0, dividing by u to the power of the last negative index gives a strictly increasing function from negative to positive, proving the unique minimum below the no-reset mean. At and above sqrt(6), the coefficients are nonnegative with positive tail, proving strict monotonicity. For the critical expansion use the analytic N/u³ at u=0: c_3′(sqrt(6))=8 and c_4(sqrt(6))=3(8−sqrt(6))/2>0. The local implicit root is positive just below critical and is the global stationary point by uniqueness; converting via q=u(u+d) gives the stated slope without requiring numerical localization.

## originality

PASS

The supported distinct result is the all-positive-rate sign classification, the critical equality case and sharp optimizer asymptotic for the same-rate Erlang-two clock and positive drift. Renewal and Laplace-transform ingredients are established. The most closely matching indexed model was checked and concerns a different observable, while primary Poisson, general renewal and frequent gamma-reset results do not yield the classification. This is best-of-knowledge assessment, not proof of priority.

## value

PASS

The first non-memoryless Erlang renewal clock preserves tractability while changing the critical Péclet number in a standard search model. Distinguishing a local small-rate gain from a unique global optimum, or ruling out improvement at every rate including the critical drift, answers the operational rate-choice question. The slope gives the rate scale as the beneficial region closes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
