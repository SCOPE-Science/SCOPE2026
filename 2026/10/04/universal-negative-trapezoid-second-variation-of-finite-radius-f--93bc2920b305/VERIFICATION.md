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

The exact polar-area formula and affine Funk-ball parametrization reduce the volume to the one-dimensional analytic integral displayed in RESULT.md. Differentiation at \((\delta,s)=(0,0)\) gives the three Hessian entries. Since \(V_{ss}>0\), the minimizing center is an analytic implicit branch and the optimized second variation is the stated Schur complement. Its numerator is a quadratic in \(A=\operatorname{artanh}\lambda\) with positive leading coefficient and upper root below \(\lambda\), while \(A>\lambda\); hence the second variation is strictly negative for every finite radius. The finite quadrature verifier agrees with the three closed Hessian formulas at representative radii but is not used for the universal sign.

## originality

PASS

Faifman's finite-radius work gives the general volume identity and extremal results for unconditional bodies, while Faifman--Vernicos--Walsh prove regular-polygon extremality for a large-radius coefficient after optimal centering. The latter explicitly leaves the analogous finite-radius polygon-volume extremum open. Neither inspected source gives a finite-radius shape Hessian for nonsymmetric trapezoid perturbations or the center-response coefficient. Fresh Resultary search found the audited theorem as the only direct exact hit.

## value

PASS

The theorem gives an exact all-radii local answer in the simplest full affine deformation family beyond parallelograms for a finite-radius extremal problem that the polygon literature leaves open globally. The moving-center coefficient and strict curvature are natural local invariants, not a sampled numerical effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
