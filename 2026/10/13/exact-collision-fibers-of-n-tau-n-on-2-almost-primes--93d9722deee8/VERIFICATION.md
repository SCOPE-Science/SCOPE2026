---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

On inputs n>=2 with Omega(n)<=2, tau(n) can only be 2 (prime), 3 (prime square), or 4 (squarefree product of two distinct primes). In a collision F(m)=F(n) with m<n we require n-m=tau(m)-tau(n)>0. Thus possible pairs of divisor counts are exactly (3,2), (4,2), (4,3). The first forces (m,n)=(4,5) because p²+1 prime only for p=2; the second gives exactly m=qr with distinct odd primes q<r and n=qr+2 prime, and the converse is immediate; the third would force qr=p²−1 divisible by 8 for odd p, impossible for squarefree qr of v2<=1 (p=2 also impossible). Distinct possible pairs share no third value in the restricted domain, so max fiber cardinality is 2. Independent sieve over 2<=n<=100000 computed all F-fibers on Omega<=2, finding 2,961 nontrivial fibers and no counterexample; symbolic case exhaustion, not finite scan, proves infinite assertion.

## originality

PASS

The studied map is exactly n+tau(n) from Pollack–Troupe and Gabdullin–Iudelevich–Luca; those papers study statistical output and image size rather than exact low-Omega fibers. An all-input injectivity or full collision classification would dominate the restricted result, but the cited image/additive-energy theorems provide bounds rather than an iff description and do not logically imply it. A lower/upper density bound for the image or additive-energy estimate does not rule out one rare triple fiber, and hence cannot imply maximum restricted fiber 2. Primary text inspections and Resultary cross-checks found no exact or dominating theorem for the complete claim; this is a best-of-knowledge PASS with the listed explicit literature and accessibility risks, not proof of absolute novelty.

## value

PASS

The natural low-prime-factor filtration Omega(n)<=2 is the first layer where a shifted multiplicative divisor statistic n+tau(n) can collide; the complete exact fiber description and maximum multiplicity give a concrete combinatorial input to studying injectivity, images and additive energy of this specifically studied arithmetic map. It is an elementary but exact, self-contained full classification of a natural sparsity class, not an arbitrary search cutoff, claimed only for the restricted domain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
