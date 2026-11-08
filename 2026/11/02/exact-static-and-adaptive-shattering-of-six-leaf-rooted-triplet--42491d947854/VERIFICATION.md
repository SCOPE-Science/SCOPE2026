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

Root-bipartition recursion yields (2n−3)!! distinct rooted binary tree cluster systems; the 60 queries ab|c are true exactly when some proper cluster contains a,b but not c. Independent reconstruction generated all 945 trees and query incidence masks. Fixing the first query by S6 relabeling, an exhaustive canonical shattered-support recursion found counts of sizes 1..5 equal 1,57,1458,18144,0, giving VC=4. The actual frozen depth9_certificate.json was independently traversed against reconstructed tree masks: 511 internal nodes, 512 distinct consistent leaf concepts, so Ldim≥9; 945<1024 excludes 10. Attached original checker also handles n=3,4,5. Zero response allows either other triplet topology, not a specified multiclass alternative; this convention is essential.

## originality

PASS

Tree Learning: Optimal Sample Complexity and Algorithms gives Natarajan n−2 and multiclass Littlestone order n log n, with two fixed labels per query; those results are not the Boolean one-vs-rest notion and do not force the exact 945-tree figures. Other rooted-tree encoding and triplet-consistency complexity results are about different invariants.

## value

PASS

Exact adaptive depth nine attaining the information-theoretic limit and five-unit VC/Littlestone gap in the natural six-leaf labeled phylogeny hypothesis space show substantial structural offline/online distinction. This is a meaningful finite cutoff with 945 hypotheses and an exhaustive certificate, not an arbitrary tiny sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
