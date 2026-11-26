---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently reduced the unit-gap constraint on the class-constant mean-zero subspace using coordinates (peripheral value minus hub, pendant minus hub). The energy slack has diagonal k(a−2/(k+2)), c−(k+1)/(k+2) and off-diagonal k/(k+2); its PSD condition gives exactly a>2/(k+2), c≥c(a). The transverse modes require a+kb≥1. Permutation averaging preserves cost and cannot lower the gap. Positive prices force the lower bounds on b,c in the reduced optimum. On each side of a=1 the cost has positive second derivative, and the kink is upward. The left and right slopes there are kP−R/k−(k−1)Q/2 and kP−R/k. I checked the two stationary-point cost formulas by symbolic substitution, and the slopes give both stated threshold equalities, including a=c=1 and b=0 at R=k²P. For unrestricted uniqueness the quotient unit eigenvector of the average retains its Rayleigh energy under any optimum. Its nonzero edge differences force every hub rate; then either b=0 by nonnegativity or the peripheral compression has lower bound I and trace k−1, forcing equal peripheral weights. Budget scaling is exact by homogeneity.

## originality

PASS

Pass for the full independent-price phase diagram and rigidity, not for the equal-price pendant/spoke slice. The prior pendant-clique result is a genuine theorem-level overlap, but its two-price theorem is not sufficient for the new competing branch at R>k²P, nor for its transition and unrestricted uniqueness over the independent three-price space. The general convex program and symmetry method are established prior work.

## value

PASS

Independent edge prices are natural for budgeted diffusion. The theorem tells when an entire edge class should be dropped, separates the two distinct zero-peripheral-rate behaviors, and certifies uniqueness over individual edge rates even at the boundaries. These are useful exact design facts beyond the known equal-price slice or a numerical SDP solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
