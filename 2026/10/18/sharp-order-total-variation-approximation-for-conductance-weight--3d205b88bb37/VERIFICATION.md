---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Every vertex has exactly one selected outgoing edge. If the undirected image is a spanning tree, precisely one selected edge must be mutual, and all others uniquely point toward that mutual edge. For each mutual e, the choice product equals w(T)c_e/prod_v d_v, hence Pr(H=T)=w(T)sum_{e in T}c_e/prod d_v and Q(T)=P(T)C(T)/mu. This yields TV=E_P|C−mu|/(2mu). Equality of tree laws iff C constant on all trees; fundamental-cycle single-edge exchanges characterize precisely monochromatic conductances on every simple cycle, allowing arbitrary bridges. Reduced weighted Laplacian determinant gives Cov(I_e,I_f)=−c_ec_f(b_e^T L_*^(-1)b_f)^2≤0 for e≠f; thus Var C≤cmax mu and mu≥(n−1)cmin, proving universal upper bound. For chain of m disjoint 1,2,3 triangles linked by bridges, independent triangle selections give X∈{3,4,5} with probabilities 2/11,3/11,6/11 and Var X=72/121; CLT plus uniformly bounded L2 gives sqrt(m) TV→6/(59 sqrt pi)>0. Independently enumerated the rational three-vertex example (TV=7/88), corroborating finite identity only.

## originality

PASS

Best-of-knowledge review of the final claim and stronger implications: specific exact result not found to be subsumed by inspected primary sources; acknowledged overlapping premises and priority risks are itemized.

## value

PASS

Conditioning an independent weighted one-out graph to be a spanning tree is a natural probabilistic ensemble. The exact conductance-sum size-bias density, necessary-and-sufficient equality criterion via graph cycles, dimension-dependent strong total-variation control, and explicit optimal-order sequence form a coherent quantitative comparison to weighted spanning trees, not a routine application of an existing unconditioned coupling theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
