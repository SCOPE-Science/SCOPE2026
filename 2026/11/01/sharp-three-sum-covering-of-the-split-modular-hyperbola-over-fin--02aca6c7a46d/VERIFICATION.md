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

For axis targets explicit one-parameter nonzero triples avoid finitely many t values. For nonzero coordinates use the multiplicative automorphism to normalize target (1,w), realize as an affine cubic Cw cut by e1=1,e2=w e3. Its projective completion has exactly six disallowed rational points (three infinity, three distinct zero-coordinate affine), and is nonsingular genus one except w=1 or w=9; these singular values have direct triple witnesses. Hasse q+1-2sqrt(q)>6 for q>=13 forces a valid rational point for every other nonzero w. Origin criterion e1=e2=0 becomes either characteristic 3 or split third roots of unity. Explicit exhaustive F11 check excludes (1,6). Independent exact prime-field enumeration q=11,13,17,19,23,29,31 agrees, but proof supplies all prime powers.

## originality

PASS

Bower et al 2012 prove scalar coordinate sums with fixed multiplicative product; Khan et al 2013 study modular hyperbola geometry; a published Resultary result handles the nonsplit norm-one torus of size q+1 rather than split inverse graph size q-1. None of these statements implies the two-coordinate triple sum and q=11 sharp threshold via the inspected theorem comparisons. Priority risk persists for unindexed finite-field rational-point covering.

## value

PASS

A sharp exact covering radius/threefold additive support theorem for the canonical split 1-dimensional algebraic torus is a natural finite-field combinatorial geometry question; its genus-one reduction, cube-root zero obstruction and sharp small-field threshold give independently useful structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
