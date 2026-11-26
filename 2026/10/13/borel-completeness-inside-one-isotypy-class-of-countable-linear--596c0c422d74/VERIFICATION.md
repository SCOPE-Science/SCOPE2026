---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Finite distance is a convex equivalence relation. A class with an immediate predecessor and successor at every point is a copy of Z, because the finite interval condition makes every element finitely many successor or predecessor steps from a basepoint. Every order in the proposed class is therefore the lexicographic product of its infinite quotient with Z. Gvozdevsky's Corollary 3.4 gives isotypy of these products. Conversely, every realized singleton type in such a product requires both neighbors, and for each n the product realizes a tuple type asserting arbitrarily many points between every pair of n coordinates. An isotypic order has both neighbors everywhere and at least n distinct classes for every n. Each fixed-coordinate finite-distance test is Borel, and the neighbor and infinite-class conditions use only countable Boolean operations on Borel tests. The product map from orders on N is continuous coordinate by coordinate; an output isomorphism induces an input isomorphism on the finite-distance quotients, and any input isomorphism lifts. Friedman–Stanley completeness transfers along this reduction. The frozen artifacts/verify.py checks only finite coding comparisons, not the infinite structural steps; the relabeling claim in RESULT.md is not a separate test in the code. The infinite proof does not depend on the script.

## originality

PASS

The construction A×Z, the isotypy of its infinite products, and quotient recovery are already known. The narrower supported contribution is the explicit characterization of the entire realized-type class as an invariant Borel class and the localization of Friedman–Stanley completeness to it. No inspected prior statement supplies that combined conclusion.

## value

PASS

The result separates realized type spectra from isomorphism complexity inside an explicit invariant Borel class. It pinpoints maximal complexity after fixing strictly more information than a complete theory, and provides a usable continuous reduction and intrinsic description of the target class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
