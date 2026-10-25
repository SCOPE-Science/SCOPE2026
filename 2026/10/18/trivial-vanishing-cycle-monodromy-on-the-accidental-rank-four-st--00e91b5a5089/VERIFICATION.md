---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Read source matrix and exact symbolic verifier from actual Git blobs. Independently expanded det M under polynomial coordinates a=x,b=v,d=y-w,s=w,t=z and verified F/2=(s²-4)(a²+b²-tab)+(t²-4)d²+a²b²+a²d²+2sa²d-stabd. Computed normal 3x3 Hessian with determinant -16(s²-4)²(t²-4)², nonzero throughout S, and verified tangential Hessian zero. Parametrized holomorphic Morse lemma yields smooth 2D factor times transverse complex A1 surface node. A1 Milnor fiber retracts to S²; the integral rank-one vanishing cohomology is twisted by orientation of the quadratic normal bundle. Global normal trivialization and algebraic square root 4i(s²-4)(t²-4) split the determinant double cover on the whole twice-punctured parameter base, establishing trivial monodromy along the stratum (NOT smoothing-parameter Picard–Lefschetz sign). A1 link RP³ is a rational homology sphere so product is rationally smooth. No claim about excluded rank-drop or full character variety.

## originality

PASS

Hikami locates the accidental rank-four locus in a determinantal quintic, but does not compute its normal Hessian, A1 analytic type, integral orientation/vanishing local system or rational smoothness in the inspected same-object primary sections. Generic Morse theory supplies technique, not the explicit global discriminant square. Related SCOPE transverse A1 result concerns a different six-point conic determinant. Simpson five-puncture Betti-fibration chapter is plausible broader overlap, but complete text could not be obtained from OA HAL (blocked) or authorized institutional access (VPN disconnected); no whole-chapter noncoverage claim.

## value

PASS

The global monodromy of the integral vanishing lattice on a non-simply-connected singular stratum is a natural refinement beyond a local A1 classification. The unexpected global square class and rational smoothness are exact geometric invariants of a specified interesting determinantal character-variety model. Their distinction from smoothing-parameter monodromy is mathematically substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
