---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Maximal independent sets on C_n correspond exactly to cyclic words with 1-gaps of 2 or 3. The short-gap obstruction for shattered supports proves n≥3k−1, while explicit directed fillings cover n≡0,±1 mod3, so VCdim=floor((n+1)/3). Independently enumerated concepts, all fixed query supports, and every recursive adaptive partition for C3..C13: final table (13,39,VC4,Ldim5), equal VC/Ldim for n3..12. Inspected actual certificate.json: 31 query nodes, 32 leaf witnesses for depth five; 39 concepts rule out depth six. All 1287 C13 five-query supports checked in source and independently no support shattered. Additivity under disjoint products yields 4m vs5m for m C13 components, hence unbounded gap on vertex-transitive 2-regular graphs.

## originality

PASS

Perrin-type counts of maximal independent sets on cycles and general Littlestone/shattering theory are prior. Neither those counts nor general theorems imply exact membership-query VC dimensions or first adaptive threshold for connected cycles. Semantic searches by independent domination/cycle gap and primary literature did not find a dominating result; residual graph-concept-learning literature risk remains.

## value

PASS

The all-cycle VC formula and sharp C13 first adaptive gap resolve natural graph-learning invariants and yield a vertex-transitive degree-two class with unbounded static-versus-adaptive separation. The exact finite C13 statement is valuable without a claimed general Littlestone formula for n>13.

The dated certificate retains the supplied scientific assessment, sources and limitations.
