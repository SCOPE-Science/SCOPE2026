---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For three distinct directed two-species reactions with source and product total molecularity <=4 and strictly positive rate constants, writing N=product-X minus reactant-X, M analogously for Y, and U=N times reactant-X order, the rank-two positive-flux fold condition reduces to an all-same-strict-sign cross product N x U and M dot (N x U)=0. The integer moments n20, n01, m10, m01 impose n20 !=0, n01*m10<0, m01>0; arbitrary positive null flux can be realized at a chosen positive (x,y) by rates k_r=v_r/(x^a y^b). A separately written exact enumeration over unordered reaction triples independently reproduced the source counts: degree 2 0, degree 3 82 positive-null/16 fold/11 negative/5 zero/0 positive and degree 4 1590 positive-null/350 fold/278 negative/63 zero/9 positive, with 210 directed reactions and 1,521,520 triples at degree 4. Archived nine-row data were inspected; witness equilibrium x*=beta/(2 gamma y*), y*=(beta^2/(4 alpha gamma))^(1/3), Jacobian trace eps*alpha*y*>0 and determinant 3eps*alpha*beta*y*>0 for all positive rates. Complete finite classification is for labelled reaction sets, NOT a theorem about all canard dynamics.

## originality

PASS

The prior Beldiman–Halanay classification supplies the flux and rank criteria and all degree-three examples, finding no positive slow trace. The nine positive-trace degree-four labelled networks, their table and minimal reactant-degree distinction are a new bounded extension relative to the inspected primary sections. Banaji–Boros–Hofbauer quadratic-sourced Hopf examples do not imply these rank-two pinned folds. Best-of-knowledge only; a separately indexed degree-four census could exist.

## value

PASS

A sharp first molecularity threshold and complete finite classification of minimal three-reaction planar mass-action pinned folds gives a structural boundary for network design, with explicit positive-trace witnesses. The nine count is motivated by the natural degree-four frontier beyond a published complete degree-three classification and is not presented as a Hopf bifurcation result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
