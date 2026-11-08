---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For n>=3 labelled simple cycles and synchronous integer sign-gradient update, express edges as e_i=x_{i+1}-x_i, signs s_i and next-step signs t_i. Period at most two forces s_i+t_i a constant; zero sum of differences forces zero, hence reverses every nonzero sign. The local equation e_i^new=e_i+s_{i-1}-2s_i+s_{i+1} makes q=|e_i| range from 1 to 1-s_i(s_{i-1}+s_{i+1}) for nonzero edges; for zero edges forces adjacent signs sum zero. The 9-pair-state Laurent matrix exactly enumerates choices; coefficient z^0 imposes global zero winding and produces one translation class per closed edge word. Only constant fixed class exists, and the rest pair into distinct two-cycles by conserved total chip sum. Explicit cycles give sharp edge gap three n>=4 and two n=3. Independent direct sign-update enumerations n=3..6 matched coefficients 19,47,171,517; all-n proof is analytic transfer bijection, while eventual period<=2 relies on Long–Narayanan.

## originality

PASS

Bounded best-of-knowledge originality: exact specialized formula and classification not shown to follow from inspected prior theorems; known general mechanisms and finite examples are credited, with residual priority risk.

## value

PASS

The global zero-sum constraint is essential on cycles; deriving an exact all-n recurrent orbit census modulo translation from a local transfer captures a natural dynamical invariant distinct from path counting. Sharp bound and explicitly computable generating transfer are mathematically reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
