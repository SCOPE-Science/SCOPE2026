---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The all-dimensional proof is given in `RESULT.md`.

Critical checks:
- a radius-\(\rho\) shift changes coordinate bounds by \(\rho\) and each chainlink bound by \(\rho\sqrt2\);
- translating \(x_i\) by \(\rho\) gives a difference-constraints system with one auxiliary zero vertex;
- every simple directed cycle is either a zero-node cycle corresponding to one cyclic interval or the full directed ring;
- the weight of an interval cycle is
  \[
  \sum_{k\in I}a_k-(|I|-1)l-\rho\bigl(2+(|I|-1)\sqrt2\bigr);
  \]
- the full-ring weight is
  \[
  \sum_i a_i-sl-s\rho\sqrt2;
  \]
- the standard no-negative-cycle lemma is proved in the result, making the barrier conditions necessary and sufficient;
- a zero-weight minimizing cycle forces all constituent shifted inequalities to be equalities;
- for equal parts, the interval barriers form a monotone linear-fractional sequence and reduce to the two endpoint values \(a/2\) and \((a-l)/\sqrt2\).

`verify.py` independently solves the complete Chebyshev linear program by generic active-set enumeration for deterministic compositions in dimensions two through four, then compares the optimum with the barrier formula. It separately checks the homogeneous collapse in dimensions through twelve. The finite replay is corroborative only and does not assess originality.
