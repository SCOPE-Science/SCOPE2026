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

For every prime power q≡7 (mod8), t²−6t+1=0 has two distinct nonzero non±1 roots (since 2 is a square, char odd). For monic X²+uX+v, z=(u²−4v)/4 converts simultaneous irreducibility at shifts {−t,−1,1,t} to four negative quadratic characters, with q coefficient choices per z. Expanding H(z)=Π(1−chi(z−s)) gives pair total −6 and cancellation of cubic sums under z↦−z. The projective Mobius identity [(A²−B²)(A²−t²B²)]=−(t+1)^4[(z²−1)(z²−t²)] defines a bijection of P¹, and chi(−1)=−1 forces the projective sum zero; removing infinity gives affine quartic character sum −1. Hence ΣH=q−7. The four exceptional z corrections B are 0 or 8 (at most one exceptional z can have all opposite differences nonsquare), and 16-divisibility fixes B by q mod16, so N=floor((q−7)/16), M=qN. Independently verified homogeneous polynomial identity modulo t²−6t+1 symbolically and counted 8 prime-field cases including q=7,23,31,47,71,79,103,127; these are corroborative, not infinite proof.

## originality

PASS

Qualified PASS: Bary-Soroker 2012 and Bank–Bary-Soroker 2014 provide broad asymptotic prime-polynomial counts with error terms, not this exact q floor((q−7)/16) law. An earlier four-term arithmetic-progression exact count covers the characteristic-seven part, which is credited; the harmonic quartet is not affinely equivalent to a four-term progression in other allowable characteristics. Older quartic character-sum identities could still duplicate the result.

## value

PASS

A canonical harmonic four-point configuration yields a uniform *exact* irreducibility count over infinitely many prime powers, including a sharp vanishing threshold and cancellation of the usual genus-one quartic fluctuation. This is a substantive exact-function-field prime-tuple invariant, not a finite table or only asymptotic specialization; limited to a special symmetric configuration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
