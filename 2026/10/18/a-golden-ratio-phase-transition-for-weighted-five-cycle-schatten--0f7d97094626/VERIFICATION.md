---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independently expanded the trace: the diagonal-square cross term contributes 2t²(1−t)² times the adjacent products, the two opposite degree-two shifts contribute the same again, and all nonzero net displacements (±2 and ±4 modulo 5) have zero trace. On the simplex tangent space the first sign change is in modes 2 and 3 at q=1/cos(π/5), with no other zero modes; this proves the entire critical polygon. Above the threshold the same negative tangent eigenvalue occurs on the full support and the zero-sum last sine mode of any induced four-vertex path. The three-point path lower bound is 1/2+(q−1)y+(3/2−q)y² ≥ 1/2, with equality only when the middle mass is zero and the endpoints are equal. On the other three-point face, completing the square in the isolated mass z gives z=(2+q)/(6+q) and the remaining term (2−q)(a−b)²/4. Every support of size at most two is contained in one of these faces. Thus all the listed equality sets, arbitrary phases and both endpoints follow. The equal-q choices of t on line 42 are complementary (their odds are reciprocal); the word 'reciprocal' applied to t itself is an editorial slip, not a different transition parameter.

## originality

PASS

Passes on the full q-dependent C5 minimum and equality classification, not on the definition, general trace technique or the classical endpoint extremal value. Inspected closest claims share parts of the method or an endpoint, not the five-cycle classification.

## value

PASS

This is a natural normalized extremal problem on the smallest simple odd cycle with a nonadjacent pair and an induced edge plus an isolated vertex. It gives a sharp boundary between uniform and sparse optimizers, including a positive-dimensional critical family and a separate endpoint degeneration. The transition and equality geometry are not supplied by the endpoint value or by a Fourier stability test alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
