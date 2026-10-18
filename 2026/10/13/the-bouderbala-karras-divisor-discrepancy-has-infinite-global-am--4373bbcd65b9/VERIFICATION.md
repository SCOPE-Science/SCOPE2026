---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The exact prime-factor identity Delta_k(n)=sum_{p^a||n}(gcd(k,a)-log_2(a+1)) settles all cases. For k=1 every summand is nonpositive and is zero exactly when a=1; prime powers q^a give Delta→−infinity. For k>=2 choose any prime divisor r of k and let N_t be a product of t distinct primes each to exponent r: Delta_k(N_t)=t[r-log_2(r+1)]→+infinity because 2^r>r+1. Conversely M_t=q^{kt+1} has gcd(k,kt+1)=1 and Delta_k(M_t)=1-log_2(kt+2)→−infinity. These constructions prove an infinite global range rather than merely finite examples. Independent finite exponent-regression checks support the algebra without claiming to prove the limits.

## originality

PASS

The originating 2022 Bouderbala--Karras primary PDF introduces f_k and explicitly poses the amplitude of f_k(n)−log_2 tau(n) as a question, giving broad pointwise inequalities only. Those inequalities alone do not decide whether the difference stays bounded because both arithmetic functions lie between omega and Omega. The present result fixes the natural global-over-n interpretation and yields a complete signed k=1 vs k>=2 split. It does not claim asymptotics for max_{n<=x}.

## value

PASS

A precise and complete resolution of an explicitly posed arithmetic-function boundedness question is a worthwhile narrow mathematical fact even though the proof is short. The positive/negative exponent constructions expose a qualitative parameter discontinuity between k=1 and k>=2, not just another numerical example. It is an elementary answer, not advertised as a deep general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
