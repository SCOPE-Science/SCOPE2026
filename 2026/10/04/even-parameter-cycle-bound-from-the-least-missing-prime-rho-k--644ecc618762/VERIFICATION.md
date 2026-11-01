---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For any even k>=2, rho(k) is the least prime not dividing k. For any prime p>B(k)>=rho(k), p is odd and p≠rho. Since k is invertible mod rho, one of p,p+k,...,p+(rho-1)k is divisible by rho; the first such positive-index composite occurs by ell<=rho-1. As k even, c=p+ell*k is odd composite, hence P^+(c)<=c/3<= (p+k(rho-1))/3<p whenever p>k(rho-1)/2. A periodic orbit contains a prime; if all its primes exceeded B, consecutive prime-block transitions would strictly descend, contradicting cyclicity. Distinct orbits are disjoint and inject into primes<=B, giving L(k)<=pi(B). For even k>=4 with 3∤k, rho=3 and B=k; for 6|k,5∤k, rho=5 and B=2k; k=2 B=3. Git-blob-verified verify.py replay returned VERIFY_OK for finite ranges, but symbolic proof establishes all even k.

## originality

PASS

Best of knowledge: the exact least-missing-prime run-length lemma of Dubickas and the generic finite-cycle mechanism of Das are antecedents, not new. Neither inspected primary theorem implies the claimed parity-sensitive intrinsic cycle threshold B(k)=max{rho(k),k(rho(k)-1)/2} without the new combination with the odd-composite one-third contraction. The distinct published odd-k census is not an all-even-parameter upper bound. The bound and corollary L(k)<=pi(k) for even k>=4, 3∤k, were not found as earlier established theorems. Novelty is qualified because an elementary consequence of close antecedent lemmas can appear in unindexed work or be considered implicit.

## value

PASS

This provides a start-independent, parameter-explicit localization of every periodic orbit for a natural arithmetic dynamical map and bounds the number of cycles. For the infinite congruence family of even k>=8 with 3∤k it replaces Das’s k sqrt(k)/2 prime-locator scale with the linear bound B=k; for 6|k,5∤k it gives the similarly explicit B=2k. The mathematical reason is a structural parity-specific 1/3 contraction after a prime-run bounded by rho(k), not a finite empirical gain or renaming. This is useful for exact searches and for the open study of cycle growth; it does not determine L(k) exactly or solve its unboundedness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
