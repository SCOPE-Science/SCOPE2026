---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The proof reduces all quadrilaterals to the four listed facets of \(Q_{p,q}\), \(0<p\le q\le1\). Direct exact symbolic simplification separately confirms that the three lower-bound weights sum to one, their weighted facet normals vanish, and the four witness constraint slacks are \(0,0,(1-q^2)/q,0\). The unbounded, continuous parameter region is covered by the algebraic proof, not by sampling.

Run `python checks/verify.py` from the directory containing this document. This dependency-free Python program enumerates full-rank intersections of triples of the actual four inequalities in \((z_x,z_y,s)\), minimizes the objective over feasible intersections, and independently verifies all four constraints for the proposed witness. Output observed: `PASS: 64 exact rational full-LP vertex enumerations and candidate feasibility certificates`; `PASS: both parameter orderings, symmetric and nonsymmetric boundary cases`.

All arithmetic in these tests uses `fractions.Fraction`. Tested ratios are drawn independently from \(\{1/11,1/7,1/5,1/3,1/2,3/4,9/10,1\}\). The code performs exact finite checks, not an exhaustive verification of real parameters. No third-party certificate was used, and independent external review remains unperformed.
