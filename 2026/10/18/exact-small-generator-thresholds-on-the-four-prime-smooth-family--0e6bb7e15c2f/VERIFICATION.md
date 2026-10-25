---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For all a,b,c,d>=1, n=2^a3^b5^c7^d, least B generating all units from coprime integers t<=B is controlled by CRT and finite-abelian Frattini quotients. Reduction to exponents min(a,3),min(b,2),min(c,2),min(d,2) kills only local Frattini subgroups, hence the all-exponent family reduces to finite elementary character coordinates modulo 4,8,9,25,49. Primitive roots 2 (9,25) and 3 (49) yield exact discrete-log rows for 11,13,17,19,23. Three 2-character rank matrices for a=1,2,>=3 have determinants 1,-1,-3 (odd); the 3-character 2x2 minor has determinant -2 modulo3, and the 5/7 coordinates of 11 are nonzero. Thus B<=19 for a<=2, B<=23 for a>=3. Conversely 2-rank dimensions 3,4,5 force bounds; at a=1 the first 3 rows are dependent, so <=17 fails. Independently computed all 24 reduced exponent rank cases and exact subgroups at cutoff and immediately below on n=210,420,840,22050,44100,88200. These finite checks support local certificates, while Frattini reduction proves the unbounded-exponent quantifier.

## originality

PASS

This is the same least generating-set function, not a different invariant. A general almost-all estimate does not imply exact G(n) on a zero-density fixed-radical family.

The general estimates do not dominate an exact 19/23 dichotomy for every exponent quadruple. An inaccessible plausible older original is recorded as historical risk, not grounds to invent a negative or positive coverage result.

A table of finite n does not imply Frattini stabilization over all powers or explain the sharp transition between a=2 and a=3. No located exact infinite table covered the statement.

The exact equality on this thin family is not implied by asymptotic statements, and the elementary Frattini reduction alone needs concrete coupled discrete-log matrices. The theorem is not just an arbitrary one-modulus numerical test.

## value

PASS

Least unit-group generating cutoffs are a motivated classical arithmetic invariant. The exact 19/23 threshold on an unbounded natural four-prime-support family exhibits a genuine 2-adic character-rank jump and a reusable finite local criterion; it is not a single tiny modulus computation or a known-table copy. Uniformity in arbitrary exponents gives a precise benchmark for the least-generator function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
