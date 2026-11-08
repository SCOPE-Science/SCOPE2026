---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

At position t in Z_n the symbol is a_{1+nu_2(t)}. Every Z_m occurrence begins at residue 1 mod 2^m. The continuation set of a proper prefix is one letter except for exact Z_m prefixes where all higher-ranked center letters can follow; border lengths of Z_s are exactly 2^m−1. Induct on n via the unique a_n: old minimal absent words persist; a word with two a_n occurrences must have them as endpoints enclosing a border Z_m; with one a_n it cannot appear internally as the unique occurrence permits context gluing, so endpoint continuations exactly generate a_n Z_m a_j and their reversals. This proves exhaustiveness and counting across all n. An independent suffix/prefix factor oracle constructed actual Z_n and compared full sets for n=1..7 (counts 1,3,8,18,35,61,98), not merely predicted totals; the proof rather than these finite checks establishes all-rank result.

## originality

PASS

Earlier Zimin-factor pattern matching gives generic occurrence criteria, and universal minimal-absent-word algorithms list factors of any fixed input. The compact all-rank parametric anti-dictionary with its spectrum and cubic count is an additional structural classification not located in the inspected work. One can algorithmically compute examples from prior general machinery, but a uniform formula does not logically follow without exploiting Zimin recursion.

## value

PASS

The family Z_n is canonical in pattern avoidance and compressed strings; a concise explicit forbidden-factor basis and exact length spectrum are natural data for factor automata, indexing and combinatorics on words, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
