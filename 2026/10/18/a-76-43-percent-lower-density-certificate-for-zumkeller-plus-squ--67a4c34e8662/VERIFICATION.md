---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Mahanta–Saikia–Yaqubi Theorem 2.6 gives 2^a p (p≤2^(a+1)−1) Zumkeller, and their Lemma 2.8 preserves Zumkeller under coprime prime-power multiplication; hence v2(z)≥a, vp(z)=1 suffices. For each certified N, CRT combines a square root modulo 2^a with x mod p² such that vp(N−x²)=1, giving 1≤x≤2^a p²≤15376. For N>15376² this yields a positive Zumkeller complement. The p²-good residue count is (p−1)(p+2)/2: nonzero quadratic residues mod p and nonzero multiples of p, disjoint. Binary-square strata have densities 1/2,1/8,1/8,1/4, with independent odd prime CRT failure factors. Independent local enumeration for all ten primes confirmed counts; rational arithmetic recomputed 63520442937841228526/83108492151210387225≈0.7643074888456645. This is only the exact density of the certificate subset and a lower bound on representables, not the true density.

## originality

PASS

Somu–Kukla–Tran (2023) Proposition 4.11 establishes representations on 10 residue classes modulo 18, giving asymptotic coverage at least 5/9; Conjecture 4.21 predicts zero density of exceptions but does not prove it. Mahanta–Saikia–Yaqubi (2020) supplies the two-prime Zumkeller criterion and multiplier facts without additive-square sieve density. The current ten-odd-prime p² sieve and binary stratification produce a strict 0.7643 improvement not implied by the directly examined sources, while relying on their genuine premises.

## value

PASS

Quantitatively improving a published 5/9 lower bound to >0.7643 for the central open additive representation question is a meaningful, motivated finite-prime sieve. It provides constructive residue certificates for all sufficiently large members of a periodic family; no unsupported claim of optimality or conjecture resolution is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
