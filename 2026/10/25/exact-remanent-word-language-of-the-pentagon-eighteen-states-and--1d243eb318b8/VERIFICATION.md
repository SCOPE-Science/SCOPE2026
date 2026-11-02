---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For each of the 32 orientations of C5, letter-labeled step maps act on subsets of five vertices; a word is in the intersection language iff all 32 reachable endpoint subsets remain nonempty. Exhaustive BFS of the finite product from full subsets closes on 23 non-sink states and one rejecting sink; stable Myhill–Nerode partition refinement has class counts 2,4,7,9,11,13,16,18 and 18 final classes. Independent fresh transition construction matched 24 reachable states and 18 inequivalent states, not just finite tested words. From displayed quotient transition matrix the 27 coefficient zero tests and degree≤26 cross-numerator bound prove generating function (1+z)(1-z²+z⁷)/((1-z)(1-3z²+2z⁴-z⁷)) for every length. Direct triangle and pentagon orientation checks establish separating words 00100/11011. Finite state closure, unlike finite-word enumeration alone, is a complete infinite-language proof.

## originality

PASS

Best-of-knowledge qualified PASS for the concrete minimal C5 automaton/length enumerator, distinguishing it from generic intersection regularity. However Pujol 2026 defines remanent languages on graphs and its complete paper was inaccessible: abstract-only reading cannot establish absence of the pentagon 18-state census from that paper. Potential exact prior coverage remains a material priority risk; this judgment must be revisited if the original text becomes accessible.

## value

PASS

The five-cycle is the first nontrivial odd cycle beyond a triangle, so its exact remanent language and minimal-state invariant are motivated by the graph-orientation intersection construction rather than arbitrary data mining. The rational length enumerator gives a reusable exact infinite-word invariant, and two explicit words separate C3 and C5.

The dated certificate retains the supplied scientific assessment, sources and limitations.
