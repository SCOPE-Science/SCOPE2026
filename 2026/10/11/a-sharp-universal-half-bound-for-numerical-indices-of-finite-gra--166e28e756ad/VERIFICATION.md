---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Every shortest-path normalized molecule is the average of oriented edge molecules, so edges norm any operator. An extreme normalized dual Lipschitz potential has a spanning connected tight-edge graph; otherwise a slack component could be shifted in both directions. Tight differences are \(\pm1\), forcing integral vertex values. At a neutral edge \(h(a)=h(b)\), directed costs \(c(s,t)=1+\min(0,h(t)-h(s))\in\{0,1\}\) give distance \(g(b)=0,g(a)=1\): zero-cost paths lower the integer potential strictly and cannot connect equal heights. Forward and reverse triangle inequalities imply both \(g\) and \(h-g\) are 1-Lipschitz. Normalized components norm the chosen edge with opposite signs; thus \(|h(Tm)|\le2v(T)\), and extremal dual evaluation yields the global norm inequality. The equilateral triangle equality follows from Cobollo--Guirao--Montesinos, Corollary 5.3. Independently reproduced the shortest-path splitting for all 771 labeled connected graphs on 2--5 vertices, 41,463 integer Lipschitz potentials, and 88,156 neutral-edge incidences; this finite test is corroboration only.

## originality

PASS

The closest complete primary source classifies only three-point spaces and their two-dimensional subspaces, not ambient numerical indices for arbitrary finite graph metrics. Earlier indexed graph-specific research referred to in the assigned package treats numerical index one on bipartite graphs and special sharp families (equilateral metrics, cycles, wheel); those statements do not dominate a universal lower bound for nonbipartite graphs. The integral-potential neutral-edge splitting is an additional all-graphs lemma. Exact independent published-finding retrieval was temporarily unavailable this execution; this is recorded as a coverage risk rather than misreported as a negative search.

## value

PASS

A sharp dimension-independent numerical-radius estimate for all finite connected unit-edge graph free spaces closes a natural gap between index-one classifications and special nonbipartite examples. The constructive integer-potential splitting is a nonstandard structural lemma independently applicable to norming functionals; \(K_3\) proves the constant optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
