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

For distinct primes p>q>a>=2, gcd(a,p-a)=gcd(a,p)=1 and likewise for q, so the definition p-a|pq-a reduces to p-a|q-1. Set r=p-a, s=q-a, c=a-1; r>s>0 and r|(s+c), s|(r+c). Unique u=(s+c)/r, v=(r+c)/s satisfy 1<=u<v and with d=uv-1>0 give r=(v+1)c/d and s=(u+1)c/d. Conversely any such integer u,v giving prime a+r,a+s satisfies both congruences. From s>=1, v<=c+(c+1)/u<=2c+1, so the parameter search is finite. If a even, r,s,c odd and u,v even. The rational ratio (v+1)/(uv-1) decreases with either variable, maximizing at (u,v)=(1,2) without parity or (2,4) under even parity. Thus p<=4a-3 if a odd and p<=a+5(a-1)/7 if even. Exact equality witnesses (a,p,q)=(11,41,31),(8,13,11) are prime and satisfy both divisibilities. Independently enumerated all primes for 79 shifts 2..80 and matched all 133 parametrized pairs; finite agreement is supportive, not the all-a proof.

## originality

PASS

The generalized shifted-Korselt definition is prior work; the displayed two-prime parameter bijection and sharp parity-restricted largest-prime thresholds are a distinct finite prime-support classification absent from the materially reviewed Wright and Zheng theorems. The modular reduction itself is elementary and is not claimed to be novel. A possible older k-Korselt semiprime parametrization is a significant priority risk.

## value

PASS

The prescribed two-prime support is the first nontrivial compositeness case for shifted Carmichael divisibility and is naturally contrasted with the ordinary (1,1) condition, for which semiprimes are impossible. A complete finite parameterization and parity-sharp global size bounds for all shifts are useful as structural classification and an algorithmic sieve; motivation is not dependent on large computational tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
