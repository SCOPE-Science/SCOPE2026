# Independent scientific review — 2026-10-01

## Final claim

Let \(p<q<r\) be odd primes in arithmetic progression and suppose \(n=pqr\). Then \(n\) is Lucas–Carmichael in the sense \(s+1\mid n+1\) for every prime divisor \(s\mid n\) if and only if there are unique coprime integers \(u>v>0\) of opposite parity and an integer \(w>0\) with \(u^2-v^2\mid2v^2w-3\) such that \((p,q,r)=(uw(u-v)-1,u^2w-1,uw(u+v)-1)\). Each primitive shape lies on one admissible congruence ray; the classical \((6m-1,12m-1,18m-1)\) family is the \((u,v)=(2,1)\) ray.

## Correctness — PASS

Writing \(q+1=h\) and common difference \(d\), the three Lucas–Carmichael divisibilities reduce exactly to \(h-d\mid d(2d-3)\), \(h\mid d^2\), and \(h+d\mid d(2d+3)\). With \(g=\gcd(h,d)\), \(h=gu\), \(d=gv\), coprimality forces \(g=uw\), hence \(h=u^2w\), \(d=uvw\). The outer conditions become divisibility of \(2v^2w-3\) by both \(u-v\) and \(u+v\); same parity is impossible, and opposite parity makes these two factors coprime, yielding the single modulus \(u^2-v^2\). Reversing the algebra gives the converse and uniqueness. The fixed-shape admissibility argument correctly treats primes dividing the modulus, primes outside it, and the parity restriction. The finite artifact checks are supplementary, not the proof.

**Risk:** No unconditional infinitude of prime values is proved; the ray-admissibility consequence is conditional on the prime-tuples conjecture as stated.

## Originality — PASS

The open Einsele–Paterson 2024 article was inspected through its full HTML section on Lucas–Carmichael numbers with three prime factors. It develops general counting bounds and normalized shifted-factor variables but contains no “arithmetic progression” occurrence and no audited AP iff parametrization. OEIS A290810 records the known special ray \(6m-1,12m-1,18m-1\), confirming that this ray is prior art rather than the full theorem. Resultary returned an earlier 2026-09-20 SCOPE theorem on a different primitive-gcd uniqueness question, not AP classification.

**Risk:** Older Guy/De Koninck references and obscure arithmetic-progression treatments were not exhaustively inspected in full.

## Value — PASS

Arithmetic progression is a natural structured slice of three-prime Lucas–Carmichael numbers. The theorem replaces an isolated classical parametric family by a complete unique shape/ray classification and connects every shape to an admissible prime-tuple problem. This is a natural exact classification rather than an arbitrary finite slice.

**Risk:** The result is conditional only for infinitude; the iff classification itself is unconditional.

## Overall disposition

**PASSED**
