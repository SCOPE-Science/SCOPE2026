---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Writing a target (s,w) as (x,x³)+(y,y³)+(s−x−y,(s−x−y)³) gives smooth projective cubic E: (X+Y)(X−sZ)(Y−sZ)=cZ³ for c=(s³−w)/3 when char≥5. Singular c=0 and c=8s³/27 have explicit triples; otherwise E has exactly three rational infinity points and is smooth genus one, so Hasse #E(F_q)≥q+1−2sqrt(q)>3 for q≥11 guarantees an affine triple. Direct exhaustive enumeration confirmed F5 omissions (s,3s³) for s≠0, F7 omissions (0,±2), and no 3-sum omissions for primes 11,13,17,19,23. Because each small complement has <q points, 4C(F)=F². In characteristic 3 Frobenius makes C additive so it never spans; in every odd characteristic 2C misses (0,w≠0). Covers odd extension fields via uniform Hasse, not characteristic two.

## originality

PASS

Best-of-knowledge PASS for exact all-odd-characteristic basis-order census and exceptional targets of a natural cubic parametrized curve. Classical Sidon-set/finite-field incidence and algebraic curve methods are credited; they do not trivially give universal three-sum coverage.

## value

PASS

The exact additive basis order is a natural structural invariant of the cubic graph in F_q², and small-field and characteristic-three exceptions are mathematically sharp. It combines an elliptic curve argument with a full all-q classification, beyond a table or a single computed finite field.

The dated certificate retains the supplied scientific assessment, sources and limitations.
