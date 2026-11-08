# Independent mathematical audit

## correctness

PASS

Original proof contains a FALSE claim that when 7 divides both U=108m²+1 and V=27m²+16, its exponents in both are exactly one. Counterexamples: m=11 gives exponents (1,2) and m=17 gives (4,1). The theorem itself survives after corrected full proof: U−4V=−63 gives min(v7(U),v7(V))=1, not both equal one; the two U linear roots and one V root are pairwise distinct mod7 from triple gcd one. If one exponent >1, its 1 or 2 disjoint maximal-valuation roots cannot be invariant under 7^(max−1), forcing full higher 7-power period. Other odd primes and 2 cases follow prime-wise valuation roots. Reconstructed all polynomial identities, triple gcd, CRT-free per-prime lower bound and full local-period argument from corrected final RESULT.md. 9000 exact direct quotient comparisons and all 4 high-7-power regression cases passed corrected verify.py.

## originality

PASS

Bodin–Drouin 2024 provide polynomial gcd/resultant periodicity and local valuations, and Dubickas 2022 general polynomial LCM period bounds; the corrected result gives explicit family-specific linear-gcd factors and exact least period including higher shared 7-powers. Hong–Qian treats quadratic progressions. These known general bounds do not, in read material, give this explicit Eisenstein cubic class formula. Best-of-knowledge novelty remains qualified by possibly broader full literature.

## value

PASS

A natural irreducible cubic family has a complete closed quotient and exact smallest period with a genuine, sharply classified exceptional prime interaction. The high-7-power correction is substantive: it fixes a false proof step and verifies a family-specific period that is not routine parameter renaming from general periodicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
