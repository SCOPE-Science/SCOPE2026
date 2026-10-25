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

The one-step inverse occurs iff the word contains ab bar(b) bar(a), exactly q² forbidden length-four factors. Inspected complete marked cluster shift table: only overlap lengths 3 (type A), 2 (one same-type), 1 (q successors). Two continuation equations eliminate to J(z)=1+z+2z²+(q+1)z³+qz⁴+qz⁵ and denominator 1-(q-1)z-(q-2)z²-(q-1)z³. The first six coefficients are consistent with inclusion/exclusion of length-four occurrences. A separate independently written last-three-symbol DP and formal series recurrence matched q=2,4,6 for n through 10; this is bounded corroboration, not the all-n proof. The 3×3 recurrence matrix for all even q≥2 is primitive (q=2 has q-2=0 yet remains strongly connected with a loop), so Perron–Frobenius gives unique dominant positive λ between q-1 and q and Θ_q(λ^n).

## originality

PASS

Read original 2022 full primary PDF and found it already characterizes binary irreducibles and their forbidden factors; that antecedent is explicitly credited. The exact all-even-q rational GF and entropy are not in the inspected source or subsequent 2026 conjugacy and code-capacity papers. Best-of-knowledge pass with genuine prior-language alias risk.

## value

PASS

Counting locally irreversible roots is a natural exact language growth invariant for the DNA reverse-complement channel, not merely a coding bound. The uniform all-even-alphabet rational GF and entropy explicitly quantifies constrained words beyond the previously analyzed binary automaton; the proper result remains useful even if future higher-block classifications are open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
