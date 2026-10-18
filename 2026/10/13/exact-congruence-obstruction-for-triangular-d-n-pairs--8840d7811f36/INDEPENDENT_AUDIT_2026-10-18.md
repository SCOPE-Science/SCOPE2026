# Independent mathematical audit

## correctness

PASS

PASS: Mod3 squares and triangular residues force T_a≡T_b≡1, c≡0 whenever n≡2 mod3; then T_{1+3u}≡1 mod9, forcing n≡8 mod9. The triangular map j↦T_j is bijective mod 2^k on j=0,...,2^k−1 by the factorization 2(T_a−T_b)=(a−b)(a+b+1) and opposite parity factors, so choose b=1,c=2. For p>3 choose t∉{0,−1} with d=t(t+1)≠16n; the two (p+1)/2-element quadratic-image sets intersect in a nonzero solution x²−d y²=16n−d, with nonvanishing x or y derivative, Hensel lifts and invertible 2,4 recover indices. For p=3, the n≡0 or1 cases admit simple one-variable Hensel roots, while n=8+9m uses a=1+3u,b=1+3v,c=3w and T_{1+3u}=1+9T_u to give a simple w-root in every m mod3; CRT combines indices with one extra 2-power to respect T_j periods. Independent residue scans exactly matched good n for every 3^1..3^5 and checked all 2^1..2^8 permutations, plus nonsingular conic seeds for all n mod primes 5,7,11,13,17,19. No inference from finite checks to infinitely many powers.

## originality

PASS

PASS: The primary Bagchi–Zhou-Zheng arXiv:2608.27697 proves impossibility for 2,5 mod9 and all-modulus solvability when 9 does not divide M; full-text Theorems 11, 13–17 explicitly stop short of the 3-adic power direction. The new simple-Hensel 3-adic construction closes the exact unresolved prime and gives a complete all-modulus iff, not an integral Hasse principle. Related work on actual integer pairs/triples does not imply this local classification.

## value

PASS

PASS: The primary source isolates mod3-power local solubility as the missing step in explaining putatively sporadic parameters such as n=12,17,42. Completing the local obstruction classification proves all remaining admissible parameters are locally unobstructed, distinguishing global arithmetic failures from modular ones. This is a natural theorem answering a specific mathematical gap with new 3-adic seed, not an arbitrary modular experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
