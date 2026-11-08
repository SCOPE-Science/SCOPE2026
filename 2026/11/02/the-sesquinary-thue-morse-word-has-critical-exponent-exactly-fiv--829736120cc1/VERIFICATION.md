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

The recurrence x_{3m}=u_m, x_{3m+1}=1-u_m, x_{3m+2}=u_m with u_m=x_{2m} yields u-blocks (u_{2m},u_{2m},1-u_{2m+1}). Hence u has no four-letter alternating factor and no six-letter constant factor; x has no three-letter constant factor or ten-letter alternating factor. A period p not divisible by three and long enough forces all cyclic adjacent edges constant in u, or alternating in x, contradicting these obstructions. For a 3r period in u, retaining aligned blocks recovers contiguous period-2r input with Lnew>=2L/3-8/3, so repeated desubstitution excludes u periods q>=2 with length>=5q-1. A 3q period in x produces >=5q-1 complete blocks and reduces to u; q=1 is ruled out by the no-six-equal bound. Literal recursion gives x[18:33]=(101)^5; therefore critical exponent exactly five for all periods, including fractional powers. The finite tests corroborate rather than replace the desubstitution proof.

## originality

PASS

Dekking 2023 poses exactly this critical-exponent-five assertion as a conjecture, but the accurate number in the primary PDF is Conjecture **10**, not Conjecture 9 as the frozen RESULT.md states. Cassaigne–Espinoza–Rigo–Stipulanti 2026 treat the same unscaled word and its frequencies, reversals, recurrence, but do not state the universal 5p+1 period exclusion in accessible full text. The other Shallit-conjectures paper addresses a different Thue–Morse-like family. Resultary search returned adjacent word problems, no identical conclusion. Historical priority remains provisional.

## value

PASS

Solving a published sharp repetition conjecture for a naturally defined rational-base digit-parity word is an explicit mathematical target; an infinite threshold and a length-15 attaining witness are precise combinatorics-on-words results, not a finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
