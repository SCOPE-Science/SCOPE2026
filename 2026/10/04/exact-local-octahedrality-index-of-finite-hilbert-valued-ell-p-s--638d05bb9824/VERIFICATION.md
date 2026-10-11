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

For p<=2 a least-norm coordinate plus a Hilbert-orthogonal unit vector gives the lower bound, and the scalar function 1-a^p+(1+a^2)^(p/2) is decreasing. At the balanced base point, concavity of t^(p/2) and convexity of c -> (a^2+c^(2/p))^(p/2) make the symmetric sum maximal at a simplex vertex, yielding the matching upper bound. For p>=2, coordinatewise orthogonal copies give both distances exactly sqrt(2); a one-coordinate base vector and the monotonic scalar bound give the reverse inequality. The p=2 and n=1 boundaries agree.

## originality

PASS

The defining primary source gives only the basic Hilbert value and qualitative sum theory; no checked source implies the exact finite-n phase formula.

## value

PASS

This is a complete exact finite-cardinality classification of a natural quantitative local-octahedrality invariant and exhibits a sharp transition at the Hilbert exponent. The n-dependence below p=2 is structural rather than a small-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
