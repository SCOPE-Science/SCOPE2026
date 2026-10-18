---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

In the A_{m-1} incidence lattice the cycle edge vectors have the unique primitive linear relation sum_i s_i v_i=0, and any m-1 edges form a unimodular tree basis. For imbalance r=|p-q|>0 the vectors (v_i,1) generate an index-r sublattice, so Q_C is a full (m-1)-simplex of normalized volume r. The r fundamental-parallelepiped class representatives have heights 0,a+1,...,b-1, giving h*(Q_C)=1+sum_{k=a+1}^{b-1} t^k. For p=q the affine relation gives dimension m-2 and an oriented-circuit spanning-tree triangulation h*=sum_{k=0}^{a-1}t^k. Adding the origin gives a unimodular oriented-circuit triangulation of h*=sum_{k=0}^{b-1}t^k; in the balanced case a lattice pyramid. Checked the proof's integral index argument and read the actual verifier which checks exact determinants for every orientation through m=8; the all-m conclusions come from the primitive cycle relation, not finite enumeration.

## originality

PASS

Kálmán–Tóthmérész's 2021/2022 primary source develops root-polytope dimensions and semi-balanced digraph theory and remarks that unsemibalanced cycle simplices are nonunimodular without distinguishing imbalance 1; the present exact determinant is 1 precisely when imbalance 1. The later h*-vector and interior-polynomial works cover more general digraph constructions but do not state the full pair of elementary orientation-imbalance formulas in the inspected material. A general circuit-lattice theorem could imply these as a special case, and that is a genuine residual risk, but no actual stronger coefficient theorem was found in the closely relevant full text.

## value

PASS

This naturally completes the single oriented-cycle family with full Ehrhart h* polynomials for both ordinary and extended root polytopes, identifies orientation-independent placement effects, and corrects the earlier blanket nonunimodularity statement at imbalance 1. It is a meaningful complete classification and a usable base case for graph-root-polytope theory, not a random tabulated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
