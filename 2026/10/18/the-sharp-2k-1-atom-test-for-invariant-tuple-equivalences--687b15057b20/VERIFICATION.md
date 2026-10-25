---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For B of size 2k+1 and a Sym(A)-invariant relation R on A^k, reflexivity and symmetry transfer from any pair of tuples using at most 2k atoms. The nontrivial transitivity lifting uses finite quotient Q=B^k/E. For stabilizers K containing pointwise fixers of ≤k atoms, graph connectivity of transpositions outside two supports S,T (since B>S∪T) implies the intersection fixer is in K. Minimal support S is K-setwise-invariant, giving coset orbits Inj_t(B)/H with t≤k. On each equality-pattern orbit the quotient map selects an equivariant injective list of input coordinates modulo H; the same finite presentation defines a quotient map over arbitrary A, whose kernel agrees with R by supportwise injection of any input pair into B. The sharp counterexample relates equal or disjoint supports of injective k-tuples: on 2k atoms disjointness is complementation, a genuine equivalence; on 2k+1 atoms chains via disjoint k-sets break transitivity. Argument treats repeated tuples as singleton classes, infinite A and k≥2, and does not assume definability.

## originality

PASS

General nominal-set results and Ciobanu finite-context semantics establish equivariant quotients, orbit supports and formal context, but no located theorem provides both the exact universal finite equivalence test 2k+1 and matching 2k counterexample. Strong potential equivalences under symmetric-group overgroups/least-support terminology were considered. Actual full-text inspection supports a best-of-knowledge PASS, with meaningful residual risk of an implicit older representation theorem.

## value

PASS

A minimal finite atom carrier that certifies a universally equivariant binary relation is a natural finite-model-verification invariant. The theorem supplies a uniform exact sharp bound for every tuple arity and a structural group-theoretic explanation, not an arbitrary small carrier experiment. Its precise cutoff can be used whenever quotient constructions rely on global equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
