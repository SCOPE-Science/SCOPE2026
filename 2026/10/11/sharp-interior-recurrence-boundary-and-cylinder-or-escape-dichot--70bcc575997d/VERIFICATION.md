---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For f=1-x²-y², direct symbolic differentiation gives f_prime=-2fxy(y-a x+z), preserving its positive sign; on interior |z_prime|≤1+|b| ensures both-time completeness. Independent SymPy exact expansion confirmed Phi_prime=f[f+(x-y/a)²+(1+a^-2-b)y²] for a≠0 and (z+bx)_prime=f at a=0. If b≤B=1+a^-2 then Phi_prime≥f², forbidding complete compact invariant interior sets; a=0 is similarly monotone. If Phi is bounded above, f² integrable; bounded z and f_prime imply f uniformly continuous, so f→0; otherwise monotonic Phi→∞ and bounded x imply z→∞. For b>B explicit E±=(±1/(a√b),±1/√b,0) have f=1-B/b>0 and exhaust interior equilibria. For b=B equilibria on boundary only. The printed script check_es9.py was read; independent exact symbolic identity test was run locally.

## originality

PASS

Jafari et al. 2016 Table 1 ES9 defines the system at a=5,b=7 and numerically observes an equilibrium cylinder; Li et al. 2021 reproduces ES9 variants. Neither inspected source derives the sharp all-real parameter boundary, global strict Lyapunov identity, nor the infinite-time cylinder-or-escape dichotomy. Resultary related Sprott recurrences concern different vector fields. The complete implication goes beyond simply solving the interior equilibrium equations.

## value

PASS

A sharp all-parameter boundary between possible interior compact recurrence and its exclusion is motivated by the system’s equilibrium cylinder and numerical chaos interpretation. The global escape/boundary dichotomy rules out hidden interior compact dynamics despite potential lack of equilibria and provides useful rigorous understanding of a named nonlinear flow.

The dated certificate retains the supplied scientific assessment, sources and limitations.
