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

The local table gives the stated two labeled edge sets, and every finite path corresponds to an extendable bilateral input block. Starting from all four vertices yields the listed eight subsets including the empty one; the two proposed identifications have equal transitions on classes, leaving five live states plus the sink. The empty suffix separates the sink; 0 separates E from the other live states, 10 separates D from A/B/C, 010 separates C from A/B, and 1010 separates A/B. Summing labeled paths from A gives the word count, since the presentation is deterministic. Eliminating the five continuation series yields A(z)=(1-z+z^2)/[(1-z)(1-2z+z^2-z^3-z^4)]. The live graph is strongly connected and has a self-loop; its Perron root exceeds one and is the largest root of the quartic, yielding the logarithmic spatial entropy. The independent enumeration of all binary inputs of length n+2 through n=13 gave the stated counts and then 5252, and numerical bisection gave root 1.8971794010653942 and log 0.6403682574172238. Every 010^m10 with m>=1 exits from E to the sink; its immediate prefix ends at E and its immediate suffix at D. Thus its proper factors are allowed, and arbitrarily long minimally forbidden words rule out finite type.

## originality

PASS

The generic de Bruijn/determinization method and the Rule 110 non-SFT conclusion already have coverage. The exact entropy also overlaps with the indexed spectrum and follows from the same-day periodic-point formula by the periodic growth identity for irreducible sofic shifts; no same-day priority order is assumed. The inspected sources do not give the evaluated minimal language automaton, its block-count generating function, or the exhibited minimal forbidden family. The pass credits these distinct exact language results, not generic methods or standalone novelty of the type classification.

## value

PASS

Rule 110 is a canonical dynamical system and its spatial image is a natural constrained language. A minimal five-live-state description supplies exact recognition and all finite-block counts, while the explicit forbidden family gives a directly checkable obstruction pattern. These give usable language-level data beyond a type label or a periodic count, even though the deduction of the entropy from a compact presentation is standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
