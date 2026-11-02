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

PASS: The roots alpha,beta of X²-PX-1 have product -1, and the discriminant Delta=P²+4 is nonsquare and positive for P>=3. At odd unramified primes let w=alpha/beta; p|V_n iff w^n=-1, which occurs exactly at odd multiples of the first trace-zero rank lambda. If w has order 2lambda, odd-power LTE gives nu_p(V_(lambda k))=nu_p(V_lambda)+nu_p(k) for odd k and zero valuations off that support. Möbius inversion then yields signed support only at lambda,2lambda,lambda p^j,2lambda p^j (with index-one collision treated separately), so the least repair is 2lambda/gcd(2lambda,p-1); at ramified odd primes both repeated roots are nonzero and trace never vanishes. Split Frobenius gives order 2lambda dividing p-1, so Dold holds, while inert Frobenius forces existence of a trace-zero rank precisely when p=3 mod4 and its least repair is lambda. At p=2, if P is odd the nonzero transform is T(1)=1,T(3)=3,T(6)=-2, giving repair 3; if P is even with v2(P)=s, T(1)=2^s,T(2)=2-2^s, giving repair 1 and positivity only when s=1. These combine with quadratic character independence modulo 4 and prime distribution in arithmetic progressions to give exactly density 1/4 for bad odd primes. Independently checked 8,316 local Dold congruence cells over seven parameters P in {3,4,5,6,7,10,13}, twelve primes<=37 and n<=99; all matched Legendre-class predictions. Exact spot transforms included P=3,p=7: T4=6,T8=-6,T28=42,T56=-42; P=3,p=2: T1=1,T3=3,T6=-2; and P=4,p=2: T1=4,T2=-2. This finite evidence supplements the infinite proof.

## originality

PASS

PASS qualified: Chuysurichay–Jaidee–Panraksa–Ward (2026) explicitly focus on classical Fibonacci/Lucas (P=1), whose Dold good-prime density is 3/4 and whose least repair has a similar structure. That prior result is credited: its arguments and special-case statements are not novel here. The assessed new scope is the entire nonsplit family P>=3 with varying real-quadratic discriminant, exact trace-rank/ramification and binary branches, complete signed transform and local realizability, and uniform 1/4 failure density. Resultary related work covers split companion Lucas pairs and q=-1 period comparisons, not the full nonsplit local Dold law. Generalized Lucas valuations are established prior ingredients and might imply the new theorem with substantial adaptation; no inspected primary theorem explicitly covers all P>=3.

## value

PASS

PASS: The question of local Dold integrality and nonnegative realizability for a whole natural companion-Lucas family is motivated by periodic-point counting, exact signed Möbius transforms, and arithmetic prime splitting. The uniform inert-prime criterion, sharp repair factors, exceptional binary branch and density 1/4 answer the exact structural problem across infinitely many P, rather than a small numerical parameter extension. Although the old P=1 case already has density 3/4, the varying-discriminant full family requires a genuinely new uniform arithmetic classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
