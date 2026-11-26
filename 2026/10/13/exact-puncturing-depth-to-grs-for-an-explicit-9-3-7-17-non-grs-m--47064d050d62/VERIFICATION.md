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

The generator matches Example 1. An exact independent finite reproduction confirmed all 84 three-column subsets are independent. On each surviving subset, evaluate the six quadratic monomials modulo 17 on (1,t^3,t^4). Rank below six detects a conic; no three points are collinear, so a singular conic (two lines over the algebraic closure, possibly coincident) cannot contain five of them. A smooth conic can be projectively parametrized with an unused rational point at infinity, giving an ordinary GRS code up to monomial equivalence; GRS columns conversely lie on such a conic. The independent enumeration of all 256 surviving sets gave rank-(5,6) counts (0,1),(0,9),(0,36),(6,78),(126,0) in descending size order. The six deletion triples matched exactly: {4,10,16}, {3,7,9}, {3,5,16}, {2,5,9}, {2,4,7}, and {0,2,3}. Hence the least puncturing depth is three. Replay: the frozen verify.py specifies the finite instance; independently, enumerate the subsets of S and row-reduce the rows (1,t^6,t^8,t^3,t^4,t^7) modulo 17.

## originality

PASS

Credit the original construction, the general conic test, and the automatic five-point GRS case. The minimum depth and six successful deletion triples are a distinct unreported profile in the checked sources. The nearest indexed recovery theorem is not a special-case cover even after allowing a projective equivalence of the full arc.

## value

PASS

Puncturing to GRS is a natural recovery invariant of the published explicit non-GRS MDS example. Knowing that three punctures are necessary and sufficient, and which six choices work, tells a reader how robust its non-GRS property is under deletion; neither the general recognition test nor the automatic five-point case gives that information. The contribution is finite and example-specific.

The dated certificate retains the supplied scientific assessment, sources and limitations.
