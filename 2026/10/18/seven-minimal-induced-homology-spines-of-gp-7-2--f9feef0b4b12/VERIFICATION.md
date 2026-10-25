---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Build GP(7,2) with 7 outer cycle edges, 7 spokes, 7 inner +2 edges. Enumerating all independent faces gives f=(14,70,154,147,49), 434 nonempty. From actual certificate.json, all 134 ordered elementary free-face pairs were independently checked against the complete live face set; exactly the 166 faces of the induced 11-vertex complex W0 deleting v0,v1,v2 remain. Rotations yield seven analogous collapses. The separate 82-pair matched Hasse diagram on W0 was recomputed and topologically sorted across 166 faces, acyclic with exactly one critical vertex and one critical 3-cell, so W0 and whole K are integrally S3. For obstruction K-u0, 3-boundary rank 73 and 4-boundary rank 32 out of 105 3-simplices imply H3(F2)=0; for K-{v0,v3}, 55+23=78 gives H3(F2)=0. Every subset of missing inner indices without a pair at cyclic distance 3 lies in a 3-consecutive set (all 128 checked); a noncarrier lies in one of the two obstruction types. Their zero mod-2 H3 rules out rational H3, hence no nonzero image into ambient Z. Conversely W containing some Wi composes with its inclusion isomorphism and is a carrier. Exactly seven Wi are inclusion-minimal.

## originality

PASS

Best-of-knowledge PASS: Barmak develops independence-complex topology of cycles/forests and structural moves, not this seven-support iff criterion. Besharati-Ebrahimi-Azadi study maximum independent-set cardinalities of generalized Petersen graphs, not induced homology or collapses. Resultary Petersen higher-independence S3 computation is for GP(5,2), a different graph and higher-independence parameter.

## value

PASS

A complete, nontrivial classification of the vertex-minimal supports of a natural integral homology generator, plus explicit simple-homotopy spines, for a standard generalized Petersen graph. It resolves a natural support-complexity question not encoded by the ordinary independence number and demonstrates robust local carriers for a global S3 class. Useful even without a general GP(n,2) theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
