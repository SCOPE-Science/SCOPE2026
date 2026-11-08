---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

At a word with x rotations and even positive y reflections, the rotation exponent is x−2j mod n for any 0≤j≤x by placement in alternating reflection gaps. Hence identity counts are: y=0 iff n|x; odd y never; positive even y with n even iff x even; with n odd iff x even or x≥n. Myhill–Nerode equivalence of commutative language prefixes is exactly equality of these shifted (x+u,y+v) predicates. For even n≥4, y=0 yields n congruence classes and y>0 yields four disjoint parity classes, each separated with specified suffixes; n=2 merges to four parity classes. For odd n≥3, the y=0 classes are n−1 short-tail states and n residue-cycle states, and y>0 gives 2n classes from y-parity and saturation min(x,n−1). Long a-suffixes/b² test separate the families. Thus 4n−1; original Cayley DFA is 2n by positive inverses. No experimental range is presented as proof. Independent from-scratch group-product dynamic programming found 2290 agreement triples for n=2..26, and independently enumerated pairwise distinguishable suffix signatures with b-suffix lengths 0,1,2 for all quotient witnesses n=2..54, recovering all claimed state counts. All source paths/7 blob identities and tree SHA validated against Git tree.

## originality

PASS

Best-of-knowledge PASS on the exact dihedral rotation/reflection identity-language all-parameter quotient count. Three primary works inspected on actual theorem statements: 2013 regularity/polynomial-of-group-languages, Hoffmann 2020 product upper bounds, Hoffmann 2021 shuffle regularity and upper bounds. None implies the exact minimal 4n−1/n+4 pattern; 2013 S3 and D4 examples use different acceptance predicates. Several Resultary semantic searches mostly returned dihedral homology and automata compression, not equivalent identity language. Unindexed or otherwise inaccessible work may still cover it; absence of hits is no proof of novelty.

## value

PASS

This is a complete all-n exact state-complexity classification for a canonical, naturally given group identity language, with an explicit structural parity transition in the direction of complexity change. Group-theoretic parity and eventual saturation explain n+4 versus 4n−1; it is not a single arbitrary finite computation, mere parameter substitution, or direct consequence of the published generic regularity bounds. It supplies reusable explicit minimal right-quotient descriptions for a familiar nonabelian finite-group family. The limited alphabet and identity acceptance are essential scope restrictions, not hidden generalizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
