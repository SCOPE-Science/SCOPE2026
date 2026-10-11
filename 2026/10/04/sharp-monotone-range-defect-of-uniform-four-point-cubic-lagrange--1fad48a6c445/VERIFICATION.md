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

On normalized nodes \(-1,0,1,2\), rewriting the cubic Lagrange interpolant in nonnegative monotone increments gives coefficient ordering \(q_0(t)\ge1\ge q_1(t)\ge0\ge q_2(t)\) throughout \(0\le t\le1\). Linear optimization over the increment simplex therefore makes the lower and upper extrema the step data \((0,0,0,M)\) and \((0,M,M,M)\). The defect is \((t-t^3)/6\), whose unique maximum occurs at \(t=1/\sqrt3\) with value \(\sqrt3/27\); the upper defect is its reflection. The strictly increasing positive witness follows by exact substitution. A fresh dense-grid simplex replay reproduced the two sharp extrema and their reflected locations.

## originality

PASS

Fritsch and Carlson's complete primary paper proves general necessary and sufficient conditions for a single Hermite cubic to be monotone and develops a modified monotone scheme; it does not state the sharp range of the unmodified four-value Lagrange cubic. Berzins explicitly motivates adaptive equal-grid interpolation by the need for data-bounded monotone polynomials, again modifying the local polynomial rather than quantifying the unmodified four-point defect. Current Resultary and exact-constant web searches found no prior statement of the \(\sqrt3/27\) monotone-data range defect or the exact step extremizers.

## value

PASS

The uniform four-point cubic is a canonical local interpolation stencil, while avoiding range and sign violations is a standard shape-preservation objective. The exact \(6.415\%\) worst defect and its extremizing monotone steps provide a precise baseline against which modified monotone schemes can be judged. Although the proof is elementary, the invariant is natural rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
