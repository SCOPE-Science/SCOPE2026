---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An induced matching realizes all patterns by picking one endpoint per edge, then extending to an inclusion-maximal independent set. For cographs the key converse lemma is valid: for at least two query vertices, realizing the nonempty patterns suffices. In a union with queries in both factors, put a positive in one factor while realizing the local empty pattern in the other and then combine the two local empty witnesses. If all queries lie in one factor, induct; in a join spanning both factors the all-positive pattern is impossible, and if queries lie in one factor all nonempty patterns come from it. Thus nonsingleton shattered supports in a join come from one factor with no help from the other; singletons can take a mate across the join. This proves the all-support theorem, including empty, union, and isolate cases. It also gives the stated recurrences: the constant term is counted once at a join, the extra singletons are the isolated vertices of the factors, and other coefficients add. For a binary decomposition, the sum of products of child sizes is at most n(n−1)/2, charging pairs to their least common ancestor; child linear terms also total O(n²). This is an arithmetic-operation bound, not a bit-complexity bound. For the finite boundary, any shattered pair x,y has distinct private neighbors a,b from the one-negative assignments. In a gap at n≤5 the matching number must be one, and a,b must be adjacent (or xa,yb is an induced matching). With no remaining vertex, or an extra vertex adjacent to at most one of x,y, the empty trace is impossible: every pair of private choices on opposite sides is adjacent. Hence the fifth vertex is adjacent to both x,y, completing the path x-a-b-y to a C5; zero, one or two extra adjacencies to a,b give C5, house and gem. The fifth vertex witnesses the empty pattern, and the others are witnessed by independent pairs. No triple can be shattered on five vertices because each support vertex needs a distinct outside private neighbor. The automorphism group orders 10,2,2 give 12,60,60 labeled copies. The gem is chordal since its only other four vertices induce a path and the universal vertex cannot be on a chordless cycle of length at least four. Fresh independently written enumeration at /workspace/branches/11bf5394-2c59-43f5-aeb7-012b4e8d080e/independent_boundary.py reproduced zero gaps in orders 0–4 and exactly the three classes with those counts in order 5 (run_n0_to5.json). The frozen verifier was inspected, not executed. The census only checks its finite domain; the universal theorem uses induction.

## originality

PASS

On the evidence inspected, the cograph converse on individual supports and its counting recurrence, with the sharp general-graph boundary as corroboration, are distinct. The universal forward direction from induced matchings is not credited as new. The closest general bound uses a different matching invariant and does not imply this equivalence.

## value

PASS

The exact support-wise characterization goes beyond the dimension and yields a usable polynomial for counting supports from a cotree. The smallest gap is an informative boundary: the gem shows that chordality alone is insufficient, while classifying every smallest witness avoids treating an isolated counterexample as representative without evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
