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

For a≠0 the two sign-fixed full-period integrating-factor mismatches are nonzero. At zero, the crossing direction is determined by sin t; the only possible tangencies, at 0 and π, force the same sign on both sides and cannot occur on a sign-changing periodic orbit. For upward phase t and downward phase π+r, the two signed arc equations imply (D−C)(t)=(D−C)(r), in the frozen notation. Its derivative 2 sin(t) sinh(a sin(t)) has a strict sign, so r=t. The remaining phase equation has opposite endpoint signs and strictly negative derivative. The constructed integral arc is positive in its interior and the reflected arc matches classically. To verify differentiability of the period map, take two distinct trajectories and write their difference as its initial value times the exponential of the integral of a cos(t) times the secant quotient for |x|. The quotient has magnitude at most one and tends to the orbit sign except at the isolated crossing times. Dominated convergence gives exp(−4a sin θ). The map is increasing, and its opposite-sign translations on the two tails determine the displacement signs on the whole half-lines about its sole fixed point, proving convergence or escape. At a=0 the return map is the identity; minimal period follows there directly from the cosine solution, not from a two-crossing argument. Oddness of the phase displacement and the analytic implicit equation give the stated small-a coefficients. For large positive a, the scaling s=u/a at each endpoint gives the two stated integrals with O(a^−2) scaled error: in an endpoint neighborhood sin s is comparable to s, and the Taylor error in a sin(u/a) is bounded by u^3/(6a^2), integrable against a polynomial times a decaying exponential for the negative exponent. The positive exponent integral is over a bounded scaled interval. Monotonicity brackets the scaled root, and the simple zero of (z+1)e^(−z)−(z−1)e^z gives the phase and multiplier errors. An independent numerical evaluation of c tanh c=1 corroborates c≈1.19967864 and exp(−4c)≈0.00824033.

## originality

PASS

The strongest accessible primary antecedent already treats this equation as a member of its first-harmonic family and gives the two weighted half-maps and a general multiplier formula. These are not new here. Its intersection criterion does not establish the alignment of the crossings for every periodic orbit, the exact count or the global basin in the quadrature slice. The specialized crossing comparison and the positive large-amplitude saturation law are supported distinct contributions. No inspected indexed comparator covers them. This is a best-of-knowledge assessment, not a priority guarantee.

## value

PASS

The quadrature slice is a natural nonaligned first-harmonic case of a family for which only much larger general cycle bounds are available. The result gives a full real-line period-map classification and an exact stability scale. In particular the phase shrinks at the reciprocal parameter scale, leaving a positive limiting multiplier rather than progressively stronger contraction. This is not just a single orbit evaluated at a convenient parameter value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
