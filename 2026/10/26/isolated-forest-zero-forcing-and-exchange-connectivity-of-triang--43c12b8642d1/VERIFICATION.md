---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Represent white pairs as edge graph H on base labels. For blue pair uv, its number of white neighbors equals d_H(u)+d_H(v) because uv is absent; a unique white neighbor exists exactly for an isolated endpoint and degree-one endpoint. Thus every force removes a white leaf edge. With no isolate no first force; a white cycle cannot lose its first edge under the rule, proving necessity. If H is a forest with isolate z, use blue edge uz with a leaf u to force its sole white incident edge, iterating; sufficiency is constructive. Maximum white edges n-2 gives Z=binom(n,2)-n+2 and exactly n(n-1)^{n-3} Cayley trees with isolated vertex. Labeled-forest exponential assembly with at least one singleton proves the entire polynomial. Between isolates r!=s, exchange iff deleting the unique edge incident to s and adding unique edge incident to r leaves common tree U on n-2 others; choose U and two attachment labels, giving binom(n,2)(n-2)^{n-2} cross-class edges. Within-isolate usual spanning-tree exchange connected; star-switch crosses classes. Independent line-graph forcing and forest-isolate exhaustive checks for n=3..6, plus cross-class counts, agree; universal iff rests on the local degree lemma.

## originality

PASS

The scalar zero forcing number is established for line/Johnson graphs and cannot count toward originality. Fallat et al 2015 compute a POSITIVE zero forcing quantity, a distinct forcing rule; Abiad et al 2023 cover ordinary scalar. Boyer et al define polynomial generally; Geneson et al study reconfiguration generally. In the inspected primary articles, no stronger theorem implies the ordinary white-forest-isolate iff, the full J(n,2) polynomial and exact cross-isolate exchanges. Prior forest and reconfiguration arguments are used but a possible unpublished triangular graph specialization remains.

## value

PASS

The triangular graphs are a canonical association-scheme and line-graph family. A single structural forest-and-isolate criterion solves the natural decision problem for every initially blue set, yields a full exact enumerator beyond the known optimum, and describes how all Cayley-tree minimizers interconvert by token jumping, with explicit cross-fibre edges. These are natural structural invariants, not a restatement of the prior scalar minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
