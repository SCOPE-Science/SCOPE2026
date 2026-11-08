---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The biquadratic function field k(x)(sqrt(P),sqrt(Q)) is degree 4 since branch loci disjoint; its eight simple branch values yield genus5 by Riemann–Hurwitz. The affine singularity equations force y=0, P−Q=0, and P=Q nonzero at such points. The local exact square-root change y sqrt(2(P+Q)-y²) reduces equation to v²−(P−Q)²; a multiplicity-e root gives A_{2e−1}. Homogenization with quartic P4,Q4 and cubic D3 gives at (0:1:0) completed v²−u⁴ and at (1:0:0), when d<3, v²−u^{2(3−d)}; no other infinite singularities. Two smooth branches intersect at order e and sum delta=5. Independent exact symbolic quartics P=x^4+x+1, Q=P−D for all seven root partitions have squarefree coprime branch quartics (nonzero Q discriminants), supporting nonemptiness. The local proof covers unrestricted parameters; seven examples alone do not.

## originality

PASS

Kudo (2024) constructs precisely this sextic, proves genus/irreducibility, locates singular supports and supplies seven support-count patterns, all credited. The inspected primary Proposition 4.1.3, 4.1.4 and Table 1 do not state exact A_{2e-1} analytic forms, delta and Tjurina invariants or no-cusp classification. An equivalent computation in a journal edition is a material priority risk.

## value

PASS

The completed local analytic classification refines a published singular support table into explicit ADE equisingularity strata, contact orders and genus defects, which determine resolution and deformation behavior of a natural genus-five cover construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
