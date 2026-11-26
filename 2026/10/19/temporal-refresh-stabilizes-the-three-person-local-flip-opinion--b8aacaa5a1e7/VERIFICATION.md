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

Expanding the cubic gives z'=zC(z²,a,b), with centered independent uniform contributions of widths 3(1-z²)/2 and (3+z²)/2. Squaring and using variance 1/12 gives the stated quadratic in z², bounded sharply by 3/8 as nonzero states approach the tie. Geometric decay of the second moment gives almost-sure convergence by summable tail probabilities and forces every invariant law to have zero second moment. Conditional on each past, reflecting both uniforms changes C to -C and the b-slope stays at least 3/2 in magnitude, so C has no atom at zero even at |z|=1. From a nonzero initial imbalance all finite-time signs are therefore conditionally fair given the whole past and jointly independent. The same b-slope gives uniformly bounded log-squared moments by integrating on [-3/2,3/2]; this gives uniform integrability and continuity of the mean log multiplier. The series of centered increments weighted by 1/(t+1) converges in the square-integrable martingale argument, so its unweighted averages tend to zero. The triangular density 2(1-s) of |1-a-b| then gives h(0)=log(3/2)-3/2. This is a geometric mean pathwise rate, not a deterministic one-step ratio; the sign and log-rate assertions exclude the fixed tie. The two frozen corner triangles have total area 1/9. Proof reviewed at RESULT.md §§1–4; the finite identity tests and simulation in verify_temporal_galam.py were inspected as supplemental, not executed or relied upon.

## originality

PASS

The supported distinct claim concerns independent common renewal at each round and the joint conclusion of almost-sure tie, exact nonlinear Lyapunov exponent, and independent fair majority signs. The polynomial update and the 1/9 frozen contrast are not new. The strongest inspected random-iteration matches concern other maps or different temporal laws; best-of-knowledge assessment, not an exhaustive priority claim.

## value

PASS

Separating static random parameters from common temporal refresh is a substantive modeling distinction. An exact almost-sure decay exponent and independent sign fluctuations despite a vanishing majority margin identify the behavior more precisely than stability of the tie or a generic negative-drift criterion. No conclusion about finite populations or arbitrary renewal laws is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
