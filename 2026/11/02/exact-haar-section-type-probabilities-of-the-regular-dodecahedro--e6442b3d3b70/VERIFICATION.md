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

# Reproducible verification

Extract `check.py` from the same package and run `python3 check.py` with Python 3; it has no third-party dependencies. The expected final output is `EXACT_ALGEBRAIC_ARRANGEMENT_CERTIFICATE_PASSED`, after listing the \(6\)-, \(8\)- and \(10\)-vertex probabilities.

The checker works in exact coordinates \((a,b)\leftrightarrow a+b\varphi\) with \(\varphi^2=\varphi+1\) and \(\varphi=(1+\sqrt5)/2\). It proves the strict rational bounds on \(\varphi\) by squaring \(2\varphi-1=\sqrt5\). Every sign predicate either follows from those certified bounds or halts without a PASS. Exhaustively it builds 20 vertices, 30 edges, 10 antipodal normal representatives, 45 pairwise great-circle intersections with two antipodal rays each, and 1024 candidate sign patterns. The absence of triple intersections is checked exactly. The program uses those exact predicates to certify 20 spherical hexagons with six-sided sections, 60 spherical triangles with eight-sided sections, and 12 spherical pentagons with ten-sided sections. The verified interior-angle dot products give the exact spherical areas via Girard's theorem. Floating-point evaluation appears only after this exact classification, for user-facing decimal values.

The proof that all spherical chamber vertices appear among pairwise great-circle intersections, and that the sign-discordant edges bijectively give polygon vertices, is provided in RESULT.md. The generic ten-circle region-count check independently gives 92. The output does **not** assert machine-checked mathematical formalization, independent validation, historical uniqueness, or the analogous result for noncentral planes.
