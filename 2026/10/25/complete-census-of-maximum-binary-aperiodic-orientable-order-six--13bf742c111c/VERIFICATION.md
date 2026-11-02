---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS: Each nonpalindromic 6-bit factor belongs to one of exactly 28 reversal pairs; a legal word is a walk in the order-five de Bruijn digraph using each permitted reversal orbit at most once. The exact recurrence F(v,S), evaluated over all 32 five-bit starts, has maximal 21 edges, hence word length 26. An independently coded exhaustive memoized recurrence of 6,824 states recovered exactly 22 maximizing linear words, partitioned into six reversal/complement orbits of sizes 2,4,4,4,4,4. Every maximum begins with 00000 and ends 11111 or the complement arrangement, 11 in each orientation. The source supplies a second independent literal-string search and a full 22-word list. Finite classification is exhaustive by the state recurrence, not an extrapolation.

## originality

PASS

Best-of-knowledge original complete finite census and orbit/endpoint classification at previously known binary order-six optimum; prior optimal LENGTH and individual ideal constructions explicitly credited.

## value

PASS

PASS: Knowing all maxima at the first nontrivial published aperiodic orientability optimum, their symmetry classes, and that all are ideal up to complement is a motivated complete classification. The exact count and endpoint rigidity are not implied by previously known optimal length or example construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
