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

The value/first-jet matrix on the seven P2(F2) points has full rank 21, so I5 is 14-dimensional and 3^7=2187 forms pass all rational first-jet tests. The independently reconstructed GF(2) mask, GL3 action and three-affine-chart Groebner unit-ideal tests found 1512 geometrically smooth forms, 50400 unordered XOR-valid pairs, and 16800 pencils. Exact projective-orbit enumeration gave (orbit size,base reducedness) multiplicities (168,true):93,(168,false):3,(56,true):9,(56,false):3. Bezout and transverse rational differentials give length25 with seven reduced rational points and residual length18; the 2-dimensional first-jet target at any rational point proves the global dimension upper bound. Tests use geometric unit ideals, not bounded extension-field sampling.

## originality

PASS

The closest primary finite-field papers concern existence of smooth pencils or enumeration of single curves rather than the all-smooth rational three-member filling-quintic incidence, 108 orbit classes and reducedness strata. This does not rule out unindexed earlier classification; no primary covering theorem was found.

## value

PASS

This is a natural sharp extremal degree-five plane-filling linear-system classification over the smallest field, giving a nontrivial finite incidence and orbit/stabilizer census and a geometric base-reducedness dichotomy. It goes beyond merely counting individual curves or restating the first-jet upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
