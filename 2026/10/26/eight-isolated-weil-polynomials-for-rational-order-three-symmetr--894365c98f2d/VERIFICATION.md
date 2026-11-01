---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Structural proof: order-3 automorphism descends to PGL2(F3), conjugate to x↦x+1; its geometric fixed infinity cannot be a reduced six-point branch of invariant degree six. Invariants under translation are F3[x³−x], so models y²=c((x³−x)²+a(x³−x)+b) with c∈{1,2}, a²−b nonzero; a↔−a yields eight arithmetic models. Independently enumerated all 3^7−1=2186 nonzero binary sextic coefficients; derivative gcd plus infinity-degree test leaves exactly 1296 geometrically squarefree forms. Independent 24-element PGL2(F3) action partitions into 69 orbits; exact F3/F9 point counts yield 50 Weil coefficient pairs. Exactly the eight stated target pairs have singleton orbit fibers, with orbit sizes [1,1,4,4,8,8,8,8]; no extrapolation from incomplete enumeration. Frobenius coefficient A1=#C(F3)−4 and A2=(#C(F9)−10+A1²)/2 checked. The supplied artifacts/verify.py was read as evidence; independent implementation produced same counts.

## originality

PASS

A prior complete 69-class genus-two sextic orbit census with stabilizers already allows identifying eight order-3 symmetry classes: neither count nor representatives are novel. The differentiated result is that each of eight Weil polynomials has a singleton fiber among all 69 arithmetic classes, a statement requiring the quadratic extension point counts not given by a stabilizer/branch table alone.

## value

PASS

Weil polynomial usually determines an unpolarized Jacobian isogeny class rather than a unique genus-two curve. The eight F3 symmetry isogeny classes unexpectedly isolate a single curve each, so a natural arithmetic invariant exactly detects a wild automorphism on a complete field-specific locus. This is a motivated exact finite classification, not an arbitrary list of eight coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
