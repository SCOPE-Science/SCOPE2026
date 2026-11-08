---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

RESULT.md proves over GF(2), for d>=2, A²=(d mod 2)I via commuting involutory coordinate flips. H=A+delta I has H²=0 and rank 2^(d-1); with e at one origin, D=H+ee^T has rank h+1, D² image span(e,He), and restriction [[1,delta],[1,0]]. Even d therefore has one fixed line and nilpotent J3(0) plus h-2 J2(0) blocks; the exact entry shells follow from kernel ranks. Odd d yields one irreducible degree-two 3-cycle factor and h-1 unipotent J2(1) blocks, yielding exact primitive orbit counts for 1,2,3,6. Independently exhaustively reimplemented direct GF2 state updates for d=2,3,4; first-entry d2=(2,2,4,8), d4=(2,254,32512,32768), d3 period-state populations (8,56,24,168) all match. These finite tests are not the infinite proof. No claim beyond one self-feedback defect, even/odd d>=2, or unlabelled orbit quotient.

## originality

PASS

Best-of-knowledge PASS for the exact defective-distance-one-cube rank-one update classification; previously known additive cellular-automaton algebra and uniform hypercube rules do not supply the explicit one-site-defect Jordan form and period-3/6 census.

## value

PASS

Adding precisely one self-feedback vertex to the canonical Boolean-cube parity automaton is a natural minimal local perturbation. The all-d exact transient shell and primitive orbit census distinguishes two parity regimes and produces new periods 3 and 6, a structural dynamical classification not implied by generic linear algebra alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
