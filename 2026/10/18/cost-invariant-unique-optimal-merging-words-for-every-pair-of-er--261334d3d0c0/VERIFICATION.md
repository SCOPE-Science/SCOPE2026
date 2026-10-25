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

Using the exact pair transitions for a cycle a and one collapsing b, branch potentials L and R have componentwise ordered letter counts according to 2(j−i)<n or ≥n. The one-step Bellman inequalities F(px)≥F(p)−weight(x) have exactly one equality letter, a away from upper boundary and a/b at boundary by the gap dichotomy. Positive weights ensure strict descent to merge; any deviation strictly costs more. Cost-ratio invariance gives componentwise letter-count minimality, and unit weights partition all C(n,2) pairs into consecutive distinct distance intervals; the unique worst-pair trajectory visits all pairs. Independent reverse shortest-path computation checks all pairs for n=3..17 at four positive integer cost profiles, strict optimal letter and entire length spectrum; this finite range only corroborates the all-n argument.

## originality

PASS

Statement-and-implication comparisons with primary literature and published Resultary records below support a best-of-knowledge new exact statement or motivated refinement. Prior auxiliary lemmas and special cases are credited; unseen equivalent work is a residual risk.

## value

PASS

A deterministic two-state synchronization law with unique universal optimum under any positive costs and a length bijection 1..C(n,2) is a motivated exact structural property of the classical extremal automaton, rather than just computing Dijkstra once.

The dated certificate retains the supplied scientific assessment, sources and limitations.
