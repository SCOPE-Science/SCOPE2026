# Independent audit — 2026-09-30

**Record:** `2026/09/21/prime-power-egyptian-two-prime-rigidity--36f7915745ba`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `17ec48bfc78da5fa9c732c5dd1ef732b49b03d1a`  
**Disposition:** **PASSED**

## Correctness

**PASS.** The two classifications follow cleanly from the defining Egyptian-fraction equations. If the smaller prime p is odd, geometric reciprocal-sum bounds force E_+<49/60 and 0<E_-<3/4, excluding the target values. For p=2, the pseudoperfect equation factors as (1-q^{-b})[(q-1)^{-1}-2^{-a}]=0, forcing q=2^a+1 with b unrestricted. On the Giuga side integrality forces E_-=1; clearing denominators and setting c=2^a-q+1 reduces the equation to c(1+q+...+q^{b-1})=2 with c a positive even integer, forcing c=2, b=1, q=2^a-1. Independent exact-rational enumeration over primes below 80 and exponents through 4 found no mismatch.

## Originality

**PASS (literature-bounded).** Machacek (2018) gives sufficient Fermat/Mersenne constructions and explicitly observes that a two-prime term of A073935 must have the Fermat form 2^k(2^k+1)^j. He does not state the converse for all prime-power pseudoperfect numbers, and on the Giuga side states only the Mersenne sufficient family. The assigned theorem closes those two-prime-support converses. Current OEIS material likewise records the Mersenne family as an inclusion. Targeted exact-form searches and repository code search found no equivalent full classification. Because the proof is short, differently phrased problem/sequence literature remains a residual priority risk.

## Scientific value

**PASS.** The result completely settles the smallest nontrivial prime-support case for both prime-power Egyptian-fraction classes, shows Machacek's sufficient constructions are exhaustive there, and isolates the sharp asymmetry that the Fermat-side odd-prime exponent is free while the Mersenne-side exponent is forced to one.

## Literature and evidence

- Machacek, Egyptian Fractions and Prime Power Divisors: https://arxiv.org/abs/1706.01008
- OEIS A283423, Prime power pseudoperfect numbers: https://oeis.org/A283423
- OEIS A286497, Prime power Giuga numbers: https://oeis.org/A286497
- Grau, Oller-Marcen and Sadornil, On mu-Sondow numbers: https://arxiv.org/abs/2111.14211

## Limitations

- The classification is restricted to integers with exactly two distinct prime factors.
- The pseudoperfect side is closely foreshadowed by Machacek's support-two description for the narrower sequence A073935; the novelty is the converse for the larger prime-power pseudoperfect class and the Giuga converse.
- A short equivalent observation could exist under poorly indexed sequence/problem terminology.


This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
