---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For nonnegative nondecreasing data on \(P_n\), every fixed-radius centered ball average is nondecreasing as the center moves right: an interval either shifts right, gains a new largest value, loses an old smallest value, or is unchanged. The pointwise maximum over radii is therefore nondecreasing. At the left endpoint its maximal value is the global mean, while at the right endpoint it is the terminal value. Hence \(\operatorname{Var}(Mf)=f(n)-\overline f\). The elementary bound \(\overline f\ge((n-1)f(1)+f(n))/n\) gives the sharp factor \(1-1/n\), and equality for nonconstant data forces \(f(1)=\cdots=f(n-1)<f(n)\). Reflection gives the nonincreasing case. This proves the quantified theorem symbolically; finite checks are not needed for the infinite statement.

## originality

PASS

The complete primary preprint formulates the path constant \(1-1/n\) as an open conjecture and reports computation only for small paths. Full-text searches in this round found no occurrence of 'monotone' or 'nondecreasing', and no theorem giving the endpoint-minus-mean identity or equality cases. Resultary returned the submitted record as the direct exact match and no earlier equivalent finite-path monotone theorem. The claim therefore establishes a genuine structured all-size slice of the open conjecture.

## value

PASS

The theorem proves the conjectured sharp factor for every path size on a natural structured class, identifies its extremizers, and shows that any counterexample to the full conjecture must be genuinely oscillatory. That materially narrows an explicitly open problem rather than merely checking more small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
