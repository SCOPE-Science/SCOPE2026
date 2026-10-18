---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For a norming pair (x,x*) and every y∈B_X, each z with x*(z)=1 satisfies ||z-y||≥1-x*(y); equality is attained exactly by z=y+(1-x*(y))x. Infimizing gives eta_X(epsilon,(x,x*))=upsilon_X(epsilon,(x,x*)) with no compactness assumption. Under symmetric Birkhoff orthogonality w=y-x*(y)x is orthogonal to x in Birkhoff sense, so ||w||≤||y||≤1; then ||x-y||≤2-x*(y) establishes eta_X(epsilon)≥max(0,epsilon-1). In the hexagonal norm N(s,t)=max(|s|,|t|,|s-t|), quarter-turn of the polar hexagon establishes Birkhoff symmetry; y=(1,epsilon) for epsilon≤1 and y=(2-epsilon,1) for epsilon≥1 meet the lower envelope identically. Inspected full source verify.py and independently evaluated the exact rational unit-ball witnesses; the 401-point grid is supplementary, not the continuum proof. The claim is for real Banach spaces; boundary epsilon=0,1,2 is covered.

## originality

PASS

The defining 2023 source proves only 2delta_X≤upsilon_X≤eta_X and computes the Hilbert-space value; the 2024 follow-up still uses one-sided inequalities and special endpoint conclusions. No inspected source states universal equality or this exact Radon hexagon profile. The identity is elementary as an affine-hyperplane distance formula, so equivalence under an unnamed convex-analysis formulation is a genuine priority risk.

## value

PASS

Eliminates a distinct-seeming auxiliary geometric index in all real Banach spaces and supplies a sharp structural lower bound for the natural symmetric-Birkhoff/Radon class. A standard non-Hilbert extremal plane has a flat-then-linear exact function, in sharp contrast to the Hilbert quadratic profile; this is a motivated geometric benchmark rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
