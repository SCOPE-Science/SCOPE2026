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

For two hits at a<b with exponent difference t, the identity h d=2^u(2^t-1) and n>=0 give exactly the odd-divisibility and inequality conditions; all such progressions give the same word after power-of-two normalization. Conversely the frozen n,d are integral and attain the word, allowing n=0. For three hits the odd first Mersenne factor is coprime to 2^t, forcing 2^t to divide the spacing after b. Above the cutoff t=floor(log_2 k), this excludes a third hit and the start constraint forces a=0. Each exceptional pair {0,b} is realizable by an arbitrarily large t divisible by the order of 2 modulo odd(b) (with modulus 1 separate). The printed divisibility argument is read precisely as: q/gcd(q,2^s-1) divides b for an intermediate exponent s; that actual divisor is at least (2^t-1)/(2^(t/2)-1)>b, not that the lower bound itself divides b. This establishes the claimed contradiction without changing the theorem or construction. Zero and singleton words come from unbounded gaps. The divisor estimates for a=0 and a>=1 each cost at most 4k/(1-1/sqrt(2)); first three families contribute precisely 2k distinct words, including the k=1 case. In the first estimate, 1+log_2 k<=2sqrt(k) follows by applying the tangent bound for log to sqrt(k) at 2. The all-length proof is analytic; the uploaded finite checker was inspected, not executed, and is not used as exhaustion.

## originality

PASS

The strongest corpus overlap studies the same support up to an index shift and gives sharp occupancy and a quadratic upper bound, but not the exact full factor language or the linear bound in base two. The primary general automatic-sequence theorem gives a subexponential bound here, not a linear one. The exact language prescription and linear bound are distinct on the inspected evidence; no priority claim is made beyond that comparison.

## value

PASS

Powers of two form a canonical sparse automatic support. The finite generator replaces an unbounded progression search with explicit bounded parameters, handles arbitrary factor length and can certify attainable masks and exact counts at a chosen length. Linear growth is a significant refinement of the general subexponential or specific quadratic estimates and follows from structural constraints on several hits, not from a table of small instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
