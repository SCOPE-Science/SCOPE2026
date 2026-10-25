# Independent mathematical audit

## correctness

PASS

The fixed normalized gcd gives coprime increasing a_n<b_n for every k≥2. For coprime a<b, choose α inverse of a modulo b in [1,b−1] and β=(ab+1−aα)/b in [1,a]. The complementary Bézout identity gives either the witness ((α−1)/2,(β−1)/2) to M when both α,β are odd, or ((b−α−1)/2,(a−β−1)/2) to M−1 otherwise; the latter two numerators are odd by aα+bβ=ab+1 mod 2. Every target <ab has at most one nonnegative representation because x is determined mod b; Frobenius complement F=ab−a−b=2M−1 proves only one of M,M−1 is representable, with a=1 handled separately. Under (a,b)→(b,kb−a), transported (α,β)→(kα+β−a,b−α) satisfies the new Bézout equation and positivity. Modulo 2 this transformation permutes all six admissible parity states in three 2-cycles if k even, or two 3-cycles if k odd, each with nonconstant δ pattern and exact least period. Independent exact six-state calculation reproduced these cycles and least periods. Original verify.py was inspected; its finite tests cannot substitute for the parity-state proof.

## originality

PASS

An all-seed, all-coefficient (k≥2) sharp period-2/period-3 law for the negative-sign recurrence with explicit modular inverse witnesses is not implied by the positive-sign recurrence analyses or isolated balancing-sequence cases.

## value

PASS

The solvability of paired midpoint Frobenius equations is a natural question with known isolated recurrence instances; the exact universal least 2/3 period, frequencies, and explicit witness recurrence resolve the natural arbitrary-seed negative-sign extension. It is a sharp structural classification, not merely substituting the sign in known formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
