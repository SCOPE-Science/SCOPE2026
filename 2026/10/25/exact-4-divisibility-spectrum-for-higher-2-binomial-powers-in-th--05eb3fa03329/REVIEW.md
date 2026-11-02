# Independent mathematical audit

## correctness

PASS

For equal-length binary words, the complete order-two binomial signature is exactly (S=sum bits,J=sum positional weights), since #01=J-binomial(S,2), while #00,#11,#10 follow from ones count and total length. The Thue–Morse relation t_{2a}=t_a,t_{2a+1}=1-t_a forces each aligned two-letter pair to contain one 1. Three adjacent odd-root blocks cannot have equal ones counts, since one of their adjacent pairs starts on an even boundary and has counts h+b versus h+1-b. For m=2h with h odd, even starts reduce equality of J(mu(x))=h²-S(x) to the forbidden odd-root abelian cube; odd starts use four boundary bits, whose equal differences must all vanish, and a left-rotation moment identity gives the same forbidden cube. For m=4k, mu²(0)=0110 and mu²(1)=1001 both have two ones and moment 3, and order-2 binomial equivalence is a concatenation congruence, so any aligned concatenation length4k works for every exponent. Independent 8192-bit arithmetic-prefix calculation checked all starting positions for m<=64 and uniform aligned examples; finite tests corroborate but not replace proof for all m and exponent.

## originality

PASS

The theorem precisely determines an all-root-length occurrence spectrum for 2-binomial cubes and every higher exponent in Thue–Morse, not just factor equivalence class counts or existence of a separate avoiding word. Its odd-start desubstitution obstruction and universal 4-aligned construction are additional to the general binomial congruence.

## value

PASS

Thue–Morse is a canonical automatic word; the precise allowed root lengths of all 2-binomial cubes and higher powers are fundamental repetition/avoidance invariants. The sharp arithmetic threshold m divisible by four and the stronger every aligned start, every exponent construction form a uniform all-m classification and a natural answer for power avoidance, not a finite prefix statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
