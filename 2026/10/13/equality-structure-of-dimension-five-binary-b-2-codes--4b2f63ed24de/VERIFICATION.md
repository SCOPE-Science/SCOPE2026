---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Ordinary sum equality of unordered pairs including repetitions is invariant under every xor translation (each flipped coordinate sends 0,1,2 to 2,1,0) and coordinate permutations. Normalize one word to 00000. An independently written backtracker exhaustively examines all increasing candidate sets containing zero, maintaining exactly all seen ordinary coordinatewise pair-sum triples; max 12, 72 normalized maxima. XOR all 32 translations and deduplicate: 192 distinct labeled maxima. Full 3840 signed coordinate permutations act transitively on these 192 (stabilizer 20). On a representative, five coordinates each have six ones, exactly one antipodal pair, and pair distance counts [5,20,30,10,1]. Unlike a heuristic search, the normalization/pruning is lossless and complete over the finite cube. Independent re-enumeration confirmed the figures.

## originality

PASS

OEIS A309370 already lists dimension-5 optimum 12 and a witness: the 12 optimum is not original. Primary B2-code literature fixes the additive-pair condition, asymptotic bounds and constant-weight variants; no inspected source gives the 192 labeled solutions or single Hamming orbit. Resultary exact phrase query for 192 Sidon cube maxima returned unrelated same-numerical-count objects, not this one. The exact classification remains best-of-knowledge original.

## value

PASS

Given a known maximum in a natural Boolean-cube Sidon/adder-code problem, identifying all extremizers and their unique isometry class is the canonical next structural fact; uniform balance, antipodal and distance invariants follow across all maxima. Fully finite but complete and reproducible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
