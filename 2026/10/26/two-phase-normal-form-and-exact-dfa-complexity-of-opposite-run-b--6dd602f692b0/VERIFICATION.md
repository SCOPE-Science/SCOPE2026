---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Any shuffle of u=0^a1^b and v=1^c0^d (a,b,c,d≥1) must have exactly a zeros in its first a+c positions: fewer prevents u entering its one-run, more requires v to have exhausted its c one-run. Every x∈B(a,c), y∈B(d,b) has an explicit valid source assignment, hence L=B(a,c)B(d,b), fixed boundary, |L|=binom(a+c,a)binom(b+d,d). Prefix left quotients within each phase depend only on the remaining zero/one counts and are distinguished by required zero counts in the remaining phase; different total prefix lengths have different residual accepted lengths. The two count rectangles share one boundary quotient; adding a single dead quotient yields minimal complete DFA state complexity (a+1)(c+1)+(b+1)(d+1), all parameters positive. An independently implemented exhaustive shuffle and quotient-set enumeration verified both normal form and minimal states for all 81 parameter quadruples 1≤a,b,c,d≤3. Analytic Myhill–Nerode proof covers all positive integers.

## originality

PASS

Best-of-knowledge PASS: Biegler–Daley–McQuillan (2009) full text gives periodic common-pattern shuffle constructions and quadratic bounds, but its conditions do not cover two opposite monotone binary runs and its results do not imply the exact two-phase normal form and quotient profile. Other language/shuffle papers inspect distinct operations, e.g. self-shuffle or regular-language pattern matching. Equivalents in unindexed automata literature remain possible.

## value

PASS

Natural canonical four-parameter finite-word family receives an exact factorization, cardinality, minimal DFA complexity and every depth-specific quotient multiplicity. Distinct-word counting and state complexity are genuine invariants, not a mere renaming of a standard bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
