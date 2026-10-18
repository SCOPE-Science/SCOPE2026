---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For vertices e_i+f_j of standard simplex product, a generic functional has additive scores p_i+q_j. Its top two scores must differ in only one index; conversely every ordered distinct same-row or same-column pair is forced as the top two by making the untouched factor score gap sufficiently large. The source vertex-lineup criterion therefore yields exactly de(e-1)+de(d-1)=de(d+e-2) distinct vertices for alpha>beta>0. Each occupation vector has squared norm 1+alpha^2+beta^2 and row/column coordinate sums 1, so its squared distance from c=(1/d 1_d,1/e 1_e) is R^2=1+alpha^2+beta^2-1/d-1/e. The de cyclic same-row contact vertices have average c (both alpha and beta visit each column once per row). For any candidate center q their average squared distance is R^2+||q-c||^2; hence every other center requires radius strictly >R, proving exact uniqueness and that all vertices are contacts. All d,e>=2 and admissible alpha,beta follow algebraically; exact rational checker finite d,e<=8 is not extrapolated.

## originality

PASS

Best-of-knowledge comparison of mathematical statements and implications against named primary sources, published findings and exact source-object searches. The current Resultary hit for the very assignment under audit is not independent novelty evidence. A mirror of this assigned 2026-10-11 finding returned as the highest-ranked Resultary hit is not counted as independent prior art.

## value

PASS

This computes a natural sharp Euclidean invariant for a family of lineup polytopes motivated by product-simplex and quantum marginal geometry, classifies every vertex and proves an unusual all-contact phenomenon. The de-vertex positive barycentric certificate gives a useful compact exact optimality proof for every d,e and weight ratio. Although the combinatorial dichotomy is elementary, the uniform minimum enclosing sphere statement and sparse contact structure are independently reusable geometric facts, not arbitrary tiny instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
