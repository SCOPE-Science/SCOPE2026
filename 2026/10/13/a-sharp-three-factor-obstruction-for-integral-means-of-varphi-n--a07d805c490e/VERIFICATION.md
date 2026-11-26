---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed the integer-pair lemma in RESULT.md lines 35–103. For u=(x−1)(y−1), v=(x+1)(y+1), S=xy+1 and T=x+y satisfy S>T>0 and uv=S²−T². Let d=gcd(S,T), a=S/d, c=T/d. Integral G forces d|G by prime valuations and b=G/d satisfies a²=b²+c², with gcd(a,b)=1 since gcd(a,c)=1. Integral H=db²/a forces a|d. The integers X=cx−a, Y=cy−a are positive since S/T is strictly less than both x and y. Multiplying gives XY=a²−c²=b² and X+Y≤b²+1. Thus a c²≤d c²=X+Y+2a≤(a+1)²−c², so c²≤a+1. But b=1 would imply (a−c)(a+c)=1, impossible with c≥1; hence c²=(a−b)(a+b)≥a+2, a contradiction. This excludes semiprimes with distinct primes by multiplicativity; for a prime the product p²−1 falls strictly between consecutive squares, and for p² the sum 2p²+1 is odd. Independently counted totatives and summed divisors of 418 and 477, obtaining (φ,σ)=(180,720) and (312,702) and mean triples (450,360,288) and (507,468,432). Both factor with multiplicity exactly 3. The statement excludes n=1. Read VERIFICATION.md and verify.py; no uploaded script was run. The pair and integer censuses are finite corroboration, not a premise of the unrestricted proof.

## originality

PASS

The exact sequence and sharp examples were already tabulated; prime-power exclusion for the geometric-only problem is also known. The credited claim is the unconditional joint geometric/harmonic obstruction for the shifted pair, which excludes all distinct-prime semiprimes and makes the support bound sharp.

## value

PASS

The minimum prime multiplicity in the established simultaneous-means sequence is a natural exact question; the geometric and harmonic restrictions separately allow semiprimes. The new obstruction explains why their intersection does not and holds for all shifted pairs regardless of primality. It is an unrestricted structural result, not a recomputation of the known witnesses and not a density claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
