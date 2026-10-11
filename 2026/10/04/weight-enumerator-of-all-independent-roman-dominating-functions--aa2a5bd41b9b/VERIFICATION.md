---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Independence forces all positive labels into one part. A zero left in that same part would have no positive neighbor, so the entire chosen part must be positive; zeros outside are defended exactly when at least one chosen vertex is labeled 2. This gives the displayed binomial summand for each part. The reconstruction argument is triangular in descending part size because the coefficient at degree twice the largest part size counts precisely the largest parts. I independently compared the literal definition to the classifier on every ordered multipartite composition through order seven, totaling 164682 labelings, and matched the polynomial histograms for all such profiles; the packaged verifier extends its own census through order nine.

## originality

PASS

The primary independent-Roman literature inspected studies minimum parameters, bounds, extremal trees and Nordhaus-Gaddum relations, not an all-function weight polynomial on arbitrary complete multipartite graphs. A later note improves scalar bounds. Resultary and exact polynomial searches found no covering enumerator or reconstruction theorem; the scalar minimum is not relied upon for originality.

## value

PASS

Although the feasibility proof is short, the exact all-function polynomial is a natural invariant of a canonical graph family and has a nontrivial reconstruction consequence: within connected complete multipartite graphs it determines the graph up to isomorphism. That makes the result more than a routine minimum calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
