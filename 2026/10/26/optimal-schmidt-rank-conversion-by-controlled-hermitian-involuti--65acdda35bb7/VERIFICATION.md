---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Rank-product lower bound applies to U and U−1=U. Decreasing-rank construction groups input Schmidt indices and swaps disjoint second-factor basis vectors; output has q orthogonal groups. Increasing-rank construction embeds an abstract q-frame with normalized per-input group sums into first factor, then uses orthogonal control projectors and transposition involutions; exactly q orthogonal Schmidt terms survive. Independent 4×4 p=2→q=3 realignment check confirms self-adjointness, square-one and OSR=2.

## originality

PASS

Kian–Moslehian proves precisely the unrestricted unitary minimum, a stronger comparison on a larger admissible class but not an involutory minimizer. The new constrained realization is not a formal consequence of the unrestricted bound. Full same-paper proof inaccessible, leaving a substantive construction-overlap risk.

## value

PASS

Replaces arbitrary optimal unitaries by reversible self-adjoint controlled reflections for every Schmidt-rank transition, a motivated and nontrivial structural restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
