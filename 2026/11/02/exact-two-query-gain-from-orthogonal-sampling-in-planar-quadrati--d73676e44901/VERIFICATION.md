---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The claim covers every planar SPD Q, deterministic start, and two *sequential exact* line minimizations. Whitening Q reduces one step to a Euclidean rank-one projection; integrating over angle gives independent-pair D and orthogonal-pair C, with C=((κ−1)/(κ+1))²D as full matrices (not isotropically averaged starts). An independent midpoint quadrature with 100,000 angles at κ=1,1.2,2,4,9,49 reproduced the entire matrix identity to <3e−8. Partial-fraction/angular formulas in RESULT.md establish it for continuum κ; κ=1 handled separately.

## originality

PASS

Convergence bounds for finite-difference Haar subspace gradient steps are not two *sequential exact line minimizations*. A PDF-level inspection of Kozak et al. says the backtracking line-search analysis was not covered and its quadratic specialization merits tailored study. Thus its claimed generality does not imply the orientation-uniform two-query matrix coefficient. General projection formulas remain a priority risk.

## value

PASS

The exact relative benefit of paired orthogonal versus independent direction queries at fixed condition number is a natural design quantity for randomized direction optimization; the universal-in-start gain and κ→1/∞ regimes are meaningful, although restricted to dimension two and exact line searches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
