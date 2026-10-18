---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The finite domain is exactly cyclic position classes of permutations of 0,…,10, represented uniquely by p[0]=0, hence 10!=3628800. Inspected frozen Git RESULT.md blob 2a525b1fa65927b30c480720fe734535ac6ccf8a, source tree af69e9a980e335c89bc08194ee3b5ef19ed265d9, and bundled C++17 verifier blob 52ff8421d232497feb849f2f44848071721b3c0b. The T− predicate checks cyclic neighbors with height difference one. Crossing exchange enumerates all eleven basepoints, admissible m,w, the two required pairs and interval-nesting for every remaining pair. R adds 1 mod 11; S reverses and complements heights, both renormalizing p[0]=0. Separately written and compiled C++17 enumerator (not execution of packaged opaque code) exhausted all 3628800 words and independently obtained no_T=393410, no_X=1971006, both absent=325398, dihedrally stable=270630, orbit counts 12786 and histogram 1:8,11:954,22:11824. The identity 8+954·11+11824·22=270630 holds exactly. These computations exhaust this fixed finite domain but do NOT certify knot types, infinite N or asymptotic density.

## originality

PASS

Best-of-knowledge original finite eleven-petal global local-move census with new dihedral-stability refinement relative to published move definitions and reported nine-petal calculations; full access to the most directly relevant 2026 preprint failed, so the exact priority comparison is materially limited. Resultary service failed and supplies no negative originality evidence.

## value

PASS

Eleven petals is the first natural odd size beyond the source’s reported nine-petal enumeration; an exact complete finite baseline for when the two canonical simplifying moves are unavailable, refined by natural dihedral symmetry, is a mathematically motivated structural classification. It does not pretend to count hard unknots; 3.6-million-case exact finite obstruction data can guide further petal-move topology without claiming a knot classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
