---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed 10-vertex Kneser/disjointness Petersen adjacency, component-bound filtration on all 1023 nonempty masks, ordered exact F2 simplicial boundary column reduction (511 pivot pairs), reduced intervals 4*[degree2,1,2), [degree3,2,5),10*[degree3,4,5),61*[degree4,5,6),74*[degree5,6,7),36*[degree6,7,8),9*[degree7,8,9),[degree8,9,10). The pair certificate from actual collapse_pairs.json was replayed: each of 60 low faces has exactly one remaining strict coface, all removed faces outside K2, 380-120=260 faces remain. These are exhaustive finite-domain proofs, not samples; no integral barcode inferred.

## originality

PASS

The ordinary r=1 homology and isolated r=2=S^3 calculation are prior. Full filtration ranks/inclusion maps, persistence intervals above r=2 and 60 relative elementary collapses do not follow just from those snapshot homotopy types. A different Petersen Čech/Rips metric filtration has different simplices/parameter; its barcode is not a reduction to this component-size filtration.

## value

PASS

This is a complete, natural higher-independence filtration invariant of the canonical Petersen graph. It distinguishes a 3-dimensional interval persisting from r=2 to r=5 from ten transient 3D intervals at r=4 and proves K3 collapses onto K2 integrally. The finite scope is a complete, motivated classification rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
