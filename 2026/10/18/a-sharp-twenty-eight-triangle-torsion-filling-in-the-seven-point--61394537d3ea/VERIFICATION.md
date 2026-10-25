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

Reconstructed M(K7) with 21 matching edges, 105 1-simplices and 105 2-simplices; independently enumerated all 945 simple 4-cycles and 630 six-label chordless versus 315 seven-label chorded. Source certificate is a 105-long integer primal chain satisfying ∂c=3z with l1=28 and 105-long rational cochain y with ||δy||∞≤1 and <y,3z>=28, proving the minimum for all real (hence integer) fillings when exact checks hold. Inspected source verifier and complete primal/dual coefficient files; independently solved same finite real LP with scipy linprog, obtaining optimum 28.0 (numerical corroboration only). Source exact mod3 rank84 and nonzero class plus published H1(M7;Z)=Z/3 establish generator; S7 transitivity covers all 630 shortest classes.

## originality

PASS

Best-of-knowledge originality assessed by comparing exact mathematical objects, implications and stronger general statements; accessible primary and published sources inspected. Residual priority risk is recorded, and a failed search is not taken as a novelty proof.

## value

PASS

The first torsion matching complex M(K7) is a canonical finite combinatorial object; the minimum exact l1 area filling three times a shortest torsion cycle is a natural torsion filling invariant independent of homology-group order and certified by dual extremality. 630 carrier orbit count adds meaningful geometric classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
