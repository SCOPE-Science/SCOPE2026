---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For all connected weight designs, log(det grounded Laplacian) is strictly concave in the full edge vector because the grounded edge-incidence map determines each edge weight. The unique design must respect the stabilizer of the exceptional edge. Three conductance classes a,b,c yield nonzero Laplacian eigenvalues s=2a+(n-2)b, nb, and t=2b+(n-2)c with multiplicity n-3, giving exact tau=b*s*t^(n-3). Euler homogeneity fixes lambda=(n-1)/B. Full KKT equations solve to the displayed positive a,b,c for r<(n-1)/(n-2) and to a=0, b=2B/(n-1)^2, c=2B(n-3)/((n-1)^2(n-2)) otherwise. At a=0 the derivative 2/((n-2)b) <=lambda r holds exactly above the threshold; uniqueness follows including equality. Independently computed grounded minors, budgets and every original edge-gradient KKT condition in 16 exact rational test cases; tests corroborate the all-n argument.

## originality

PASS

Osting–Brune–Osher derive general Laplacian D-optimal spanning-tree objectives, and Harman–Benková provide general constrained D-optimal equivalence/KKT machinery. Neither inspected result evaluates the full K_n single-edge price allocation and sharp (n-1)/(n-2) active-set threshold. The calculation is a specialization of known tools but the all-parameter explicit design and one-edge support transition are not mechanically stated in inspected literature.

## value

PASS

An exact cost premium above 1+1/(n-2) deletes one pairwise comparison entirely from the determinant-optimal fully connected information network, while all other edges remain active. The threshold and all weights for every n and positive budget/price are natural experimental-design invariants and identify a sharp support phase transition, rather than a selected numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
