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

From φ(n)=2^k and T(n)=1 one obtains φ(σ(n))=2^(k+1). For every d dividing σ(n), φ(d) divides that power of two by the prime-power formula. A dyadic totient forces the odd part of n to be a squarefree product of Fermat primes. For F_j with j≥2, its divisor-sum factor F_j+1 has odd part 2^t+1 with odd t=2^j−1≥3. Any Fermat prime F_i with i≥1 has order 2^(i+1) for base 2, which cannot divide 2t. If the odd part had dyadic totient, it would therefore have to be 3 alone with exponent one, impossible. Only supports 1,3,5,15 remain. The odd cases 3,5,15 have differences −1,−5,−7. For a≥1 and M=2^(a+1)−1, the 5-ray needs φ(6M)=2(M+1) but φ(6M)≤2M. On the 15-ray, even a+1 gives 9|24M; odd a+1 gives gcd(24,M)=1 and requires φ(M)=2^a. Both remaining rays also require this last equality. If m=a+1 has an odd prime divisor ℓ then a prime divisor of 2^ℓ−1 has order ℓ, inconsistent with φ(2^m−1) dyadic. Thus m=2^s. For s≥6 the Fermat prefix includes F_5 with prime divisor 641 and hence φ has a factor 5; for 1≤s≤5 the prime Fermat prefix gives exactly φ(2^m−1)=2^(m−1). This also excludes the odd exponent on the 15-ray and proves both directions on the two surviving rays. Independently verified primality by trial division through the respective square roots and the factorization of F_5. A separate trial-factorization evaluation on the ten listed n verified dyadic φ(n) and T(n)=1, using the prime-power product formulas for each intermediate φ and σ.

## originality

PASS

The ten numbers, two generating rays and pure-power Fermat-prefix mechanism are known. The distinct supported claim is the unconditional absence of any other solution with dyadic totient, particularly the exclusions of the 5 and 15 rays and of all potential larger Fermat-prime factors. Neither the numerical database equality with the ten presently known entries nor the general conjecture on A116083 supplies that classification.

## value

PASS

The dyadic-totient class is independently natural both via constructibility and because the unit difference makes the divisor sum's totient dyadic as well. The result proves an unbounded exclusion over all potential Fermat-prime supports and places a structural restriction on any additional A116083 solution. This is not another finite search or a list of already known examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
