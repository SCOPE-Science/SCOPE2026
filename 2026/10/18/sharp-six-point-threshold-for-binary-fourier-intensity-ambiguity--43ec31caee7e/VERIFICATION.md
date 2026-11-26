---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Walsh inversion recovers autocorrelation, with each nonzero value twice its unordered-pair count; its support spans the direction space. For affinely independent sets the distinct differences form the edge labels of a complete graph, and two labels sum to another label exactly for intersecting edges (disjoint edges would give a nonempty even relation). A normalized competing set gives a clique, normally a star; at size four the triangle option repeats pair differences and is impossible. The dependent size-four set is a plane, and the dependent size-five set consists of a plane and a point, whose coset is read off from the counts. At size six the direction rank lies in 3–5. In rank three, the two omitted points in the flat are determined up to translation by their difference, the sole nonzero shift with intersection size six. In rank four the unique relation has weight four or six. For weight four the counts recover the plane and the two full outer cosets, plus a singleton coset entry fixing the outer representatives' sum. Thus the representatives can only change by a common plane shift. For weight six all 15 pair differences are distinct and exhaust H minus zero; the correlation is 4δ₀+2·1_H, giving 36 on H⊥ and 4 elsewhere. Conversely that correlation fixes H and rules out every four-point relation, hence characterizes precisely these circuits. In a fixed four-flat the independent five-sets number 16·15·14·12·8/5!=2688. Their xor-sums extend each to a circuit and each circuit is counted six times, giving 448 circuits per coset. A nonzero stabilizer would have correlation six, so every orbit has 2^d members and there are 28 orbits. The displayed examples have rank four and xor zero; none of the six translates of A that contain zero is B.

## originality

PASS

The supported distinction is the translation reconstruction threshold and the full indexed homometry-fiber classification. The six-point affine types, the flat spectrum of the classical difference sets, and counting consequences of that known difference-set structure should not be mistaken for independently novel ingredients.

## value

PASS

The result fixes the first nontrivial sparsity boundary for indexed binary phase retrieval and describes exactly what goes wrong there: the lost information is translation class inside one recoverable four-dimensional direction space. The complete all-dimension treatment is useful beyond the already known individual bent supports or a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
