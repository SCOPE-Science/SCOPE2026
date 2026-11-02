---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: For every height≤2 poset, incidence multiplication makes the strict-interval radical square zero. Solving aba=a vertexwise and edgewise proves a is regular exactly when each edge coordinate connecting two ZERO diagonal endpoints vanishes. For diagonal-zero set T there are (q−1)^(n−|T|) q^(m−e_G(T)) choices, giving the exact all-prime-power count. Inclusion--exclusion of bad edges gives Σ_{F⊆E}(−1)^|F|(q−1)^|F|/q^(|F|+|V(F)|), and the q^(−3) coefficient m+h(G) arises only from singleton and incident-edge-pair sets (bipartite triangle-free). Independent evaluation for all q=2..16 reproduces the path/star degree-7 polynomials and difference q(q−1)^3. More strongly, a freshly written direct linear-system solver (no use of this criterion) counts (path,star) regular elements as (89,91) over F2, (1777,1801) over F3 and (14377,14485) over F4. Simultaneous diagonal idempotent conjugacy and weighted tree-coloring prove that every commuting idempotent t-tuple count equals 2^t[1+(2^t−1)q]^3; independently checked 16 t,q parameter pairs. Includes char2 and isolated vertices; asymptotic keeps graph fixed.

## originality

PASS

PASS (qualified): The 2008/2009 Khripchenko--Novikov theorem already proves regular elements are two-sided unit-equivalent to diagonal idempotents in general finitary incidence algebras; idempotent diagonal conjugacy is also prior. Neither inspected theorem supplies the field-counting partition function, its induced-edge subgraph expansion, or the fully quantified pair of indistinguishable idempotent-tuple profiles separated by regularity. Such counts could be readily derived by specializing older incidence algebra techniques, a residual priority concern.

## value

PASS

PASS: The exact regularity count is a natural semigroup/algebra invariant; the first connected tree-shape pair (path vs star) has identical all-arity commuting-idempotent tuples but distinct regularity polynomials, visibly detecting incident edge pairs not encoded by the free graphic matroid. This is a complete structural separation rather than a random field-size sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
