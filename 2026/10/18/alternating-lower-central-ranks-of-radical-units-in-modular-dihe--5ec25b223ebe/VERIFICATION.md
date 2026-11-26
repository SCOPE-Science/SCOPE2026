---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently reconstructed the lower central series by u-degree. One may use u=r−r⁻¹ itself, which has leading term 2(r−1) and is negated by s. Its ideal is nilpotent with semisimple quotient k×k, hence is J. For a,c≥1 and b,d∈{0,1}, the bracket is ((−1)^(bc)−(−1)^(ad))u^(a+c)s^(b+d). In any even target degree t the only possible image is k u^t s, and in odd target degree t both basis vectors are allowed. Bracketing degree t−1 with degree one generates the full allowed target: for even t use the two different parity-of-s basis vectors in the odd degrees; for odd t use u^(t−1)s against u and us. This works also with the restricted degree-(t−1) image from the previous lower central term. Thus for i≥2 the i-th Lie term is exactly the sum of the allowed spaces in degrees t≥i through p−1. Nilpotence J^p=0 makes the associative exp/log and BCH identities valid in degrees <p, and the class-<p Lazard correspondence transports the entire lower central series. Counting gives the stated orders and all additive quotients, including p=3; (1+x)^p=1 gives the Frattini conclusion over every field extension. This is a symbolic replay, not an extrapolation from the finite tests.

## originality

PASS

The evidence supports the full alternating lower-central quotient profile as the distinct claim. Previously recorded order, exponent, center and class bound are not credited as new.

## value

PASS

The lower central quotients are natural structural invariants of the distinguished modular unit group. The alternating dimensions describe every noncentral commutator layer uniformly over primes and extension fields; a center computation or class bound cannot substitute for that profile. The exact series resolves sharpness and supplies the number of generators without separately assuming either invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
